#!/usr/bin/env python3
"""
Author : Tanneeru Deepak <dangerousdeepak25@gmail.com>
Date   : today
Purpose: Chapter-4 Solution
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Jump the five algorithm",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("ctext", metavar="str", help="cryptic text")

    parser.add_argument(
        "-a",
        "--arg",
        help="A named string argument",
        metavar="str",
        type=str,
        default="",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.ctext

    num_jump = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }

    decode_text = ""

    for char in str_arg:
        if char.isnumeric():
            new_char = num_jump[char]
            decode_text += new_char
        else:
            decode_text += char

    print(f"{decode_text}")


# --------------------------------------------------
if __name__ == "__main__":
    main()
