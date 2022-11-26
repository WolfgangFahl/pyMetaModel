'''
Created on 2022-11-23

@author: wf
'''
from tests.basemwtest import BaseMediawikiTest
from meta.mw import MediaWikiContext,SMWAccess
from meta.metamodel import Context
from wikibot.wikiuser import WikiUser
from sidif.sidif import SiDIFParser
import datetime

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
            
    def check_contexts(self,wikiId:str):
        smwAccess=SMWAccess(wikiId,debug=self.debug)
        mw_contexts=smwAccess.getMwContexts()
        for name,mw_context in mw_contexts.items():
            print(f"{name}: {mw_context.sidif_url()}")
        print (f"found {len(mw_contexts)} Contexts")
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
        mw_contexts=[
            MediaWikiContext("wiki",
                "https://wiki.bitplan.com",
                "MetaModel",
                datetime.datetime(2015, 1, 23, 0, 0),
                "http://master.bitplan.com"
            ),  
            MediaWikiContext("royals",
                "http://royal-family.bitplan.com",
                "FamilyContext",
                None,
                "http://royal-family.bitplan.com"
            )
        ]
        
        debug=True
        for mw_context in mw_contexts:
            context,error=Context.fromWikiContext(mw_context,debug=debug)
            self.assertIsNotNone(context)
            if debug:
                print(f"{mw_context.context} has context {context.name}")
                print(context)
                for _name,topic in context.topics.items():
                    print(topic)
                    for _name,property in topic.properties.items():
                        print(property)
            self.assertIsNone(error)
            self.assertEqual(mw_context.context,context.name)
            