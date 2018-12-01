#!/usr/local/bin/python3

import argparse

def quicksort(arr):
    arr.sort()
    return arr

def main():
    parser = argparse.ArgumentParser(description='Sort an array of numbers using quicksort.')
    parser.add_argument('numbers', metavar='Numbers', type=float, nargs='+',
                        help='The list of numbers to sort')

    args = parser.parse_args()
    print(quicksort(args.numbers))

if __name__ == '__main__':
    main()
