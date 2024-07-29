"""
Created on 2024-07-29

@author: wf
"""

import os
import tempfile
from pathlib import Path
from tests.basetest import Basetest
from meta.metamodel_cmd import MetaModelCmd
import subprocess

class TestGenerators(Basetest):
    """
    test generators
    """

    def setUp(self, debug=True, profile=True):
        Basetest.setUp(self, debug=debug, profile=profile)
        self.temp_dir = tempfile.TemporaryDirectory()
        self.examples_dir = Path(__file__).parent.parent / "examples"
        self.mm_cmd = MetaModelCmd()
        self.sidif_files = list(self.examples_dir.glob("**/*.sidif"))

    def tearDown(self):
        self.temp_dir.cleanup()
        super().tearDown()

    def generate_yaml(self, sidif_file):
        """Generate YAML from SIDIF file"""
        args = ["-i", str(sidif_file), "-l"]
        yaml = self.mm_cmd.genLinkML(self.mm_cmd.getArgParser().parse_args(args))
        yaml_file = self.temp_dir.name / sidif_file.with_suffix('.yaml').name
        with open(yaml_file, 'w') as f:
            f.write(yaml)
        return yaml_file

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

    def test_plantuml_generation(self):
        """
        test plant uml generation
        """
        for sidif_file in self.sidif_files:
            uml=self.generate_plantuml(sidif_file, withAt=False)
            uml_with_at = self.generate_plantuml(sidif_file, withAt=True)
            self.assertTrue(str(uml_with_at).startswith("@startuml"))
            self.assertTrue(str(uml_with_at).endswith("@enduml"))

    def xtest_linkml_generation(self):
        for sidif_file in self.sidif_files:
            yaml_file = self.generate_yaml(sidif_file)
            self.assertTrue(os.path.exists(yaml_file))
            with open(yaml_file, 'r') as f:
                yaml_content = f.read()
            self.assertTrue(len(yaml_content) > 0)

    def xtest_mermaid_generation(self):
        for sidif_file in self.sidif_files:
            yaml_file = self.generate_yaml(sidif_file)
            mermaid_output = self.run_command('gen-erdiagram', str(yaml_file))
            self.assertTrue(len(mermaid_output) > 0)

    def xtest_python_generation(self):
        for sidif_file in self.sidif_files:
            yaml_file = self.generate_yaml(sidif_file)
            python_output = self.run_command('gen-python', str(yaml_file))
            self.assertTrue(len(python_output) > 0)

    def xtest_excel_generation(self):
        for sidif_file in self.sidif_files:
            yaml_file = self.generate_yaml(sidif_file)
            excel_file = self.temp_dir.name / sidif_file.with_suffix('.xlsx').name
            self.run_command('gen-excel', str(yaml_file), '--output', str(excel_file))
            self.assertTrue(os.path.exists(excel_file))