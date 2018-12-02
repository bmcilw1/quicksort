#!/usr/local/bin/python3

import argparse

def partition(arr, low, high):
    pivot = int((low + high) / 2)

    while (low < high):
        if arr[low] < arr[pivot]:
            low += 1
        elif arr[high] > arr[pivot]:
            high -= 1
        else:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1
    
    arr[pivot], arr[low] = arr[low], arr[pivot]

    return pivot

def quicksort(arr, low, high):
    if (low >= high):
        return
    
    pivot = partition(arr, low, high)
    quicksort(arr, low, pivot)
    quicksort(arr, pivot+1, high)
    return

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
