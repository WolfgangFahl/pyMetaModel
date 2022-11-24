'''
Created on 2022-11-23

@author: wf
'''
from datetime import datetime
from dataclasses import dataclass
from meta.mw import MediaWikiContext
from sidif.sidif import SiDIFParser
from lodstorage.jsonable import JSONAble

class MetaModelElement(JSONAble):
    '''
    a generic MetaModelElement
    
    to handle the technicalities of being a MetaModelElement so that derived
    MetaModelElements can focus on the MetaModel domain specific aspects
    '''
    
class Context(MetaModelElement):
    """
    A Context groups some topics like a Namespace/Package.
    This class provides helper functions and constants to render a Context to corresponding wiki pages
    """
    
    @classmethod
    def getSamples(cls):
        samples = [{
            "name": "MetaModel",
            "since": datetime.strptime("2015-01-23","%Y-%m-%d"),
            "copyright": "2015-2022 BITPlan GmbH",
            "master": "http://master.bitplan.com"
        }]
        return samples
    
    def __init__(self,debug:bool=False):
        """
        constructor
        
        Args:
            debug(bool): if True handle debugging
        """
        self.debug=debug
        
    @classmethod
    def fromDictOfDicts(cls,did:dict)->'Context':
        """
        fill me from the given dict of dicts
        
        Args:
            did(dict): the dict of dicts
            
        Returns:
            Context: the context read
        """
        context=None
        for key,record in did.items():
            isA=record["isA"]
            if isA=="Context":
                context=Context()
                context.fromDict(record)
                pass
        return context
        
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
        context=None
        error=None
        if debug:
            print(f"reading sidif for {mw_context.context} from {mw_context.wikiId}")
        sidif=mw_context.read_sidif()
        if sidif is not None:
            sp = SiDIFParser(debug=debug)
            parsed, error = sp.parseText(sidif, mw_context.wikiId)
            if debug:
                sp.printResult(parsed)
            if error is None:
                dif=parsed[0]
                did=dif.toDictOfDicts()
                context=Context.fromDictOfDicts(did)
        return context,error
    
    
@dataclass
class Topic:
    name:str
    pluralName: str
    documentation: str
    context:Context