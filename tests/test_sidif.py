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
    def setUp(self, debug=True, profile=True):
        Basetest.setUp(self, debug=debug, profile=profile)
        self.examples_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")


    def check_sidif(self,sidif_path,file)->Context:
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
            for prop in topic.properties.values():
                self.assertTrue(hasattr(prop, 'name'), f"Property without name in {file}")
                self.assertTrue(hasattr(prop, 'type'), f"Property without type in {file}")
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

    def testInheritance(self):
        for sidif_file,topics in {
            "infrastructure/infrastructure.sidif": ["Computer","Monitor","Printer"],
            "scientific-events/scientific-events.sidif": ["Country","Region","Scholar"],
        }.items():
            sidif_path = os.path.join(self.examples_dir, sidif_file)
            context = self.check_sidif(sidif_path, sidif_file)

            for topic_name in topics:
                self.assertIn(topic_name, context.topics, f"Topic {topic_name} not found in {sidif_file}")
                topic = context.topics[topic_name]
                self.assertTrue(hasattr(topic, 'extends'), f"Topic {topic_name} in {sidif_file} does not have 'extends' attribute")
                if self.debug:
                    print(f"{topic_name} extends {topic.extends}")

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
