"""
Created on 2022-11-23

@author: wf
"""
import json
import sys

from wikibot3rd.wikiuser import WikiUser

from meta.metamodel import Context
from meta.mw import SMWAccess
from tests.basemwtest import BaseMediawikiTest


class TestMediawiki(BaseMediawikiTest):
    """
    test reading SiDIF from Mediawiki pages
    """

    def setUp(self, debug=False, profile=True):
        """
        setUp
        """
        BaseMediawikiTest.setUp(self, debug=debug, profile=profile)
        for wikiId in ["wiki", "royals", "cr"]:
            self.getSMWAccess(wikiId, save=True)

    def check_contexts(self, wikiId: str, ignoreExceptions: bool = True):
        """
        check the mediawiki contexts  for the given wikiId

        Args:
            wikiId(str): the wikiId to check
            ignoreExceptions(bool): if True only print out a warning other wise raise exception
        """
        mw_contexts = {}
        try:
            smwAccess = self.smwAccessMap[wikiId]
            mw_contexts = smwAccess.getMwContexts()
            for name, mw_context in mw_contexts.items():
                print(f"{name}: {mw_context.sidif_url()}")
            print(f"found {len(mw_contexts)} Contexts")
        except Exception as ex:
            print(
                f"warning Mediawiki context for {wikiId} fetching failed due to {str(ex)}",
                file=sys.stderr,
            )
            if not ignoreExceptions:
                raise ex
        return mw_contexts

    def getContext(
        self, wikiId: str = "wiki", context_name: str = "MetaModel", debug: bool = False
    ):
        """
        get the default meta model context
        """
        mw_contexts = self.check_contexts(wikiId)
        mw_context = mw_contexts[context_name]
        context, error, errMsg = Context.fromWikiContext(mw_context, debug=debug)
        self.assertIsNone(error)
        return context

    def test_contexts(self):
        """
        test getting the list of mediawiki contexts
        """
        mw_contexts = self.check_contexts("wiki")
        self.assertTrue(len(mw_contexts) >= 15)

    def test_conceptProperty(self):
        """
        test the conceptProperty handling
        """
        debug = self.debug
        context = self.getContext(debug=debug)
        topic = context.topics["Property"]
        self.assertIsNotNone(topic.conceptProperty)
        if debug:
            print(topic.conceptProperty)
        self.assertEqual("name", topic.conceptProperty.name)

    def test_sortProperties(self):
        """
        test the access to the list of sort properties
        """
        debug = self.debug
        context = self.getContext(debug=debug)
        topic = context.topics["Property"]
        sorted_props = topic.sortProperties()
        self.assertEqual(1, len(sorted_props))
        sort_prop = sorted_props[0]
        self.assertEqual("name", sort_prop.name)

    def test_propertiesByIndex(self):
        """
        test the properties by Index access
        """
        debug = self.debug
        context = self.getContext(debug=debug)
        topic = context.topics["Topic"]
        props = topic.propertiesByIndex()
        if debug:
            for prop in props:
                print(f"{prop.index}:{prop.name}")
        self.assertEqual(11, len(props))
        self.assertTrue("pluralName", props[1].name)

    def testAskQuery4Topic(self):
        """
        test creating the ask query for a topic
        """
        debug = self.debug
        debug = True
        context = self.getContext(debug=debug)
        topic = context.topics["Property"]
        ask_query = topic.askQuery()
        if debug:
            print(ask_query)

    def test_topicLinks(self):
        """
        test topic links
        """
        debug = False
        context = self.getContext(wikiId="cr", context_name="CrSchema", debug=debug)
        city_topic = context.topics["City"]
        stl = city_topic.sourceTopicLinks
        ttl = city_topic.targetTopicLinks
        debug = True
        if debug:
            print(json.dumps(stl, indent=2, default=str))
            print(json.dumps(ttl, indent=2, default=str))
        self.assertEqual(1, len(stl))
        self.assertEqual(1, len(ttl))

    def test_Issue3(self):
        """
        https://github.com/WolfgangFahl/pyMetaModel/issues/3
        """
        return
        debug = True
        wikiUsers = WikiUser.getWikiUsers(lenient=True)
        if "test" in wikiUsers:
            mw_contexts = self.check_contexts("test")
            tc = mw_contexts["Training"]
            context, error, errMsg = Context.fromWikiContext(tc, debug=self.debug)
            self.assertIsNotNone(context)
            self.assertIsNone(error)
            # changed 2022-12-04 since error doesn't happen any more
        #    errorMessage=SiDIFParser.errorMessage("Training context parsing error",error)
        #    if debug:
        #        print(errorMessage)
        #    self.assertTrue("property Qualität" in errorMessage)

    def test_Issue8(self):
        """
        https://github.com/WolfgangFahl/pyMetaModel/issues/3
        handle maintopic
        """
        debug = True
        wikiUsers = WikiUser.getWikiUsers(lenient=True)
        if "wiki" in wikiUsers:
            mw_contexts = self.check_contexts("wiki")
            mw_context = mw_contexts["OpenSourceProjectsContext"]
            context, error, errMsg = Context.fromWikiContext(mw_context, debug=debug)
            self.assertIsNone(error)
            self.assertIsNone(errMsg)
            self.assertTrue("OsProject" in context.topics)
            pass

    def test_Issue23(self):
        """
        https://github.com/WolfgangFahl/pyMetaModel/issues/23
        handle "showInGrid"
        """

    def test_metamodel_from_wikis(self):
        """
        test reading meta models from wikis
        """
        debug = False
        lenient = True
        for wikiId in WikiUser.getWikiUsers(lenient=True):
            mw_contexts = self.check_contexts(wikiId)
            for name, mw_context in mw_contexts.items():
                if debug:
                    print(f"reading context {name} from wiki {wikiId}")
                context, error, errMsg = Context.fromWikiContext(
                    mw_context, debug=debug
                )
                if not lenient:
                    self.assertIsNotNone(context)
                else:
                    if context is None:
                        continue
                if debug:
                    print(f"{mw_context.context} has context {context.name}")
                    print(context)
                    for _name, topic in context.topics.items():
                        print(topic)
                        for _name, property in topic.properties.items():
                            print(property)
                if error is not None:
                    print(error)
                if len(context.errors) > 0:
                    for error in context.errors:
                        print(error)
                if not lenient:
                    self.assertIsNone(error)
                    self.assertEqual(0, len(context.errors))
                    self.assertEqual(mw_context.context, context.name, wikiId)
