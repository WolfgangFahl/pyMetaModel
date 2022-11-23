'''
Created on 2022-11-23

@author: wf
'''
from tests.basetest import Basetest
from meta.mw import MediaWikiContext
from meta.metamodel import MetaModel

class TestMediawiki(Basetest):
    """
    test reading SiDIF from Mediawiki pages
    """

    def test_metamodel_from_wikis(self):
        """
        test reading meta models from wikis
        """
        mw_contexts=[
            MediaWikiContext("royals",
                "http://royal-family.bitplan.com",
                "Family"
            )
        ]
        
        debug=True
        for mw_context in mw_contexts:
            mm,error=MetaModel.fromWikiContext(mw_context,debug=debug)
            self.assertIsNone(error)
            
