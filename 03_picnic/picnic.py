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
        description='List out the items bought for picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',
                        help='List of item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sorts items',
                        action='store_true')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items_list = args.item

    if args.sorted:
        items_list.sort()

    if len(items_list) == 1:
        print(f'You are bringing {items_list[0]}.')
    elif len(items_list) == 2:
        print(f'You are bringing {items_list[0]} and {items_list[1]}.')
    else:
        print(f'You are bringing {", ".join(items_list[:-1])}, and {items_list[-1]}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
