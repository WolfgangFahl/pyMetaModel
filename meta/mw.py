'''
Created on 23.11.2022

@author: wf
'''
from dataclasses import dataclass
from wikibot.wikiuser import WikiUser
from wikibot.wikiclient import WikiClient
from wikibot.smw import SMWClient
import mwparserfromhell
import datetime
   
@dataclass
class MediaWikiContext():
    """Class for keeping track of MediaWiki Context"""
    wikiId:str
    wiki_url: str
    context:str 
    since:datetime.datetime
    master:str

    def sidif_url(self):
        """
        return the sidif url
        """
        url=f"{self.wiki_url}/index.php/{self.context}#sidif"
        return url
    
    def read_sidif(self)->str:
        """
        
        Read the SiDIF for this Mediawiki context
        
        Args:
            withLogin(bool): if True login
            
        Returns:
            str: the SiDIF
        """
        sidif=None
        wikiusers=WikiUser.getWikiUsers(lenient=True)
        if self.wikiId in wikiusers:
            wikiUser=wikiusers[self.wikiId]
            self.wikiClient=WikiClient.ofWikiId(wikiUser.wikiId)
            if self.wikiClient.needsLogin():
                self.wikiClient.login()
            pageTitle=f"{self.context}"
            page=self.wikiClient.getPage(pageTitle)
            if page.exists:
                markup=page.text()
                mw_code=mwparserfromhell.parse(markup)
                sidif_sections=mw_code.get_sections(matches="sidif")
                if len(sidif_sections)!=1:
                    raise Exception(f"found {len(sidif_sections)} sidif sections but expected exactly 1")
                for node in sidif_sections[0].filter_tags(matches="source"):
                    sidif=str(node.contents)
        return sidif
    
class SMWAccess:
    """
    access to semantic MediaWiki
    """
    
    def __init__(self,wikiId:str="wiki",debug:bool=False):
        """
        constructor
        """
        self.wikiId=wikiId
        self.smw=self.getSMW(wikiId)
        self.debug=debug
        self.url=f"{self.wikiClient.wikiUser.getWikiUrl()}"
        
    def getSMW(self,wikiId:str):
        """
        get the semantic mediawiki access
        """
        self.wikiClient=WikiClient.ofWikiId(wikiId)
        if self.wikiClient.needsLogin():
            self.wikiClient.login()
        smw=SMWClient(self.wikiClient.getSite())
        return smw 
    
    def getMwContexts(self):
        """
        get the contexts
        """
        ask="""{{#ask: [[Concept:Context]]
|mainlabel=Context
| ?Context name = name
| ?Context since = since
| ?Context master = master

|sort=Context name
|order=ascending
}}"""
        mw_contexts={}
        context_records=self.smw.query(ask, "list of contexts")
        for context_name,context_record in context_records.items():
            if self.debug:
                print(context_record)
            mw_contexts[context_name]=MediaWikiContext(self.wikiId,
                self.url,context_name,
                context_record["since"],
                context_record["master"])
        return mw_contexts
        