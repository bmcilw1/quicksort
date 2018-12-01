#!/usr/local/bin/python3

from hypothesis import given
import hypothesis.strategies as st
import quicksort as q

@given(arr=st.lists(st.floats(allow_nan=False, allow_infinity=False) | st.integers()))
def test_quicksort_sorts(arr):
    arr_sorted = q.quicksort(arr)
    assert all(arr_sorted[i] <= arr_sorted[i+1] for i in range(len(arr)-1))
