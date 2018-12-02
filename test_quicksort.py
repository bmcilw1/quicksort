#!/usr/local/bin/python3

from hypothesis import given
from unittest.mock import MagicMock, Mock, patch
import hypothesis.strategies as st
import quicksort as q
import argparse

@given(arr=st.lists(st.floats(allow_nan=False, allow_infinity=False) | st.integers()))
def test_quicksort_sorts(arr):
    arr_sorted = q.quicksort(arr)
    assert all(arr_sorted[i] <= arr_sorted[i+1] for i in range(len(arr)-1))

@patch('quicksort.argparse')
def test_main_calls_quicksort(argparseMock):
    q.main()
    assert argparseMock.ArgumentParser.called_once_with(description='Sort an array of numbers using quicksort.')
