"""
Created on 2022-11-23

@author: wf
"""

from dataclasses import field
from datetime import datetime
import sys
from typing import List, Optional, Tuple, Dict
import typing

from basemkit.persistent_log import Log
from basemkit.yamlable import lod_storable
from meta.mw import MediaWikiContext
from meta.smw_type import SMW_Type
from sidif.sidif import SiDIFParser
import urllib3

# see also https://wiki.bitplan.com/index.php/PyMetaModel


@lod_storable
class Context:
    """
    A Context groups some topics like a Namespace/Package.
    This class provides helper functions and constants to render a Context to corresponding wiki pages
    """
    name: Optional[str] = None
    since: Optional[str] = None # isodate string
    updated: Optional[str] = None # isodate string
    copyright: Optional[str] = None
    master: Optional[str] = None
    demo: Optional[str] = None
    topics: Dict[str, 'Topic'] = field(default_factory=dict)
    types: Dict[str, 'Topic'] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.log=Log()
        pass

    @classmethod
    def getSamples(cls):
        samples = [
            {
                "name": "MetaModel",
                "since": datetime.strptime("2015-01-23", "%Y-%m-%d"),
                "updated": datetime.strptime("2024-08-07", "%Y-%m-%d"),
                "copyright": "2015-2025 BITPlan GmbH",
                "master": "https://contexts.bitplan.com",
                "demo": "https://wiki.bitplan.com/index.php/List_of_Contexts"
            }
        ]
        return samples

    def sanitize(self,key:str):
        """
        make sure my needed properties exist
        """
        if not hasattr(self,"name"):
            self.name=key
            pass
        pass

    def error(self, msg):
        print(msg, file=sys.stderr)
        self.errors.append(msg)

    def lookupTopic(self, topic_name: str, purpose: str) -> "Topic":
        """
        lookup the given topic_name in my topics for the given purpose

        Args:
            topic_name (str): the name of the topic to lookup
            purpose (str): the purpose to do the lookup for

        Returns:
            Topic: the topic if found else None and an error is added to my errors
        """
        if topic_name in self.topics:
            return self.topics[topic_name]
        else:
            self.error(
                f"""topic {topic_name} not found in context {getattr(self,"name","?")} for {purpose}"""
            )
            return None

    def propertyAlreadyDeclared(
        self, prop_name: str, topic: "Topic", purpose: str
    ) -> bool:
        """
        check whether the given property or role name is already Declared

        Args:
            prop_name (str): the property to check for duplicates
            topic (Topic): the topic to check
            purpose (str): the purpose to be displayed in error messages

        Returns:
            bool: True if this prop_name has already been use
        """
        in_use = prop_name in topic.properties or prop_name in topic.targetTopicLinks
        if in_use:
            self.error(
                f"duplicate name {prop_name} in topic {topic.name} for {purpose}"
            )
        return in_use

    def link_source_with_target(
        self, tl: "TopicLink", source: "Topic", target: "Topic"
    ):
        """
        link the source with the target via the given topicLink

        Args:
            tl (TopicLink): the topicLink
            source (Topic): the source Topic
            target (Topic): the target Topic
        """
        ok = True
        ok = ok and not self.propertyAlreadyDeclared(
            tl.sourceRole, target, f"{tl.name}"
        )
        ok = ok and not self.propertyAlreadyDeclared(
            tl.targetRole, source, f"{tl.name}"
        )
        if ok:
            # n:m handling with two lists on each side
            source.sourceTopicLinks[tl.sourceRole] = tl
            source.targetTopicLinks[tl.targetRole] = tl

    def addLink(self, tl: "TopicLink"):
        """
        link source and target of the given topicLink

        Args:
            tl (TopicLink): the topicLink
        """
        tl.sourceTopic = self.lookupTopic(tl.source, f"topicLink {tl.name}")
        tl.targetTopic = self.lookupTopic(tl.target, f"topicLink {tl.name}")
        if tl.targetTopic is not None and tl.sourceTopic is not None:
            self.link_source_with_target(tl, tl.sourceTopic, tl.targetTopic)

    def addProperty(self, prop: "Property") -> bool:
        """
        add the given property to this context

        Args:
            prop (Property): the property to add

        Returns:
            bool: True if the property adding was successful
        """
        if not hasattr(prop, "topic"):
            self.error(f"prop  {prop} has no topic")
            return False
        topic_name = prop.topic
        if not hasattr(prop, "name"):
            self.error(f"prop {prop} has no name")
            return False
        if not hasattr(prop, "type"):
            prop.type = "Text"
        topic = self.lookupTopic(topic_name, f"property {prop.name}")
        if topic:
            topic.properties[prop.name] = prop
            return True

    def createProperty4TopicLink(self, tl: "TopicLink") -> "Property":
        """
        create a property for the given topic link

        Args:
            tl (TopicLink):  the topiclink to create a property for
        """
        # see https://wiki.bitplan.com/index.php/SiDIFTemplates#properties
        prop = Property()
        prop.name = tl.sourceRole
        prop.label = prop.name
        if hasattr(tl, "sourceDocumentation"):
            prop.documentation = tl.sourceDocumentation
        else:
            prop.documentation = f"{prop.name}"
        prop.topic = tl.target
        prop.type = "Page"
        prop.topicLink = tl
        prop.isLink = True
        prop.showInGrid = False
        return prop

    @classmethod
    def fromDictOfDicts(cls, did: dict) -> "Context":
        """
        fill me from the given dict of dicts

        Args:
            did (dict): the dict of dicts

        Returns:
            Context: the context read
        """
        context = None
        for key, record in did.items():
            try:
                isA = record.get("isA")
                if isA == "Context":
                    context = Context.from_dict2(record)
                    context.sanitize(key)
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
                    tl = TopicLink.from_dict2(record)
                    context.addLink(tl)
                elif isA == "Property":
                    prop = Property.from_dict2(record)
                    prop.sanitize()
                    context.addProperty(prop)
                elif isA == "SMW_Type":
                    smw_type=SMW_Type.from_dict2(record) # @UndefinedVariable
                    context.types[smw_type.type]=smw_type
                else:  # isA == Topic or in declared topics
                    topic = Topic.from_dict2(record)
                    topic.sanitize()
                    if context is None:
                        context = Context()
                        context.name = "GlobalContext"
                        context.since = "2022-11-26"
                        context.master = "http://contexts.bitplan.com"
                        context.error(f"topic {topic.name} has no defined context")
                    if hasattr(topic, "name") and topic.name:
                        context.topics[topic.name] = topic
                        topic.context_obj=context
                    else:
                        # potential foreign or extends declaration
                        context.error(f"missing name for topic {topic} {key} - foreign declaration?")
            except Exception as ex:
                if context:
                    msg=f"invalid dict {record}: {str(ex)}"
                    context.log.log("❌","dict",msg)
                else:
                    raise ex
        # link topic to concepts and add topicLinks
        for topic in context.topics.values():
            topic.setConceptProperty()
            for _tl_name, tl in topic.targetTopicLinks.items():
                prop = context.createProperty4TopicLink(tl)
                context.addProperty(prop)
                pass
        return context

    @classmethod
    def fromSiDIF_input(cls, sidif_input: str, debug: bool = False)->Tuple['Context',str,str]:
        """
        initialize me from the given SiDIF input which might be a file path
        or url

        Args:
            sidif_input (str): path to local file or URL
            debug (bool): if True swith debugging on

        Returns:
            Tuple[Context,str,str]: context, error and errorMessage
        """
        if sidif_input.startswith("http:") or sidif_input.startswith("https:"):
            url = sidif_input
            http = urllib3.PoolManager()
            response = http.request("GET", url)
            sidif = response.data.decode("utf-8")
        else:
            sidif_path = sidif_input
            with open(sidif_path, "r") as sidif_file:
                sidif = sidif_file.read()
        return Context.fromSiDIF(sidif, title=sidif_input, debug=debug)

    @classmethod
    def fromSiDIF(
        cls, sidif: str, title: str, depth: int = None, debug: bool = False
    ) -> typing.Tuple["Context", object, str]:
        """
        initialize me from the given SiDIF markup

        Args:
            sidif (str): the SiDIF markup to parse
            title (str): the title for the SiDIF
            depth (int): the explain depth to show for the errorMessage
            debug (bool): if True handle debugging

        Returns:
            Tuple[Context,str,str]: context, error and errorMessage

        """
        errMsg = None
        context = None
        sp = SiDIFParser(debug=debug)
        parsed, error = sp.parseText(sidif, title, depth=depth)
        if debug:
            sp.printResult(parsed)
        if error is None:
            dif = parsed[0]
            did = dif.toDictOfDicts()
            context = Context.fromDictOfDicts(did)
            context.dif = dif
            context.did = did
        else:
            errMsg = sp.errorMessage(title, error, depth=depth)
        return context, error, errMsg

    @classmethod
    def fromWikiContext(
        cls, mw_context: MediaWikiContext, depth: int = None, debug: bool = False
    ) -> Tuple["Context", Optional[Exception], Optional[str]]:
        """
        initialize me from the given MediaWiki Context

        Args:
            mw_context (MediaWikiContext): the Mediawiki context
            depth (int): the explain depth to show for the errorMessage
            debug (bool): if True handle debugging

        Return:
            tuple(Context,Exception,str): the metamodel and potential parsing errors as Exception and error Message
        """
        context = None
        error = None
        errMsg = None
        sidif = None
        msg=f"reading sidif for {mw_context.context} from {mw_context.wikiId}"
        if debug:
            print(msg)
        try:
            sidif = mw_context.read_sidif()
        except BaseException as ex:
            error = ex
            errMsg = str(ex)
        if sidif is not None:
            context, error, errMsg = cls.fromSiDIF(
                sidif=sidif, title=mw_context.wikiId, depth=depth, debug=debug
            )
        else:
            errMsg=f"{msg} failed"
            error=ValueError(msg)
        return context, error, errMsg

