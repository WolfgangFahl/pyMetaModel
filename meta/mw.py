'''
Created on 23.11.2022

@author: wf
'''
from dataclasses import dataclass
from wikibot.wikiuser import WikiUser
from wikibot.wikiclient import WikiClient
import mwparserfromhell
   
@dataclass
class MediaWikiContext():
    """Class for keeping track of MediaWiki Context"""
    wikiId:str
    wiki_url: str
    context:str 

    def sidif_url(self):
        """
        return the sidif url
        """
        url=f"{self.wiki_url}/index.php/{self.context}Context#sidif"
        return url
    
    def read_sidif(self,withLogin:bool=False)->str:
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
            if withLogin:
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
            
        