"""
Created on 2023-02-25

@author: wf
"""

from meta.metamodel import Context
from tests.basetest import Basetest


class TestSiDIF(Basetest):
    """
    test plantuml handling
    """

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
