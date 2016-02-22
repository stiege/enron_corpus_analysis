import argparse
import sys
import traceback
from .db import create

_POSIX_SUCCESS = 0
_POSIX_FAIL = -1


def main(args):
    retval = _POSIX_SUCCESS
    try:
        if args.create:
            create.create_db(args.create, args.database)
    except:
        traceback.print_exc()
        retval = _POSIX_FAIL
    return retval

if __name__ == '__main__':
    a = argparse.ArgumentParser()
    a.add_argument(
        "--create", "-c",
        help="Create a database.db file from the directory specified")
    a.add_argument(
        "--database", "-d",
        help="Select the type of database to create",
        default="sqlite:///database.db")
    args = a.parse_args()
    sys.exit(
        main(args))
