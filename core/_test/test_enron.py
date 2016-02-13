import unittest
import re
from .. import enron

_simple_email_location = (
    "core/_test_fixtures/maildir/stokley-c/chris_stokley/mid_markt/19.")
_simple_email_content = re.sub(
    "[\r\n\t ]",
    "",
    """
    Chris:
    I didn't exactly ask for confirmation.
    Can you let me know if the payment is set to be made?
    C
     -----Original Message-----
    From:   Foster, Chris H.
    Sent:   Thursday, May 03, 2001 4:55 PM
    To: Ratnala, Melissa; Stokley, Chris
    Cc: Hyde, Godfrey
    Subject:
    Melissa:
    I just correct a mistake in one of the dela entries for Harbor.
    The attached spreadsheet reflects the correct amount.
    The total payment to Harbor should be $2,770,821.77.
    When you are set to make the payment, please forward an e-mail to
    Harbor (or me).
    Thanks
    Chris
    """)

_multiple_recipient_email_location = (
    "")


class EmailParsing(unittest.TestCase):

    def test_can_parse_email(self):
        email = enron._parse_email(_simple_email_location)
        self.assertEqual(
            "<28674844.1075858514812.JavaMail.evans@thyme>",
            email["Message-ID"])
        self.assertEqual(
            "Mon, 7 May 2001 08:51:02 -0700 (PDT)",
            email["Date"])
        self.assertEqual(
            "h..foster@enron.com",
            email["From"])
        self.assertEqual(
            "chris.stokley@enron.com",
            email["To"])
        self.assertEqual(
            "FW:",
            email["Subject"])
        self.assertEqual(
            "1.0",
            email["Mime-Version"])
        self.assertEqual(
            "text/plain; charset=us-ascii",
            email["Content-Type"])
        self.assertEqual(
            "7bit",
            email["Content-Transfer-Encoding"])
        self.assertEqual(
            "Foster, Chris H. </O=ENRON/OU=NA/CN=RECIPIENTS/CN=CFOSTER>",
            email["X-From"])
        self.assertEqual(
            "Stokley, Chris </O=ENRON/OU=NA/CN=RECIPIENTS/CN=Mstokle>",
            email["X-To"])
        self.assertEqual(
            "",
            email["X-cc"])
        self.assertEqual(
            "",
            email["X-bcc"])
        self.assertEqual(
            "\Stokley, Chris (Non-Privileged)\Chris Stokley\Mid Markt",
            email["X-Folder"])
        self.assertEqual(
            "Stokley-C",
            email["X-Origin"])
        self.assertEqual(
            "Stokley, Chris (Non-Privileged).pst",
            email["X-FileName"])
        self.assertEqual(
            _simple_email_content,
            re.sub("[\r\n\t ]", "", email["Content"]))

    def test_can_parse_with_multiple_recipients(self):
        pass