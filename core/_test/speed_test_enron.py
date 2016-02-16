import unittest
import time
from .. import enron
from .test_enron import _get_test_fixture_list
import logging
import sys

logging.basicConfig(level=logging.INFO)


class EnronSpeedTests(unittest.TestCase):

    def test_time_optimisation(self):
        one_time_unit = 0
        duration = 0
        start = time.time()
        for fixture_location in _get_test_fixture_list():
            with open(fixture_location) as f:
                f.readlines()
        finish = time.time()
        one_time_unit = one_time_unit + finish - start
        start = time.time()
        for fixture_location in _get_test_fixture_list():
            try:
                enron._parse_email(fixture_location)
            except:
                pass
        finish = time.time()
        duration = duration + finish - start
        slowness = duration / one_time_unit

        if sys.version_info == (3, 5, 1, 'final', 0):
            expected = "~1.5"
        else:
            expected = "?"
        logging.info("_parse_email slowness: {:.02f} ({})".format(
            slowness, expected))
