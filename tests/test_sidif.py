"""
Created on 2023-02-25

@author: wf
"""
import os
from meta.metamodel import Context
from tests.basetest import Basetest


class TestSiDIF(Basetest):
    """
    test SiDIF handling
    """
    def setUp(self, debug=False, profile=True):
        Basetest.setUp(self, debug=debug, profile=profile)
        self.examples_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")


    def check_sidif(self,sidif_path,file)->Context:
        """
        check the given SiDIF input
        """
        debug=self.debug
        context, error, errMsg = Context.fromSiDIF_input(sidif_path, debug=debug)
        self.assertFalse(error, f"Error in {file}: {errMsg}")
        self.assertIsNone(errMsg, f"Error message in {file}: {errMsg}")
        self.assertIsNotNone(context, f"Context is None for {file}")

        if debug:
            print(f"Processed: {file}")
            print(context)

        # Additional assertions to verify the context
        self.assertIsInstance(context, Context)
        self.assertTrue(len(context.topics) > 0, f"No topics found in {file}")

        # Check if all topics have names
        for topic in context.topics.values():
            self.assertTrue(hasattr(topic, 'name'), f"Topic without name in {file}")

        # Check if all properties have names and types
        for topic in context.topics.values():
            for key, prop in topic.properties.items():
                for needed_prop in ["name", "type", "showInGrid"]:
                    self.assertTrue(
                        hasattr(prop, needed_prop),
                        f"Property '{key}' missing attribute '{needed_prop}' in {file}"
                    )
        return context


    def testExamples(self):
        """
        Test all .sidif files in the ../examples directory
        """
        for root, _dirs, files in os.walk(self.examples_dir):
            for file in files:
                if file.endswith(".sidif"):
                    sidif_path = os.path.join(root, file)
                    with self.subTest(file=file):
                        self.check_sidif(sidif_path,file)


    def test_properties_by_index(self):
        """
        test the properties by index handling
        """
        sidif_file="infrastructure/infrastructure.sidif"
        sidif_path = os.path.join(self.examples_dir, sidif_file)
        context = self.check_sidif(sidif_path, sidif_file)
        debug=self.debug
        #debug=True
        for topic_name,topic in context.topics.items():
            props_dict=topic.propertiesDict()
            if debug:
                print(f"Properties Dict for {topic_name}:{topic.documentation}/{topic.wikiDocumentation}")
                for topic_name,(topic_name,props) in enumerate(props_dict.items()):
                    print(f"{topic_name}:")
                    for j,prop in enumerate(props):
                        print(f"  {j:3}:{prop.name} ({getattr(prop,'index','?')})")


    def testInheritance(self):
        """
        test inheritance
        """
        for sidif_file,topics in {
            "infrastructure/infrastructure.sidif": [
                ("Computer","name",["Device"]),
                ("Monitor","name",["Device"]),
                ("Printer","name",["Device"])
            ],
            "scientific-events/scientific-events.sidif":
                [("Event",  "name",["WebWdItem","WikidataItem"]),
                 ("Country","name",["WebWdItem","WikidataItem"]),
                 ("Region" ,"name",["WikidataItem"]),
                 ("Scholar","name",["WebWdItem","WikidataItem"]),
                ],
        }.items():
            sidif_path = os.path.join(self.examples_dir, sidif_file)
            context = self.check_sidif(sidif_path, sidif_file)
            debug=self.debug
            #debug=True
            for topic_name,concept_property_name,extends_list in topics:
                self.assertIn(topic_name, context.topics, f"Topic {topic_name} not found in {sidif_file}")
                topic = context.topics[topic_name]
                self.assertTrue(hasattr(topic, 'extends'), f"Topic {topic_name} in {sidif_file} does not have 'extends' attribute")
                if debug:
                    print(f"{topic_name} extends {topic.extends}")
                extends_topics=topic.get_extends_topics()
                self.assertEqual(len(extends_topics),len(extends_list),topic_name)
                for i,extends_topic in enumerate(extends_topics):
                    expected=extends_list[i]
                    if debug:
                        print(f"{i+1}:{extends_topic.name}={expected}?")
                    self.assertEqual(extends_topic.name,expected)
                props_by_index=topic.propertiesByIndex(to_root=True)
                if debug:
                    for i,prop in enumerate(props_by_index):
                        print(f"{i:3}:{prop.name} ({getattr(prop,'index','?')})")
                self.assertTrue(topic.conceptProperty is not None,topic.name)
                if self.debug:
                    print(f"{topic_name}.{topic.conceptProperty.name} is concept property")
                self.assertEqual(concept_property_name,topic.conceptProperty.name,topic.name)

                pass
            pass


    def testIssue18_readingFromSiDIF_input(self):
        """
        https://github.com/WolfgangFahl/py-sidif/issues/4
        add fromSiDIF_input api to allow reading Context from url or file_path via API
        """
        debug = self.debug
        # debug=True
        for url in [
            "https://raw.githubusercontent.com/WolfgangFahl/pyMetaModel/main/examples/city/city.sidif"
        ]:
            context, error, errMsg = Context.fromSiDIF_input(url, debug=debug)
            self.assertFalse(error)
            self.assertIsNone(errMsg)
            self.assertIsNotNone(context)
            if debug:
                print(context)
