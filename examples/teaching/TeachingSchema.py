# Auto generated from TeachingSchema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-02-23T20:29:00
# Schema: TeachingSchema
#
# id: TeachingSchema
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
TEACHINGSCHEMA = CurieNamespace('TeachingSchema', 'TeachingSchema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SHEX = CurieNamespace('shex', 'http://www.w3.org/ns/shex#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = TEACHINGSCHEMA


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = TEACHINGSCHEMA.String


class Integer(int):
    """ An integer """
    type_class_uri = XSD.integer
    type_class_curie = "xsd:integer"
    type_name = "integer"
    type_model_uri = TEACHINGSCHEMA.Integer


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = TEACHINGSCHEMA.Boolean


class Float(float):
    """ A real number that conforms to the xsd:float specification """
    type_class_uri = XSD.float
    type_class_curie = "xsd:float"
    type_name = "float"
    type_model_uri = TEACHINGSCHEMA.Float


class Double(float):
    """ A real number that conforms to the xsd:double specification """
    type_class_uri = XSD.double
    type_class_curie = "xsd:double"
    type_name = "double"
    type_model_uri = TEACHINGSCHEMA.Double


class Decimal(Decimal):
    """ A real number with arbitrary precision that conforms to the xsd:decimal specification """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal"
    type_model_uri = TEACHINGSCHEMA.Decimal


class Time(XSDTime):
    """ A time object represents a (local) time of day, independent of any particular day """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "time"
    type_model_uri = TEACHINGSCHEMA.Time


class Date(XSDDate):
    """ a date (year, month and day) in an idealized calendar """
    type_class_uri = XSD.date
    type_class_curie = "xsd:date"
    type_name = "date"
    type_model_uri = TEACHINGSCHEMA.Date


class Datetime(XSDDateTime):
    """ The combination of a date and time """
    type_class_uri = XSD.dateTime
    type_class_curie = "xsd:dateTime"
    type_name = "datetime"
    type_model_uri = TEACHINGSCHEMA.Datetime


class DateOrDatetime(str):
    """ Either a date or a datetime """
    type_class_uri = LINKML.DateOrDatetime
    type_class_curie = "linkml:DateOrDatetime"
    type_name = "date_or_datetime"
    type_model_uri = TEACHINGSCHEMA.DateOrDatetime


class Uriorcurie(URIorCURIE):
    """ a URI or a CURIE """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uriorcurie"
    type_model_uri = TEACHINGSCHEMA.Uriorcurie


class Curie(Curie):
    """ a compact URI """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "curie"
    type_model_uri = TEACHINGSCHEMA.Curie


class Uri(URI):
    """ a complete URI """
    type_class_uri = XSD.anyURI
    type_class_curie = "xsd:anyURI"
    type_name = "uri"
    type_model_uri = TEACHINGSCHEMA.Uri


class Ncname(NCName):
    """ Prefix part of CURIE """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "ncname"
    type_model_uri = TEACHINGSCHEMA.Ncname


class Objectidentifier(ElementIdentifier):
    """ A URI or CURIE that represents an object in the model. """
    type_class_uri = SHEX.iri
    type_class_curie = "shex:iri"
    type_name = "objectidentifier"
    type_model_uri = TEACHINGSCHEMA.Objectidentifier


class Nodeidentifier(NodeIdentifier):
    """ A URI, CURIE or BNODE that represents a node in a model. """
    type_class_uri = SHEX.nonLiteral
    type_class_curie = "shex:nonLiteral"
    type_name = "nodeidentifier"
    type_model_uri = TEACHINGSCHEMA.Nodeidentifier


# Class references



@dataclass
class Chapter(YAMLRoot):
    """
    a chapter of a lecture
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Chapter
    class_class_curie: ClassVar[str] = "TeachingSchema:Chapter"
    class_name: ClassVar[str] = "Chapter"
    class_model_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Chapter

    key: Optional[str] = None
    no: Optional[str] = None
    pres_id: Optional[str] = None
    week: Optional[str] = None
    de: Optional[str] = None
    en: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.key is not None and not isinstance(self.key, str):
            self.key = str(self.key)

        if self.no is not None and not isinstance(self.no, str):
            self.no = str(self.no)

        if self.pres_id is not None and not isinstance(self.pres_id, str):
            self.pres_id = str(self.pres_id)

        if self.week is not None and not isinstance(self.week, str):
            self.week = str(self.week)

        if self.de is not None and not isinstance(self.de, str):
            self.de = str(self.de)

        if self.en is not None and not isinstance(self.en, str):
            self.en = str(self.en)

        super().__post_init__(**kwargs)


@dataclass
class Presentation(YAMLRoot):
    """
    a presentation of a lecture
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Presentation
    class_class_curie: ClassVar[str] = "TeachingSchema:Presentation"
    class_name: ClassVar[str] = "Presentation"
    class_model_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Presentation

    key: Optional[str] = None
    num: Optional[str] = None
    name: Optional[str] = None
    ppt_file: Optional[str] = None
    sciebo: Optional[str] = None
    gitlab: Optional[str] = None
    moodle: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.key is not None and not isinstance(self.key, str):
            self.key = str(self.key)

        if self.num is not None and not isinstance(self.num, str):
            self.num = str(self.num)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.ppt_file is not None and not isinstance(self.ppt_file, str):
            self.ppt_file = str(self.ppt_file)

        if self.sciebo is not None and not isinstance(self.sciebo, str):
            self.sciebo = str(self.sciebo)

        if self.gitlab is not None and not isinstance(self.gitlab, str):
            self.gitlab = str(self.gitlab)

        if self.moodle is not None and not isinstance(self.moodle, str):
            self.moodle = str(self.moodle)

        super().__post_init__(**kwargs)


@dataclass
class LearningGoal(YAMLRoot):
    """
    a LearningGoal of a lecture
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEACHINGSCHEMA.LearningGoal
    class_class_curie: ClassVar[str] = "TeachingSchema:LearningGoal"
    class_name: ClassVar[str] = "LearningGoal"
    class_model_uri: ClassVar[URIRef] = TEACHINGSCHEMA.LearningGoal

    key: Optional[str] = None
    qKey: Optional[str] = None
    id: Optional[str] = None
    chapter: Optional[str] = None
    chapterKey: Optional[str] = None
    subChapter: Optional[str] = None
    subChapterKey: Optional[str] = None
    relevance: Optional[str] = None
    keywords: Optional[str] = None
    since: Optional[str] = None
    until: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.key is not None and not isinstance(self.key, str):
            self.key = str(self.key)

        if self.qKey is not None and not isinstance(self.qKey, str):
            self.qKey = str(self.qKey)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.chapter is not None and not isinstance(self.chapter, str):
            self.chapter = str(self.chapter)

        if self.chapterKey is not None and not isinstance(self.chapterKey, str):
            self.chapterKey = str(self.chapterKey)

        if self.subChapter is not None and not isinstance(self.subChapter, str):
            self.subChapter = str(self.subChapter)

        if self.subChapterKey is not None and not isinstance(self.subChapterKey, str):
            self.subChapterKey = str(self.subChapterKey)

        if self.relevance is not None and not isinstance(self.relevance, str):
            self.relevance = str(self.relevance)

        if self.keywords is not None and not isinstance(self.keywords, str):
            self.keywords = str(self.keywords)

        if self.since is not None and not isinstance(self.since, str):
            self.since = str(self.since)

        if self.until is not None and not isinstance(self.until, str):
            self.until = str(self.until)

        super().__post_init__(**kwargs)


@dataclass
class Keyword(YAMLRoot):
    """
    a keyword
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Keyword
    class_class_curie: ClassVar[str] = "TeachingSchema:Keyword"
    class_name: ClassVar[str] = "Keyword"
    class_model_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Keyword

    key: Optional[str] = None
    aliases: Optional[str] = None
    de: Optional[str] = None
    en: Optional[str] = None
    wikidataid: Optional[str] = None
    links: Optional[str] = None
    literature: Optional[str] = None
    urls: Optional[str] = None
    stackoverflow_tag: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.key is not None and not isinstance(self.key, str):
            self.key = str(self.key)

        if self.aliases is not None and not isinstance(self.aliases, str):
            self.aliases = str(self.aliases)

        if self.de is not None and not isinstance(self.de, str):
            self.de = str(self.de)

        if self.en is not None and not isinstance(self.en, str):
            self.en = str(self.en)

        if self.wikidataid is not None and not isinstance(self.wikidataid, str):
            self.wikidataid = str(self.wikidataid)

        if self.links is not None and not isinstance(self.links, str):
            self.links = str(self.links)

        if self.literature is not None and not isinstance(self.literature, str):
            self.literature = str(self.literature)

        if self.urls is not None and not isinstance(self.urls, str):
            self.urls = str(self.urls)

        if self.stackoverflow_tag is not None and not isinstance(self.stackoverflow_tag, str):
            self.stackoverflow_tag = str(self.stackoverflow_tag)

        super().__post_init__(**kwargs)


@dataclass
class Slide(YAMLRoot):
    """
    I am a presentation slide
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Slide
    class_class_curie: ClassVar[str] = "TeachingSchema:Slide"
    class_name: ClassVar[str] = "Slide"
    class_model_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Slide

    qkey: Optional[str] = None
    pkey: Optional[str] = None
    basename: Optional[str] = None
    page: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    keywords: Optional[str] = None
    links: Optional[str] = None
    literature: Optional[str] = None
    learningGoal: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.qkey is not None and not isinstance(self.qkey, str):
            self.qkey = str(self.qkey)

        if self.pkey is not None and not isinstance(self.pkey, str):
            self.pkey = str(self.pkey)

        if self.basename is not None and not isinstance(self.basename, str):
            self.basename = str(self.basename)

        if self.page is not None and not isinstance(self.page, str):
            self.page = str(self.page)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.keywords is not None and not isinstance(self.keywords, str):
            self.keywords = str(self.keywords)

        if self.links is not None and not isinstance(self.links, str):
            self.links = str(self.links)

        if self.literature is not None and not isinstance(self.literature, str):
            self.literature = str(self.literature)

        if self.learningGoal is not None and not isinstance(self.learningGoal, str):
            self.learningGoal = str(self.learningGoal)

        super().__post_init__(**kwargs)


@dataclass
class Check(YAMLRoot):
    """
    I am a quality check
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Check
    class_class_curie: ClassVar[str] = "TeachingSchema:Check"
    class_name: ClassVar[str] = "Check"
    class_model_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Check

    qKey: Optional[str] = None
    key: Optional[str] = None
    concept: Optional[str] = None
    since: Optional[str] = None
    check: Optional[str] = None
    problem: Optional[str] = None
    ok: Optional[str] = None
    total: Optional[str] = None
    pain: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.qKey is not None and not isinstance(self.qKey, str):
            self.qKey = str(self.qKey)

        if self.key is not None and not isinstance(self.key, str):
            self.key = str(self.key)

        if self.concept is not None and not isinstance(self.concept, str):
            self.concept = str(self.concept)

        if self.since is not None and not isinstance(self.since, str):
            self.since = str(self.since)

        if self.check is not None and not isinstance(self.check, str):
            self.check = str(self.check)

        if self.problem is not None and not isinstance(self.problem, str):
            self.problem = str(self.problem)

        if self.ok is not None and not isinstance(self.ok, str):
            self.ok = str(self.ok)

        if self.total is not None and not isinstance(self.total, str):
            self.total = str(self.total)

        if self.pain is not None and not isinstance(self.pain, str):
            self.pain = str(self.pain)

        super().__post_init__(**kwargs)


@dataclass
class Issue(YAMLRoot):
    """
    I am a an issue
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Issue
    class_class_curie: ClassVar[str] = "TeachingSchema:Issue"
    class_name: ClassVar[str] = "Issue"
    class_model_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Issue

    item: Optional[str] = None
    check: Optional[str] = None
    fix: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.item is not None and not isinstance(self.item, str):
            self.item = str(self.item)

        if self.check is not None and not isinstance(self.check, str):
            self.check = str(self.check)

        if self.fix is not None and not isinstance(self.fix, str):
            self.fix = str(self.fix)

        super().__post_init__(**kwargs)


@dataclass
class RelevanceLevel(YAMLRoot):
    """
    I am a relevance level
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEACHINGSCHEMA.RelevanceLevel
    class_class_curie: ClassVar[str] = "TeachingSchema:RelevanceLevel"
    class_name: ClassVar[str] = "RelevanceLevel"
    class_model_uri: ClassVar[URIRef] = TEACHINGSCHEMA.RelevanceLevel

    id: Optional[str] = None
    expectation: Optional[str] = None
    examination: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.expectation is not None and not isinstance(self.expectation, str):
            self.expectation = str(self.expectation)

        if self.examination is not None and not isinstance(self.examination, str):
            self.examination = str(self.examination)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Publication(YAMLRoot):
    """
    A Publication is e.g. a scholarly article
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Publication
    class_class_curie: ClassVar[str] = "TeachingSchema:Publication"
    class_name: ClassVar[str] = "Publication"
    class_model_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Publication

    id: Optional[str] = None
    doi: Optional[str] = None
    wikidataid: Optional[str] = None
    isbn: Optional[str] = None
    title: Optional[str] = None
    authors: Optional[str] = None
    publisher: Optional[str] = None
    year: Optional[str] = None
    pdfUrl: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.doi is not None and not isinstance(self.doi, str):
            self.doi = str(self.doi)

        if self.wikidataid is not None and not isinstance(self.wikidataid, str):
            self.wikidataid = str(self.wikidataid)

        if self.isbn is not None and not isinstance(self.isbn, str):
            self.isbn = str(self.isbn)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.authors is not None and not isinstance(self.authors, str):
            self.authors = str(self.authors)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.year is not None and not isinstance(self.year, str):
            self.year = str(self.year)

        if self.pdfUrl is not None and not isinstance(self.pdfUrl, str):
            self.pdfUrl = str(self.pdfUrl)

        super().__post_init__(**kwargs)


@dataclass
class Sheet(YAMLRoot):
    """
    I am a sheet in a spreadsheet
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Sheet
    class_class_curie: ClassVar[str] = "TeachingSchema:Sheet"
    class_name: ClassVar[str] = "Sheet"
    class_model_uri: ClassVar[URIRef] = TEACHINGSCHEMA.Sheet

    gid: Optional[str] = None
    concept: Optional[str] = None
    url: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.gid is not None and not isinstance(self.gid, str):
            self.gid = str(self.gid)

        if self.concept is not None and not isinstance(self.concept, str):
            self.concept = str(self.concept)

        if self.url is not None and not isinstance(self.url, str):
            self.url = str(self.url)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.key = Slot(uri=TEACHINGSCHEMA.key, name="key", curie=TEACHINGSCHEMA.curie('key'),
                   model_uri=TEACHINGSCHEMA.key, domain=None, range=Optional[str])

slots.no = Slot(uri=TEACHINGSCHEMA.no, name="no", curie=TEACHINGSCHEMA.curie('no'),
                   model_uri=TEACHINGSCHEMA.no, domain=None, range=Optional[str])

slots.pres_id = Slot(uri=TEACHINGSCHEMA.pres_id, name="pres_id", curie=TEACHINGSCHEMA.curie('pres_id'),
                   model_uri=TEACHINGSCHEMA.pres_id, domain=None, range=Optional[str])

slots.week = Slot(uri=TEACHINGSCHEMA.week, name="week", curie=TEACHINGSCHEMA.curie('week'),
                   model_uri=TEACHINGSCHEMA.week, domain=None, range=Optional[str])

slots.de = Slot(uri=TEACHINGSCHEMA.de, name="de", curie=TEACHINGSCHEMA.curie('de'),
                   model_uri=TEACHINGSCHEMA.de, domain=None, range=Optional[str])

slots.en = Slot(uri=TEACHINGSCHEMA.en, name="en", curie=TEACHINGSCHEMA.curie('en'),
                   model_uri=TEACHINGSCHEMA.en, domain=None, range=Optional[str])

slots.num = Slot(uri=TEACHINGSCHEMA.num, name="num", curie=TEACHINGSCHEMA.curie('num'),
                   model_uri=TEACHINGSCHEMA.num, domain=None, range=Optional[str])

slots.name = Slot(uri=TEACHINGSCHEMA.name, name="name", curie=TEACHINGSCHEMA.curie('name'),
                   model_uri=TEACHINGSCHEMA.name, domain=None, range=Optional[str])

slots.ppt_file = Slot(uri=TEACHINGSCHEMA.ppt_file, name="ppt_file", curie=TEACHINGSCHEMA.curie('ppt_file'),
                   model_uri=TEACHINGSCHEMA.ppt_file, domain=None, range=Optional[str])

slots.sciebo = Slot(uri=TEACHINGSCHEMA.sciebo, name="sciebo", curie=TEACHINGSCHEMA.curie('sciebo'),
                   model_uri=TEACHINGSCHEMA.sciebo, domain=None, range=Optional[str])

slots.gitlab = Slot(uri=TEACHINGSCHEMA.gitlab, name="gitlab", curie=TEACHINGSCHEMA.curie('gitlab'),
                   model_uri=TEACHINGSCHEMA.gitlab, domain=None, range=Optional[str])

slots.moodle = Slot(uri=TEACHINGSCHEMA.moodle, name="moodle", curie=TEACHINGSCHEMA.curie('moodle'),
                   model_uri=TEACHINGSCHEMA.moodle, domain=None, range=Optional[str])

slots.qKey = Slot(uri=TEACHINGSCHEMA.qKey, name="qKey", curie=TEACHINGSCHEMA.curie('qKey'),
                   model_uri=TEACHINGSCHEMA.qKey, domain=None, range=Optional[str])

slots.id = Slot(uri=TEACHINGSCHEMA.id, name="id", curie=TEACHINGSCHEMA.curie('id'),
                   model_uri=TEACHINGSCHEMA.id, domain=None, range=Optional[str])

slots.chapter = Slot(uri=TEACHINGSCHEMA.chapter, name="chapter", curie=TEACHINGSCHEMA.curie('chapter'),
                   model_uri=TEACHINGSCHEMA.chapter, domain=None, range=Optional[str])

slots.chapterKey = Slot(uri=TEACHINGSCHEMA.chapterKey, name="chapterKey", curie=TEACHINGSCHEMA.curie('chapterKey'),
                   model_uri=TEACHINGSCHEMA.chapterKey, domain=None, range=Optional[str])

slots.subChapter = Slot(uri=TEACHINGSCHEMA.subChapter, name="subChapter", curie=TEACHINGSCHEMA.curie('subChapter'),
                   model_uri=TEACHINGSCHEMA.subChapter, domain=None, range=Optional[str])

slots.subChapterKey = Slot(uri=TEACHINGSCHEMA.subChapterKey, name="subChapterKey", curie=TEACHINGSCHEMA.curie('subChapterKey'),
                   model_uri=TEACHINGSCHEMA.subChapterKey, domain=None, range=Optional[str])

slots.relevance = Slot(uri=TEACHINGSCHEMA.relevance, name="relevance", curie=TEACHINGSCHEMA.curie('relevance'),
                   model_uri=TEACHINGSCHEMA.relevance, domain=None, range=Optional[str])

slots.keywords = Slot(uri=TEACHINGSCHEMA.keywords, name="keywords", curie=TEACHINGSCHEMA.curie('keywords'),
                   model_uri=TEACHINGSCHEMA.keywords, domain=None, range=Optional[str])

slots.since = Slot(uri=TEACHINGSCHEMA.since, name="since", curie=TEACHINGSCHEMA.curie('since'),
                   model_uri=TEACHINGSCHEMA.since, domain=None, range=Optional[str])

slots.until = Slot(uri=TEACHINGSCHEMA.until, name="until", curie=TEACHINGSCHEMA.curie('until'),
                   model_uri=TEACHINGSCHEMA.until, domain=None, range=Optional[str])

slots.aliases = Slot(uri=TEACHINGSCHEMA.aliases, name="aliases", curie=TEACHINGSCHEMA.curie('aliases'),
                   model_uri=TEACHINGSCHEMA.aliases, domain=None, range=Optional[str])

slots.wikidataid = Slot(uri=TEACHINGSCHEMA.wikidataid, name="wikidataid", curie=TEACHINGSCHEMA.curie('wikidataid'),
                   model_uri=TEACHINGSCHEMA.wikidataid, domain=None, range=Optional[str])

slots.links = Slot(uri=TEACHINGSCHEMA.links, name="links", curie=TEACHINGSCHEMA.curie('links'),
                   model_uri=TEACHINGSCHEMA.links, domain=None, range=Optional[str])

slots.literature = Slot(uri=TEACHINGSCHEMA.literature, name="literature", curie=TEACHINGSCHEMA.curie('literature'),
                   model_uri=TEACHINGSCHEMA.literature, domain=None, range=Optional[str])

slots.urls = Slot(uri=TEACHINGSCHEMA.urls, name="urls", curie=TEACHINGSCHEMA.curie('urls'),
                   model_uri=TEACHINGSCHEMA.urls, domain=None, range=Optional[str])

slots.stackoverflow_tag = Slot(uri=TEACHINGSCHEMA.stackoverflow_tag, name="stackoverflow_tag", curie=TEACHINGSCHEMA.curie('stackoverflow_tag'),
                   model_uri=TEACHINGSCHEMA.stackoverflow_tag, domain=None, range=Optional[str])

slots.qkey = Slot(uri=TEACHINGSCHEMA.qkey, name="qkey", curie=TEACHINGSCHEMA.curie('qkey'),
                   model_uri=TEACHINGSCHEMA.qkey, domain=None, range=Optional[str])

slots.pkey = Slot(uri=TEACHINGSCHEMA.pkey, name="pkey", curie=TEACHINGSCHEMA.curie('pkey'),
                   model_uri=TEACHINGSCHEMA.pkey, domain=None, range=Optional[str])

slots.basename = Slot(uri=TEACHINGSCHEMA.basename, name="basename", curie=TEACHINGSCHEMA.curie('basename'),
                   model_uri=TEACHINGSCHEMA.basename, domain=None, range=Optional[str])

slots.page = Slot(uri=TEACHINGSCHEMA.page, name="page", curie=TEACHINGSCHEMA.curie('page'),
                   model_uri=TEACHINGSCHEMA.page, domain=None, range=Optional[str])

slots.title = Slot(uri=TEACHINGSCHEMA.title, name="title", curie=TEACHINGSCHEMA.curie('title'),
                   model_uri=TEACHINGSCHEMA.title, domain=None, range=Optional[str])

slots.learningGoal = Slot(uri=TEACHINGSCHEMA.learningGoal, name="learningGoal", curie=TEACHINGSCHEMA.curie('learningGoal'),
                   model_uri=TEACHINGSCHEMA.learningGoal, domain=None, range=Optional[str])

slots.concept = Slot(uri=TEACHINGSCHEMA.concept, name="concept", curie=TEACHINGSCHEMA.curie('concept'),
                   model_uri=TEACHINGSCHEMA.concept, domain=None, range=Optional[str])

slots.check = Slot(uri=TEACHINGSCHEMA.check, name="check", curie=TEACHINGSCHEMA.curie('check'),
                   model_uri=TEACHINGSCHEMA.check, domain=None, range=Optional[str])

slots.problem = Slot(uri=TEACHINGSCHEMA.problem, name="problem", curie=TEACHINGSCHEMA.curie('problem'),
                   model_uri=TEACHINGSCHEMA.problem, domain=None, range=Optional[str])

slots.ok = Slot(uri=TEACHINGSCHEMA.ok, name="ok", curie=TEACHINGSCHEMA.curie('ok'),
                   model_uri=TEACHINGSCHEMA.ok, domain=None, range=Optional[str])

slots.total = Slot(uri=TEACHINGSCHEMA.total, name="total", curie=TEACHINGSCHEMA.curie('total'),
                   model_uri=TEACHINGSCHEMA.total, domain=None, range=Optional[str])

slots.pain = Slot(uri=TEACHINGSCHEMA.pain, name="pain", curie=TEACHINGSCHEMA.curie('pain'),
                   model_uri=TEACHINGSCHEMA.pain, domain=None, range=Optional[str])

slots.item = Slot(uri=TEACHINGSCHEMA.item, name="item", curie=TEACHINGSCHEMA.curie('item'),
                   model_uri=TEACHINGSCHEMA.item, domain=None, range=Optional[str])

slots.fix = Slot(uri=TEACHINGSCHEMA.fix, name="fix", curie=TEACHINGSCHEMA.curie('fix'),
                   model_uri=TEACHINGSCHEMA.fix, domain=None, range=Optional[str])

slots.expectation = Slot(uri=TEACHINGSCHEMA.expectation, name="expectation", curie=TEACHINGSCHEMA.curie('expectation'),
                   model_uri=TEACHINGSCHEMA.expectation, domain=None, range=Optional[str])

slots.examination = Slot(uri=TEACHINGSCHEMA.examination, name="examination", curie=TEACHINGSCHEMA.curie('examination'),
                   model_uri=TEACHINGSCHEMA.examination, domain=None, range=Optional[str])

slots.description = Slot(uri=TEACHINGSCHEMA.description, name="description", curie=TEACHINGSCHEMA.curie('description'),
                   model_uri=TEACHINGSCHEMA.description, domain=None, range=Optional[str])

slots.doi = Slot(uri=TEACHINGSCHEMA.doi, name="doi", curie=TEACHINGSCHEMA.curie('doi'),
                   model_uri=TEACHINGSCHEMA.doi, domain=None, range=Optional[str])

slots.isbn = Slot(uri=TEACHINGSCHEMA.isbn, name="isbn", curie=TEACHINGSCHEMA.curie('isbn'),
                   model_uri=TEACHINGSCHEMA.isbn, domain=None, range=Optional[str])

slots.authors = Slot(uri=TEACHINGSCHEMA.authors, name="authors", curie=TEACHINGSCHEMA.curie('authors'),
                   model_uri=TEACHINGSCHEMA.authors, domain=None, range=Optional[str])

slots.publisher = Slot(uri=TEACHINGSCHEMA.publisher, name="publisher", curie=TEACHINGSCHEMA.curie('publisher'),
                   model_uri=TEACHINGSCHEMA.publisher, domain=None, range=Optional[str])

slots.year = Slot(uri=TEACHINGSCHEMA.year, name="year", curie=TEACHINGSCHEMA.curie('year'),
                   model_uri=TEACHINGSCHEMA.year, domain=None, range=Optional[str])

slots.pdfUrl = Slot(uri=TEACHINGSCHEMA.pdfUrl, name="pdfUrl", curie=TEACHINGSCHEMA.curie('pdfUrl'),
                   model_uri=TEACHINGSCHEMA.pdfUrl, domain=None, range=Optional[str])

slots.gid = Slot(uri=TEACHINGSCHEMA.gid, name="gid", curie=TEACHINGSCHEMA.curie('gid'),
                   model_uri=TEACHINGSCHEMA.gid, domain=None, range=Optional[str])

slots.url = Slot(uri=TEACHINGSCHEMA.url, name="url", curie=TEACHINGSCHEMA.curie('url'),
                   model_uri=TEACHINGSCHEMA.url, domain=None, range=Optional[str])

slots.chapter__key = Slot(uri=TEACHINGSCHEMA.key, name="chapter__key", curie=TEACHINGSCHEMA.curie('key'),
                   model_uri=TEACHINGSCHEMA.chapter__key, domain=None, range=Optional[str])

slots.chapter__no = Slot(uri=TEACHINGSCHEMA.no, name="chapter__no", curie=TEACHINGSCHEMA.curie('no'),
                   model_uri=TEACHINGSCHEMA.chapter__no, domain=None, range=Optional[str])

slots.chapter__pres_id = Slot(uri=TEACHINGSCHEMA.pres_id, name="chapter__pres_id", curie=TEACHINGSCHEMA.curie('pres_id'),
                   model_uri=TEACHINGSCHEMA.chapter__pres_id, domain=None, range=Optional[str])

slots.chapter__week = Slot(uri=TEACHINGSCHEMA.week, name="chapter__week", curie=TEACHINGSCHEMA.curie('week'),
                   model_uri=TEACHINGSCHEMA.chapter__week, domain=None, range=Optional[str])

slots.chapter__de = Slot(uri=TEACHINGSCHEMA.de, name="chapter__de", curie=TEACHINGSCHEMA.curie('de'),
                   model_uri=TEACHINGSCHEMA.chapter__de, domain=None, range=Optional[str])

slots.chapter__en = Slot(uri=TEACHINGSCHEMA.en, name="chapter__en", curie=TEACHINGSCHEMA.curie('en'),
                   model_uri=TEACHINGSCHEMA.chapter__en, domain=None, range=Optional[str])

slots.presentation__key = Slot(uri=TEACHINGSCHEMA.key, name="presentation__key", curie=TEACHINGSCHEMA.curie('key'),
                   model_uri=TEACHINGSCHEMA.presentation__key, domain=None, range=Optional[str])

slots.presentation__num = Slot(uri=TEACHINGSCHEMA.num, name="presentation__num", curie=TEACHINGSCHEMA.curie('num'),
                   model_uri=TEACHINGSCHEMA.presentation__num, domain=None, range=Optional[str])

slots.presentation__name = Slot(uri=TEACHINGSCHEMA.name, name="presentation__name", curie=TEACHINGSCHEMA.curie('name'),
                   model_uri=TEACHINGSCHEMA.presentation__name, domain=None, range=Optional[str])

slots.presentation__ppt_file = Slot(uri=TEACHINGSCHEMA.ppt_file, name="presentation__ppt_file", curie=TEACHINGSCHEMA.curie('ppt_file'),
                   model_uri=TEACHINGSCHEMA.presentation__ppt_file, domain=None, range=Optional[str])

slots.presentation__sciebo = Slot(uri=TEACHINGSCHEMA.sciebo, name="presentation__sciebo", curie=TEACHINGSCHEMA.curie('sciebo'),
                   model_uri=TEACHINGSCHEMA.presentation__sciebo, domain=None, range=Optional[str])

slots.presentation__gitlab = Slot(uri=TEACHINGSCHEMA.gitlab, name="presentation__gitlab", curie=TEACHINGSCHEMA.curie('gitlab'),
                   model_uri=TEACHINGSCHEMA.presentation__gitlab, domain=None, range=Optional[str])

slots.presentation__moodle = Slot(uri=TEACHINGSCHEMA.moodle, name="presentation__moodle", curie=TEACHINGSCHEMA.curie('moodle'),
                   model_uri=TEACHINGSCHEMA.presentation__moodle, domain=None, range=Optional[str])

slots.learningGoal__key = Slot(uri=TEACHINGSCHEMA.key, name="learningGoal__key", curie=TEACHINGSCHEMA.curie('key'),
                   model_uri=TEACHINGSCHEMA.learningGoal__key, domain=None, range=Optional[str])

slots.learningGoal__qKey = Slot(uri=TEACHINGSCHEMA.qKey, name="learningGoal__qKey", curie=TEACHINGSCHEMA.curie('qKey'),
                   model_uri=TEACHINGSCHEMA.learningGoal__qKey, domain=None, range=Optional[str])

slots.learningGoal__id = Slot(uri=TEACHINGSCHEMA.id, name="learningGoal__id", curie=TEACHINGSCHEMA.curie('id'),
                   model_uri=TEACHINGSCHEMA.learningGoal__id, domain=None, range=Optional[str])

slots.learningGoal__chapter = Slot(uri=TEACHINGSCHEMA.chapter, name="learningGoal__chapter", curie=TEACHINGSCHEMA.curie('chapter'),
                   model_uri=TEACHINGSCHEMA.learningGoal__chapter, domain=None, range=Optional[str])

slots.learningGoal__chapterKey = Slot(uri=TEACHINGSCHEMA.chapterKey, name="learningGoal__chapterKey", curie=TEACHINGSCHEMA.curie('chapterKey'),
                   model_uri=TEACHINGSCHEMA.learningGoal__chapterKey, domain=None, range=Optional[str])

slots.learningGoal__subChapter = Slot(uri=TEACHINGSCHEMA.subChapter, name="learningGoal__subChapter", curie=TEACHINGSCHEMA.curie('subChapter'),
                   model_uri=TEACHINGSCHEMA.learningGoal__subChapter, domain=None, range=Optional[str])

slots.learningGoal__subChapterKey = Slot(uri=TEACHINGSCHEMA.subChapterKey, name="learningGoal__subChapterKey", curie=TEACHINGSCHEMA.curie('subChapterKey'),
                   model_uri=TEACHINGSCHEMA.learningGoal__subChapterKey, domain=None, range=Optional[str])

slots.learningGoal__relevance = Slot(uri=TEACHINGSCHEMA.relevance, name="learningGoal__relevance", curie=TEACHINGSCHEMA.curie('relevance'),
                   model_uri=TEACHINGSCHEMA.learningGoal__relevance, domain=None, range=Optional[str])

slots.learningGoal__keywords = Slot(uri=TEACHINGSCHEMA.keywords, name="learningGoal__keywords", curie=TEACHINGSCHEMA.curie('keywords'),
                   model_uri=TEACHINGSCHEMA.learningGoal__keywords, domain=None, range=Optional[str])

slots.learningGoal__since = Slot(uri=TEACHINGSCHEMA.since, name="learningGoal__since", curie=TEACHINGSCHEMA.curie('since'),
                   model_uri=TEACHINGSCHEMA.learningGoal__since, domain=None, range=Optional[str])

slots.learningGoal__until = Slot(uri=TEACHINGSCHEMA.until, name="learningGoal__until", curie=TEACHINGSCHEMA.curie('until'),
                   model_uri=TEACHINGSCHEMA.learningGoal__until, domain=None, range=Optional[str])

slots.keyword__key = Slot(uri=TEACHINGSCHEMA.key, name="keyword__key", curie=TEACHINGSCHEMA.curie('key'),
                   model_uri=TEACHINGSCHEMA.keyword__key, domain=None, range=Optional[str])

slots.keyword__aliases = Slot(uri=TEACHINGSCHEMA.aliases, name="keyword__aliases", curie=TEACHINGSCHEMA.curie('aliases'),
                   model_uri=TEACHINGSCHEMA.keyword__aliases, domain=None, range=Optional[str])

slots.keyword__de = Slot(uri=TEACHINGSCHEMA.de, name="keyword__de", curie=TEACHINGSCHEMA.curie('de'),
                   model_uri=TEACHINGSCHEMA.keyword__de, domain=None, range=Optional[str])

slots.keyword__en = Slot(uri=TEACHINGSCHEMA.en, name="keyword__en", curie=TEACHINGSCHEMA.curie('en'),
                   model_uri=TEACHINGSCHEMA.keyword__en, domain=None, range=Optional[str])

slots.keyword__wikidataid = Slot(uri=TEACHINGSCHEMA.wikidataid, name="keyword__wikidataid", curie=TEACHINGSCHEMA.curie('wikidataid'),
                   model_uri=TEACHINGSCHEMA.keyword__wikidataid, domain=None, range=Optional[str])

slots.keyword__links = Slot(uri=TEACHINGSCHEMA.links, name="keyword__links", curie=TEACHINGSCHEMA.curie('links'),
                   model_uri=TEACHINGSCHEMA.keyword__links, domain=None, range=Optional[str])

slots.keyword__literature = Slot(uri=TEACHINGSCHEMA.literature, name="keyword__literature", curie=TEACHINGSCHEMA.curie('literature'),
                   model_uri=TEACHINGSCHEMA.keyword__literature, domain=None, range=Optional[str])

slots.keyword__urls = Slot(uri=TEACHINGSCHEMA.urls, name="keyword__urls", curie=TEACHINGSCHEMA.curie('urls'),
                   model_uri=TEACHINGSCHEMA.keyword__urls, domain=None, range=Optional[str])

slots.keyword__stackoverflow_tag = Slot(uri=TEACHINGSCHEMA.stackoverflow_tag, name="keyword__stackoverflow_tag", curie=TEACHINGSCHEMA.curie('stackoverflow_tag'),
                   model_uri=TEACHINGSCHEMA.keyword__stackoverflow_tag, domain=None, range=Optional[str])

slots.slide__qkey = Slot(uri=TEACHINGSCHEMA.qkey, name="slide__qkey", curie=TEACHINGSCHEMA.curie('qkey'),
                   model_uri=TEACHINGSCHEMA.slide__qkey, domain=None, range=Optional[str])

slots.slide__pkey = Slot(uri=TEACHINGSCHEMA.pkey, name="slide__pkey", curie=TEACHINGSCHEMA.curie('pkey'),
                   model_uri=TEACHINGSCHEMA.slide__pkey, domain=None, range=Optional[str])

slots.slide__basename = Slot(uri=TEACHINGSCHEMA.basename, name="slide__basename", curie=TEACHINGSCHEMA.curie('basename'),
                   model_uri=TEACHINGSCHEMA.slide__basename, domain=None, range=Optional[str])

slots.slide__page = Slot(uri=TEACHINGSCHEMA.page, name="slide__page", curie=TEACHINGSCHEMA.curie('page'),
                   model_uri=TEACHINGSCHEMA.slide__page, domain=None, range=Optional[str])

slots.slide__name = Slot(uri=TEACHINGSCHEMA.name, name="slide__name", curie=TEACHINGSCHEMA.curie('name'),
                   model_uri=TEACHINGSCHEMA.slide__name, domain=None, range=Optional[str])

slots.slide__title = Slot(uri=TEACHINGSCHEMA.title, name="slide__title", curie=TEACHINGSCHEMA.curie('title'),
                   model_uri=TEACHINGSCHEMA.slide__title, domain=None, range=Optional[str])

slots.slide__keywords = Slot(uri=TEACHINGSCHEMA.keywords, name="slide__keywords", curie=TEACHINGSCHEMA.curie('keywords'),
                   model_uri=TEACHINGSCHEMA.slide__keywords, domain=None, range=Optional[str])

slots.slide__links = Slot(uri=TEACHINGSCHEMA.links, name="slide__links", curie=TEACHINGSCHEMA.curie('links'),
                   model_uri=TEACHINGSCHEMA.slide__links, domain=None, range=Optional[str])

slots.slide__literature = Slot(uri=TEACHINGSCHEMA.literature, name="slide__literature", curie=TEACHINGSCHEMA.curie('literature'),
                   model_uri=TEACHINGSCHEMA.slide__literature, domain=None, range=Optional[str])

slots.slide__learningGoal = Slot(uri=TEACHINGSCHEMA.learningGoal, name="slide__learningGoal", curie=TEACHINGSCHEMA.curie('learningGoal'),
                   model_uri=TEACHINGSCHEMA.slide__learningGoal, domain=None, range=Optional[str])

slots.check__qKey = Slot(uri=TEACHINGSCHEMA.qKey, name="check__qKey", curie=TEACHINGSCHEMA.curie('qKey'),
                   model_uri=TEACHINGSCHEMA.check__qKey, domain=None, range=Optional[str])

slots.check__key = Slot(uri=TEACHINGSCHEMA.key, name="check__key", curie=TEACHINGSCHEMA.curie('key'),
                   model_uri=TEACHINGSCHEMA.check__key, domain=None, range=Optional[str])

slots.check__concept = Slot(uri=TEACHINGSCHEMA.concept, name="check__concept", curie=TEACHINGSCHEMA.curie('concept'),
                   model_uri=TEACHINGSCHEMA.check__concept, domain=None, range=Optional[str])

slots.check__since = Slot(uri=TEACHINGSCHEMA.since, name="check__since", curie=TEACHINGSCHEMA.curie('since'),
                   model_uri=TEACHINGSCHEMA.check__since, domain=None, range=Optional[str])

slots.check__check = Slot(uri=TEACHINGSCHEMA.check, name="check__check", curie=TEACHINGSCHEMA.curie('check'),
                   model_uri=TEACHINGSCHEMA.check__check, domain=None, range=Optional[str])

slots.check__problem = Slot(uri=TEACHINGSCHEMA.problem, name="check__problem", curie=TEACHINGSCHEMA.curie('problem'),
                   model_uri=TEACHINGSCHEMA.check__problem, domain=None, range=Optional[str])

slots.check__ok = Slot(uri=TEACHINGSCHEMA.ok, name="check__ok", curie=TEACHINGSCHEMA.curie('ok'),
                   model_uri=TEACHINGSCHEMA.check__ok, domain=None, range=Optional[str])

slots.check__total = Slot(uri=TEACHINGSCHEMA.total, name="check__total", curie=TEACHINGSCHEMA.curie('total'),
                   model_uri=TEACHINGSCHEMA.check__total, domain=None, range=Optional[str])

slots.check__pain = Slot(uri=TEACHINGSCHEMA.pain, name="check__pain", curie=TEACHINGSCHEMA.curie('pain'),
                   model_uri=TEACHINGSCHEMA.check__pain, domain=None, range=Optional[str])

slots.issue__item = Slot(uri=TEACHINGSCHEMA.item, name="issue__item", curie=TEACHINGSCHEMA.curie('item'),
                   model_uri=TEACHINGSCHEMA.issue__item, domain=None, range=Optional[str])

slots.issue__check = Slot(uri=TEACHINGSCHEMA.check, name="issue__check", curie=TEACHINGSCHEMA.curie('check'),
                   model_uri=TEACHINGSCHEMA.issue__check, domain=None, range=Optional[str])

slots.issue__fix = Slot(uri=TEACHINGSCHEMA.fix, name="issue__fix", curie=TEACHINGSCHEMA.curie('fix'),
                   model_uri=TEACHINGSCHEMA.issue__fix, domain=None, range=Optional[str])

slots.relevanceLevel__id = Slot(uri=TEACHINGSCHEMA.id, name="relevanceLevel__id", curie=TEACHINGSCHEMA.curie('id'),
                   model_uri=TEACHINGSCHEMA.relevanceLevel__id, domain=None, range=Optional[str])

slots.relevanceLevel__expectation = Slot(uri=TEACHINGSCHEMA.expectation, name="relevanceLevel__expectation", curie=TEACHINGSCHEMA.curie('expectation'),
                   model_uri=TEACHINGSCHEMA.relevanceLevel__expectation, domain=None, range=Optional[str])

slots.relevanceLevel__examination = Slot(uri=TEACHINGSCHEMA.examination, name="relevanceLevel__examination", curie=TEACHINGSCHEMA.curie('examination'),
                   model_uri=TEACHINGSCHEMA.relevanceLevel__examination, domain=None, range=Optional[str])

slots.relevanceLevel__description = Slot(uri=TEACHINGSCHEMA.description, name="relevanceLevel__description", curie=TEACHINGSCHEMA.curie('description'),
                   model_uri=TEACHINGSCHEMA.relevanceLevel__description, domain=None, range=Optional[str])

slots.publication__id = Slot(uri=TEACHINGSCHEMA.id, name="publication__id", curie=TEACHINGSCHEMA.curie('id'),
                   model_uri=TEACHINGSCHEMA.publication__id, domain=None, range=Optional[str])

slots.publication__doi = Slot(uri=TEACHINGSCHEMA.doi, name="publication__doi", curie=TEACHINGSCHEMA.curie('doi'),
                   model_uri=TEACHINGSCHEMA.publication__doi, domain=None, range=Optional[str])

slots.publication__wikidataid = Slot(uri=TEACHINGSCHEMA.wikidataid, name="publication__wikidataid", curie=TEACHINGSCHEMA.curie('wikidataid'),
                   model_uri=TEACHINGSCHEMA.publication__wikidataid, domain=None, range=Optional[str])

slots.publication__isbn = Slot(uri=TEACHINGSCHEMA.isbn, name="publication__isbn", curie=TEACHINGSCHEMA.curie('isbn'),
                   model_uri=TEACHINGSCHEMA.publication__isbn, domain=None, range=Optional[str])

slots.publication__title = Slot(uri=TEACHINGSCHEMA.title, name="publication__title", curie=TEACHINGSCHEMA.curie('title'),
                   model_uri=TEACHINGSCHEMA.publication__title, domain=None, range=Optional[str])

slots.publication__authors = Slot(uri=TEACHINGSCHEMA.authors, name="publication__authors", curie=TEACHINGSCHEMA.curie('authors'),
                   model_uri=TEACHINGSCHEMA.publication__authors, domain=None, range=Optional[str])

slots.publication__publisher = Slot(uri=TEACHINGSCHEMA.publisher, name="publication__publisher", curie=TEACHINGSCHEMA.curie('publisher'),
                   model_uri=TEACHINGSCHEMA.publication__publisher, domain=None, range=Optional[str])

slots.publication__year = Slot(uri=TEACHINGSCHEMA.year, name="publication__year", curie=TEACHINGSCHEMA.curie('year'),
                   model_uri=TEACHINGSCHEMA.publication__year, domain=None, range=Optional[str])

slots.publication__pdfUrl = Slot(uri=TEACHINGSCHEMA.pdfUrl, name="publication__pdfUrl", curie=TEACHINGSCHEMA.curie('pdfUrl'),
                   model_uri=TEACHINGSCHEMA.publication__pdfUrl, domain=None, range=Optional[str])

slots.sheet__gid = Slot(uri=TEACHINGSCHEMA.gid, name="sheet__gid", curie=TEACHINGSCHEMA.curie('gid'),
                   model_uri=TEACHINGSCHEMA.sheet__gid, domain=None, range=Optional[str])

slots.sheet__concept = Slot(uri=TEACHINGSCHEMA.concept, name="sheet__concept", curie=TEACHINGSCHEMA.curie('concept'),
                   model_uri=TEACHINGSCHEMA.sheet__concept, domain=None, range=Optional[str])

slots.sheet__url = Slot(uri=TEACHINGSCHEMA.url, name="sheet__url", curie=TEACHINGSCHEMA.curie('url'),
                   model_uri=TEACHINGSCHEMA.sheet__url, domain=None, range=Optional[str])
