from __future__ import print_function
import sqlalchemy
import glob2
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
import sys
from core import enron

_session = None
_Base = declarative_base()


class _Email(_Base):
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


def _create_db(file_dir, engine_config="sqlite:///:memory:"):
    """
    Recursively take all emails from a directory and insert them into a
    database
    """
    global _session
    engine = sqlalchemy.create_engine(
        engine_config)

    _Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    _session = Session()

    for email_loc in glob2.glob(file_dir + "/**/*."):
        try:
            email = enron._parse_email(email_loc)
            _session.add(
                _Email(
                    msg_id=email["Message-ID"],
                    date=email["Date"],
                    frm=email["From"],
                    to=email["To"],
                    subject=email["Subject"],
                    mime_version=email["Mime-Version"],
                    content_type=email["Content-Type"],
                    content_transfer_encoding=email[
                        "Content-Transfer-Encoding"],
                    x_from=email["X-From"],
                    x_to=email["X-To"],
                    x_cc=email["X-cc"],
                    x_bcc=email["X-bcc"],
                    x_folder=email["X-Folder"],
                    x_origin=email["X-Origin"],
                    x_filename=email["X-FileName"],
                    content=email["Content"]
                    ))
        except AssertionError:
            continue
        except:
            print("Failed on {}".format(email_loc), file=sys.stderr)
            raise
    _session.commit()

if __name__ == '__main__':
    _create_db(sys.argv[1], sys.argv[2])
