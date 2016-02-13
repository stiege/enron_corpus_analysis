import unittest
import re
from .. import enron
import glob2

# "find . -type f | wc -l" indicates 2195 is the right number
_test_fixture_count = 2195
# If this changes be sure to update the readme.md for marketing purposes
_expected_yield = 56

_whitespace_regex = "[\r\n\t ]"
_fixture_dir = "core/_test_fixtures/maildir/"
_simple_email_location = (
    _fixture_dir + "stokley-c/chris_stokley/mid_markt/19.")
_simple_email_content = re.sub(
    _whitespace_regex,
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
            re.sub(_whitespace_regex, "", email["Content"]))

    def _get_test_fixture_list(self):
        return glob2.glob(_fixture_dir + "/**/*.")

    def test_can_get_paths_to_all_test_fixtures(self):
        # This tests our private function _get_test_fixture_list to make
        # sure we've got the right regex etc and the result is what we expect.
        fixture_list = self._get_test_fixture_list()
        self.assertEqual(
            _test_fixture_count,
            len(fixture_list))

    def test_yield_on_test_fixtures(self):
        no_loss_of_data_count = 0
        content = None
        for fixture_location in self._get_test_fixture_list():
            with open(fixture_location) as f:
                content = "".join(f.readlines())
            try:
                email = enron._parse_email(fixture_location)
                msg = enron._assemble_email_from_dict(email)
                if (re.sub(_whitespace_regex, "", content) ==
                        re.sub(_whitespace_regex, "", msg)):
                    no_loss_of_data_count = no_loss_of_data_count + 1
            except TypeError:
                pass
        parse_yield = float(no_loss_of_data_count)/_test_fixture_count * 100

        self.assertEqual(_expected_yield, int(parse_yield))
