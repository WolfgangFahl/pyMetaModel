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
        self.__metamodel_props = {}
        cls = self.__class__
        if hasattr(cls, "getSamples"):
            for sample in cls.getSamples():
                for key in sample.keys():
                    if not key in self.__metamodel_props:
                        self.__metamodel_props[key] = key  # Property(self,key)
    
    def __str__(self):
        """
        get a string representation of me
        """
        text = self.__class__.__name__
        for prop_name in self.__metamodel_props.keys():
            if not isinstance(prop_name, str):
                pass
            elif hasattr(self, prop_name):
                value = getattr(self, prop_name)
                text += f"\n  {prop_name}={str(value)}"
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
        self.topics = {}
        self.errors = []
    
    @classmethod
    def getSamples(cls):
        samples = [{
            "name": "MetaModel",
            "since": datetime.strptime("2015-01-23", "%Y-%m-%d"),
            "copyright": "2015-2022 BITPlan GmbH",
            "master": "http://master.bitplan.com"
        }]
        return samples
    
    def error(self, msg):
        print(msg, file=sys.stderr)
        self.errors.append(msg)
        
    def lookupTopic(self,topic_name:str,purpose:str)->'Topic':
        """
        lookup the given topic_name in my topics for the given purpose
        
        Args:
            topic_name(str): the name of the topic to lookup
            purpose(str): the purpose to do the lookup for
        
        Returns:
            Topic: the topic if found else None and an error is added to my errors
        """
        if topic_name in self.topics:
            return self.topics[topic_name]
        else:
            self.error(f"""topic {topic_name} not found in context {getattr(self,"name","?")} for {purpose}""")
            return None
        
    def propertyAlreadyDeclared(self,prop_name:str,topic:'Topic',purpose:str)->bool:
        """
        check whether the given property or role name is already Declared
        
        Args:
            prop_name(str): the property to check for duplicates
            topic(Topic): the topic to check
            purpose(str): the purpose to be displayed in error messages
            
        Returns:
            bool: True if this prop_name has already been use
        """
        in_use=prop_name in topic.properties or prop_name in topic.targetTopicLinks
        if in_use:
            self.error(f"duplicate name {prop_name} in topic {topic.name} for {purpose}")
        return in_use
        
    def link_source_with_target(self,tl:'TopicLink',source:'Topic',target:'Topic'):
        """
        link the source with the target via the given topicLink
        
        Args:
            tl(TopicLink): the topicLink
            source(Topic): the source Topic
            target(Topic): the target Topic
        """
        ok=True
        ok=ok and not self.propertyAlreadyDeclared(tl.sourceRole,target,f"{tl.name}")
        ok=ok and not self.propertyAlreadyDeclared(tl.targetRole,source,f"{tl.name}")
        if ok:
            # n:m handling with two lists on each side
            source.sourceTopicLinks[tl.sourceRole]=tl
            source.targetTopicLinks[tl.targetRole]=tl
    

    def addLink(self,tl:'TopicLink'):
        """
        link source and target of the given topicLink
         
        Args:
            tl(TopicLink): the topicLink
            context(Context): the context in which the link "lives"
        """
        tl.sourceTopic=self.lookupTopic(tl.source,f"topicLink {tl.name}")
        tl.targetTopic=self.lookupTopic(tl.target,f"topicLink {tl.name}")
        if tl.targetTopic is not None and tl.sourceTopic is not None:
            self.link_source_with_target(tl, tl.sourceTopic, tl.targetTopic)      
        
    @classmethod
    def fromDictOfDicts(cls, did:dict) -> 'Context':
        """
        fill me from the given dict of dicts
        
        Args:
            did(dict): the dict of dicts
            
        Returns:
            Context: the context read
        """
        context = None
        for key, record in did.items():
            isA = record["isA"]
            if isA == "Context":
                context = Context()
                context.fromDict(record)
            elif isA == "Topic":
                topic = Topic()
                topic.fromDict(record)
                if context is None:
                    context = Context()
                    context.name = "GeneralContext"
                    context.since = "2022-11-26"
                    context.master = "http://master.bitplan.com"
                    context.error(f"topic {topic.name} has no defined context")
                if hasattr(topic, "name"):
                    context.topics[topic.name] = topic
                else:
                    context.error(f"missing name for topic {topic}")
            elif isA == "TopicLink":
                """
# Event n : 1 City
Event_in_City isA TopicLink
"eventInCity" is name of it
"city" is sourceRole of it
false is sourceMultiple of it
"City" is source of it
"event" is targetRole of it
true is targetMultiple of it
"Event" is target of it 
                """
                tl=TopicLink()
                tl.fromDict(record)
                context.addLink(tl)
            elif isA == "Property":
                prop = Property()
                prop.fromDict(record)
                if not hasattr(prop, "topic"):
                    context.error(f"prop  {prop} has no topic")
                    continue
                topic_name = prop.topic
                if not hasattr(prop, "name"):
                    context.error(f"prop {prop} has no name")
                    continue
                topic=context.lookupTopic(topic_name,f"property {prop.name}")
                if topic:
                    topic.properties[prop.name] = prop
        return context
        
    @classmethod
    def fromWikiContext(cls, mw_context:MediaWikiContext, depth:int=None,debug:bool=False) -> 'MetaModel':
        """
        initialize me from the given MediaWiki Context
        
        Args:
            mw_context(MediaWikiContext): the Mediawiki context
            depth(int): the explain depth to show for the errorMessage
            debug(bool): if True handle debugging
            
        Return:
            tuple(MetaModel,Exception,str): the metamodel and potential parsing errors as Exception and error Message
        """
        context = None
        error = None
        errMsg = None
        sidif = None
        if debug:
            print(f"reading sidif for {mw_context.context} from {mw_context.wikiId}")
        try:
            sidif = mw_context.read_sidif()
        except BaseException as ex:
            error = ex
            errMsg=str(ex)
        if sidif is not None:
            sp = SiDIFParser(debug=debug)
            parsed, error = sp.parseText(sidif, mw_context.wikiId,depth=depth)
            if debug:
                sp.printResult(parsed)
            if error is None:
                dif = parsed[0]
                did = dif.toDictOfDicts()
                context = Context.fromDictOfDicts(did)
            else:
                errMsg=sp.errorMessage(mw_context.wikiId,error, depth=depth)
        return context, error,errMsg
    
