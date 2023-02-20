'''
Created on 2023-02-20

@author: wf
'''
from meta.metamodel import Context
from linkml_runtime.utils.schemaview import SchemaView
from linkml_runtime.linkml_model import SchemaDefinition, ClassDefinition
from linkml.generators.linkmlgen import LinkmlGenerator
import yaml

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
            sv.add_class(cd)
            pass
      
        lml_gen=LinkmlGenerator(schema=sd,format='yaml')
        yaml_text=lml_gen.serialize()
        return yaml_text