#!/usr/bin/env python3
"""
Author : Tanneeru Deepak <dangerousdeepak25@gmail.com>
Date   : today
Purpose: Chapter- Solution
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Arguments extraction',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    
    print(f'str_arg = "{str_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
