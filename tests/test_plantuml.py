"""
Created on 19.02.2023

@author: wf
"""

from urllib.request import urlopen

import xmltodict
from sidif.sidif import DataInterchange, SiDIFParser

from meta.uml import PlantUml
from tests.basetest import Basetest


class TestPlantUml(Basetest):
    """
    test plantuml handling
    """

    def setUp(self, debug=False, profile=True):
        Basetest.setUp(self, debug=debug, profile=profile)

    def testIssue4(self):
        """
        https://github.com/WolfgangFahl/py-sidif/issues/4
        convert dict tree to sidif
        """
        uri = "https://raw.githubusercontent.com/semstats/semstats.github.io/master/2019/ceur/workshop.xml"
        xml = urlopen(uri).read().decode()
        wsdict = xmltodict.parse(xml)
        if self.debug:
            print(wsdict)
        dif = DataInterchange.ofDict(wsdict, context="ceurws")
        sidifStr = dif.asSiDIF()
        if self.debug:
            print(sidifStr)
        self.assertTrue("workshop isA Topic" in sidifStr)
        self.assertTrue("homepage isA Property" in sidifStr)
        uml = PlantUml(
            title="CEUR-WS", copyRight="© Christoph Lange and contributors 2012–2020"
        )
        uml.fromDIF(dif)
        debug = self.debug
        #debug = True
        if debug:
            print(uml)
        self.assertTrue("""workshop " 1" -- "editors *" editor""" in uml.uml)

    def getDif(self, url, title: str="Presentation"):
        """
        """
        sp = SiDIFParser(debug=self.debug)
        parsed, error = sp.parseUrl(url, title=title)
        self.assertTrue(error is None)
        # self.debug=True
        if self.debug:
            sp.printResult(parsed)
        dif = parsed[0]
        return dif

    def getPlantUmlFromSidifUrl(self, url, title, copy_right, debug: bool = None):
        if debug is None:
            debug = self.debug
        dif = self.getDif(url, title)
        uml = PlantUml(title=title, copyRight=copy_right)
        uml.fromDIF(dif)
        if debug:
            print(uml)
        return uml

    def testIssue5(self):
        """
        https://github.com/WolfgangFahl/py-sidif/issues/5
        convert sidif to plantuml #5
        """
        self.baseUrl = "https://raw.githubusercontent.com/BITPlan/org.sidif.triplestore/master/src/test/resources/sidif"
        url = f"{self.baseUrl}/presentation.sidif"
        title = "Presentation"
        copy_right = "© BITPlan GmbH 2015-2024"
        uml = self.getPlantUmlFromSidifUrl(url, title, copy_right)
        self.assertTrue("package Presentation {" in uml.uml)
        self.assertTrue("class Icon {" in uml.uml)
        self.assertTrue("author:Text" in uml.uml)

    def testIssue25(self):
        """
        https://github.com/WolfgangFahl/pyMetaModel/issues/25
        support inheritance of topics

        """
        url = "https://raw.githubusercontent.com/WolfgangFahl/pyMetaModel/main/examples/infrastructure/infrastructure.sidif"
        title = "Infrastructure"
        copy_right = "© BITPlan GmbH 2024"
        uml = self.getPlantUmlFromSidifUrl(url, title, copy_right, debug=True)
        self.assertTrue("Harddisk extends Device" in uml.uml)
