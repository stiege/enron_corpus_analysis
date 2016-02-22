import unittest
from .. import create
from .test_email_parsing import _fixture_dir
import sys
import logging
import time
from .speed_test_email_parsing import _one_time_unit
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
        create.create_db(
            file_dir=_fixture_dir,
            engine_config="sqlite:///test_db.db")

        finish = time.time()

        duration = finish - start
        slowness = duration / _one_time_unit

        if sys.version_info == (3, 5, 1, 'final', 0):
            expected = "~4"
        else:
            expected = "?"
        logging.info("create_db slowness: {:.02f} ({})".format(
            slowness, expected))
