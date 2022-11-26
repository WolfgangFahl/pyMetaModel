'''
Created on 2022-11-23

@author: wf
'''
from tests.basemwtest import BaseMediawikiTest
from meta.mw import SMWAccess
from meta.metamodel import Context
from wikibot.wikiuser import WikiUser
from sidif.sidif import SiDIFParser
import sys

class TestMediawiki(BaseMediawikiTest):
    """
    test reading SiDIF from Mediawiki pages
    """
    
    def setUp(self, debug=False, profile=True):
        """
        setUp
        """
        BaseMediawikiTest.setUp(self, debug=debug, profile=profile)
        for wikiId in ["wiki","royals"]:
            self.getWikiUser(wikiId, save=True)
            
    def check_contexts(self,wikiId:str,ignoreExceptions:bool=True):
        """
        """
        mw_contexts={}
        try:
            smwAccess=SMWAccess(wikiId,debug=self.debug)
            mw_contexts=smwAccess.getMwContexts()
            for name,mw_context in mw_contexts.items():
                print(f"{name}: {mw_context.sidif_url()}")
            print (f"found {len(mw_contexts)} Contexts")
        except Exception as ex:
            print(str(ex),file=sys.stderr)
            if not ignoreExceptions:
                raise ex
        return mw_contexts
            
            
    def test_contexts(self):
        """
        test getting the list of mediawiki contexts
        """
        mw_contexts=self.check_contexts("wiki")
        self.assertTrue(len(mw_contexts)>=15)
        
    def test_Issue3(self):
        """
        https://github.com/WolfgangFahl/pyMetaModel/issues/3
        """
        debug=True
        wikiUsers=WikiUser.getWikiUsers(lenient=True)
        if "test" in wikiUsers:
            mw_contexts=self.check_contexts("test")
            tc=mw_contexts["Training"]
            context,error=Context.fromWikiContext(tc, debug=self.debug)
            self.assertIsNone(context)
            self.assertIsNotNone(error)
            errorMessage=SiDIFParser.errorMessage("Training context parsing error",error)
            if debug:
                print(errorMessage)
            self.assertTrue("property Qualität" in errorMessage)

    def test_metamodel_from_wikis(self):
        """
        test reading meta models from wikis
        """
        debug=False
        lenient=True
        for wikiId in WikiUser.getWikiUsers(lenient=True):
            mw_contexts=self.check_contexts(wikiId)
            for name,mw_context in mw_contexts.items():
                if debug:
                    print(f"reading context {name} from wiki {wikiId}")
                context,error=Context.fromWikiContext(mw_context,debug=debug)
                if not lenient:
                    self.assertIsNotNone(context)
                else:
                    if context is None:
                        continue
                if debug:
                    print(f"{mw_context.context} has context {context.name}")
                    print(context)
                    for _name,topic in context.topics.items():
                        print(topic)
                        for _name,property in topic.properties.items():
                            print(property)
                if error is not None:
                    print(error)
                if len(context.errors)>0:
                    for error in context.errors:
                        print(error)
                if not lenient:
                    self.assertIsNone(error)
                    self.assertEqual(0,len(context.errors))
                    self.assertEqual(mw_context.context,context.name,wikiId)
                