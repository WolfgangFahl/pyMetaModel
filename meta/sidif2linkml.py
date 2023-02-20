'''
Created on 2023-02-20

@author: wf
'''
from meta.metamodel import Context
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.linkml_model import SchemaDefinition, ClassDefinition, SlotDefinition
from linkml.generators.linkmlgen import LinkmlGenerator

class SiDIF2LinkML:
    """
    converter between SiDIF and LINKML
    """
    
    def __init__(self,context:Context):
        self.context=context
        
    def asYaml(self)->str:
        """
        convert my context
        """
        # https://linkml.io/linkml-model/docs/SchemaDefinition/
        sd=SchemaDefinition(id=self.context.name,name=self.context.name)
        sv=SchemaView(sd)
        for topic in self.context.topics.values():
            cd=ClassDefinition(name=topic.name)
            cd.description=topic.documentation
            sv.add_class(cd)
            for prop in topic.properties.values():
                qname=f"{topic.name}.{prop.name}"
                slot=SlotDefinition(name=qname)
                if hasattr(prop,"documentation"):
                    slot.description=prop.documentation
                sv.add_slot(slot)
                cd.slots.append(slot)
                pass
            
            pass
      
        lml_gen=LinkmlGenerator(schema=sd,format='yaml')
        yaml_text=lml_gen.serialize()
        return yaml_text