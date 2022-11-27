'''
Created on 2022-11-23

@author: wf
'''
from datetime import datetime
from meta.mw import MediaWikiContext
from sidif.sidif import SiDIFParser
from lodstorage.jsonable import JSONAble
import sys

class MetaModelElement(JSONAble):
    '''
    a generic MetaModelElement
    
    to handle the technicalities of being a MetaModelElement so that derived
    MetaModelElements can focus on the MetaModel domain specific aspects
    '''
    
    def __init__(self):
        """
        construct me
        """
        self.__metamodel_props={}
        cls=self.__class__
        if hasattr(cls,"getSamples"):
            for sample in cls.getSamples():
                for key in sample.keys():
                    if not key in self.__metamodel_props:
                        self.__metamodel_props[key]=key # Property(self,key)
    
    def __str__(self):
        """
        get a string representation of me
        """
        text=self.__class__.__name__
        for prop_name in self.__metamodel_props.keys():
            if not isinstance(prop_name,str):
                pass
            elif hasattr(self,prop_name):
                value=getattr(self,prop_name)
                text+=f"\n  {prop_name}={str(value)}"
        return text
    
class Context(MetaModelElement):
    """
    A Context groups some topics like a Namespace/Package.
    This class provides helper functions and constants to render a Context to corresponding wiki pages
    """       
    
    def __init__(self):
        """
        constructor
        """
        MetaModelElement.__init__(self)
        self.topics={}
        self.errors=[]
    
    @classmethod
    def getSamples(cls):
        samples = [{
            "name": "MetaModel",
            "since": datetime.strptime("2015-01-23","%Y-%m-%d"),
            "copyright": "2015-2022 BITPlan GmbH",
            "master": "http://master.bitplan.com"
        }]
        return samples
    
    def error(self,msg):
        print(msg,file=sys.stderr)
        self.errors.append(msg)
        
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
            elif isA=="Topic":
                topic=Topic()
                topic.fromDict(record)
                if context is None:
                    context=Context()
                    context.name="GeneralContext"
                    context.since="2022-11-26"
                    context.master="http://master.bitplan.com"
                    context.error(f"topic {topic.name} has no defined context")
                if hasattr(topic, "name"):
                    context.topics[topic.name]=topic
                else:
                    context.error(f"missing name for topic {topic}")
            elif isA=="Property":
                prop=Property()
                prop.fromDict(record)
                if not hasattr(prop, "topic"):
                    context.error(f"prop  {prop} ha not topic")
                    continue
                topic_name=prop.topic
                if not hasattr(topic, "name"):
                    context.error(f"missing name for topic {topic}")
                    continue
                if topic_name in context.topics:
                    topic=context.topics[topic_name]
                    topic.properties[prop]=prop
                else:
                    context.error(f"topic {topic.name} not found in context {context.name} for property {prop.name}")
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
        sidif=None
        if debug:
            print(f"reading sidif for {mw_context.context} from {mw_context.wikiId}")
        try:
            sidif=mw_context.read_sidif()
        except BaseException as ex:
            error=ex
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
    
    
class Topic(MetaModelElement):
    """
    A Topic is a Concept/Class/Thing/Entity
    """
    
    def __init__(self):
        """
        constructor
        """
        MetaModelElement.__init__(self)
        self.properties={}
    
    @classmethod
    def getSamples(cls):
        samples = [{
                "pageTitle": "Concept:Topic",
                "name": "Topic",
                "pluralName": "Topics",
                "icon": "File:Topic_icon.png",
                "iconUrl": "/images/a/ae/Index.png",
                "documentation": "A Topic is a Concept/Class/Thing/Entity",
                "wikiDocumentation": "A Topic is a Concept/Class/Thing/Entity",
                "context": "MetaModel",
                "listLimit": 7,
                "cargo": True
                }]
        return samples
    
    def getPluralName(self)->str:
        """
        get the plural name for this topic
                
        Returns:
            str: the pluralname e.g. "Topics" for "Topic" or "Status" for "Status" or
            "Entities" for "Entity"
        """
        plural_name=self.pluralName if hasattr(self, "pluralName") else f"{self.name}s"
        return plural_name
    
    def getListLimit(self)->int:
        """
        get the list limit for this topic
        """
        listLimit=getattr(self,"listLimit",200)
        return listLimit
    
    
class Property(MetaModelElement):
    """
    Provides helper functions and constants for properties
    """
    @classmethod
    def getSamples(cls):
        samples = [{"name": "Title",
                "label": "Offical Name",
                "type": "Special:Types/Test",
                "index": 2,
                "sortPos": 2,
                "primaryKey": False,
                "mandatory": True,
                "namespace": "Test",
                "size": 25,
                "uploadable": False,
                "defaultValue": "Some Title",
                "inputType": "combobox",
                "allowedVaues": "Tile A, Title B",
                "documentation": " Documentation can contain\n line breaks",
                "values_from": "property=Title",
                "showInGrid": False,
                "isLink": False,
                "nullable": False,
                "topic": "Concept:Event"
                },
               # Properties that are not included in the MetaModel
               {"placeholder": "e.g. SMWCon",
                "regexp": "NaturalNumber",
                "usedFor": "Concept:Event, Concept:Event series",
                "pageTitle": "Property:Title"
                }]
        return samples