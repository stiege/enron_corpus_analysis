"""
Enron testing module
"""

import unittest
import re
import glob2
import doctest
from .. import enron

# "find . -type f | wc -l" indicates 2195 is the right number
_test_fixture_count = 2195
_expected_yield = 100  # Percent
_expected_parse_count = 2195

_whitespace_regex = "[\s]"
_fixture_dir = "core/_test_fixtures/"
_mail_fixture_dir = _fixture_dir + "maildir/"
_simple_email_location = (
    _mail_fixture_dir + "stokley-c/chris_stokley/mid_markt/19.")
_simple_email_content = re.sub(
    _whitespace_regex, "",
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

_multi_to_email_location = (
    _mail_fixture_dir + "motley-m/inbox/75.")
_multi_to_recipients = re.sub(
    _whitespace_regex, "",
    """
    tom.alonso@enron.com, robert.anderson@enron.com, robert.badeer@enron.com,
    serena.bishop@enron.com, jody.blackburn@enron.com,
    james.bruce@enron.com, jim.buerkle@enron.com,
    darren.cavanaugh@enron.com, paul.choi@enron.com, ed.clark@enron.com,
    timothy.coffing@enron.com, m..driscoll@enron.com,
    mo.elafandi@enron.com, caroline.emmert@enron.com,
    fredrik.eriksson@enron.com, kenton.erwin@enron.com,
    michael.etringer@enron.com, mark.fischer@enron.com,
    jim.gilbert@enron.com, stan.gray@enron.com, mark.guzman@enron.com,
    don.hammond@enron.com, e..jones@enron.com, paul.kaufman@enron.com,
    julie.kearney@enron.com, wayne.mays@enron.com, matt.motley@enron.com,
    p..o'neil@enron.com, jonalan.page@enron.com, todd.perry@enron.com,
    john.postlethwaite@enron.com, mike.purcell@enron.com,
    susan.rance@enron.com, dale.rasmussen@enron.com,
    lester.rawson@enron.com, grace.rodriguez@enron.com,
    stewart.rosman@enron.com, julie.sarnowski@enron.com,
    gordon.savage@enron.com, kathryn.sheppard@enron.com,
    g..slaughter@enron.com, virginia.thompson@enron.com,
    bill.williams@enron.com""")
_bcc_email_location = _multi_to_email_location
_bcc_content = "amy.fitzpatrick@enron.com"

_non_utf8_location = _fixture_dir + "non_utf8"

def _get_test_fixture_list():
    """
    Return a list of paths to all test fixtures
    """
    return glob2.glob(_mail_fixture_dir + "/**/*.")


class EmailParsing(unittest.TestCase):
    """
    EmailParsing contains all tests related to email parsing correctness
    """

    def test_documentation(self):
        """
        Test all documented methods
        """
        doctest.testmod(enron)

    def test_can_parse_email(self):
        """
        Show how a specific email is parsed successfully
        """
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
            re.sub(_whitespace_regex, "", email["Content"]))

    def _get_test_fixture_list(self):
        """
        Return a list of paths to all test fixtures
        """
        return glob2.glob(_mail_fixture_dir + "/**/*.")

    def test_can_get_paths_to_all_test_fixtures(self):
        """
        Check :func:`_get_test_fixture_list` result is as expected
        """
        # This tests our private function _get_test_fixture_list to make
        # sure we've got the right regex etc and the result is what we expect.
        fixture_list = _get_test_fixture_list()
        self.assertEqual(
            _test_fixture_count,
            len(fixture_list))

    def test_yield_on_test_fixtures(self):
        """
        Check that no code changes result in lower correct parsing yield
        """
        no_loss_of_data_count = 0
        content = None

        for fixture_location in _get_test_fixture_list():
            with open(fixture_location) as f:
                content = "".join(f.readlines())

            try:
                email = enron._parse_email(fixture_location)
            except AssertionError as e:
                meta = re.search("Corrupt parse on (.*)", str(e)).group(1)
                self.fail("Bad parse of {} at {}".format(
                    meta, fixture_location))
            msg = enron._assemble_email_from_dict(email)
            if (re.sub(_whitespace_regex, "", content) ==
                    re.sub(_whitespace_regex, "", msg)):
                no_loss_of_data_count = no_loss_of_data_count + 1
            else:
                self.fail("Returned corrupt message at {}".format(
                    fixture_location))

        parse_yield = float(no_loss_of_data_count) / _test_fixture_count * 100

        self.assertEqual(_expected_yield, int(parse_yield))
        self.assertEqual(_expected_parse_count, no_loss_of_data_count)

    def test_parse_multiple_recipients(self):
        """
        Check parsing of an email with multiple recipients
        """
        email = enron._parse_email(_multi_to_email_location)
        self.assertEqual(
            _multi_to_recipients,
            re.sub(_whitespace_regex, "", email["To"]))

    def test_bcc(self):
        """
        Check parsing of an email with a bcc
        """
        email = enron._parse_email(_bcc_email_location)
        self.assertEqual(
            _bcc_content,
            re.sub(_whitespace_regex, "", email["Bcc"]))

    def test_non_utf8(self):
        """
        Check parsing of an email with a non-utf8 encoding
        """
        email = enron._parse_email(_non_utf8_location)
        self.assertEqual(
            "Shapiro-R",
            re.sub(_whitespace_regex, "", email["X-Origin"]))
