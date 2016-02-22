from ..db import create
import unittest
import textblob
import statistics


class SentimentAnalysis(unittest.TestCase):

    def test_can_get_mean(self):
        """
        Simple test to get the mean sentiment from all test fixtures
        """
        session = create.create_db(
            "core/_test_fixtures/maildir")
        emails = session.query(create._Email).all()
        blobs = map(textblob.TextBlob, map(lambda e: e.content, emails))
        sentiments = map(lambda b: b.sentiment.polarity, blobs)
        print(statistics.mean(sentiments))
