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
        msg.append(
            meta + ":" + email[meta])
    msg.append(email["Content"])
    return "".join(msg)


def _parse_email(file_loc):
    email = {}
    with open(file_loc) as f:
        for meta in _known_email_metadata:
            email[meta] = f.readline().strip()

        for key in email:
            if not email[key].startswith(key):
                email[key] = None
            else:
                email[key] = re.search(
                    key + ":(.*)", email[key]).group(1).strip()

        email["Content"] = "".join(f.readlines())
        email["Content"] = email["Content"].strip()

    return email


def main():
    pass

if __name__ == '__main__':
    main()
