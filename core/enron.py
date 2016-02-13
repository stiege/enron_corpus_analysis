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
    msg = []
    for meta in _known_email_metadata:
        if email[meta] is not None:
            msg.append(
                meta + ":" + email[meta])
    msg.append(email["Content"])
    return "".join(msg)


def _parse_email(file_loc, allow_corrupt=False):
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


def main():
    pass

if __name__ == '__main__':
    main()
