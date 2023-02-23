'''
Created on 2023-02-20

@author: wf
'''
from meta.metamodel import Context
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.linkml_model import SchemaDefinition, ClassDefinition, SlotDefinition
from linkml.generators.linkmlgen import LinkmlGenerator
from linkml_runtime.linkml_model import Prefix

class SiDIF2LinkML:
    """
    converter between SiDIF and LINKML
    """
    
    def __init__(self,context:Context):
        self.context=context
        
    def asYaml(self,common_property_slots:bool=True,delim="_")->str:
        """
        convert my context
        
        Args:
            common_property_slots(bool): if True reuse slots 
            
        Returns:
            str: the yaml markup
        
        """
        # https://linkml.io/linkml-model/docs/SchemaDefinition/
        context=self.context
        sd=SchemaDefinition(id=context.name,name=context.name)
        sd.default_range="string"
        sd.default_prefix=context.name
        sv=SchemaView(sd)
        if hasattr(context,"copyright"):
            copyright_str=f" copyright {context.copyright}"
        else:
            copyright_str=""
        if hasattr(context,"master"):
            master=context.master
        else:
            master="http://example.com"
        uri=f"{master}/{context.name}"
        # Create a Prefix instance
        prefix = Prefix(
            #name=context.name,
            prefix_prefix=context.name,
            prefix_reference=uri,
            #default_curi=True,
            #description=f"{context.name}{copyright_str}"
        )

        # Add the Prefix instance to the SchemaDefinition
        sd.prefixes[context.name] = prefix
        for topic in self.context.topics.values():
            cd=ClassDefinition(name=topic.name)
            cd.description=topic.documentation
            sv.add_class(cd)
            for prop in topic.properties.values():
                slot=None
                if common_property_slots:
                    qname=prop.name
                    if prop.name in sd.slots:
                        slot=sd.slots[prop.name]
                        slot.description+=","+prop.documentation
                else:
                    qname=f"{topic.name}{delim}{prop.name}"
                if slot is None:
                    slot=SlotDefinition(name=qname)
                    if hasattr(prop,"documentation"):
                        slot.description=prop.documentation  
                    slot.range="string"       
                    sv.add_slot(slot)
                cd.attributes[qname]=slot
                pass
            
            pass
      
        lml_gen=LinkmlGenerator(schema=sd,format='yaml')
        yaml_text=lml_gen.serialize()
        return yaml_text