class Topic(MetaModelElement):
    """
    A Topic is a Concept/Class/Thing/Entity
    """
    
    def __init__(self):
        """
        constructor
        """
        MetaModelElement.__init__(self)
        self.properties = {}
        self.sourceTopicLinks={}
        self.targetTopicLinks={}
    
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
    
    def getPluralName(self) -> str:
        """
        get the plural name for this topic
                
        Returns:
            str: the pluralname e.g. "Topics" for "Topic" or "Status" for "Status" or
            "Entities" for "Entity"
        """
        plural_name = self.pluralName if hasattr(self, "pluralName") else f"{self.name}s"
        return plural_name
    
    def getListLimit(self) -> int:
        """
        get the list limit for this topic
        """
        listLimit = getattr(self, "listLimit", 200)
        return listLimit
    
    def sortProperties(self) -> list:
        """
        get the properties that we should sort by
        
        Returns:
            list: a list of properties in sort order
        """
        prop_list = []
        for prop in self.properties.values():
            if hasattr(prop, "sortPos"):
                sortPos = prop.sortPos
                if sortPos:
                    prop_list.append(prop)
        prop_list = sorted(prop_list, key=lambda prop: prop.sortPos)
        return prop_list
    
    def propertiesByIndex(self) ->list:
        """
        return the properties by index
        
        Returns:
            list: the list of properties sorted by index
        """
        def index(prop:'Property')->int:
            if hasattr(prop,"index"):
                return int(prop.index)
            else:
                return sys.maxsize
        prop_list=sorted(self.properties.values(),key=lambda prop:index(prop))
        return prop_list

    
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

    
class TopicLink(MetaModelElement):
    """
    A TopicLink links two Concepts/Topics
    """

    @classmethod
    def getSamples(cls):
        samples = [
            {
                "isA": "TopicLink",
                "name": "containedProperties",
                "sourceRole": "topic",
                "sourceMultiple": False,
                "source": "Topic",
                "targetRole": "properties",
                "targetMultiple": True,
                "target": "Property"
            },
            {
                "isA": "TopicLink",
                "name": "containedTopics",
                "sourceRole": "context",
                "sourceMultiple": False,
                "source": "Context",
                "targetRole": "topics",
                "targetMultiple": True,
                "target": "Topic"
            },
            {
                "isA": "TopicLink",
                "name": "typeOfProperty",
                "sourceRole": "usedByProperties",
                "sourceMultiple": True,
                "source": "Property",
                "sourceDocumentation": "the properties having this type",
                "targetRole": "smw_type",
                "targetMultiple": False,
                "target": "SMW_Type",
                "masterDetail": False,
                "targetDocumentation": "the smw_type being used by this property"
            }    
        ]
        return samples
