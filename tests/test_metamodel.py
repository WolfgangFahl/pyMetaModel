"""
Created on 2023-02-25

@author: wf
"""

from meta.smw_type import SMW_Type
from tests.basemwtest import BaseMediawikiTest


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
            self.getSMWAccess(wikiId, save=True)

    def testSMW_Type(self):
        """
        test SMW_Type handling
        """
        debug = self.debug
        smwAccess = self.smwAccessMap["wiki"]
        ask_query = SMW_Type.askQuery()
        did = smwAccess.smw.query(ask_query)
        for record in did.values():
            smw_type = SMW_Type.from_dict(record) # @UndefinedVariable
            if debug:
                print(smw_type)
            self.assertIsInstance(smw_type, SMW_Type)
