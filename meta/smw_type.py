from typing import Optional

from basemkit.yamlable import lod_storable

@lod_storable
class SMW_Type:
    """
    an SMW_Type is a data type which determines the possible values for that type e.g. a Boolean can hold true/false values while a Number can hold 3.1459 or 20. A Page can hold the name of a Wiki page see https://semantic-mediawiki.org/wiki/Help:List_of_datatypes
    """

    pageTitle: Optional[str]
    type: Optional[
        str
    ]  # The Semantic MediaWiki type  without the prefix e.g. Text, Number, Boolean
    documentation: Optional[str]  # The documentation of this Semantic Media Wiki type
    id: Optional[str]  # SMW internal id of the type
    helppage: Optional[str]  # The url of the 'official' documentation page of this type
    typepage: Optional[
        str
    ]  # The Semantic Media Wiki Special page for this specific type e.g. Special:Types/Text, Special:Types/Boolean, Special:Types/Date, Special:Types/Number, Special:Types/Page
    javaType: Optional[str]  # Java mapping of this type

    def __post_init__(self):
        if self.pageTitle is None:
            self.pageTitle=self.typepage
        if self.pageTitle is not None and self.id is None:
            self.id = self.pageTitle.split("Special:Types/")[-1]
        pass

    @classmethod
    def askQuery(cls)->str:
        """
        get the ask Query for SMW_Type

        Returns:
            str: the mediawiki markup for the ask query
        """
        ask = """{{#ask: [[Concept:SMW_Type]]
|mainlabel=pageTitle
|?SMW_Type type = type
|?SMW_Type documentation = documentation
|?SMW_Type id = id
|?SMW_Type helppage = helppage
|?SMW_Type typepage = typepage
|?SMW_Type javaType = javaType
| limit=200
}}"""
        return ask