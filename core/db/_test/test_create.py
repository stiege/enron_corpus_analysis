import unittest
from .test_email_parsing import (_fixture_dir, _expected_parse_count)
from .. import create
import datetime


class ModuleTests(unittest.TestCase):
    """
    Tests pertaining to the database creation by db.py
    """

    def setUp(self):
        create.create_db(
            file_dir=_fixture_dir + "maildir",
            engine_config="sqlite:///:memory:")
        self._session = create._session
        self._table = create._Email
        self._test_email = self._session.query(self._table).filter_by(
                msg_id="<28674844.1075858514812.JavaMail.evans@thyme>").first()

    def test_create_sql_db_in_memory(self):

        self.assertEqual(
            _expected_parse_count,
            self._session.query(self._table).count())

    def test_date_parsing(self):
        # "Mon, 7 May 2001 08:51:02 -0700 (PDT)"
        self.assertEqual(
            datetime.datetime(
                year=2001,
                month=5,
                day=7,
                hour=16,
                minute=44,
                second=2),
            self._test_email.date)
