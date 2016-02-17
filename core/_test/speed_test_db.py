import unittest
from .. import db
from .test_enron import _fixture_dir
import sys
import logging
import time
from .speed_test_enron import _one_time_unit
import os

logging.basicConfig(level=logging.INFO)


class DbSpeedTests(unittest.TestCase):
    """
    Tests pertaining to the database creation by db.py
    """

    def tearDown(self):
        try:
            os.remove("test_db.db")
        except FileNotFoundError:
            pass

    def test_create_sql_db(self):
        start = time.time()
        db._create_db(
            file_dir=_fixture_dir,
            engine_config="sqlite:///test_db.db")

        finish = time.time()

        duration = finish - start
        slowness = duration / _one_time_unit

        if sys.version_info == (3, 5, 1, 'final', 0):
            expected = "~7"
        else:
            expected = "?"
        logging.info("_create_db slowness: {:.02f} ({})".format(
            slowness, expected))
