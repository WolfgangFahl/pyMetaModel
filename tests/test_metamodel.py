'''
Created on 2023-02-25

@author: wf
'''
from tests.basemwtest import BaseMediawikiTest
from meta.smw_type import SMW_Type
from meta.mw import SMWAccess

class TestMetaModel(BaseMediawikiTest):
    """
    test round trip meta model handling
    """
    
    def setUp(self, debug=False, profile=True):
        """
        setUp
        """
        BaseMediawikiTest.setUp(self, debug=debug, profile=profile)
        for wikiId in ["wiki"]:
            self.getSMWAccess(wikiId,save=True)        
            
    def testSMW_Type(self):
        """
        test SMW_Type handling
        """
        debug=True
        smwAccess=self.smwAccessMap["wiki"]
        ask_query=SMW_Type.askQuery()
        did=smwAccess.smw.query(ask_query)
        for record in did.values():
            smw_Type=SMW_Type.fromDict(record)
            if debug:
                print(smw_Type)
            pass
        