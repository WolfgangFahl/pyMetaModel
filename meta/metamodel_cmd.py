'''
Created on 2023-02-19

@author: wf
'''
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
import sys
import traceback
import os
from meta.version import Version
from meta.mw import SMWAccess
from meta.uml import PlantUml
from meta.metamodel import Context

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

    def readContext(self,wikiId:str,context_name:str):
        """
        read the context with the given name from the given wiki
        
        Args:
            wikiId(str): the wikiId of the wiki to read the context from
            context_name: the name of the context to read
        """
        self.wikiId=wikiId
        self.smwAccess=SMWAccess(wikiId)
        self.mw_contexts=self.smwAccess.getMwContexts()
        self.mw_context=self.mw_contexts.get(context_name,None)
        self.context,self.error,self.errMsg=Context.fromWikiContext(self.mw_context, debug=self.debug)
        
    def genUml(self,args):
        """
        generate uml for the given context with the given name from the given wiki
        
        Args:
           args: the command line arguments
        """
        self.readContext(args.wikiId, args.context)  
        if self.error is not None:
            print(f"reading Context failed:\n{self.errMsg}\n{self.error}")
            return None
        else:
            uml=PlantUml(title=args.title,copyRight=args.copyright)
            uml.fromDIF(self.context.dif)
            return str(uml)

__version__ = Version.version
__date__ = Version.date
__updated__ = Version.updated 


def main(argv=None): # IGNORE:C0111
    '''main program.'''

    if argv is None:
        argv=sys.argv[1:]
    
    program_name = os.path.basename(__file__)
    program_shortdesc = Version.description
    
    program_version =f"v{__version__}" 
    program_build_date = str(__updated__)
    program_version_message = f'{program_name} ({program_version},{program_build_date})'

    user_name="Wolfgang Fahl"
    program_license = '''%s

  Created by %s on %s.
  Copyright 2022 Wolfgang Fahl. All rights reserved.

  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0

  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, user_name,str(__date__))
    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("--about",help="show about info [default: %(default)s]",action="store_true")
        parser.add_argument('--context', default="MetaModel",help='context to read [default: %(default)s]')
        parser.add_argument("--copyright",help="copyright message for diagrams")
        parser.add_argument("-d", "--debug", dest="debug", action="store_true", help="show debug info")
        parser.add_argument("-i", "--input", nargs="+", help="list of inputs")
        parser.add_argument('--wikiId', default="wiki",help='id of the wiki to generate for [default: %(default)s]')
        parser.add_argument("-u", "--uml", action="store_true", help="create plantuml diagram")
        parser.add_argument("-t", "--title",help="the title of a diagram")
        if len(argv) < 1:
            parser.print_usage()
            sys.exit(1)
            
        args = parser.parse_args(argv)
        if args.about:
            print(program_version_message)
            print(f"see {Version.doc_url}")
            webbrowser.open(Version.doc_url)
        if args.uml:
            mm_cmd=MetaModelCmd(debug=args.debug)
            uml=mm_cmd.genUml(args)
            print(uml)
    
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
    
