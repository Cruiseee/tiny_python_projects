#!/usr/bin/env python
"""
Author: Tanneeru Deepak <dangerousdeepak25@gmail.com>
Purpose: Say hello """

import argparse


def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Say hello")
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )
    return parser.parse_args()


# Print Hello, world! on system output with input argument
def main():
    """Says Hello with the -name as input argument"""
    args = get_args()
    print("Hello, " + args.name + "!")


if __name__ == "__main__":
    main()
