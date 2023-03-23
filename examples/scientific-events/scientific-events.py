# Auto generated from scientific-events.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-23T07:27:44
# Schema: CrSchema
#
# id: CrSchema
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
CRSCHEMA = CurieNamespace('CrSchema', 'CrSchema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CRSCHEMA


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = CRSCHEMA.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = CRSCHEMA.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = CRSCHEMA.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD.float
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = CRSCHEMA.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD.double
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = CRSCHEMA.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = CRSCHEMA.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time"
    type_model_uri = CRSCHEMA.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD.date
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = CRSCHEMA.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = CRSCHEMA.Datetime


class DateOrDatetime(str):
    """ Either a date or a datetime """
    type_class_uri = LINKML.DateOrDatetime
    type_class_curie = "linkml:DateOrDatetime"
    type_name = "date_or_datetime"
    type_model_uri = CRSCHEMA.DateOrDatetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = CRSCHEMA.Uriorcurie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = CRSCHEMA.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = CRSCHEMA.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX.iri
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = CRSCHEMA.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX.nonLiteral
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = CRSCHEMA.Nodeidentifier


# Class references



@dataclass
class EventSeries(YAMLRoot):
    """
    a series of Events
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRSCHEMA.EventSeries
    class_class_curie: ClassVar[str] = "CrSchema:EventSeries"
    class_name: ClassVar[str] = "EventSeries"
    class_model_uri: ClassVar[URIRef] = CRSCHEMA.EventSeries

    acronym: Optional[str] = None
    description: Optional[str] = None
    title: Optional[str] = None
    wikidataid: Optional[str] = None
    homepage: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.wikidataid is not None and not isinstance(self.wikidataid, str):
            self.wikidataid = str(self.wikidataid)

        if self.homepage is not None and not isinstance(self.homepage, str):
            self.homepage = str(self.homepage)

        super().__post_init__(**kwargs)


@dataclass
class Event(YAMLRoot):
    """
    a meeting of researchers at a specific time and place
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRSCHEMA.Event
    class_class_curie: ClassVar[str] = "CrSchema:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = CRSCHEMA.Event

    acronym: Optional[str] = None
    description: Optional[str] = None
    title: Optional[str] = None
    homepage: Optional[str] = None
    wikidataid: Optional[str] = None
    series: Optional[Union[dict, EventSeries]] = None
    city: Optional[Union[dict, "City"]] = None
    country: Optional[Union[dict, "Country"]] = None
    region: Optional[Union[dict, "Region"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.homepage is not None and not isinstance(self.homepage, str):
            self.homepage = str(self.homepage)

        if self.wikidataid is not None and not isinstance(self.wikidataid, str):
            self.wikidataid = str(self.wikidataid)

        if self.series is not None and not isinstance(self.series, EventSeries):
            self.series = EventSeries(**as_dict(self.series))

        if self.city is not None and not isinstance(self.city, City):
            self.city = City(**as_dict(self.city))

        if self.country is not None and not isinstance(self.country, Country):
            self.country = Country(**as_dict(self.country))

        if self.region is not None and not isinstance(self.region, Region):
            self.region = Region(**as_dict(self.region))

        super().__post_init__(**kwargs)


@dataclass
class City(YAMLRoot):
    """
    large permanent human settlement
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRSCHEMA.City
    class_class_curie: ClassVar[str] = "CrSchema:City"
    class_name: ClassVar[str] = "City"
    class_model_uri: ClassVar[URIRef] = CRSCHEMA.City

    name: Optional[str] = None
    wikidataid: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.wikidataid is not None and not isinstance(self.wikidataid, str):
            self.wikidataid = str(self.wikidataid)

        super().__post_init__(**kwargs)


@dataclass
class Country(YAMLRoot):
    """
    distinct region in geography; a broad term that can include political divisions or regions associated with
    distinct political characteristics
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRSCHEMA.Country
    class_class_curie: ClassVar[str] = "CrSchema:Country"
    class_name: ClassVar[str] = "Country"
    class_model_uri: ClassVar[URIRef] = CRSCHEMA.Country

    name: Optional[str] = None
    wikidataid: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.wikidataid is not None and not isinstance(self.wikidataid, str):
            self.wikidataid = str(self.wikidataid)

        super().__post_init__(**kwargs)


@dataclass
class Region(YAMLRoot):
    """
    first-level administrative country subdivision e.g. Region/province
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRSCHEMA.Region
    class_class_curie: ClassVar[str] = "CrSchema:Region"
    class_name: ClassVar[str] = "Region"
    class_model_uri: ClassVar[URIRef] = CRSCHEMA.Region

    name: Optional[str] = None
    wikidataid: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.wikidataid is not None and not isinstance(self.wikidataid, str):
            self.wikidataid = str(self.wikidataid)

        super().__post_init__(**kwargs)


@dataclass
class Proceedings(YAMLRoot):
    """
    Proceedings are a collection of papers mostly documenting the results of an academic event
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRSCHEMA.Proceedings
    class_class_curie: ClassVar[str] = "CrSchema:Proceedings"
    class_name: ClassVar[str] = "Proceedings"
    class_model_uri: ClassVar[URIRef] = CRSCHEMA.Proceedings

    wikidataid: Optional[str] = None
    title: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.wikidataid is not None and not isinstance(self.wikidataid, str):
            self.wikidataid = str(self.wikidataid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


@dataclass
class Scholar(YAMLRoot):
    """
    scholar/researcher: person who engages in research, professionally or otherwise
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRSCHEMA.Scholar
    class_class_curie: ClassVar[str] = "CrSchema:Scholar"
    class_name: ClassVar[str] = "Scholar"
    class_model_uri: ClassVar[URIRef] = CRSCHEMA.Scholar

    wikiDataId: Optional[str] = None
    name: Optional[str] = None
    firstName: Optional[str] = None
    description: Optional[str] = None
    homepage: Optional[str] = None
    orcid: Optional[str] = None
    dblpId: Optional[str] = None
    googleScholarUser: Optional[str] = None
    linkedInId: Optional[str] = None
    researchGate: Optional[str] = None
    gndId: Optional[str] = None
    smartCRMId: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.wikiDataId is not None and not isinstance(self.wikiDataId, str):
            self.wikiDataId = str(self.wikiDataId)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.firstName is not None and not isinstance(self.firstName, str):
            self.firstName = str(self.firstName)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.homepage is not None and not isinstance(self.homepage, str):
            self.homepage = str(self.homepage)

        if self.orcid is not None and not isinstance(self.orcid, str):
            self.orcid = str(self.orcid)

        if self.dblpId is not None and not isinstance(self.dblpId, str):
            self.dblpId = str(self.dblpId)

        if self.googleScholarUser is not None and not isinstance(self.googleScholarUser, str):
            self.googleScholarUser = str(self.googleScholarUser)

        if self.linkedInId is not None and not isinstance(self.linkedInId, str):
            self.linkedInId = str(self.linkedInId)

        if self.researchGate is not None and not isinstance(self.researchGate, str):
            self.researchGate = str(self.researchGate)

        if self.gndId is not None and not isinstance(self.gndId, str):
            self.gndId = str(self.gndId)

        if self.smartCRMId is not None and not isinstance(self.smartCRMId, str):
            self.smartCRMId = str(self.smartCRMId)

        super().__post_init__(**kwargs)


@dataclass
class Institution(YAMLRoot):
    """
    structure or mechanism of social order and cooperation governing the behaviour of a set of individuals within a
    given community
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRSCHEMA.Institution
    class_class_curie: ClassVar[str] = "CrSchema:Institution"
    class_name: ClassVar[str] = "Institution"
    class_model_uri: ClassVar[URIRef] = CRSCHEMA.Institution

    title: Optional[str] = None
    wikidataid: Optional[str] = None
    homepage: Optional[str] = None
    smartCRMId: Optional[str] = None
    scholar: Optional[Union[dict, Scholar]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.wikidataid is not None and not isinstance(self.wikidataid, str):
            self.wikidataid = str(self.wikidataid)

        if self.homepage is not None and not isinstance(self.homepage, str):
            self.homepage = str(self.homepage)

        if self.smartCRMId is not None and not isinstance(self.smartCRMId, str):
            self.smartCRMId = str(self.smartCRMId)

        if self.scholar is not None and not isinstance(self.scholar, Scholar):
            self.scholar = Scholar(**as_dict(self.scholar))

        super().__post_init__(**kwargs)


@dataclass
class Paper(YAMLRoot):
    """
    A paper is e.g. a scholarly article
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CRSCHEMA.Paper
    class_class_curie: ClassVar[str] = "CrSchema:Paper"
    class_name: ClassVar[str] = "Paper"
    class_model_uri: ClassVar[URIRef] = CRSCHEMA.Paper

    description: Optional[str] = None
    id: Optional[str] = None
    wikidataid: Optional[str] = None
    title: Optional[str] = None
    authors: Optional[str] = None
    pdfUrl: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.wikidataid is not None and not isinstance(self.wikidataid, str):
            self.wikidataid = str(self.wikidataid)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.authors is not None and not isinstance(self.authors, str):
            self.authors = str(self.authors)

        if self.pdfUrl is not None and not isinstance(self.pdfUrl, URI):
            self.pdfUrl = URI(self.pdfUrl)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.acronym = Slot(uri=CRSCHEMA.acronym, name="acronym", curie=CRSCHEMA.curie('acronym'),
                   model_uri=CRSCHEMA.acronym, domain=None, range=Optional[str])

slots.description = Slot(uri=CRSCHEMA.description, name="description", curie=CRSCHEMA.curie('description'),
                   model_uri=CRSCHEMA.description, domain=None, range=Optional[str])

slots.title = Slot(uri=CRSCHEMA.title, name="title", curie=CRSCHEMA.curie('title'),
                   model_uri=CRSCHEMA.title, domain=None, range=Optional[str])

slots.wikidataid = Slot(uri=CRSCHEMA.wikidataid, name="wikidataid", curie=CRSCHEMA.curie('wikidataid'),
                   model_uri=CRSCHEMA.wikidataid, domain=None, range=Optional[str])

slots.homepage = Slot(uri=CRSCHEMA.homepage, name="homepage", curie=CRSCHEMA.curie('homepage'),
                   model_uri=CRSCHEMA.homepage, domain=None, range=Optional[str])

slots.series = Slot(uri=CRSCHEMA.series, name="series", curie=CRSCHEMA.curie('series'),
                   model_uri=CRSCHEMA.series, domain=None, range=Optional[Union[dict, EventSeries]])

slots.city = Slot(uri=CRSCHEMA.city, name="city", curie=CRSCHEMA.curie('city'),
                   model_uri=CRSCHEMA.city, domain=None, range=Optional[Union[dict, City]])

slots.country = Slot(uri=CRSCHEMA.country, name="country", curie=CRSCHEMA.curie('country'),
                   model_uri=CRSCHEMA.country, domain=None, range=Optional[Union[dict, Country]])

slots.region = Slot(uri=CRSCHEMA.region, name="region", curie=CRSCHEMA.curie('region'),
                   model_uri=CRSCHEMA.region, domain=None, range=Optional[Union[dict, Region]])

slots.name = Slot(uri=CRSCHEMA.name, name="name", curie=CRSCHEMA.curie('name'),
                   model_uri=CRSCHEMA.name, domain=None, range=Optional[str])

slots.wikiDataId = Slot(uri=CRSCHEMA.wikiDataId, name="wikiDataId", curie=CRSCHEMA.curie('wikiDataId'),
                   model_uri=CRSCHEMA.wikiDataId, domain=None, range=Optional[str])

slots.firstName = Slot(uri=CRSCHEMA.firstName, name="firstName", curie=CRSCHEMA.curie('firstName'),
                   model_uri=CRSCHEMA.firstName, domain=None, range=Optional[str])

slots.orcid = Slot(uri=CRSCHEMA.orcid, name="orcid", curie=CRSCHEMA.curie('orcid'),
                   model_uri=CRSCHEMA.orcid, domain=None, range=Optional[str])

slots.dblpId = Slot(uri=CRSCHEMA.dblpId, name="dblpId", curie=CRSCHEMA.curie('dblpId'),
                   model_uri=CRSCHEMA.dblpId, domain=None, range=Optional[str])

slots.googleScholarUser = Slot(uri=CRSCHEMA.googleScholarUser, name="googleScholarUser", curie=CRSCHEMA.curie('googleScholarUser'),
                   model_uri=CRSCHEMA.googleScholarUser, domain=None, range=Optional[str])

slots.linkedInId = Slot(uri=CRSCHEMA.linkedInId, name="linkedInId", curie=CRSCHEMA.curie('linkedInId'),
                   model_uri=CRSCHEMA.linkedInId, domain=None, range=Optional[str])

slots.researchGate = Slot(uri=CRSCHEMA.researchGate, name="researchGate", curie=CRSCHEMA.curie('researchGate'),
                   model_uri=CRSCHEMA.researchGate, domain=None, range=Optional[str])

slots.gndId = Slot(uri=CRSCHEMA.gndId, name="gndId", curie=CRSCHEMA.curie('gndId'),
                   model_uri=CRSCHEMA.gndId, domain=None, range=Optional[str])

slots.smartCRMId = Slot(uri=CRSCHEMA.smartCRMId, name="smartCRMId", curie=CRSCHEMA.curie('smartCRMId'),
                   model_uri=CRSCHEMA.smartCRMId, domain=None, range=Optional[str])

slots.scholar = Slot(uri=CRSCHEMA.scholar, name="scholar", curie=CRSCHEMA.curie('scholar'),
                   model_uri=CRSCHEMA.scholar, domain=None, range=Optional[Union[dict, Scholar]])

slots.id = Slot(uri=CRSCHEMA.id, name="id", curie=CRSCHEMA.curie('id'),
                   model_uri=CRSCHEMA.id, domain=None, range=Optional[str])

slots.authors = Slot(uri=CRSCHEMA.authors, name="authors", curie=CRSCHEMA.curie('authors'),
                   model_uri=CRSCHEMA.authors, domain=None, range=Optional[str])

slots.pdfUrl = Slot(uri=CRSCHEMA.pdfUrl, name="pdfUrl", curie=CRSCHEMA.curie('pdfUrl'),
                   model_uri=CRSCHEMA.pdfUrl, domain=None, range=Optional[Union[str, URI]])

slots.eventSeries__acronym = Slot(uri=CRSCHEMA.acronym, name="eventSeries__acronym", curie=CRSCHEMA.curie('acronym'),
                   model_uri=CRSCHEMA.eventSeries__acronym, domain=None, range=Optional[str])

slots.eventSeries__description = Slot(uri=CRSCHEMA.description, name="eventSeries__description", curie=CRSCHEMA.curie('description'),
                   model_uri=CRSCHEMA.eventSeries__description, domain=None, range=Optional[str])

slots.eventSeries__title = Slot(uri=CRSCHEMA.title, name="eventSeries__title", curie=CRSCHEMA.curie('title'),
                   model_uri=CRSCHEMA.eventSeries__title, domain=None, range=Optional[str])

slots.eventSeries__wikidataid = Slot(uri=CRSCHEMA.wikidataid, name="eventSeries__wikidataid", curie=CRSCHEMA.curie('wikidataid'),
                   model_uri=CRSCHEMA.eventSeries__wikidataid, domain=None, range=Optional[str])

slots.eventSeries__homepage = Slot(uri=CRSCHEMA.homepage, name="eventSeries__homepage", curie=CRSCHEMA.curie('homepage'),
                   model_uri=CRSCHEMA.eventSeries__homepage, domain=None, range=Optional[str])

slots.event__acronym = Slot(uri=CRSCHEMA.acronym, name="event__acronym", curie=CRSCHEMA.curie('acronym'),
                   model_uri=CRSCHEMA.event__acronym, domain=None, range=Optional[str])

slots.event__description = Slot(uri=CRSCHEMA.description, name="event__description", curie=CRSCHEMA.curie('description'),
                   model_uri=CRSCHEMA.event__description, domain=None, range=Optional[str])

slots.event__title = Slot(uri=CRSCHEMA.title, name="event__title", curie=CRSCHEMA.curie('title'),
                   model_uri=CRSCHEMA.event__title, domain=None, range=Optional[str])

slots.event__homepage = Slot(uri=CRSCHEMA.homepage, name="event__homepage", curie=CRSCHEMA.curie('homepage'),
                   model_uri=CRSCHEMA.event__homepage, domain=None, range=Optional[str])

slots.event__wikidataid = Slot(uri=CRSCHEMA.wikidataid, name="event__wikidataid", curie=CRSCHEMA.curie('wikidataid'),
                   model_uri=CRSCHEMA.event__wikidataid, domain=None, range=Optional[str])

slots.event__series = Slot(uri=CRSCHEMA.series, name="event__series", curie=CRSCHEMA.curie('series'),
                   model_uri=CRSCHEMA.event__series, domain=None, range=Optional[Union[dict, EventSeries]])

slots.event__city = Slot(uri=CRSCHEMA.city, name="event__city", curie=CRSCHEMA.curie('city'),
                   model_uri=CRSCHEMA.event__city, domain=None, range=Optional[Union[dict, City]])

slots.event__country = Slot(uri=CRSCHEMA.country, name="event__country", curie=CRSCHEMA.curie('country'),
                   model_uri=CRSCHEMA.event__country, domain=None, range=Optional[Union[dict, Country]])

slots.event__region = Slot(uri=CRSCHEMA.region, name="event__region", curie=CRSCHEMA.curie('region'),
                   model_uri=CRSCHEMA.event__region, domain=None, range=Optional[Union[dict, Region]])

slots.city__name = Slot(uri=CRSCHEMA.name, name="city__name", curie=CRSCHEMA.curie('name'),
                   model_uri=CRSCHEMA.city__name, domain=None, range=Optional[str])

slots.city__wikidataid = Slot(uri=CRSCHEMA.wikidataid, name="city__wikidataid", curie=CRSCHEMA.curie('wikidataid'),
                   model_uri=CRSCHEMA.city__wikidataid, domain=None, range=Optional[str])

slots.country__name = Slot(uri=CRSCHEMA.name, name="country__name", curie=CRSCHEMA.curie('name'),
                   model_uri=CRSCHEMA.country__name, domain=None, range=Optional[str])

slots.country__wikidataid = Slot(uri=CRSCHEMA.wikidataid, name="country__wikidataid", curie=CRSCHEMA.curie('wikidataid'),
                   model_uri=CRSCHEMA.country__wikidataid, domain=None, range=Optional[str])

slots.region__name = Slot(uri=CRSCHEMA.name, name="region__name", curie=CRSCHEMA.curie('name'),
                   model_uri=CRSCHEMA.region__name, domain=None, range=Optional[str])

slots.region__wikidataid = Slot(uri=CRSCHEMA.wikidataid, name="region__wikidataid", curie=CRSCHEMA.curie('wikidataid'),
                   model_uri=CRSCHEMA.region__wikidataid, domain=None, range=Optional[str])

slots.proceedings__wikidataid = Slot(uri=CRSCHEMA.wikidataid, name="proceedings__wikidataid", curie=CRSCHEMA.curie('wikidataid'),
                   model_uri=CRSCHEMA.proceedings__wikidataid, domain=None, range=Optional[str])

slots.proceedings__title = Slot(uri=CRSCHEMA.title, name="proceedings__title", curie=CRSCHEMA.curie('title'),
                   model_uri=CRSCHEMA.proceedings__title, domain=None, range=Optional[str])

slots.scholar__wikiDataId = Slot(uri=CRSCHEMA.wikiDataId, name="scholar__wikiDataId", curie=CRSCHEMA.curie('wikiDataId'),
                   model_uri=CRSCHEMA.scholar__wikiDataId, domain=None, range=Optional[str])

slots.scholar__name = Slot(uri=CRSCHEMA.name, name="scholar__name", curie=CRSCHEMA.curie('name'),
                   model_uri=CRSCHEMA.scholar__name, domain=None, range=Optional[str])

slots.scholar__firstName = Slot(uri=CRSCHEMA.firstName, name="scholar__firstName", curie=CRSCHEMA.curie('firstName'),
                   model_uri=CRSCHEMA.scholar__firstName, domain=None, range=Optional[str])

slots.scholar__description = Slot(uri=CRSCHEMA.description, name="scholar__description", curie=CRSCHEMA.curie('description'),
                   model_uri=CRSCHEMA.scholar__description, domain=None, range=Optional[str])

slots.scholar__homepage = Slot(uri=CRSCHEMA.homepage, name="scholar__homepage", curie=CRSCHEMA.curie('homepage'),
                   model_uri=CRSCHEMA.scholar__homepage, domain=None, range=Optional[str])

slots.scholar__orcid = Slot(uri=CRSCHEMA.orcid, name="scholar__orcid", curie=CRSCHEMA.curie('orcid'),
                   model_uri=CRSCHEMA.scholar__orcid, domain=None, range=Optional[str])

slots.scholar__dblpId = Slot(uri=CRSCHEMA.dblpId, name="scholar__dblpId", curie=CRSCHEMA.curie('dblpId'),
                   model_uri=CRSCHEMA.scholar__dblpId, domain=None, range=Optional[str])

slots.scholar__googleScholarUser = Slot(uri=CRSCHEMA.googleScholarUser, name="scholar__googleScholarUser", curie=CRSCHEMA.curie('googleScholarUser'),
                   model_uri=CRSCHEMA.scholar__googleScholarUser, domain=None, range=Optional[str])

slots.scholar__linkedInId = Slot(uri=CRSCHEMA.linkedInId, name="scholar__linkedInId", curie=CRSCHEMA.curie('linkedInId'),
                   model_uri=CRSCHEMA.scholar__linkedInId, domain=None, range=Optional[str])

slots.scholar__researchGate = Slot(uri=CRSCHEMA.researchGate, name="scholar__researchGate", curie=CRSCHEMA.curie('researchGate'),
                   model_uri=CRSCHEMA.scholar__researchGate, domain=None, range=Optional[str])

slots.scholar__gndId = Slot(uri=CRSCHEMA.gndId, name="scholar__gndId", curie=CRSCHEMA.curie('gndId'),
                   model_uri=CRSCHEMA.scholar__gndId, domain=None, range=Optional[str])

slots.scholar__smartCRMId = Slot(uri=CRSCHEMA.smartCRMId, name="scholar__smartCRMId", curie=CRSCHEMA.curie('smartCRMId'),
                   model_uri=CRSCHEMA.scholar__smartCRMId, domain=None, range=Optional[str])

slots.institution__title = Slot(uri=CRSCHEMA.title, name="institution__title", curie=CRSCHEMA.curie('title'),
                   model_uri=CRSCHEMA.institution__title, domain=None, range=Optional[str])

slots.institution__wikidataid = Slot(uri=CRSCHEMA.wikidataid, name="institution__wikidataid", curie=CRSCHEMA.curie('wikidataid'),
                   model_uri=CRSCHEMA.institution__wikidataid, domain=None, range=Optional[str])

slots.institution__homepage = Slot(uri=CRSCHEMA.homepage, name="institution__homepage", curie=CRSCHEMA.curie('homepage'),
                   model_uri=CRSCHEMA.institution__homepage, domain=None, range=Optional[str])

slots.institution__smartCRMId = Slot(uri=CRSCHEMA.smartCRMId, name="institution__smartCRMId", curie=CRSCHEMA.curie('smartCRMId'),
                   model_uri=CRSCHEMA.institution__smartCRMId, domain=None, range=Optional[str])

slots.institution__scholar = Slot(uri=CRSCHEMA.scholar, name="institution__scholar", curie=CRSCHEMA.curie('scholar'),
                   model_uri=CRSCHEMA.institution__scholar, domain=None, range=Optional[Union[dict, Scholar]])

slots.paper__description = Slot(uri=CRSCHEMA.description, name="paper__description", curie=CRSCHEMA.curie('description'),
                   model_uri=CRSCHEMA.paper__description, domain=None, range=Optional[str])

slots.paper__id = Slot(uri=CRSCHEMA.id, name="paper__id", curie=CRSCHEMA.curie('id'),
                   model_uri=CRSCHEMA.paper__id, domain=None, range=Optional[str])

slots.paper__wikidataid = Slot(uri=CRSCHEMA.wikidataid, name="paper__wikidataid", curie=CRSCHEMA.curie('wikidataid'),
                   model_uri=CRSCHEMA.paper__wikidataid, domain=None, range=Optional[str])

slots.paper__title = Slot(uri=CRSCHEMA.title, name="paper__title", curie=CRSCHEMA.curie('title'),
                   model_uri=CRSCHEMA.paper__title, domain=None, range=Optional[str])

slots.paper__authors = Slot(uri=CRSCHEMA.authors, name="paper__authors", curie=CRSCHEMA.curie('authors'),
                   model_uri=CRSCHEMA.paper__authors, domain=None, range=Optional[str])

slots.paper__pdfUrl = Slot(uri=CRSCHEMA.pdfUrl, name="paper__pdfUrl", curie=CRSCHEMA.curie('pdfUrl'),
                   model_uri=CRSCHEMA.paper__pdfUrl, domain=None, range=Optional[Union[str, URI]])
