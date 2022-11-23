'''
Created on 2022-11-23

@author: wf
'''
from dataclasses import dataclass
from meta.mw import MediaWikiContext
from sidif.sidif import SiDIFParser

@dataclass
class Context:
    name:str

@dataclass
class Topic:
    name:str
    pluralName: str
    documentation: str
    context:Context
        
class MetaModel:
    """
    a MetaModel
    """
    
    def __init__(self,debug:bool=False):
        """
        constructor
        
        Args:
            debug(bool): if True handle debugging
        """
        self.debug=debug
        
    def fromDictOfDicts(self,did:dict):
        """
        fill me from the given dict of dicts
        
        Args:
            did(dict): the dict of dicts
        """
        for key,record in did.items():
            isA=record["isA"]
            pass
        
    @classmethod
    def fromWikiContext(cls,mw_context:MediaWikiContext,debug:bool=False)->'MetaModel':
        """
        initialize me from the given MediaWiki Context
        
        Args:
            mw_context(MediaWikiContext): the Mediawiki context
            debug(bool): if True handle debugging
            
        Return:
            MetaModel: the metamodel and potential parsing errors
        """
        mm=None
        sidif=mw_context.read_sidif()
        sp = SiDIFParser(debug=debug)
        parsed, error = sp.parseText(sidif, mw_context.wikiId)
        if debug:
            sp.printResult(parsed)
        if error is None:
            dif=parsed[0]
            did=dif.toDictOfDicts()
            mm=MetaModel(debug=debug)
            mm.fromDictOfDicts(did)
        return mm,error