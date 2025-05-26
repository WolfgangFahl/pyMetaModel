"""
Created on 2022-11-23

@author: wf
"""

import json

from wikibot3rd.wikiuser import WikiUser
from tqdm import tqdm
from meta.metamodel import Context
from tests.basesmwtest import BaseSemanticMediawikiTest


class TestMediawiki(BaseSemanticMediawikiTest):
    """
    test reading SiDIF from Mediawiki pages
    """

    def setUp(self, debug=False, profile=True):
        """
        setUp
        """
        BaseSemanticMediawikiTest.setUp(self, debug=debug, profile=profile)
        for wikiId in ["wiki", "royals", "cr"]:
            self.getSMWAccess(wikiId, save=True)

    def test_contexts(self):
        """
        test getting the list of mediawiki contexts
        """
        _smwAccess, mw_contexts = self.check_contexts("wiki")
        self.assertTrue(len(mw_contexts) >= 15)

    def test_conceptProperty(self):
        """
        test the conceptProperty handling
        """
        debug=self.debug
        cc = self.getContextContext()
        topic = cc.context.topics["Property"]
        self.assertIsNotNone(topic.conceptProperty)
        if debug:
            print(topic.conceptProperty)
        self.assertEqual("name", topic.conceptProperty.name)

    def test_sortProperties(self):
        """
        test the access to the list of sort properties
        """
        cc = self.getContextContext()
        topic = cc.context.topics["Property"]
        sorted_props = topic.sortProperties()
        self.assertEqual(1, len(sorted_props))
        sort_prop = sorted_props[0]
        self.assertEqual("name", sort_prop.name)

    def test_propertiesByIndex(self):
        """
        test the properties by Index access
        """
        debug=self.debug
        cc = self.getContextContext()
        topic = cc.context.topics["Topic"]
        props = topic.propertiesByIndex()
        if debug:
            for prop in props:
                print(f"{getattr(prop,'index','?')}:{prop.name}")
        self.assertEqual(13, len(props))
        self.assertTrue("pluralName", props[1].name)

    def testAskQuery4Topic(self):
        """
        test creating the ask query for a topic
        """
        debug = self.debug
        #debug = True
        cc = self.getContextContext()
        topic = cc.context.topics["Property"]
        ask_query = topic.askQuery()
        if debug:
            print(ask_query)

    def test_topicLinks(self):
        """
        test topic links
        """
        cc = self.getContextContext(wikiId="cr", context_name="CrSchema")
        city_topic = cc.context.topics["City"]
        stl = city_topic.sourceTopicLinks
        ttl = city_topic.targetTopicLinks
        debug = self.debug
        if debug:
            print(json.dumps(stl, indent=2, default=str))
            print(json.dumps(ttl, indent=2, default=str))
        self.assertEqual(1, len(stl))
        self.assertEqual(1, len(ttl))


    def test_Issue8(self):
        """
        https://github.com/WolfgangFahl/pyMetaModel/issues/3
        handle maintopic
        """
        debug = True
        wikiUsers = WikiUser.getWikiUsers(lenient=True)
        if "wiki" in wikiUsers:
            _smwAccess, mw_contexts = self.check_contexts("wiki")
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
        cc=self.getContextContext(context_name="Infrastructure")
        topic=cc.context.topics["Harddisk"]
        debug=self.debug
        #debug=True
        for filterShowInGrid in [False,True]:
            ask_query = topic.askQuery(filterShowInGrid=filterShowInGrid)

            if debug:
                print(f"showInGrid: {filterShowInGrid}")
                print(ask_query)
            self.assertTrue("|?Device name = name" in ask_query)
            if filterShowInGrid:
                self.assertFalse("purpose" in ask_query)


    def test_metamodel_from_wikis(self):
        """
        test reading meta models from wikis
        """
        debug = False
        lenient = True
        with_progress=False
        wiki_users = WikiUser.getWikiUsers(lenient=True)
        wiki_iter = tqdm(wiki_users, desc="Wikis") if with_progress else wiki_users
        for wikiId in wiki_iter:
            _smwAccess, mw_contexts = self.check_contexts(wikiId)
            for context_name in mw_contexts:
                context_info=f"{context_name}@{wikiId}"
                if debug:
                    print(f"reading context {context_info}")
                cc = self.getContextContext(wikiId=wikiId, context_name=context_name)
                context = cc.context
                if not lenient:
                    self.assertIsNotNone(context)
                else:
                    if context is None:
                        continue
                if debug:
                    print(f"{context_name} has context {context.name}")
                    print(context)
                    for _name, topic in context.topics.items():
                        print(topic)
                        for _name, prop in topic.properties.items():
                            print(prop)
                if len(context.errors) > 0:
                    for error in context.errors:
                        print(error)
                if not lenient:
                    self.assertEqual(0, len(context.errors))
                    self.assertEqual(context_name, context.name, wikiId)
