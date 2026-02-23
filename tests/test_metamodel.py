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


from meta.metamodel import Property, Topic
from tests.basetest import Basetest


class TestTopic(Basetest):
    """
    test Topic methods - see https://github.com/WolfgangFahl/pyMetaModel/issues/36
    """

    def test_get_primary_key_property(self):
        """test get_primary_key_property returns the primaryKey property or None"""
        topic = Topic()
        topic.properties = {
            "name": Property(name="name", primaryKey=True),
            "at": Property(name="at"),
        }
        pk = topic.get_primary_key_property()
        self.assertIsNotNone(pk)
        self.assertEqual(pk.name, "name")

    def test_get_primary_key_property_none(self):
        """test get_primary_key_property returns None when no primaryKey exists"""
        topic = Topic()
        topic.properties = {"at": Property(name="at")}
        self.assertIsNone(topic.get_primary_key_property())
