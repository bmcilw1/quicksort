#!/usr/local/bin/python3

import argparse

def quicksort(arr):
    arr.sort()
    return arr

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sort an array of integers using quicksort.')
    parser.add_argument('integers', metavar='Numbers', type=int, nargs='+',
                        help='The list of integers to sort')

    args = parser.parse_args()
    print(quicksort(args.integers))
