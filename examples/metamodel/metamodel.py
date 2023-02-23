# Auto generated from metamodel.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-02-23T20:29:07
# Schema: MetaModel
#
# id: MetaModel
# description:
# license:

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.metamodelcore import Bool, Curie, Decimal, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
METAMODEL = CurieNamespace('MetaModel', 'MetaModel/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = METAMODEL


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = METAMODEL.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = METAMODEL.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = METAMODEL.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD.float
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = METAMODEL.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD.double
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = METAMODEL.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = METAMODEL.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time"
    type_model_uri = METAMODEL.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD.date
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = METAMODEL.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = METAMODEL.Datetime


class DateOrDatetime(str):
    """ Either a date or a datetime """
    type_class_uri = LINKML.DateOrDatetime
    type_class_curie = "linkml:DateOrDatetime"
    type_name = "date_or_datetime"
    type_model_uri = METAMODEL.DateOrDatetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = METAMODEL.Uriorcurie


class Curie(Curie):
    """ a compact URI """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "curie"
    type_model_uri = METAMODEL.Curie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = METAMODEL.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = METAMODEL.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX.iri
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = METAMODEL.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX.nonLiteral
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = METAMODEL.Nodeidentifier


# Class references



@dataclass
class Context(YAMLRoot):
    """
    A Context groups some topics like a Namespace/Package
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = METAMODEL.Context
    class_class_curie: ClassVar[str] = "MetaModel:Context"
    class_name: ClassVar[str] = "Context"
    class_model_uri: ClassVar[URIRef] = METAMODEL.Context

    name: Optional[str] = None
    since: Optional[str] = None
    updated: Optional[str] = None
    copyright: Optional[str] = None
    master: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.since is not None and not isinstance(self.since, str):
            self.since = str(self.since)

        if self.updated is not None and not isinstance(self.updated, str):
            self.updated = str(self.updated)

        if self.copyright is not None and not isinstance(self.copyright, str):
            self.copyright = str(self.copyright)

        if self.master is not None and not isinstance(self.master, str):
            self.master = str(self.master)

        super().__post_init__(**kwargs)


@dataclass
class Property(YAMLRoot):
    """
    a Property is a Feature/Attribute of a Topic
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = METAMODEL.Property
    class_class_curie: ClassVar[str] = "MetaModel:Property"
    class_name: ClassVar[str] = "Property"
    class_model_uri: ClassVar[URIRef] = METAMODEL.Property

    name: Optional[str] = None
    label: Optional[str] = None
    type: Optional[str] = None
    index: Optional[str] = None
    sortPos: Optional[str] = None
    primaryKey: Optional[str] = None
    mandatory: Optional[str] = None
    namespace: Optional[str] = None
    size: Optional[str] = None
    uploadable: Optional[str] = None
    defaultValue: Optional[str] = None
    inputType: Optional[str] = None
    allowedValues: Optional[str] = None
    documentation: Optional[str] = None
    values_from: Optional[str] = None
    externalFormatterURI: Optional[str] = None
    showInGrid: Optional[str] = None
    isLink: Optional[str] = None
    nullable: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.index is not None and not isinstance(self.index, str):
            self.index = str(self.index)

        if self.sortPos is not None and not isinstance(self.sortPos, str):
            self.sortPos = str(self.sortPos)

        if self.primaryKey is not None and not isinstance(self.primaryKey, str):
            self.primaryKey = str(self.primaryKey)

        if self.mandatory is not None and not isinstance(self.mandatory, str):
            self.mandatory = str(self.mandatory)

        if self.namespace is not None and not isinstance(self.namespace, str):
            self.namespace = str(self.namespace)

        if self.size is not None and not isinstance(self.size, str):
            self.size = str(self.size)

        if self.uploadable is not None and not isinstance(self.uploadable, str):
            self.uploadable = str(self.uploadable)

        if self.defaultValue is not None and not isinstance(self.defaultValue, str):
            self.defaultValue = str(self.defaultValue)

        if self.inputType is not None and not isinstance(self.inputType, str):
            self.inputType = str(self.inputType)

        if self.allowedValues is not None and not isinstance(self.allowedValues, str):
            self.allowedValues = str(self.allowedValues)

        if self.documentation is not None and not isinstance(self.documentation, str):
            self.documentation = str(self.documentation)

        if self.values_from is not None and not isinstance(self.values_from, str):
            self.values_from = str(self.values_from)

        if self.externalFormatterURI is not None and not isinstance(self.externalFormatterURI, str):
            self.externalFormatterURI = str(self.externalFormatterURI)

        if self.showInGrid is not None and not isinstance(self.showInGrid, str):
            self.showInGrid = str(self.showInGrid)

        if self.isLink is not None and not isinstance(self.isLink, str):
            self.isLink = str(self.isLink)

        if self.nullable is not None and not isinstance(self.nullable, str):
            self.nullable = str(self.nullable)

        super().__post_init__(**kwargs)


@dataclass
class SMWType(YAMLRoot):
    """
    an SMW_Type is a data type which determines the possible values for that type e.g. a Boolean can hold true/false
    values while a Number can hold 3.1459 or 20. A Page can hold the name of a Wiki page see
    https://semantic-mediawiki.org/wiki/Help:List_of_datatypes
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = METAMODEL.SMWType
    class_class_curie: ClassVar[str] = "MetaModel:SMWType"
    class_name: ClassVar[str] = "SMW_Type"
    class_model_uri: ClassVar[URIRef] = METAMODEL.SMWType

    type: Optional[str] = None
    documentation: Optional[str] = None
    id: Optional[str] = None
    helppage: Optional[str] = None
    typepage: Optional[str] = None
    javaType: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.documentation is not None and not isinstance(self.documentation, str):
            self.documentation = str(self.documentation)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.helppage is not None and not isinstance(self.helppage, str):
            self.helppage = str(self.helppage)

        if self.typepage is not None and not isinstance(self.typepage, str):
            self.typepage = str(self.typepage)

        if self.javaType is not None and not isinstance(self.javaType, str):
            self.javaType = str(self.javaType)

        super().__post_init__(**kwargs)


@dataclass
class Topic(YAMLRoot):
    """
    A Topic is a Concept/Class/Thing/Entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = METAMODEL.Topic
    class_class_curie: ClassVar[str] = "MetaModel:Topic"
    class_name: ClassVar[str] = "Topic"
    class_model_uri: ClassVar[URIRef] = METAMODEL.Topic

    name: Optional[str] = None
    pluralName: Optional[str] = None
    icon: Optional[str] = None
    iconUrl: Optional[str] = None
    documentation: Optional[str] = None
    wikiDocumentation: Optional[str] = None
    defaultstoremode: Optional[str] = None
    listLimit: Optional[str] = None
    cargo: Optional[str] = None
    headerTabs: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.pluralName is not None and not isinstance(self.pluralName, str):
            self.pluralName = str(self.pluralName)

        if self.icon is not None and not isinstance(self.icon, str):
            self.icon = str(self.icon)

        if self.iconUrl is not None and not isinstance(self.iconUrl, str):
            self.iconUrl = str(self.iconUrl)

        if self.documentation is not None and not isinstance(self.documentation, str):
            self.documentation = str(self.documentation)

        if self.wikiDocumentation is not None and not isinstance(self.wikiDocumentation, str):
            self.wikiDocumentation = str(self.wikiDocumentation)

        if self.defaultstoremode is not None and not isinstance(self.defaultstoremode, str):
            self.defaultstoremode = str(self.defaultstoremode)

        if self.listLimit is not None and not isinstance(self.listLimit, str):
            self.listLimit = str(self.listLimit)

        if self.cargo is not None and not isinstance(self.cargo, str):
            self.cargo = str(self.cargo)

        if self.headerTabs is not None and not isinstance(self.headerTabs, str):
            self.headerTabs = str(self.headerTabs)

        super().__post_init__(**kwargs)


@dataclass
class Action(YAMLRoot):
    """
    An action/function/operation to be performed
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = METAMODEL.Action
    class_class_curie: ClassVar[str] = "MetaModel:Action"
    class_name: ClassVar[str] = "Action"
    class_model_uri: ClassVar[URIRef] = METAMODEL.Action

    name: Optional[str] = None
    servicetype: Optional[str] = None
    service: Optional[str] = None
    inputtype: Optional[str] = None
    input: Optional[str] = None
    actionpage: Optional[str] = None
    output: Optional[str] = None
    engine: Optional[str] = None
    author: Optional[str] = None
    since: Optional[str] = None
    comment: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.servicetype is not None and not isinstance(self.servicetype, str):
            self.servicetype = str(self.servicetype)

        if self.service is not None and not isinstance(self.service, str):
            self.service = str(self.service)

        if self.inputtype is not None and not isinstance(self.inputtype, str):
            self.inputtype = str(self.inputtype)

        if self.input is not None and not isinstance(self.input, str):
            self.input = str(self.input)

        if self.actionpage is not None and not isinstance(self.actionpage, str):
            self.actionpage = str(self.actionpage)

        if self.output is not None and not isinstance(self.output, str):
            self.output = str(self.output)

        if self.engine is not None and not isinstance(self.engine, str):
            self.engine = str(self.engine)

        if self.author is not None and not isinstance(self.author, str):
            self.author = str(self.author)

        if self.since is not None and not isinstance(self.since, str):
            self.since = str(self.since)

        if self.comment is not None and not isinstance(self.comment, str):
            self.comment = str(self.comment)

        super().__post_init__(**kwargs)


@dataclass
class TopicLink(YAMLRoot):
    """
    A TopicLink links two Concepts
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = METAMODEL.TopicLink
    class_class_curie: ClassVar[str] = "MetaModel:TopicLink"
    class_name: ClassVar[str] = "TopicLink"
    class_model_uri: ClassVar[URIRef] = METAMODEL.TopicLink

    name: Optional[str] = None
    source: Optional[str] = None
    sourceRole: Optional[str] = None
    sourceMultiple: Optional[str] = None
    sourceDocumentation: Optional[str] = None
    target: Optional[str] = None
    targetRole: Optional[str] = None
    targetMultiple: Optional[str] = None
    targetDocumentation: Optional[str] = None
    masterDetail: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.source is not None and not isinstance(self.source, str):
            self.source = str(self.source)

        if self.sourceRole is not None and not isinstance(self.sourceRole, str):
            self.sourceRole = str(self.sourceRole)

        if self.sourceMultiple is not None and not isinstance(self.sourceMultiple, str):
            self.sourceMultiple = str(self.sourceMultiple)

        if self.sourceDocumentation is not None and not isinstance(self.sourceDocumentation, str):
            self.sourceDocumentation = str(self.sourceDocumentation)

        if self.target is not None and not isinstance(self.target, str):
            self.target = str(self.target)

        if self.targetRole is not None and not isinstance(self.targetRole, str):
            self.targetRole = str(self.targetRole)

        if self.targetMultiple is not None and not isinstance(self.targetMultiple, str):
            self.targetMultiple = str(self.targetMultiple)

        if self.targetDocumentation is not None and not isinstance(self.targetDocumentation, str):
            self.targetDocumentation = str(self.targetDocumentation)

        if self.masterDetail is not None and not isinstance(self.masterDetail, str):
            self.masterDetail = str(self.masterDetail)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.name = Slot(uri=METAMODEL.name, name="name", curie=METAMODEL.curie('name'),
                   model_uri=METAMODEL.name, domain=None, range=Optional[str])

slots.since = Slot(uri=METAMODEL.since, name="since", curie=METAMODEL.curie('since'),
                   model_uri=METAMODEL.since, domain=None, range=Optional[str])

slots.updated = Slot(uri=METAMODEL.updated, name="updated", curie=METAMODEL.curie('updated'),
                   model_uri=METAMODEL.updated, domain=None, range=Optional[str])

slots.copyright = Slot(uri=METAMODEL.copyright, name="copyright", curie=METAMODEL.curie('copyright'),
                   model_uri=METAMODEL.copyright, domain=None, range=Optional[str])

slots.master = Slot(uri=METAMODEL.master, name="master", curie=METAMODEL.curie('master'),
                   model_uri=METAMODEL.master, domain=None, range=Optional[str])

slots.label = Slot(uri=METAMODEL.label, name="label", curie=METAMODEL.curie('label'),
                   model_uri=METAMODEL.label, domain=None, range=Optional[str])

slots.type = Slot(uri=METAMODEL.type, name="type", curie=METAMODEL.curie('type'),
                   model_uri=METAMODEL.type, domain=None, range=Optional[str])

slots.index = Slot(uri=METAMODEL.index, name="index", curie=METAMODEL.curie('index'),
                   model_uri=METAMODEL.index, domain=None, range=Optional[str])

slots.sortPos = Slot(uri=METAMODEL.sortPos, name="sortPos", curie=METAMODEL.curie('sortPos'),
                   model_uri=METAMODEL.sortPos, domain=None, range=Optional[str])

slots.primaryKey = Slot(uri=METAMODEL.primaryKey, name="primaryKey", curie=METAMODEL.curie('primaryKey'),
                   model_uri=METAMODEL.primaryKey, domain=None, range=Optional[str])

slots.mandatory = Slot(uri=METAMODEL.mandatory, name="mandatory", curie=METAMODEL.curie('mandatory'),
                   model_uri=METAMODEL.mandatory, domain=None, range=Optional[str])

slots.namespace = Slot(uri=METAMODEL.namespace, name="namespace", curie=METAMODEL.curie('namespace'),
                   model_uri=METAMODEL.namespace, domain=None, range=Optional[str])

slots.size = Slot(uri=METAMODEL.size, name="size", curie=METAMODEL.curie('size'),
                   model_uri=METAMODEL.size, domain=None, range=Optional[str])

slots.uploadable = Slot(uri=METAMODEL.uploadable, name="uploadable", curie=METAMODEL.curie('uploadable'),
                   model_uri=METAMODEL.uploadable, domain=None, range=Optional[str])

slots.defaultValue = Slot(uri=METAMODEL.defaultValue, name="defaultValue", curie=METAMODEL.curie('defaultValue'),
                   model_uri=METAMODEL.defaultValue, domain=None, range=Optional[str])

slots.inputType = Slot(uri=METAMODEL.inputType, name="inputType", curie=METAMODEL.curie('inputType'),
                   model_uri=METAMODEL.inputType, domain=None, range=Optional[str])

slots.allowedValues = Slot(uri=METAMODEL.allowedValues, name="allowedValues", curie=METAMODEL.curie('allowedValues'),
                   model_uri=METAMODEL.allowedValues, domain=None, range=Optional[str])

slots.documentation = Slot(uri=METAMODEL.documentation, name="documentation", curie=METAMODEL.curie('documentation'),
                   model_uri=METAMODEL.documentation, domain=None, range=Optional[str])

slots.values_from = Slot(uri=METAMODEL.values_from, name="values_from", curie=METAMODEL.curie('values_from'),
                   model_uri=METAMODEL.values_from, domain=None, range=Optional[str])

slots.externalFormatterURI = Slot(uri=METAMODEL.externalFormatterURI, name="externalFormatterURI", curie=METAMODEL.curie('externalFormatterURI'),
                   model_uri=METAMODEL.externalFormatterURI, domain=None, range=Optional[str])

slots.showInGrid = Slot(uri=METAMODEL.showInGrid, name="showInGrid", curie=METAMODEL.curie('showInGrid'),
                   model_uri=METAMODEL.showInGrid, domain=None, range=Optional[str])

slots.isLink = Slot(uri=METAMODEL.isLink, name="isLink", curie=METAMODEL.curie('isLink'),
                   model_uri=METAMODEL.isLink, domain=None, range=Optional[str])

slots.nullable = Slot(uri=METAMODEL.nullable, name="nullable", curie=METAMODEL.curie('nullable'),
                   model_uri=METAMODEL.nullable, domain=None, range=Optional[str])

slots.id = Slot(uri=METAMODEL.id, name="id", curie=METAMODEL.curie('id'),
                   model_uri=METAMODEL.id, domain=None, range=Optional[str])

slots.helppage = Slot(uri=METAMODEL.helppage, name="helppage", curie=METAMODEL.curie('helppage'),
                   model_uri=METAMODEL.helppage, domain=None, range=Optional[str])

slots.typepage = Slot(uri=METAMODEL.typepage, name="typepage", curie=METAMODEL.curie('typepage'),
                   model_uri=METAMODEL.typepage, domain=None, range=Optional[str])

slots.javaType = Slot(uri=METAMODEL.javaType, name="javaType", curie=METAMODEL.curie('javaType'),
                   model_uri=METAMODEL.javaType, domain=None, range=Optional[str])

slots.pluralName = Slot(uri=METAMODEL.pluralName, name="pluralName", curie=METAMODEL.curie('pluralName'),
                   model_uri=METAMODEL.pluralName, domain=None, range=Optional[str])

slots.icon = Slot(uri=METAMODEL.icon, name="icon", curie=METAMODEL.curie('icon'),
                   model_uri=METAMODEL.icon, domain=None, range=Optional[str])

slots.iconUrl = Slot(uri=METAMODEL.iconUrl, name="iconUrl", curie=METAMODEL.curie('iconUrl'),
                   model_uri=METAMODEL.iconUrl, domain=None, range=Optional[str])

slots.wikiDocumentation = Slot(uri=METAMODEL.wikiDocumentation, name="wikiDocumentation", curie=METAMODEL.curie('wikiDocumentation'),
                   model_uri=METAMODEL.wikiDocumentation, domain=None, range=Optional[str])

slots.defaultstoremode = Slot(uri=METAMODEL.defaultstoremode, name="defaultstoremode", curie=METAMODEL.curie('defaultstoremode'),
                   model_uri=METAMODEL.defaultstoremode, domain=None, range=Optional[str])

slots.listLimit = Slot(uri=METAMODEL.listLimit, name="listLimit", curie=METAMODEL.curie('listLimit'),
                   model_uri=METAMODEL.listLimit, domain=None, range=Optional[str])

slots.cargo = Slot(uri=METAMODEL.cargo, name="cargo", curie=METAMODEL.curie('cargo'),
                   model_uri=METAMODEL.cargo, domain=None, range=Optional[str])

slots.headerTabs = Slot(uri=METAMODEL.headerTabs, name="headerTabs", curie=METAMODEL.curie('headerTabs'),
                   model_uri=METAMODEL.headerTabs, domain=None, range=Optional[str])

slots.servicetype = Slot(uri=METAMODEL.servicetype, name="servicetype", curie=METAMODEL.curie('servicetype'),
                   model_uri=METAMODEL.servicetype, domain=None, range=Optional[str])

slots.service = Slot(uri=METAMODEL.service, name="service", curie=METAMODEL.curie('service'),
                   model_uri=METAMODEL.service, domain=None, range=Optional[str])

slots.inputtype = Slot(uri=METAMODEL.inputtype, name="inputtype", curie=METAMODEL.curie('inputtype'),
                   model_uri=METAMODEL.inputtype, domain=None, range=Optional[str])

slots.input = Slot(uri=METAMODEL.input, name="input", curie=METAMODEL.curie('input'),
                   model_uri=METAMODEL.input, domain=None, range=Optional[str])

slots.actionpage = Slot(uri=METAMODEL.actionpage, name="actionpage", curie=METAMODEL.curie('actionpage'),
                   model_uri=METAMODEL.actionpage, domain=None, range=Optional[str])

slots.output = Slot(uri=METAMODEL.output, name="output", curie=METAMODEL.curie('output'),
                   model_uri=METAMODEL.output, domain=None, range=Optional[str])

slots.engine = Slot(uri=METAMODEL.engine, name="engine", curie=METAMODEL.curie('engine'),
                   model_uri=METAMODEL.engine, domain=None, range=Optional[str])

slots.author = Slot(uri=METAMODEL.author, name="author", curie=METAMODEL.curie('author'),
                   model_uri=METAMODEL.author, domain=None, range=Optional[str])

slots.comment = Slot(uri=METAMODEL.comment, name="comment", curie=METAMODEL.curie('comment'),
                   model_uri=METAMODEL.comment, domain=None, range=Optional[str])

slots.source = Slot(uri=METAMODEL.source, name="source", curie=METAMODEL.curie('source'),
                   model_uri=METAMODEL.source, domain=None, range=Optional[str])

slots.sourceRole = Slot(uri=METAMODEL.sourceRole, name="sourceRole", curie=METAMODEL.curie('sourceRole'),
                   model_uri=METAMODEL.sourceRole, domain=None, range=Optional[str])

slots.sourceMultiple = Slot(uri=METAMODEL.sourceMultiple, name="sourceMultiple", curie=METAMODEL.curie('sourceMultiple'),
                   model_uri=METAMODEL.sourceMultiple, domain=None, range=Optional[str])

slots.sourceDocumentation = Slot(uri=METAMODEL.sourceDocumentation, name="sourceDocumentation", curie=METAMODEL.curie('sourceDocumentation'),
                   model_uri=METAMODEL.sourceDocumentation, domain=None, range=Optional[str])

slots.target = Slot(uri=METAMODEL.target, name="target", curie=METAMODEL.curie('target'),
                   model_uri=METAMODEL.target, domain=None, range=Optional[str])

slots.targetRole = Slot(uri=METAMODEL.targetRole, name="targetRole", curie=METAMODEL.curie('targetRole'),
                   model_uri=METAMODEL.targetRole, domain=None, range=Optional[str])

slots.targetMultiple = Slot(uri=METAMODEL.targetMultiple, name="targetMultiple", curie=METAMODEL.curie('targetMultiple'),
                   model_uri=METAMODEL.targetMultiple, domain=None, range=Optional[str])

slots.targetDocumentation = Slot(uri=METAMODEL.targetDocumentation, name="targetDocumentation", curie=METAMODEL.curie('targetDocumentation'),
                   model_uri=METAMODEL.targetDocumentation, domain=None, range=Optional[str])

slots.masterDetail = Slot(uri=METAMODEL.masterDetail, name="masterDetail", curie=METAMODEL.curie('masterDetail'),
                   model_uri=METAMODEL.masterDetail, domain=None, range=Optional[str])

slots.context__name = Slot(uri=METAMODEL.name, name="context__name", curie=METAMODEL.curie('name'),
                   model_uri=METAMODEL.context__name, domain=None, range=Optional[str])

slots.context__since = Slot(uri=METAMODEL.since, name="context__since", curie=METAMODEL.curie('since'),
                   model_uri=METAMODEL.context__since, domain=None, range=Optional[str])

slots.context__updated = Slot(uri=METAMODEL.updated, name="context__updated", curie=METAMODEL.curie('updated'),
                   model_uri=METAMODEL.context__updated, domain=None, range=Optional[str])

slots.context__copyright = Slot(uri=METAMODEL.copyright, name="context__copyright", curie=METAMODEL.curie('copyright'),
                   model_uri=METAMODEL.context__copyright, domain=None, range=Optional[str])

slots.context__master = Slot(uri=METAMODEL.master, name="context__master", curie=METAMODEL.curie('master'),
                   model_uri=METAMODEL.context__master, domain=None, range=Optional[str])

slots.property__name = Slot(uri=METAMODEL.name, name="property__name", curie=METAMODEL.curie('name'),
                   model_uri=METAMODEL.property__name, domain=None, range=Optional[str])

slots.property__label = Slot(uri=METAMODEL.label, name="property__label", curie=METAMODEL.curie('label'),
                   model_uri=METAMODEL.property__label, domain=None, range=Optional[str])

slots.property__type = Slot(uri=METAMODEL.type, name="property__type", curie=METAMODEL.curie('type'),
                   model_uri=METAMODEL.property__type, domain=None, range=Optional[str])

slots.property__index = Slot(uri=METAMODEL.index, name="property__index", curie=METAMODEL.curie('index'),
                   model_uri=METAMODEL.property__index, domain=None, range=Optional[str])

slots.property__sortPos = Slot(uri=METAMODEL.sortPos, name="property__sortPos", curie=METAMODEL.curie('sortPos'),
                   model_uri=METAMODEL.property__sortPos, domain=None, range=Optional[str])

slots.property__primaryKey = Slot(uri=METAMODEL.primaryKey, name="property__primaryKey", curie=METAMODEL.curie('primaryKey'),
                   model_uri=METAMODEL.property__primaryKey, domain=None, range=Optional[str])

slots.property__mandatory = Slot(uri=METAMODEL.mandatory, name="property__mandatory", curie=METAMODEL.curie('mandatory'),
                   model_uri=METAMODEL.property__mandatory, domain=None, range=Optional[str])

slots.property__namespace = Slot(uri=METAMODEL.namespace, name="property__namespace", curie=METAMODEL.curie('namespace'),
                   model_uri=METAMODEL.property__namespace, domain=None, range=Optional[str])

slots.property__size = Slot(uri=METAMODEL.size, name="property__size", curie=METAMODEL.curie('size'),
                   model_uri=METAMODEL.property__size, domain=None, range=Optional[str])

slots.property__uploadable = Slot(uri=METAMODEL.uploadable, name="property__uploadable", curie=METAMODEL.curie('uploadable'),
                   model_uri=METAMODEL.property__uploadable, domain=None, range=Optional[str])

slots.property__defaultValue = Slot(uri=METAMODEL.defaultValue, name="property__defaultValue", curie=METAMODEL.curie('defaultValue'),
                   model_uri=METAMODEL.property__defaultValue, domain=None, range=Optional[str])

slots.property__inputType = Slot(uri=METAMODEL.inputType, name="property__inputType", curie=METAMODEL.curie('inputType'),
                   model_uri=METAMODEL.property__inputType, domain=None, range=Optional[str])

slots.property__allowedValues = Slot(uri=METAMODEL.allowedValues, name="property__allowedValues", curie=METAMODEL.curie('allowedValues'),
                   model_uri=METAMODEL.property__allowedValues, domain=None, range=Optional[str])

slots.property__documentation = Slot(uri=METAMODEL.documentation, name="property__documentation", curie=METAMODEL.curie('documentation'),
                   model_uri=METAMODEL.property__documentation, domain=None, range=Optional[str])

slots.property__values_from = Slot(uri=METAMODEL.values_from, name="property__values_from", curie=METAMODEL.curie('values_from'),
                   model_uri=METAMODEL.property__values_from, domain=None, range=Optional[str])

slots.property__externalFormatterURI = Slot(uri=METAMODEL.externalFormatterURI, name="property__externalFormatterURI", curie=METAMODEL.curie('externalFormatterURI'),
                   model_uri=METAMODEL.property__externalFormatterURI, domain=None, range=Optional[str])

slots.property__showInGrid = Slot(uri=METAMODEL.showInGrid, name="property__showInGrid", curie=METAMODEL.curie('showInGrid'),
                   model_uri=METAMODEL.property__showInGrid, domain=None, range=Optional[str])

slots.property__isLink = Slot(uri=METAMODEL.isLink, name="property__isLink", curie=METAMODEL.curie('isLink'),
                   model_uri=METAMODEL.property__isLink, domain=None, range=Optional[str])

slots.property__nullable = Slot(uri=METAMODEL.nullable, name="property__nullable", curie=METAMODEL.curie('nullable'),
                   model_uri=METAMODEL.property__nullable, domain=None, range=Optional[str])

slots.sMWType__type = Slot(uri=METAMODEL.type, name="sMWType__type", curie=METAMODEL.curie('type'),
                   model_uri=METAMODEL.sMWType__type, domain=None, range=Optional[str])

slots.sMWType__documentation = Slot(uri=METAMODEL.documentation, name="sMWType__documentation", curie=METAMODEL.curie('documentation'),
                   model_uri=METAMODEL.sMWType__documentation, domain=None, range=Optional[str])

slots.sMWType__id = Slot(uri=METAMODEL.id, name="sMWType__id", curie=METAMODEL.curie('id'),
                   model_uri=METAMODEL.sMWType__id, domain=None, range=Optional[str])

slots.sMWType__helppage = Slot(uri=METAMODEL.helppage, name="sMWType__helppage", curie=METAMODEL.curie('helppage'),
                   model_uri=METAMODEL.sMWType__helppage, domain=None, range=Optional[str])

slots.sMWType__typepage = Slot(uri=METAMODEL.typepage, name="sMWType__typepage", curie=METAMODEL.curie('typepage'),
                   model_uri=METAMODEL.sMWType__typepage, domain=None, range=Optional[str])

slots.sMWType__javaType = Slot(uri=METAMODEL.javaType, name="sMWType__javaType", curie=METAMODEL.curie('javaType'),
                   model_uri=METAMODEL.sMWType__javaType, domain=None, range=Optional[str])

slots.topic__name = Slot(uri=METAMODEL.name, name="topic__name", curie=METAMODEL.curie('name'),
                   model_uri=METAMODEL.topic__name, domain=None, range=Optional[str])

slots.topic__pluralName = Slot(uri=METAMODEL.pluralName, name="topic__pluralName", curie=METAMODEL.curie('pluralName'),
                   model_uri=METAMODEL.topic__pluralName, domain=None, range=Optional[str])

slots.topic__icon = Slot(uri=METAMODEL.icon, name="topic__icon", curie=METAMODEL.curie('icon'),
                   model_uri=METAMODEL.topic__icon, domain=None, range=Optional[str])

slots.topic__iconUrl = Slot(uri=METAMODEL.iconUrl, name="topic__iconUrl", curie=METAMODEL.curie('iconUrl'),
                   model_uri=METAMODEL.topic__iconUrl, domain=None, range=Optional[str])

slots.topic__documentation = Slot(uri=METAMODEL.documentation, name="topic__documentation", curie=METAMODEL.curie('documentation'),
                   model_uri=METAMODEL.topic__documentation, domain=None, range=Optional[str])

slots.topic__wikiDocumentation = Slot(uri=METAMODEL.wikiDocumentation, name="topic__wikiDocumentation", curie=METAMODEL.curie('wikiDocumentation'),
                   model_uri=METAMODEL.topic__wikiDocumentation, domain=None, range=Optional[str])

slots.topic__defaultstoremode = Slot(uri=METAMODEL.defaultstoremode, name="topic__defaultstoremode", curie=METAMODEL.curie('defaultstoremode'),
                   model_uri=METAMODEL.topic__defaultstoremode, domain=None, range=Optional[str])

slots.topic__listLimit = Slot(uri=METAMODEL.listLimit, name="topic__listLimit", curie=METAMODEL.curie('listLimit'),
                   model_uri=METAMODEL.topic__listLimit, domain=None, range=Optional[str])

slots.topic__cargo = Slot(uri=METAMODEL.cargo, name="topic__cargo", curie=METAMODEL.curie('cargo'),
                   model_uri=METAMODEL.topic__cargo, domain=None, range=Optional[str])

slots.topic__headerTabs = Slot(uri=METAMODEL.headerTabs, name="topic__headerTabs", curie=METAMODEL.curie('headerTabs'),
                   model_uri=METAMODEL.topic__headerTabs, domain=None, range=Optional[str])

slots.action__name = Slot(uri=METAMODEL.name, name="action__name", curie=METAMODEL.curie('name'),
                   model_uri=METAMODEL.action__name, domain=None, range=Optional[str])

slots.action__servicetype = Slot(uri=METAMODEL.servicetype, name="action__servicetype", curie=METAMODEL.curie('servicetype'),
                   model_uri=METAMODEL.action__servicetype, domain=None, range=Optional[str])

slots.action__service = Slot(uri=METAMODEL.service, name="action__service", curie=METAMODEL.curie('service'),
                   model_uri=METAMODEL.action__service, domain=None, range=Optional[str])

slots.action__inputtype = Slot(uri=METAMODEL.inputtype, name="action__inputtype", curie=METAMODEL.curie('inputtype'),
                   model_uri=METAMODEL.action__inputtype, domain=None, range=Optional[str])

slots.action__input = Slot(uri=METAMODEL.input, name="action__input", curie=METAMODEL.curie('input'),
                   model_uri=METAMODEL.action__input, domain=None, range=Optional[str])

slots.action__actionpage = Slot(uri=METAMODEL.actionpage, name="action__actionpage", curie=METAMODEL.curie('actionpage'),
                   model_uri=METAMODEL.action__actionpage, domain=None, range=Optional[str])

slots.action__output = Slot(uri=METAMODEL.output, name="action__output", curie=METAMODEL.curie('output'),
                   model_uri=METAMODEL.action__output, domain=None, range=Optional[str])

slots.action__engine = Slot(uri=METAMODEL.engine, name="action__engine", curie=METAMODEL.curie('engine'),
                   model_uri=METAMODEL.action__engine, domain=None, range=Optional[str])

slots.action__author = Slot(uri=METAMODEL.author, name="action__author", curie=METAMODEL.curie('author'),
                   model_uri=METAMODEL.action__author, domain=None, range=Optional[str])

slots.action__since = Slot(uri=METAMODEL.since, name="action__since", curie=METAMODEL.curie('since'),
                   model_uri=METAMODEL.action__since, domain=None, range=Optional[str])

slots.action__comment = Slot(uri=METAMODEL.comment, name="action__comment", curie=METAMODEL.curie('comment'),
                   model_uri=METAMODEL.action__comment, domain=None, range=Optional[str])

slots.topicLink__name = Slot(uri=METAMODEL.name, name="topicLink__name", curie=METAMODEL.curie('name'),
                   model_uri=METAMODEL.topicLink__name, domain=None, range=Optional[str])

slots.topicLink__source = Slot(uri=METAMODEL.source, name="topicLink__source", curie=METAMODEL.curie('source'),
                   model_uri=METAMODEL.topicLink__source, domain=None, range=Optional[str])

slots.topicLink__sourceRole = Slot(uri=METAMODEL.sourceRole, name="topicLink__sourceRole", curie=METAMODEL.curie('sourceRole'),
                   model_uri=METAMODEL.topicLink__sourceRole, domain=None, range=Optional[str])

slots.topicLink__sourceMultiple = Slot(uri=METAMODEL.sourceMultiple, name="topicLink__sourceMultiple", curie=METAMODEL.curie('sourceMultiple'),
                   model_uri=METAMODEL.topicLink__sourceMultiple, domain=None, range=Optional[str])

slots.topicLink__sourceDocumentation = Slot(uri=METAMODEL.sourceDocumentation, name="topicLink__sourceDocumentation", curie=METAMODEL.curie('sourceDocumentation'),
                   model_uri=METAMODEL.topicLink__sourceDocumentation, domain=None, range=Optional[str])

slots.topicLink__target = Slot(uri=METAMODEL.target, name="topicLink__target", curie=METAMODEL.curie('target'),
                   model_uri=METAMODEL.topicLink__target, domain=None, range=Optional[str])

slots.topicLink__targetRole = Slot(uri=METAMODEL.targetRole, name="topicLink__targetRole", curie=METAMODEL.curie('targetRole'),
                   model_uri=METAMODEL.topicLink__targetRole, domain=None, range=Optional[str])

slots.topicLink__targetMultiple = Slot(uri=METAMODEL.targetMultiple, name="topicLink__targetMultiple", curie=METAMODEL.curie('targetMultiple'),
                   model_uri=METAMODEL.topicLink__targetMultiple, domain=None, range=Optional[str])

slots.topicLink__targetDocumentation = Slot(uri=METAMODEL.targetDocumentation, name="topicLink__targetDocumentation", curie=METAMODEL.curie('targetDocumentation'),
                   model_uri=METAMODEL.topicLink__targetDocumentation, domain=None, range=Optional[str])

slots.topicLink__masterDetail = Slot(uri=METAMODEL.masterDetail, name="topicLink__masterDetail", curie=METAMODEL.curie('masterDetail'),
                   model_uri=METAMODEL.topicLink__masterDetail, domain=None, range=Optional[str])
