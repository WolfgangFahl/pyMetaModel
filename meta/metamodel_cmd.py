'''
Created on 2023-02-19

@author: wf
'''
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
import os
import sys
import traceback
from meta.version import Version
from meta.mw import SMWAccess
from meta.uml import PlantUml
from meta.sidif2linkml import SiDIF2LinkML
from meta.metamodel import Context
import urllib3
import webbrowser

class MetaModelCmd:
    """
    command line interface for metamodel handling
    """    
    
    def __init__(self,debug:bool=False):
        """
        constructor
        
        Args:
            debug(bool): if True switch debugging on
        """
        self.debug=debug
        self.error=None
        self.errMsg=None
        self.context=None
        
    @classmethod
    def getArgParser(cls):
        """
        get my argument parser
        """
        program_shortdesc = Version.description        
        program_license = '''%s
        
          Created by %s on %s.
          Copyright 2022 Wolfgang Fahl. All rights reserved.
        
          Licensed under the Apache License 2.0
          http://www.apache.org/licenses/LICENSE-2.0
        
          Distributed on an "AS IS" basis without warranties
          or conditions of any kind, either express or implied.
        
        USAGE
        ''' % (program_shortdesc, Version.authors,str(__date__))
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("--about",help="show about info [default: %(default)s]",action="store_true")
        parser.add_argument('--context', default="MetaModel",help='context to read [default: %(default)s]')
        parser.add_argument("--copyright",help="copyright message for diagrams")
        parser.add_argument("-d", "--debug", dest="debug", action="store_true", help="show debug info")
        parser.add_argument("-i", "--input", help="input file")
        parser.add_argument("-l", "--linkml", action="store_true", help="create linkml yaml file")
        parser.add_argument("-t", "--title",help="the title of a diagram")
        parser.add_argument("-u", "--uml", action="store_true", help="create plantuml diagram")
        parser.add_argument('--wikiId', default="wiki",help='id of the wiki to generate for [default: %(default)s]')
        return parser

    def readContext(self,args):
        """
        read the context from the given args
        
        Args:
            args(Args): command line arguments
        """
        if args.input:
            if args.input.startswith("http:"):
                url=args.input
                http = urllib3.PoolManager()
                response = http.request('GET', url)
                sidif = response.data.decode('utf-8')
            else:
                sidif_path=args.input
                with open(sidif_path, 'r') as sidif_file:
                    sidif=sidif_file.read()
            self.context,self.error,self.errMsg=Context.fromSiDIF(sidif, title=args.input, debug=self.debug)
            pass
        elif args.wikiId and args.context:
            self.wikiId=args.wikiId
            self.smwAccess=SMWAccess(args.wikiId)
            self.mw_contexts=self.smwAccess.getMwContexts()
            self.mw_context=self.mw_contexts.get(args.context,None)
            self.context,self.error,self.errMsg=Context.fromWikiContext(self.mw_context, debug=self.debug)
         
    def hasError(self):  
        if self.error is not None:
            print(f"reading Context failed:\n{self.errMsg}\n{self.error}")
        return self.error
         
    def genUml(self,args)->str:
        """
        generate uml for the given context with the given name from the given wiki
        
        Args:
           args: the command line arguments
           
        Returns:
            str: the uml markup
        """
        self.readContext(args)  
        if not self.hasError():
            uml=PlantUml(title=args.title,copyRight=args.copyright)
            uml.fromDIF(self.context.dif)
            return str(uml)
        
    def genLinkML(self,args)->str:
        """
        generate linkML yaml for the given command line arguments
        
        Args:
           args: the command line arguments
           
        Returns:
            str: the uml markup
        """
        self.readContext(args)  
        if not self.hasError():
            sidif2LinkML=SiDIF2LinkML(self.context)
            yaml_text=sidif2LinkML.asYaml()
            return yaml_text

__version__ = Version.version
__date__ = Version.date
__updated__ = Version.updated 


def main(argv=None): # IGNORE:C0111
    '''main program.'''

    if argv is None:
        argv=sys.argv[1:]
    
    program_name = os.path.basename(__file__)
    program_version =f"v{__version__}" 
    program_build_date = str(__updated__)
    program_version_message = f'{program_name} ({program_version},{program_build_date})'
   
    try:
        parser=MetaModelCmd.getArgParser()
        # Setup argument parser
        if len(argv) < 1:
            parser.print_usage()
            sys.exit(1)
            
        args = parser.parse_args(argv)
        mm_cmd=MetaModelCmd(debug=args.debug)
        if args.about:
            print(program_version_message)
            print(f"see {Version.doc_url}")
            webbrowser.open(Version.doc_url)
        if args.uml:
          
            uml=mm_cmd.genUml(args)
            print(uml)
        elif args.linkml:
            mm_cmd=MetaModelCmd(debug=args.debug)
            linkml_yaml=mm_cmd.genLinkML(args)
            print (linkml_yaml)
            
    
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 1
    except Exception as e:
        if DEBUG:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        if args.debug:
            print(traceback.format_exc())
        return 2       

DEBUG = 1
if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-d")
    sys.exit(main())
    
