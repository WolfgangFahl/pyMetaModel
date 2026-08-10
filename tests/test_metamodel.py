"""
Created on 2023-02-25

@author: wf
"""

from meta.smw_type import SMW_Type
from tests.basemwtest import BaseMediawikiTest
from meta.metamodel import Context, Property, Topic
from tests.basetest import Basetest


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
            smw_type = SMW_Type.from_dict(record)  # @UndefinedVariable
            if debug:
                print(smw_type)
            self.assertIsInstance(smw_type, SMW_Type)


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

    def test_pluralName_from_wiki(self):
        """test that pluralName loaded from SiDIF is used, not the default fallback
        see https://github.com/WolfgangFahl/pyMetaModel/issues/37
        """
        topic = Topic()
        topic.name = "Property"
        topic.pluralName = "Properties"
        pluralName = topic.getPluralName()
        self.assertEqual(pluralName, "Properties")

    def test_pluralName_default_fallback(self):
        """test that getPluralName falls back to name+s when pluralName not set
        see https://github.com/WolfgangFahl/pyMetaModel/issues/37
        """
        topic = Topic()
        topic.name = "Topic"
        topic.sanitize()
        pluralName = topic.getPluralName()
        self.assertEqual(pluralName, "Topics")

    def test_pluralName_fallback_without_sanitize(self):
        """test that getPluralName falls back to name+s even when sanitize()
        has not been called - the accessor must hold its documented invariant
        on its own and not depend on the caller remembering sanitize()
        """
        for pluralName_value in (None, ""):
            topic = Topic()
            topic.name = "Query"
            topic.pluralName = pluralName_value
            pluralName = topic.getPluralName()
            self.assertEqual(pluralName, "Querys")


class TestProperty(Basetest):
    """
    test Property methods
    """

    def test_Issue39_external_formatter_uri_alias(self):
        """test that the name the MetaModel declares for the formatter uri
        reaches the field
        see https://github.com/WolfgangFahl/pyMetaModel/issues/39
        """
        sidif = """Meeting isA Context
"Meeting" is name of it
HopContent isA Topic
"HopContent" is name of it
"Meeting" is context of it
Screenshot isA Property
"screenshot" is name of it
"External identifier" is type of it
"https://rdd.bitplan.com/$1" is externalFormatterURI of it
"HopContent" is topic of it
"""
        context, error, errMsg = Context.fromSiDIF(sidif, title="issue39")
        self.assertFalse(error, errMsg)
        prop = context.topics["HopContent"].properties["screenshot"]
        self.assertEqual(prop.formatterURI, "https://rdd.bitplan.com/$1")
