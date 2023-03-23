# Auto generated from ceur-ws.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-23T07:28:10
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
from linkml_runtime.utils.metamodelcore import Bool, Decimal, ElementIdentifier, NCName, NodeIdentifier, URI, URIorCURIE, XSDDate, XSDDateTime, XSDTime

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CEURWSSCHEMA = CurieNamespace('CeurwsSchema', 'CeurwsSchema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
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

    number: Optional[float] = None
    acronym: Optional[str] = None
    wikidataid: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    date: Optional[Union[str, XSDDate]] = None
    dblp: Optional[str] = None
    k10plus: Optional[str] = None
    urn: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.number is not None and not isinstance(self.number, float):
            self.number = float(self.number)

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if self.wikidataid is not None and not isinstance(self.wikidataid, str):
            self.wikidataid = str(self.wikidataid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        if self.date is not None and not isinstance(self.date, XSDDate):
            self.date = XSDDate(self.date)

        if self.dblp is not None and not isinstance(self.dblp, str):
            self.dblp = str(self.dblp)

        if self.k10plus is not None and not isinstance(self.k10plus, str):
            self.k10plus = str(self.k10plus)

        if self.urn is not None and not isinstance(self.urn, str):
            self.urn = str(self.urn)

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
    volume: Optional[Union[dict, Volume]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.volume is not None and not isinstance(self.volume, Volume):
            self.volume = Volume(**as_dict(self.volume))

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

    description: Optional[str] = None
    id: Optional[str] = None
    wikidataid: Optional[str] = None
    title: Optional[str] = None
    pdfUrl: Optional[Union[str, URI]] = None
    volume: Optional[Union[dict, Volume]] = None
    session: Optional[Union[dict, Session]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.wikidataid is not None and not isinstance(self.wikidataid, str):
            self.wikidataid = str(self.wikidataid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.pdfUrl is not None and not isinstance(self.pdfUrl, URI):
            self.pdfUrl = URI(self.pdfUrl)

        if self.volume is not None and not isinstance(self.volume, Volume):
            self.volume = Volume(**as_dict(self.volume))

        if self.session is not None and not isinstance(self.session, Session):
            self.session = Session(**as_dict(self.session))

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.number = Slot(uri=CEURWSSCHEMA.number, name="number", curie=CEURWSSCHEMA.curie('number'),
                   model_uri=CEURWSSCHEMA.number, domain=None, range=Optional[float])

slots.acronym = Slot(uri=CEURWSSCHEMA.acronym, name="acronym", curie=CEURWSSCHEMA.curie('acronym'),
                   model_uri=CEURWSSCHEMA.acronym, domain=None, range=Optional[str])

slots.wikidataid = Slot(uri=CEURWSSCHEMA.wikidataid, name="wikidataid", curie=CEURWSSCHEMA.curie('wikidataid'),
                   model_uri=CEURWSSCHEMA.wikidataid, domain=None, range=Optional[str])

slots.title = Slot(uri=CEURWSSCHEMA.title, name="title", curie=CEURWSSCHEMA.curie('title'),
                   model_uri=CEURWSSCHEMA.title, domain=None, range=Optional[str])

slots.description = Slot(uri=CEURWSSCHEMA.description, name="description", curie=CEURWSSCHEMA.curie('description'),
                   model_uri=CEURWSSCHEMA.description, domain=None, range=Optional[str])

slots.url = Slot(uri=CEURWSSCHEMA.url, name="url", curie=CEURWSSCHEMA.curie('url'),
                   model_uri=CEURWSSCHEMA.url, domain=None, range=Optional[str])

slots.date = Slot(uri=CEURWSSCHEMA.date, name="date", curie=CEURWSSCHEMA.curie('date'),
                   model_uri=CEURWSSCHEMA.date, domain=None, range=Optional[Union[str, XSDDate]])

slots.dblp = Slot(uri=CEURWSSCHEMA.dblp, name="dblp", curie=CEURWSSCHEMA.curie('dblp'),
                   model_uri=CEURWSSCHEMA.dblp, domain=None, range=Optional[str])

slots.k10plus = Slot(uri=CEURWSSCHEMA.k10plus, name="k10plus", curie=CEURWSSCHEMA.curie('k10plus'),
                   model_uri=CEURWSSCHEMA.k10plus, domain=None, range=Optional[str])

slots.urn = Slot(uri=CEURWSSCHEMA.urn, name="urn", curie=CEURWSSCHEMA.curie('urn'),
                   model_uri=CEURWSSCHEMA.urn, domain=None, range=Optional[str])

slots.volume = Slot(uri=CEURWSSCHEMA.volume, name="volume", curie=CEURWSSCHEMA.curie('volume'),
                   model_uri=CEURWSSCHEMA.volume, domain=None, range=Optional[Union[dict, Volume]])

slots.id = Slot(uri=CEURWSSCHEMA.id, name="id", curie=CEURWSSCHEMA.curie('id'),
                   model_uri=CEURWSSCHEMA.id, domain=None, range=Optional[str])

slots.pdfUrl = Slot(uri=CEURWSSCHEMA.pdfUrl, name="pdfUrl", curie=CEURWSSCHEMA.curie('pdfUrl'),
                   model_uri=CEURWSSCHEMA.pdfUrl, domain=None, range=Optional[Union[str, URI]])

slots.session = Slot(uri=CEURWSSCHEMA.session, name="session", curie=CEURWSSCHEMA.curie('session'),
                   model_uri=CEURWSSCHEMA.session, domain=None, range=Optional[Union[dict, Session]])

slots.volume__number = Slot(uri=CEURWSSCHEMA.number, name="volume__number", curie=CEURWSSCHEMA.curie('number'),
                   model_uri=CEURWSSCHEMA.volume__number, domain=None, range=Optional[float])

slots.volume__acronym = Slot(uri=CEURWSSCHEMA.acronym, name="volume__acronym", curie=CEURWSSCHEMA.curie('acronym'),
                   model_uri=CEURWSSCHEMA.volume__acronym, domain=None, range=Optional[str])

slots.volume__wikidataid = Slot(uri=CEURWSSCHEMA.wikidataid, name="volume__wikidataid", curie=CEURWSSCHEMA.curie('wikidataid'),
                   model_uri=CEURWSSCHEMA.volume__wikidataid, domain=None, range=Optional[str])

slots.volume__title = Slot(uri=CEURWSSCHEMA.title, name="volume__title", curie=CEURWSSCHEMA.curie('title'),
                   model_uri=CEURWSSCHEMA.volume__title, domain=None, range=Optional[str])

slots.volume__description = Slot(uri=CEURWSSCHEMA.description, name="volume__description", curie=CEURWSSCHEMA.curie('description'),
                   model_uri=CEURWSSCHEMA.volume__description, domain=None, range=Optional[str])

slots.volume__url = Slot(uri=CEURWSSCHEMA.url, name="volume__url", curie=CEURWSSCHEMA.curie('url'),
                   model_uri=CEURWSSCHEMA.volume__url, domain=None, range=Optional[str])

slots.volume__date = Slot(uri=CEURWSSCHEMA.date, name="volume__date", curie=CEURWSSCHEMA.curie('date'),
                   model_uri=CEURWSSCHEMA.volume__date, domain=None, range=Optional[Union[str, XSDDate]])

slots.volume__dblp = Slot(uri=CEURWSSCHEMA.dblp, name="volume__dblp", curie=CEURWSSCHEMA.curie('dblp'),
                   model_uri=CEURWSSCHEMA.volume__dblp, domain=None, range=Optional[str])

slots.volume__k10plus = Slot(uri=CEURWSSCHEMA.k10plus, name="volume__k10plus", curie=CEURWSSCHEMA.curie('k10plus'),
                   model_uri=CEURWSSCHEMA.volume__k10plus, domain=None, range=Optional[str])

slots.volume__urn = Slot(uri=CEURWSSCHEMA.urn, name="volume__urn", curie=CEURWSSCHEMA.curie('urn'),
                   model_uri=CEURWSSCHEMA.volume__urn, domain=None, range=Optional[str])

slots.session__title = Slot(uri=CEURWSSCHEMA.title, name="session__title", curie=CEURWSSCHEMA.curie('title'),
                   model_uri=CEURWSSCHEMA.session__title, domain=None, range=Optional[str])

slots.session__volume = Slot(uri=CEURWSSCHEMA.volume, name="session__volume", curie=CEURWSSCHEMA.curie('volume'),
                   model_uri=CEURWSSCHEMA.session__volume, domain=None, range=Optional[Union[dict, Volume]])

slots.paper__description = Slot(uri=CEURWSSCHEMA.description, name="paper__description", curie=CEURWSSCHEMA.curie('description'),
                   model_uri=CEURWSSCHEMA.paper__description, domain=None, range=Optional[str])

slots.paper__id = Slot(uri=CEURWSSCHEMA.id, name="paper__id", curie=CEURWSSCHEMA.curie('id'),
                   model_uri=CEURWSSCHEMA.paper__id, domain=None, range=Optional[str])

slots.paper__wikidataid = Slot(uri=CEURWSSCHEMA.wikidataid, name="paper__wikidataid", curie=CEURWSSCHEMA.curie('wikidataid'),
                   model_uri=CEURWSSCHEMA.paper__wikidataid, domain=None, range=Optional[str])

slots.paper__title = Slot(uri=CEURWSSCHEMA.title, name="paper__title", curie=CEURWSSCHEMA.curie('title'),
                   model_uri=CEURWSSCHEMA.paper__title, domain=None, range=Optional[str])

slots.paper__pdfUrl = Slot(uri=CEURWSSCHEMA.pdfUrl, name="paper__pdfUrl", curie=CEURWSSCHEMA.curie('pdfUrl'),
                   model_uri=CEURWSSCHEMA.paper__pdfUrl, domain=None, range=Optional[Union[str, URI]])

slots.paper__volume = Slot(uri=CEURWSSCHEMA.volume, name="paper__volume", curie=CEURWSSCHEMA.curie('volume'),
                   model_uri=CEURWSSCHEMA.paper__volume, domain=None, range=Optional[Union[dict, Volume]])

slots.paper__session = Slot(uri=CEURWSSCHEMA.session, name="paper__session", curie=CEURWSSCHEMA.curie('session'),
                   model_uri=CEURWSSCHEMA.paper__session, domain=None, range=Optional[Union[dict, Session]])
