# Auto generated from FamilyContext.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-02-23T20:28:54
# Schema: FamilyContext
#
# id: FamilyContext
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
FAMILYCONTEXT = CurieNamespace('FamilyContext', 'FamilyContext/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = FAMILYCONTEXT


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = FAMILYCONTEXT.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = FAMILYCONTEXT.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = FAMILYCONTEXT.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD.float
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = FAMILYCONTEXT.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD.double
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = FAMILYCONTEXT.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = FAMILYCONTEXT.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time"
    type_model_uri = FAMILYCONTEXT.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD.date
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = FAMILYCONTEXT.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = FAMILYCONTEXT.Datetime


class DateOrDatetime(str):
    """ Either a date or a datetime """
    type_class_uri = LINKML.DateOrDatetime
    type_class_curie = "linkml:DateOrDatetime"
    type_name = "date_or_datetime"
    type_model_uri = FAMILYCONTEXT.DateOrDatetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = FAMILYCONTEXT.Uriorcurie


class Curie(Curie):
    """ a compact URI """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "curie"
    type_model_uri = FAMILYCONTEXT.Curie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = FAMILYCONTEXT.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = FAMILYCONTEXT.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX.iri
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = FAMILYCONTEXT.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX.nonLiteral
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = FAMILYCONTEXT.Nodeidentifier


# Class references



@dataclass
class Family(YAMLRoot):
    """
    In most societies, the family is the principal institution for the socialization of children.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FAMILYCONTEXT.Family
    class_class_curie: ClassVar[str] = "FamilyContext:Family"
    class_name: ClassVar[str] = "Family"
    class_model_uri: ClassVar[URIRef] = FAMILYCONTEXT.Family

    name: Optional[str] = None
    weddingDate: Optional[str] = None
    weddingPlace: Optional[str] = None
    yearMarried: Optional[str] = None
    monthMarried: Optional[str] = None
    divorced: Optional[str] = None
    husbandOf: Optional[str] = None
    wifeOf: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.weddingDate is not None and not isinstance(self.weddingDate, str):
            self.weddingDate = str(self.weddingDate)

        if self.weddingPlace is not None and not isinstance(self.weddingPlace, str):
            self.weddingPlace = str(self.weddingPlace)

        if self.yearMarried is not None and not isinstance(self.yearMarried, str):
            self.yearMarried = str(self.yearMarried)

        if self.monthMarried is not None and not isinstance(self.monthMarried, str):
            self.monthMarried = str(self.monthMarried)

        if self.divorced is not None and not isinstance(self.divorced, str):
            self.divorced = str(self.divorced)

        if self.husbandOf is not None and not isinstance(self.husbandOf, str):
            self.husbandOf = str(self.husbandOf)

        if self.wifeOf is not None and not isinstance(self.wifeOf, str):
            self.wifeOf = str(self.wifeOf)

        super().__post_init__(**kwargs)


@dataclass
class Person(YAMLRoot):
    """
    A Person is a human being
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FAMILYCONTEXT.Person
    class_class_curie: ClassVar[str] = "FamilyContext:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = FAMILYCONTEXT.Person

    qid: Optional[str] = None
    royal92id: Optional[str] = None
    name: Optional[str] = None
    nobleTitle: Optional[str] = None
    picture: Optional[str] = None
    sex: Optional[str] = None
    born: Optional[str] = None
    yearBorn: Optional[str] = None
    monthBorn: Optional[str] = None
    birthPlace: Optional[str] = None
    died: Optional[str] = None
    diedAt: Optional[str] = None
    yearDied: Optional[str] = None
    monthDied: Optional[str] = None
    noInLine: Optional[str] = None
    wikiPedia: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.qid is not None and not isinstance(self.qid, str):
            self.qid = str(self.qid)

        if self.royal92id is not None and not isinstance(self.royal92id, str):
            self.royal92id = str(self.royal92id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.nobleTitle is not None and not isinstance(self.nobleTitle, str):
            self.nobleTitle = str(self.nobleTitle)

        if self.picture is not None and not isinstance(self.picture, str):
            self.picture = str(self.picture)

        if self.sex is not None and not isinstance(self.sex, str):
            self.sex = str(self.sex)

        if self.born is not None and not isinstance(self.born, str):
            self.born = str(self.born)

        if self.yearBorn is not None and not isinstance(self.yearBorn, str):
            self.yearBorn = str(self.yearBorn)

        if self.monthBorn is not None and not isinstance(self.monthBorn, str):
            self.monthBorn = str(self.monthBorn)

        if self.birthPlace is not None and not isinstance(self.birthPlace, str):
            self.birthPlace = str(self.birthPlace)

        if self.died is not None and not isinstance(self.died, str):
            self.died = str(self.died)

        if self.diedAt is not None and not isinstance(self.diedAt, str):
            self.diedAt = str(self.diedAt)

        if self.yearDied is not None and not isinstance(self.yearDied, str):
            self.yearDied = str(self.yearDied)

        if self.monthDied is not None and not isinstance(self.monthDied, str):
            self.monthDied = str(self.monthDied)

        if self.noInLine is not None and not isinstance(self.noInLine, str):
            self.noInLine = str(self.noInLine)

        if self.wikiPedia is not None and not isinstance(self.wikiPedia, str):
            self.wikiPedia = str(self.wikiPedia)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.name = Slot(uri=FAMILYCONTEXT.name, name="name", curie=FAMILYCONTEXT.curie('name'),
                   model_uri=FAMILYCONTEXT.name, domain=None, range=Optional[str])

slots.weddingDate = Slot(uri=FAMILYCONTEXT.weddingDate, name="weddingDate", curie=FAMILYCONTEXT.curie('weddingDate'),
                   model_uri=FAMILYCONTEXT.weddingDate, domain=None, range=Optional[str])

slots.weddingPlace = Slot(uri=FAMILYCONTEXT.weddingPlace, name="weddingPlace", curie=FAMILYCONTEXT.curie('weddingPlace'),
                   model_uri=FAMILYCONTEXT.weddingPlace, domain=None, range=Optional[str])

slots.yearMarried = Slot(uri=FAMILYCONTEXT.yearMarried, name="yearMarried", curie=FAMILYCONTEXT.curie('yearMarried'),
                   model_uri=FAMILYCONTEXT.yearMarried, domain=None, range=Optional[str])

slots.monthMarried = Slot(uri=FAMILYCONTEXT.monthMarried, name="monthMarried", curie=FAMILYCONTEXT.curie('monthMarried'),
                   model_uri=FAMILYCONTEXT.monthMarried, domain=None, range=Optional[str])

slots.divorced = Slot(uri=FAMILYCONTEXT.divorced, name="divorced", curie=FAMILYCONTEXT.curie('divorced'),
                   model_uri=FAMILYCONTEXT.divorced, domain=None, range=Optional[str])

slots.husbandOf = Slot(uri=FAMILYCONTEXT.husbandOf, name="husbandOf", curie=FAMILYCONTEXT.curie('husbandOf'),
                   model_uri=FAMILYCONTEXT.husbandOf, domain=None, range=Optional[str])

slots.wifeOf = Slot(uri=FAMILYCONTEXT.wifeOf, name="wifeOf", curie=FAMILYCONTEXT.curie('wifeOf'),
                   model_uri=FAMILYCONTEXT.wifeOf, domain=None, range=Optional[str])

slots.qid = Slot(uri=FAMILYCONTEXT.qid, name="qid", curie=FAMILYCONTEXT.curie('qid'),
                   model_uri=FAMILYCONTEXT.qid, domain=None, range=Optional[str])

slots.royal92id = Slot(uri=FAMILYCONTEXT.royal92id, name="royal92id", curie=FAMILYCONTEXT.curie('royal92id'),
                   model_uri=FAMILYCONTEXT.royal92id, domain=None, range=Optional[str])

slots.nobleTitle = Slot(uri=FAMILYCONTEXT.nobleTitle, name="nobleTitle", curie=FAMILYCONTEXT.curie('nobleTitle'),
                   model_uri=FAMILYCONTEXT.nobleTitle, domain=None, range=Optional[str])

slots.picture = Slot(uri=FAMILYCONTEXT.picture, name="picture", curie=FAMILYCONTEXT.curie('picture'),
                   model_uri=FAMILYCONTEXT.picture, domain=None, range=Optional[str])

slots.sex = Slot(uri=FAMILYCONTEXT.sex, name="sex", curie=FAMILYCONTEXT.curie('sex'),
                   model_uri=FAMILYCONTEXT.sex, domain=None, range=Optional[str])

slots.born = Slot(uri=FAMILYCONTEXT.born, name="born", curie=FAMILYCONTEXT.curie('born'),
                   model_uri=FAMILYCONTEXT.born, domain=None, range=Optional[str])

slots.yearBorn = Slot(uri=FAMILYCONTEXT.yearBorn, name="yearBorn", curie=FAMILYCONTEXT.curie('yearBorn'),
                   model_uri=FAMILYCONTEXT.yearBorn, domain=None, range=Optional[str])

slots.monthBorn = Slot(uri=FAMILYCONTEXT.monthBorn, name="monthBorn", curie=FAMILYCONTEXT.curie('monthBorn'),
                   model_uri=FAMILYCONTEXT.monthBorn, domain=None, range=Optional[str])

slots.birthPlace = Slot(uri=FAMILYCONTEXT.birthPlace, name="birthPlace", curie=FAMILYCONTEXT.curie('birthPlace'),
                   model_uri=FAMILYCONTEXT.birthPlace, domain=None, range=Optional[str])

slots.died = Slot(uri=FAMILYCONTEXT.died, name="died", curie=FAMILYCONTEXT.curie('died'),
                   model_uri=FAMILYCONTEXT.died, domain=None, range=Optional[str])

slots.diedAt = Slot(uri=FAMILYCONTEXT.diedAt, name="diedAt", curie=FAMILYCONTEXT.curie('diedAt'),
                   model_uri=FAMILYCONTEXT.diedAt, domain=None, range=Optional[str])

slots.yearDied = Slot(uri=FAMILYCONTEXT.yearDied, name="yearDied", curie=FAMILYCONTEXT.curie('yearDied'),
                   model_uri=FAMILYCONTEXT.yearDied, domain=None, range=Optional[str])

slots.monthDied = Slot(uri=FAMILYCONTEXT.monthDied, name="monthDied", curie=FAMILYCONTEXT.curie('monthDied'),
                   model_uri=FAMILYCONTEXT.monthDied, domain=None, range=Optional[str])

slots.noInLine = Slot(uri=FAMILYCONTEXT.noInLine, name="noInLine", curie=FAMILYCONTEXT.curie('noInLine'),
                   model_uri=FAMILYCONTEXT.noInLine, domain=None, range=Optional[str])

slots.wikiPedia = Slot(uri=FAMILYCONTEXT.wikiPedia, name="wikiPedia", curie=FAMILYCONTEXT.curie('wikiPedia'),
                   model_uri=FAMILYCONTEXT.wikiPedia, domain=None, range=Optional[str])

slots.family__name = Slot(uri=FAMILYCONTEXT.name, name="family__name", curie=FAMILYCONTEXT.curie('name'),
                   model_uri=FAMILYCONTEXT.family__name, domain=None, range=Optional[str])

slots.family__weddingDate = Slot(uri=FAMILYCONTEXT.weddingDate, name="family__weddingDate", curie=FAMILYCONTEXT.curie('weddingDate'),
                   model_uri=FAMILYCONTEXT.family__weddingDate, domain=None, range=Optional[str])

slots.family__weddingPlace = Slot(uri=FAMILYCONTEXT.weddingPlace, name="family__weddingPlace", curie=FAMILYCONTEXT.curie('weddingPlace'),
                   model_uri=FAMILYCONTEXT.family__weddingPlace, domain=None, range=Optional[str])

slots.family__yearMarried = Slot(uri=FAMILYCONTEXT.yearMarried, name="family__yearMarried", curie=FAMILYCONTEXT.curie('yearMarried'),
                   model_uri=FAMILYCONTEXT.family__yearMarried, domain=None, range=Optional[str])

slots.family__monthMarried = Slot(uri=FAMILYCONTEXT.monthMarried, name="family__monthMarried", curie=FAMILYCONTEXT.curie('monthMarried'),
                   model_uri=FAMILYCONTEXT.family__monthMarried, domain=None, range=Optional[str])

slots.family__divorced = Slot(uri=FAMILYCONTEXT.divorced, name="family__divorced", curie=FAMILYCONTEXT.curie('divorced'),
                   model_uri=FAMILYCONTEXT.family__divorced, domain=None, range=Optional[str])

slots.family__husbandOf = Slot(uri=FAMILYCONTEXT.husbandOf, name="family__husbandOf", curie=FAMILYCONTEXT.curie('husbandOf'),
                   model_uri=FAMILYCONTEXT.family__husbandOf, domain=None, range=Optional[str])

slots.family__wifeOf = Slot(uri=FAMILYCONTEXT.wifeOf, name="family__wifeOf", curie=FAMILYCONTEXT.curie('wifeOf'),
                   model_uri=FAMILYCONTEXT.family__wifeOf, domain=None, range=Optional[str])

slots.person__qid = Slot(uri=FAMILYCONTEXT.qid, name="person__qid", curie=FAMILYCONTEXT.curie('qid'),
                   model_uri=FAMILYCONTEXT.person__qid, domain=None, range=Optional[str])

slots.person__royal92id = Slot(uri=FAMILYCONTEXT.royal92id, name="person__royal92id", curie=FAMILYCONTEXT.curie('royal92id'),
                   model_uri=FAMILYCONTEXT.person__royal92id, domain=None, range=Optional[str])

slots.person__name = Slot(uri=FAMILYCONTEXT.name, name="person__name", curie=FAMILYCONTEXT.curie('name'),
                   model_uri=FAMILYCONTEXT.person__name, domain=None, range=Optional[str])

slots.person__nobleTitle = Slot(uri=FAMILYCONTEXT.nobleTitle, name="person__nobleTitle", curie=FAMILYCONTEXT.curie('nobleTitle'),
                   model_uri=FAMILYCONTEXT.person__nobleTitle, domain=None, range=Optional[str])

slots.person__picture = Slot(uri=FAMILYCONTEXT.picture, name="person__picture", curie=FAMILYCONTEXT.curie('picture'),
                   model_uri=FAMILYCONTEXT.person__picture, domain=None, range=Optional[str])

slots.person__sex = Slot(uri=FAMILYCONTEXT.sex, name="person__sex", curie=FAMILYCONTEXT.curie('sex'),
                   model_uri=FAMILYCONTEXT.person__sex, domain=None, range=Optional[str])

slots.person__born = Slot(uri=FAMILYCONTEXT.born, name="person__born", curie=FAMILYCONTEXT.curie('born'),
                   model_uri=FAMILYCONTEXT.person__born, domain=None, range=Optional[str])

slots.person__yearBorn = Slot(uri=FAMILYCONTEXT.yearBorn, name="person__yearBorn", curie=FAMILYCONTEXT.curie('yearBorn'),
                   model_uri=FAMILYCONTEXT.person__yearBorn, domain=None, range=Optional[str])

slots.person__monthBorn = Slot(uri=FAMILYCONTEXT.monthBorn, name="person__monthBorn", curie=FAMILYCONTEXT.curie('monthBorn'),
                   model_uri=FAMILYCONTEXT.person__monthBorn, domain=None, range=Optional[str])

slots.person__birthPlace = Slot(uri=FAMILYCONTEXT.birthPlace, name="person__birthPlace", curie=FAMILYCONTEXT.curie('birthPlace'),
                   model_uri=FAMILYCONTEXT.person__birthPlace, domain=None, range=Optional[str])

slots.person__died = Slot(uri=FAMILYCONTEXT.died, name="person__died", curie=FAMILYCONTEXT.curie('died'),
                   model_uri=FAMILYCONTEXT.person__died, domain=None, range=Optional[str])

slots.person__diedAt = Slot(uri=FAMILYCONTEXT.diedAt, name="person__diedAt", curie=FAMILYCONTEXT.curie('diedAt'),
                   model_uri=FAMILYCONTEXT.person__diedAt, domain=None, range=Optional[str])

slots.person__yearDied = Slot(uri=FAMILYCONTEXT.yearDied, name="person__yearDied", curie=FAMILYCONTEXT.curie('yearDied'),
                   model_uri=FAMILYCONTEXT.person__yearDied, domain=None, range=Optional[str])

slots.person__monthDied = Slot(uri=FAMILYCONTEXT.monthDied, name="person__monthDied", curie=FAMILYCONTEXT.curie('monthDied'),
                   model_uri=FAMILYCONTEXT.person__monthDied, domain=None, range=Optional[str])

slots.person__noInLine = Slot(uri=FAMILYCONTEXT.noInLine, name="person__noInLine", curie=FAMILYCONTEXT.curie('noInLine'),
                   model_uri=FAMILYCONTEXT.person__noInLine, domain=None, range=Optional[str])

slots.person__wikiPedia = Slot(uri=FAMILYCONTEXT.wikiPedia, name="person__wikiPedia", curie=FAMILYCONTEXT.curie('wikiPedia'),
                   model_uri=FAMILYCONTEXT.person__wikiPedia, domain=None, range=Optional[str])
