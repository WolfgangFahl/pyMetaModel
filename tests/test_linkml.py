'''
Created on 2023-02-20

@author: wf
'''
from tests.basetest import Basetest
from meta.metamodel_cmd import MetaModelCmd
from meta.sidif2linkml import SiDIF2LinkML

class TestLinkML(Basetest):
    """
    test linkml handling
    
    https://linkml.io/
    """
    
    def testSiDIF2LinkML(self):
        """
        test conversion from SiDIF to LinkML
        """
        debug=self.debug
        debug=True
        mm_cmd=MetaModelCmd(debug=debug)
        for wikiId,context_name in [
            ("cr","CrSchema")
        ]:
            mm_cmd.readContext(wikiId, context_name)
            self.assertTrue(not mm_cmd.hasError())
            s2l=SiDIF2LinkML(mm_cmd.context)
            yaml_text=s2l.asYaml()
            if debug:
                print(yaml_text)