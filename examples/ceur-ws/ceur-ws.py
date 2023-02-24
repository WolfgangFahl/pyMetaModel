# Auto generated from ceur-ws.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-02-24T09:05:31
# Schema: CeurwsSchema
#
# id: CeurwsSchema
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
CEURWSSCHEMA = CurieNamespace('CeurwsSchema', 'CeurwsSchema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CEURWSSCHEMA


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = CEURWSSCHEMA.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = CEURWSSCHEMA.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = CEURWSSCHEMA.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD.float
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = CEURWSSCHEMA.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD.double
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = CEURWSSCHEMA.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = CEURWSSCHEMA.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time"
    type_model_uri = CEURWSSCHEMA.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD.date
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = CEURWSSCHEMA.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = CEURWSSCHEMA.Datetime


class DateOrDatetime(str):
    """ Either a date or a datetime """
    type_class_uri = LINKML.DateOrDatetime
    type_class_curie = "linkml:DateOrDatetime"
    type_name = "date_or_datetime"
    type_model_uri = CEURWSSCHEMA.DateOrDatetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = CEURWSSCHEMA.Uriorcurie


class Curie(Curie):
    """ a compact URI """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "curie"
    type_model_uri = CEURWSSCHEMA.Curie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = CEURWSSCHEMA.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = CEURWSSCHEMA.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX.iri
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = CEURWSSCHEMA.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX.nonLiteral
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = CEURWSSCHEMA.Nodeidentifier


# Class references



@dataclass
class Volume(YAMLRoot):
    """
    A Volume is a collection of papers mostly documenting the results of an academic event
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CEURWSSCHEMA.Volume
    class_class_curie: ClassVar[str] = "CeurwsSchema:Volume"
    class_name: ClassVar[str] = "Volume"
    class_model_uri: ClassVar[URIRef] = CEURWSSCHEMA.Volume

    number: Optional[str] = None
    title: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.number is not None and not isinstance(self.number, str):
            self.number = str(self.number)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass
class Session(YAMLRoot):
    """
    A Session is a a collection of papers as part of a Volume
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CEURWSSCHEMA.Session
    class_class_curie: ClassVar[str] = "CeurwsSchema:Session"
    class_name: ClassVar[str] = "Session"
    class_model_uri: ClassVar[URIRef] = CEURWSSCHEMA.Session

    title: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass
class Paper(YAMLRoot):
    """
    A paper is e.g. a scholarly article
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CEURWSSCHEMA.Paper
    class_class_curie: ClassVar[str] = "CeurwsSchema:Paper"
    class_name: ClassVar[str] = "Paper"
    class_model_uri: ClassVar[URIRef] = CEURWSSCHEMA.Paper

    id: Optional[str] = None
    title: Optional[str] = None
    authors: Optional[str] = None
    pdfUrl: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.authors is not None and not isinstance(self.authors, str):
            self.authors = str(self.authors)

        if self.pdfUrl is not None and not isinstance(self.pdfUrl, str):
            self.pdfUrl = str(self.pdfUrl)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.number = Slot(uri=CEURWSSCHEMA.number, name="number", curie=CEURWSSCHEMA.curie('number'),
                   model_uri=CEURWSSCHEMA.number, domain=None, range=Optional[str])

slots.title = Slot(uri=CEURWSSCHEMA.title, name="title", curie=CEURWSSCHEMA.curie('title'),
                   model_uri=CEURWSSCHEMA.title, domain=None, range=Optional[str])

slots.id = Slot(uri=CEURWSSCHEMA.id, name="id", curie=CEURWSSCHEMA.curie('id'),
                   model_uri=CEURWSSCHEMA.id, domain=None, range=Optional[str])

slots.authors = Slot(uri=CEURWSSCHEMA.authors, name="authors", curie=CEURWSSCHEMA.curie('authors'),
                   model_uri=CEURWSSCHEMA.authors, domain=None, range=Optional[str])

slots.pdfUrl = Slot(uri=CEURWSSCHEMA.pdfUrl, name="pdfUrl", curie=CEURWSSCHEMA.curie('pdfUrl'),
                   model_uri=CEURWSSCHEMA.pdfUrl, domain=None, range=Optional[str])

slots.volume__number = Slot(uri=CEURWSSCHEMA.number, name="volume__number", curie=CEURWSSCHEMA.curie('number'),
                   model_uri=CEURWSSCHEMA.volume__number, domain=None, range=Optional[str])

slots.volume__title = Slot(uri=CEURWSSCHEMA.title, name="volume__title", curie=CEURWSSCHEMA.curie('title'),
                   model_uri=CEURWSSCHEMA.volume__title, domain=None, range=Optional[str])

slots.session__title = Slot(uri=CEURWSSCHEMA.title, name="session__title", curie=CEURWSSCHEMA.curie('title'),
                   model_uri=CEURWSSCHEMA.session__title, domain=None, range=Optional[str])

slots.paper__id = Slot(uri=CEURWSSCHEMA.id, name="paper__id", curie=CEURWSSCHEMA.curie('id'),
                   model_uri=CEURWSSCHEMA.paper__id, domain=None, range=Optional[str])

slots.paper__title = Slot(uri=CEURWSSCHEMA.title, name="paper__title", curie=CEURWSSCHEMA.curie('title'),
                   model_uri=CEURWSSCHEMA.paper__title, domain=None, range=Optional[str])

slots.paper__authors = Slot(uri=CEURWSSCHEMA.authors, name="paper__authors", curie=CEURWSSCHEMA.curie('authors'),
                   model_uri=CEURWSSCHEMA.paper__authors, domain=None, range=Optional[str])

slots.paper__pdfUrl = Slot(uri=CEURWSSCHEMA.pdfUrl, name="paper__pdfUrl", curie=CEURWSSCHEMA.curie('pdfUrl'),
                   model_uri=CEURWSSCHEMA.paper__pdfUrl, domain=None, range=Optional[str])
