'''
Created on 2022-11-23

@author: wf
'''
from tests.basemwtest import BaseMediawikiTest
from meta.mw import MediaWikiContext
from meta.metamodel import Context

class TestMediawiki(BaseMediawikiTest):
    """
    test reading SiDIF from Mediawiki pages
    """
    
    def setUp(self, debug=True, profile=True):
        """
        setUp
        """
        BaseMediawikiTest.setUp(self, debug=debug, profile=profile)
        for wikiId in ["wiki","royals"]:
            self.getWikiUser(wikiId, save=True)

    def test_metamodel_from_wikis(self):
        """
        test reading meta models from wikis
        """
        mw_contexts=[
            MediaWikiContext("wiki",
                "https://wiki.bitplan.com",
                "MetaModel"
            ),  
            MediaWikiContext("royals",
                "http://royal-family.bitplan.com",
                "FamilyContext"
            )
        ]
        
        debug=True
        for mw_context in mw_contexts:
            context,error=Context.fromWikiContext(mw_context,debug=debug)
            self.assertIsNotNone(context)
            if debug:
                print(f"{mw_context.context} has context {context.name}")
            self.assertIsNone(error)
            self.assertEqual(mw_context.context,context.name)