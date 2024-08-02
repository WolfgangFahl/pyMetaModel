"""
Created on 2024-07-29

@author: wf
"""

import tempfile
from pathlib import Path
from tests.basetest import Basetest
from meta.metamodel_cmd import MetaModelCmd
import subprocess

class TestGenerators(Basetest):
    """
    test generators
    """

    def setUp(self, debug=False, profile=True):
        Basetest.setUp(self, debug=debug, profile=profile)
        self.temp_dir = tempfile.TemporaryDirectory()
        self.examples_dir = Path(__file__).parent.parent / "examples"
        self.mm_cmd = MetaModelCmd()
        self.sidif_files = list(self.examples_dir.glob("**/*.sidif"))

    def tearDown(self):
        self.temp_dir.cleanup()
        super().tearDown()


    def generate_plantuml(self,sidif_file,withAt:bool=False):
        args = ["-i", str(sidif_file), "-u"]
        if self.debug:
            args.append("-d")
        if withAt:
            args.append("--withAt")
        uml = self.mm_cmd.genUml(self.mm_cmd.getArgParser().parse_args(args))
        self.assertIsNotNone(uml)
        self.assertTrue(len(uml.uml) > 0)
        if self.debug:
            print(uml)
            pass
        return uml


    def run_command(self, command, *args):
        """Run a command and return its output"""
        result = subprocess.run([command, *args], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        return result.stdout

    def generate_yaml(self,sidif_file)->str:
        """Generate YAML from SIDIF file"""
        args = ["-i", str(sidif_file), "-l"]
        yaml = self.mm_cmd.genLinkML(self.mm_cmd.getArgParser().parse_args(args))
        return yaml

    def test_plantuml_generation(self):
        """
        test plant uml generation
        """
        for sidif_file in self.sidif_files:
            uml=self.generate_plantuml(sidif_file, withAt=False)
            uml_with_at = self.generate_plantuml(sidif_file, withAt=True)
            self.assertTrue(str(uml_with_at).startswith("@startuml"))
            self.assertTrue(str(uml_with_at).endswith("@enduml"))

    def test_linkml_generation(self):
        for sidif_file in self.sidif_files:
            yaml=self.generate_yaml(sidif_file)
            if self.debug:
                print(yaml)
        self.assertTrue(len(yaml) > 0)
