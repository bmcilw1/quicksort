#!/usr/local/bin/python3

import argparse

def quicksort(arr):
    arr.sort()
    return arr

def main():
    parser = argparse.ArgumentParser(description='Sort an array of integers using quicksort.')
    parser.add_argument('integers', metavar='Numbers', type=float, nargs='+',
                        help='The list of integers to sort')

    args = parser.parse_args()
    print(quicksort(args.integers))

if __name__ == '__main__':
    main()
