'''
Created on 2022-11-24

@author: wf
'''
from tests.basetest import Basetest
import os
from wikibot.wikiuser import WikiUser

class BaseMediawikiTest(Basetest):
    """
    special mediawiki tests
    """
    
    def setUp(self, debug=False, profile=True):
        Basetest.setUp(self, debug=debug, profile=profile)

    def getWikiUser(self, wikiId="ceur-ws", save=False):
        """
        supply media wiki user for the given wikiId
        """
        iniFile = WikiUser.iniFilePath(wikiId)
        wikiUser = None
        if not os.path.isfile(iniFile):
            wikiDict = None
            if wikiId == "royals":
                wikiDict = {"wikiId": wikiId, "email": "noreply@nouser.com", "url": "http://royal-family.bitplan.com",
                            "scriptPath": "", "version": "MediaWiki 1.35.5"}
            if wikiId == "cr":
                wikiDict = {"wikiId": wikiId, "email": "noreply@nouser.com", "url": "https://cr.bitplan.com",
                            "scriptPath": "", "version": "MediaWiki 1.35.5"}
            if wikiId == "ceur-ws":
                wikiDict = {"wikiId": wikiId, "email": "noreply@nouser.com",
                            "url": "https://ceur-ws.bitplan.com", "scriptPath": "/",
                            "version": "MediaWiki 1.35.5"}
            if wikiId == "wiki":
                wikiDict = {"wikiId": wikiId, "email": "noreply@nouser.com", "url": "https://wiki.bitplan.com",
                            "scriptPath": "/", "version": "MediaWiki 1.35.5"}
        
            if wikiDict is None:
                raise Exception(f"wikiId {wikiId} is not known")
            else:
                wikiUser = WikiUser.ofDict(wikiDict, lenient=True)
                if self.debug:
                    print(f"created wikiUser for {wikiId}")
                if save:
                    wikiUser.save()
                    if self.debug:
                        print(f"saved wikiUser for {wikiId}")
        else:
            wikiUser = WikiUser.ofWikiId(wikiId, lenient=True)
        return wikiUser
