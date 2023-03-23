# Auto generated from city.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-23T07:27:49
# Schema: GeneralContext
#
# id: GeneralContext
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
GENERALCONTEXT = CurieNamespace('GeneralContext', 'GeneralContext/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = GENERALCONTEXT


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = GENERALCONTEXT.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = GENERALCONTEXT.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = GENERALCONTEXT.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD.float
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = GENERALCONTEXT.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD.double
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = GENERALCONTEXT.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = GENERALCONTEXT.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time"
    type_model_uri = GENERALCONTEXT.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD.date
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = GENERALCONTEXT.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = GENERALCONTEXT.Datetime


class DateOrDatetime(str):
    """ Either a date or a datetime """
    type_class_uri = LINKML.DateOrDatetime
    type_class_curie = "linkml:DateOrDatetime"
    type_name = "date_or_datetime"
    type_model_uri = GENERALCONTEXT.DateOrDatetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = GENERALCONTEXT.Uriorcurie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = GENERALCONTEXT.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = GENERALCONTEXT.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX.iri
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = GENERALCONTEXT.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX.nonLiteral
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = GENERALCONTEXT.Nodeidentifier


# Class references



@dataclass
class City(YAMLRoot):
    """
    I represent a City like Berlin, New York or Tokyo
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = GENERALCONTEXT.City
    class_class_curie: ClassVar[str] = "GeneralContext:City"
    class_name: ClassVar[str] = "City"
    class_model_uri: ClassVar[URIRef] = GENERALCONTEXT.City

    name: Optional[str] = None
    webpage: Optional[Union[str, URI]] = None
    wikipedia_url: Optional[Union[str, URI]] = None
    Population: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.webpage is not None and not isinstance(self.webpage, URI):
            self.webpage = URI(self.webpage)

        if self.wikipedia_url is not None and not isinstance(self.wikipedia_url, URI):
            self.wikipedia_url = URI(self.wikipedia_url)

        if self.Population is not None and not isinstance(self.Population, float):
            self.Population = float(self.Population)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.name = Slot(uri=GENERALCONTEXT.name, name="name", curie=GENERALCONTEXT.curie('name'),
                   model_uri=GENERALCONTEXT.name, domain=None, range=Optional[str])

slots.webpage = Slot(uri=GENERALCONTEXT.webpage, name="webpage", curie=GENERALCONTEXT.curie('webpage'),
                   model_uri=GENERALCONTEXT.webpage, domain=None, range=Optional[Union[str, URI]])

slots.wikipedia_url = Slot(uri=GENERALCONTEXT.wikipedia_url, name="wikipedia_url", curie=GENERALCONTEXT.curie('wikipedia_url'),
                   model_uri=GENERALCONTEXT.wikipedia_url, domain=None, range=Optional[Union[str, URI]])

slots.Population = Slot(uri=GENERALCONTEXT.Population, name="Population", curie=GENERALCONTEXT.curie('Population'),
                   model_uri=GENERALCONTEXT.Population, domain=None, range=Optional[float])

slots.city__name = Slot(uri=GENERALCONTEXT.name, name="city__name", curie=GENERALCONTEXT.curie('name'),
                   model_uri=GENERALCONTEXT.city__name, domain=None, range=Optional[str])

slots.city__webpage = Slot(uri=GENERALCONTEXT.webpage, name="city__webpage", curie=GENERALCONTEXT.curie('webpage'),
                   model_uri=GENERALCONTEXT.city__webpage, domain=None, range=Optional[Union[str, URI]])

slots.city__wikipedia_url = Slot(uri=GENERALCONTEXT.wikipedia_url, name="city__wikipedia_url", curie=GENERALCONTEXT.curie('wikipedia_url'),
                   model_uri=GENERALCONTEXT.city__wikipedia_url, domain=None, range=Optional[Union[str, URI]])

slots.city__Population = Slot(uri=GENERALCONTEXT.Population, name="city__Population", curie=GENERALCONTEXT.curie('Population'),
                   model_uri=GENERALCONTEXT.city__Population, domain=None, range=Optional[float])