@lod_storable
class Topic:
    """
    A Topic is a Concept/Class/Thing/Entity
    """
    name: Optional[str] = None
    _pluralName: Optional[str] = None
    icon: Optional[str] = None
    iconUrl: Optional[str] = None
    documentation: Optional[str] = None
    wikiDocumentation: Optional[str] = None
    defaultstoremode: str = "property"
    extends: Optional[str] = None
    listLimit: int = 200
    cargo:bool=False
    headerTabs:bool=False
    context: Optional[str] = None
    properties: Dict[str, 'Property'] = field(default_factory=dict)
    sourceTopicLinks: Dict[str, 'TopicLink'] = field(default_factory=dict)
    targetTopicLinks: Dict[str, 'TopicLink'] = field(default_factory=dict)
    # object references
    context_obj: Optional[Context] = None
    conceptProperty: Optional['Property'] = None


    def get_extends_topics(self, l: List['Topic'] = None) -> List['Topic']:
        """
        Get the topics this topic is extending.

        Args:
        l (List['Topic']): an optional list to extend. If None, a new list is created.

        Returns:
        List['Topic']: A list of topics that this topic extends.
        """
        if l is None:
            l = []

        extends = getattr(self, "extends", None)

        # recursive inheritance
        if extends:
            extends_topic = self.context_obj.lookupTopic(extends, purpose=f"extends")
            if extends_topic and extends_topic not in l:
                l.append(extends_topic)
                extends_topic.get_extends_topics(l)

        return l

    def get_all_properties(self) -> List['Property']:
        """
        Get all properties of the topic, including those inherited from extended topics.

        Returns:
            List[Property]: A list of all properties, including inherited ones.
        """
        all_properties = list(self.properties.values())

        # Get extended topics
        extended_topics = self.get_extends_topics()

        # Add properties from extended topics
        for extended_topic in extended_topics:
            for prop in extended_topic.properties.values():
                if prop.name not in [p.name for p in all_properties]:
                    all_properties.append(prop)

        return all_properties


    def sanitize(self):
        """
        make sure my properties exist note that name is not handled here
        on purpose since it needs special treatment
        """
        doc=self.documentation if hasattr(self, "documentation") else "?"
        if not hasattr(self, "wikiDocumentation") or not self.wikiDocumentation:
            self.wikiDocumentation=doc
        if not hasattr(self,"defaultstoremode"):
            self.defaultstoremode="property"
        pass

    @classmethod
    def getSamples(cls):
        samples = [
            {
                "pageTitle": "Concept:Topic",
                "name": "Topic",
                "pluralName": "Topics",
                "icon": "File:Topic_icon.png",
                "iconUrl": "/images/a/ae/Index.png",
                "documentation": "A Topic is a Concept/Class/Thing/Entity",
                "wikiDocumentation": "A Topic is a Concept/Class/Thing/Entity",
                "context": "MetaModel",
                "listLimit": 7,
                "cargo": True,
            }
        ]
        return samples

    def setConceptProperty(self):
        """
        set my concept property to any primary key or mandatory property
        """
        self.conceptProperty = None
        all_properties=self.propertiesByIndex(to_root=True)
        for prop in all_properties:
            mandatory = False
            primaryKey = False
            if hasattr(prop, "mandatory"):
                mandatory = prop.mandatory
            if hasattr(prop, "primaryKey"):
                primaryKey = prop.primaryKey
            if mandatory or primaryKey:
                self.conceptProperty = prop
                break

    @property
    def pluralName(self)->str:
        """
        Getter for pluralName.

        Returns:
            str: The plural name of the topic.
        """
        # Default behavior if _pluralName is not explicitly set
        return self._pluralName if self._pluralName is not None else f"{self.name}s"

    @pluralName.setter
    def pluralName(self, value):
        """
        Setter for pluralName.

        Args:
            value (str): The plural name to be set for the topic.
        """
        self._pluralName = value

    def getPluralName(self) -> str:
        """
        get the plural name for this topic

        Returns:
            str: the pluralname e.g. "Topics" for "Topic" or "Status" for "Status" or
            "Entities" for "Entity"
        """
        return self.pluralName

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
        all_properties=self.get_all_properties()
        for prop in all_properties:
            if hasattr(prop, "sortPos"):
                sortPos = prop.sortPos
                if sortPos:
                    prop_list.append(prop)
        prop_list = sorted(prop_list, key=lambda prop: prop.sortPos)
        return prop_list

    def propertiesDict(self) -> dict:
        """
        Return a dictionary mapping topic names to lists of properties,
        considering the inheritance chain and sorting properties locally by index.

        Returns:
            dict: A dictionary with topic names as keys and sorted lists of properties as values.
        """
        properties_dict = {}
        inheritance_chain = self.get_extends_topics()
        inheritance_chain.append(self)
        for topic in inheritance_chain:
            sorted_props=topic.propertiesByIndex(to_root=False)
            properties_dict[topic.name] = sorted_props

        return properties_dict


    def propertiesByIndex(self,to_root:bool=False) -> list:
        """
        Return the properties by index, considering inheritance chain.

        Args:
            to_root(bool): if True follow the inheritance chain to the root

        Returns:
            list: The list of properties sorted by index,
            with inheritance considered.
        """
        if to_root:
            sorted_props = []
            for _topic_name, props in self.propertiesDict().items():
                sorted_props.extend(props)
        else:
            props = list(self.properties.values())
            props_count = len(props)

            # Sort properties locally by index
            sorted_props = sorted(props, key=lambda p: p.index or props_count)

        return sorted_props


    def askSort(self) -> str:
        """
        generate the sort clause for my SMW ask query

        Returns:
            str: the generated wiki markup
        """
        sort = ""
        order = ""
        delim = ""
        sortproperties = self.sortProperties()
        for prop in sortproperties:
            direction = (
                "ascending" if getattr(prop, "sortAscending", True) else "descending"
            )
            sort += delim + f"{self.name} {prop.name}"
            order += delim + direction
            delim = ","
            pass
        sortClause = f"|sort={sort}\n" if sort else ""
        orderClause = f"|order={order}\n" if order else ""
        markup = f"{sortClause}{orderClause}"
        return markup

    def askQuery(
        self,
        mainlabel: str = None,
        filterShowInGrid: bool = True,
        listLimit: int = None,
        result_format: str="table"
    ) -> str:
        """
        Get the askQuery for the topic, considering inheritance.

        Args:
            mainlabel (str): the mainlabel to use - topic.name as default
            filterShowInGrid (bool): if True include only properties with showInGrid not being false
            listLimit (int): the list limit to use
        Returns:
            str: the markup for the query
        """
        if listLimit is None:
            listLimit = self.getListLimit()
        if mainlabel is None:
            mainlabel = self.name
        markup = f"""{{{{#ask: [[Concept:{self.name}]]
|mainlabel={mainlabel}
"""
        properties_dict = self.propertiesDict()
        for topic_name, properties in properties_dict.items():
            for prop in properties:
                if filterShowInGrid:
                    show=getattr(prop, "showInGrid",False)
                else:
                    show = True
                if show:
                    # Use the topic_name as prefix, which will be correct for inherited properties
                    markup += f"|?{topic_name} {prop.name} = {prop.name}\n"
        markup += f"|limit={listLimit}\n"
        markup += f"|format={result_format}\n"
        markup += f"""{self.askSort()}}}}}"""
        return markup

