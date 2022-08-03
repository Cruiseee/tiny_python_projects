#!/usr/bin/env python3
"""
Author : Tanneeru Deepak <dangerousdeepak25@gmail.com>
Date   : 03-08-2022
Purpose: Chapter-2 Solution
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Shout out to captain about incoming threat',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='threat',
                        help='Incoming threat to ship',
                        type=str)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Shout out about incoming threat to the ship"""

    args = get_args()
    str_arg = args.word

    str_arg = str_arg.lower()
    
    if str_arg[0] in 'aeiou':
        article = 'an'
    else:
        article = 'a'

    print(f'Ahoy, Captain, {article} {str_arg} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
