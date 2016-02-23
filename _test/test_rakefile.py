import unittest
import subprocess


class RakeFileTests(unittest.TestCase):

    def test_doc_creation(self):
        output = subprocess.check_output(
            ["rake", "doc:make[clean html]"],
            stderr=subprocess.STDOUT)
        self.assertIn(
            "build succeeded.",
            str(output))

    def test_db_creation(self):
        output = subprocess.check_output(
            ["rake", "db:create[core/_test_fixtures, sqlite:///:memory:]"],
            stderr=subprocess.STDOUT)
        self.assertIn(
            "database created from core/_test_fixtures",
            str(output))
