'''
Created on 19.02.2023

@author: wf
'''
from tests.basetest import Basetest
import xmltodict
from urllib.request import urlopen

from meta.uml import PlantUml
from sidif.sidif import DataInterchange, SiDIFParser

class TestPlantUml(Basetest):
    """
    test plantuml handling
    """
    def testIssue4(self):
        '''
        https://github.com/WolfgangFahl/py-sidif/issues/4
        convert dict tree to sidif
        '''
        uri="https://raw.githubusercontent.com/semstats/semstats.github.io/master/2019/ceur/workshop.xml"
        xml=urlopen(uri).read().decode()
        wsdict=xmltodict.parse(xml)
        if self.debug:
            print(wsdict)
        dif=DataInterchange.ofDict(wsdict,context="ceurws")
        sidifStr=dif.asSiDIF()
        if self.debug:
            print(sidifStr)
        self.assertTrue("workshop isA Topic" in sidifStr)
        self.assertTrue("homepage isA Property" in sidifStr)
        uml=PlantUml(title="CEUR-WS",copyRight="© Christoph Lange and contributors 2012–2020")
        uml.fromDIF(dif)
        if self.debug:
            print(uml)
        self.assertTrue('''workshop " 1" -- "editors *" editor''' in uml.uml)
  
    def getPresentation(self):
        '''
        get the SiDIF parse result for the presentation example
        '''
        self.baseUrl = "https://raw.githubusercontent.com/BITPlan/org.sidif.triplestore/master/src/test/resources/sidif"    
        url = f"{self.baseUrl}/presentation.sidif" 
        sp = SiDIFParser(debug=self.debug)
        parsed, error = sp.parseUrl(url, title="Presentation")
        self.assertTrue(error is None)
        #self.debug=True
        if self.debug:
            sp.printResult(parsed)
        dif=parsed[0]
        return dif
              
    def testIssue5(self):
        '''
        https://github.com/WolfgangFahl/py-sidif/issues/5
        convert sidif to plantuml #5
        '''
        dif=self.getPresentation()
        debug=self.debug
        #debug=True
        uml=PlantUml(title="Presentation",copyRight="© BITPlan GmbH 2015-2023")
        uml.fromDIF(dif)
        if debug:
            print (uml)
        self.assertTrue("package Presentation {" in uml.uml)
        self.assertTrue("class Icon {" in uml.uml)
        self.assertTrue("author:Text" in uml.uml)