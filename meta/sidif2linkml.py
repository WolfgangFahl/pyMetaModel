"""
Created on 2023-02-20

@author: wf
"""

from linkml.generators.linkmlgen import LinkmlGenerator
from linkml.utils.schema_builder import SchemaBuilder
from linkml_runtime.linkml_model import (
    ClassDefinition,
    SlotDefinition,
)
from linkml_runtime.utils.schemaview import SchemaView

from meta.metamodel import Context


class SiDIF2LinkML:
    """
    converter between SiDIF and LINKML
    """

    def __init__(self, context: Context):
        self.context = context

    def asYaml(self, common_property_slots: bool = True, delim="_") -> str:
        """
        convert my context

        Args:
            common_property_slots (bool): if True reuse slots

        Returns:
            str: the yaml markup

        """
        context = self.context
        sb = SchemaBuilder(id=context.name, name=context.name)
        # https://linkml.io/linkml-model/docs/SchemaDefinition/
        sb.add_defaults()
        sd = sb.schema
        sv = SchemaView(sd)
        if hasattr(context, "copyright"):
            copyright_str = f" copyright {context.copyright}"
        else:
            copyright_str = ""
        if hasattr(context, "master"):
            master = context.master
        else:
            master = "http://example.com"
        uri = f"{master}/{context.name}"
        for topic in self.context.topics.values():
            if not topic.name:
                continue
            cd = ClassDefinition(name=topic.name)
            cd.description = topic.documentation
            sv.add_class(cd)
            for prop in topic.properties.values():
                slot = None
                if common_property_slots:
                    qname = prop.name
                    if prop.name in sd.slots:
                        slot = sd.slots[prop.name]
                        if prop.documentation:
                            slot.description += "," + prop.documentation
                else:
                    qname = f"{topic.name}{delim}{prop.name}"
                if slot is None:
                    slot = SlotDefinition(name=qname)
                    if hasattr(prop, "documentation"):
                        slot.description = prop.documentation
                    typesMap = {
                        "Boolean": "boolean",
                        "Code": "string",  # @TODO will need special type
                        "Date": "date",
                        "Text": "string",
                        "URL": "uri",
                        "Page": "string",  # @TODO will need own type
                        "Number": "double",  # @TODO will need special type handling
                    }
                    if prop.isLink:
                        # 1:1 and 1:n handling
                        slot.range = prop.topicLink.source
                    else:
                        if prop.type in typesMap:
                            slot.range = typesMap[prop.type]
                        else:
                            slot.range = "string"
                    sv.add_slot(slot)
                cd.attributes[qname] = slot
                pass

            pass

        lml_gen = LinkmlGenerator(schema=sd, format="yaml")
        yaml_text = lml_gen.serialize()
        return yaml_text
