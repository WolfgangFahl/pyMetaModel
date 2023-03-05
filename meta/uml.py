'''
Created on 2020-11-12

@author: wf
'''

class PlantUml(object):
    '''
    classdocs
    '''
    
    # redundant to skinparams in pylodstorage.uml
    skinparams="""
' BITPlan Corporate identity skin params
' Copyright (c) 2015-2023 BITPlan GmbH
' see http://wiki.bitplan.com/PlantUmlSkinParams#BITPlanCI
' skinparams generated by com.bitplan.restmodelmanager
skinparam note {
  BackGroundColor #FFFFFF
  FontSize 12
  ArrowColor #FF8000
  BorderColor #FF8000
  FontColor black
  FontName Technical
}
skinparam component {
  BackGroundColor #FFFFFF
  FontSize 12
  ArrowColor #FF8000
  BorderColor #FF8000
  FontColor black
  FontName Technical
}
skinparam package {
  BackGroundColor #FFFFFF
  FontSize 12
  ArrowColor #FF8000
  BorderColor #FF8000
  FontColor black
  FontName Technical
}
skinparam usecase {
  BackGroundColor #FFFFFF
  FontSize 12
  ArrowColor #FF8000
  BorderColor #FF8000
  FontColor black
  FontName Technical
}
skinparam activity {
  BackGroundColor #FFFFFF
  FontSize 12
  ArrowColor #FF8000
  BorderColor #FF8000
  FontColor black
  FontName Technical
}
skinparam classAttribute {
  BackGroundColor #FFFFFF
  FontSize 12
  ArrowColor #FF8000
  BorderColor #FF8000
  FontColor black
  FontName Technical
}
skinparam interface {
  BackGroundColor #FFFFFF
  FontSize 12
  ArrowColor #FF8000
  BorderColor #FF8000
  FontColor black
  FontName Technical
}
skinparam class {
  BackGroundColor #FFFFFF
  FontSize 12
  ArrowColor #FF8000
  BorderColor #FF8000
  FontColor black
  FontName Technical
}
skinparam object {
  BackGroundColor #FFFFFF
  FontSize 12
  ArrowColor #FF8000
  BorderColor #FF8000
  FontColor black
  FontName Technical
}
hide Circle
' end of skinparams '
"""

    def __init__(self,copyRight=None,title=None,debug=False,withSkin=True):
        '''
        Constructor
        '''
        self.debug=debug
        self.withSkin=withSkin
        self.uml=""
        self.title=title
        self.copyRight=copyRight
        
    def __str__(self):
        return self.uml
    
    def asUmlDict(self,dif):
        '''
        return the given DataInterchange as a UML Dict
        '''
        uml={'packages':{},'topiclinks':{}}
        for triple in dif.triples:
            if self.debug:
                print(triple)
            if triple.p=="isA":
                itkey=triple.s
                if triple.o=="Context":
                    packageKey=itkey
                    packages=uml['packages']
                    packages[itkey]={"classes":{}}
                    it=packages[itkey]
                elif triple.o=="TopicLink":
                    links=uml['topiclinks']
                    links[itkey]={}
                    it=links[itkey]
                elif  triple.o=="Topic":
                    classKey=itkey
                    classes=packages[packageKey]['classes']
                    classes[itkey]={"properties":{}}                   
                    it=classes[itkey]
                elif triple.o=="Property": 
                    propKey=itkey
                    properties=classes[classKey]['properties']
                    properties[propKey]={}  
                    it=properties[propKey]
            elif triple.o=="it":
                if triple.p=="addsTo":
                    # redundant forward declaration
                    pass
                elif triple.p=="context":
                    parentKey=triple.s
                    packages[parentKey]["classes"][classKey]=classes[classKey]
                    pass
                elif triple.p=="topic":
                    parentKey=triple.s
                    classes[parentKey]["properties"][propKey]=properties[propKey]
                    pass                    
                else:
                    it[triple.p]=triple.s
        return uml
        
    def fromDIF(self,dif):
        '''
        create uml from a Data Interchange
        '''
        umlDict=self.asUmlDict(dif)
        if self.title is not None:
            if self.copyRight is None:
                copyRight=""
            else:
                copyRight="\n%s" % self.copyRight
            self.uml+="title\n%s%s\nend title\n" % (self.title,copyRight)
        packages=umlDict['packages']
        for packageKey in packages.keys():
            package=packages[packageKey]
            self.uml+="package %s {\n" % package['name']
            for classKey in package["classes"]:
                uclass=package["classes"][classKey]
                className=uclass['name']
                self.uml+="  class %s {\n" % className
                for propKey in uclass["properties"]:
                    prop=uclass["properties"][propKey]
                    self.uml+="    %s:%s\n" % (prop['name'],prop['type'])
                self.uml+="  }\n"
                if 'documentation' in uclass:
                    self.uml+="Note top of %s\n%s\nEnd note\n" % (className,uclass['documentation'])
            self.uml+="}\n"        
        links=umlDict['topiclinks']
        for linkKey in links.keys():
            link=links[linkKey]
            sourceMany="*" if link['sourceMultiple'] else "1"
            targetMany="*" if link['targetMultiple'] else "1"
            sourceRole=link['sourceRole'] if 'sourceRole' in link else ''
            targetRole=link['targetRole'] if 'targetRole' in link else ''
            source=link["source"]
            target=link["target"]
            
            self.uml+="""%s "%s %s" -- "%s %s" %s\n""" % (source,sourceRole,sourceMany,targetRole,targetMany,target)
        if self.withSkin:
            self.uml+=PlantUml.skinparams    
        return self.uml