@lod_storable
class Property:
    """
    Provides helper functions and constants for properties
    """
    name: Optional[str] = None
    label: Optional[str] = None
    type: Optional[str] = None
    index: Optional[int] = None
    sortPos: Optional[int] = None
    primaryKey: bool = False
    mandatory: bool = False
    namespace: str = "Property"
    size: Optional[int] = None
    uploadable: bool = False
    defaultValue: Optional[str] = None
    inputType: Optional[str] = None
    allowedValues: Optional[str]=None
    documentation: Optional[str] = None
    values_from: Optional[str]=None
    formatterURI: Optional[str] = None # externalFormatterURI
    showInGrid: bool = True
    isLink: bool = False
    nullable: bool = False
    sortAscending: bool = True
    # Links
    topic: Optional[str] = None
    topicLink: Optional['TopicLink'] = None


    @classmethod
    def getSamples(cls):
        samples = [
            {
                "name": "Title",
                "label": "Offical Name",
                "type": "Special:Types/Text",
                "index": 2,
                "sortPos": 2,
                "primaryKey": False,
                "mandatory": True,
                "namespace": "Main",
                "scope": "Global",
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
                "topic": "Concept:Event",
            },
            {
                "name": "wikidataid",
                "type": "Special:Types/External identifier",
                "formatterURI": "https://www.wikidata.org/wiki/$1",
            },
            # Properties that are not included in the MetaModel
            {
                "placeholder": "e.g. SMWCon",
                "regexp": "NaturalNumber",
                "usedFor": "Concept:Event, Concept:Event series",
                "pageTitle": "Property:Title",
            },
        ]
        return samples


    def sanitize(self):
        """
        make sure attributes such as namespace are set properly
        """
        self.namespace="Property"
        self.topicLink=None
        if hasattr(self, "scope"):
            pass
        if not hasattr(self, "showInGrid"):
            self.showInGrid=True
        if not hasattr(self, "label"):
            self.label=getattr(self,"name")
        pass

@lod_storable
class TopicLink:
    """
    A TopicLink links two Concepts/Topics
    """

    name: Optional[str] = None
    source: Optional[str] = None
    sourceRole: Optional[str] = None
    sourceMultiple: bool = False
    sourceDocumentation: Optional[str] = None
    target: Optional[str] = None
    targetRole: Optional[str] = None
    targetMultiple: bool = False
    targetDocumentation: Optional[str] = None
    separator: Optional[str] = None

    # calculate objects
    sourceTopic: Optional[Topic] = None
    targetTopic: Optional[Topic] = None

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
                "target": "Property",
            },
            {
                "isA": "TopicLink",
                "name": "containedTopics",
                "sourceRole": "context",
                "sourceMultiple": False,
                "source": "Context",
                "targetRole": "topics",
                "targetMultiple": True,
                "target": "Topic",
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
                "targetDocumentation": "the smw_type being used by this property",
            },
        ]
        return samples
