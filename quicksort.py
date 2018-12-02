#!/usr/local/bin/python3

import argparse

def partition(arr, low, high):
    pivot = int((low + high) / 2)

    arr[pivot], arr[high] = arr[high], arr[pivot]
    pivot = high
    high -= 1

    while (low <= high):
        if arr[low] <= arr[pivot]:
            low += 1
        elif arr[high] > arr[pivot]:
            high -= 1
        else:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            
    arr[pivot], arr[low] = arr[low], arr[pivot]
    return low

def quicksort(arr, low, high):
    if (low < high):
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)

def sort(arr):
    quicksort(arr, 0, len(arr)-1)
    return arr

def main():
    parser = argparse.ArgumentParser(description='Sort an array of numbers using quicksort.')
    parser.add_argument('numbers', metavar='Numbers', type=float, nargs='+',
                        help='The list of numbers to sort')

    args = parser.parse_args()
    print(sort(args.numbers))

if __name__ == '__main__':
    main()
