"""
The enron module is a helper module for working with the the email
dataset.
"""

import re

_known_email_metadata = [
    "Message-ID",
    "Date",
    "From",
    "To",
    "Subject",
    "Mime-Version",
    "Content-Type",
    "Content-Transfer-Encoding",
    "X-From",
    "X-To",
    "X-cc",
    "X-bcc",
    "X-Folder",
    "X-Origin",
    "X-FileName"]


def _assemble_email_from_dict(email):
    """
    This function takes the `dict` generated by
    :func:`_parse_email` and reassembles the email string.
    """
    msg = []
    for meta in _known_email_metadata:
        if email[meta] is not None:
            msg.append(
                meta + ":" + email[meta])
    msg.append(email["Content"])
    return "".join(msg)


def _parse_email(file_loc, allow_corrupt=False):
    """
    _parse_email takes a path to an email that is in the common format
    of the enron dataset and parses it into a `dict`.
    """

    email = {}
    with open(file_loc) as f:
        for meta in _known_email_metadata:
            line_read = f.readline().strip()
            if not line_read.startswith(meta) and not allow_corrupt:
                raise AssertionError("Corrupt parse")
            else:
                email[meta] = re.search(
                    meta + ":(.*)", line_read).group(1).strip()

        msg_content = f.readlines()
        email["Content"] = "".join(msg_content)
        email["Content"] = email["Content"].strip()

    return email
