"""
Created on 2023-02-20

@author: wf
"""

from meta.metamodel_cmd import MetaModelCmd
from meta.sidif2linkml import SiDIF2LinkML
from tests.basemwtest import BaseMediawikiTest


class TestLinkML(BaseMediawikiTest):
    """
    test linkml handling

    https://linkml.io/
    """

    def setUp(self, debug=False, profile=True):
        """
        setUp
        """
        BaseMediawikiTest.setUp(self, debug=debug, profile=profile)
        for wikiId in ["wiki", "cr"]:
            self.getWikiUser(wikiId, save=True)

    def testSiDIF2LinkML(self):
        """
        test conversion from SiDIF to LinkML
        """
        debug = self.debug
        #debug = True
        parser = MetaModelCmd.getArgParser()
        mm_cmd = MetaModelCmd(debug=debug)
        for wikiId, context_name in [("wiki", "MetaModel"), ("cr", "CrSchema")]:
            args = parser.parse_args(["--wikiId", wikiId, "--context", context_name])
            mm_cmd.readContext(args)
            self.assertTrue(not mm_cmd.hasError())
            s2l = SiDIF2LinkML(mm_cmd.context)
            yaml_text = s2l.asYaml()
            if debug:
                print(yaml_text)
