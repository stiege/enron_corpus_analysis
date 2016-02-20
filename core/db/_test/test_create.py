import unittest
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
from .test_email_parsing import (_fixture_dir, _expected_parse_count)
from .. import create

Base = declarative_base()


class _Email(Base):
    __tablename__ = 'emails'
    _id = Column(Integer, Sequence('email_id_seq'), primary_key=True)
    msg_id = Column(String)
    date = Column(String)
    frm = Column(String)
    to = Column(String)
    subject = Column(String)
    mime_version = Column(String)
    content_type = Column(String)
    content_transfer_encoding = Column(String)
    x_from = Column(String)
    x_to = Column(String)
    x_cc = Column(String)
    x_bcc = Column(String)
    x_folder = Column(String)
    x_origin = Column(String)
    x_filename = Column(String)
    content = Column(String)

    def __repr__(self):
        return "<Email {}: From: {} To: {} Content: {}>".format(
            self._id, self.frm, self.to, self.content)


class DataBaseTesting(unittest.TestCase):
    """Prototyping with sqlalchemy"""

    def setUp(self):
        engine = sqlalchemy.create_engine(
            'sqlite:///:memory:')
        Base.metadata.create_all(engine)
        Session = sessionmaker()
        Session.configure(bind=engine)
        self.session = Session()

    def tearDown(self):
        self.session.rollback()

    def test_database_create(self):
        """
        Check the object we put into the database is the same one we get
        back
        """
        a = _Email(content="Hello")
        self.session.add(a)
        b = self.session.query(
            _Email).filter_by(content='Hello').first()
        self.assertIs(a, b)

    def test_commit_to_db(self):
        a = self.session.add(_Email(content="Committed email"))
        self.session.commit()
        b = self.session.query(
            _Email).filter_by(content='Hello').first()
        self.assertIs(a, b)
        self.session.rollback()
        b = self.session.query(
            _Email).filter_by(content='Hello').first()
        self.assertIsNone(b)


class ModuleTests(unittest.TestCase):
    """
    Tests pertaining to the database creation by db.py
    """

    def test_create_sql_db_in_memory(self):
        create._create_db(
            file_dir=_fixture_dir + "maildir",
            engine_config="sqlite:///:memory:")
        self.assertEqual(
            _expected_parse_count,
            create._session.query(create._Email).count())
