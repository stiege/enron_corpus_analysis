import unittest
import time
from .. import _email_parsing
from .test_email_parsing import _get_test_fixture_list
import logging
import sys

logging.basicConfig(level=logging.INFO)

_start = time.time()
for fixture_location in _get_test_fixture_list():
    with open(fixture_location) as f:
        f.readlines()
_finish = time.time()
_one_time_unit = _finish - _start


class EnronSpeedTests(unittest.TestCase):

    def test_time_optimisation(self):
        start = time.time()
        for fixture_location in _get_test_fixture_list():
            _email_parsing._parse_email(fixture_location)

        finish = time.time()
        duration = finish - start
        slowness = duration / _one_time_unit

        if sys.version_info == (3, 5, 1, 'final', 0):
            expected = "~1.5"
        else:
            expected = "?"
        logging.info("_parse_email slowness: {:.02f} ({})".format(
            slowness, expected))
