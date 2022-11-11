#!C:\Python311\python3.exe
"""
Author : Tanneeru Deepak <dangerousdeepak25@gmail.com>
Date   : today
Purpose: Chapter-5 Solution
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Howler - Upper case conversion",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "infile",
        help="Input howler text or file name contains hower text",
        metavar="text",
        type=str,
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Out filename",
        metavar="str",
        type=str,
        default=None,
    )

    return parser.parse_args()


def check_out(out_arg, howlers):

    if out_arg is None:
        print(howlers.upper())
    else:
        with open(out_arg, "w") as o:
            o.write(howlers.upper() + "\n")


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    infile = args.infile
    outfile = args.outfile

    if os.path.isfile(infile):
        with open(infile, "r") as g:
            howlers = g.read()
        check_out(outfile, howlers=howlers)
    else:
        check_out(outfile, howlers=infile)


# --------------------------------------------------
if __name__ == "__main__":
    main()
