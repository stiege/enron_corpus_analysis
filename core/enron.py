import re


def _parse_email(file_loc):
    email = {}
    with open(file_loc) as f:
        email["Message-ID"] = f.readline().strip()
        email["Date"] = f.readline().strip()
        email["From"] = f.readline().strip()
        email["To"] = f.readline().strip()
        email["Subject"] = f.readline().strip()
        email["Mime-Version"] = f.readline().strip()
        email["Content-Type"] = f.readline().strip()
        email["Content-Transfer-Encoding"] = f.readline().strip()
        email["X-From"] = f.readline().strip()
        email["X-To"] = f.readline().strip()
        email["X-cc"] = f.readline().strip()
        email["X-bcc"] = f.readline().strip()
        email["X-Folder"] = f.readline().strip()
        email["X-Origin"] = f.readline().strip()
        email["X-FileName"] = f.readline().strip()

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
