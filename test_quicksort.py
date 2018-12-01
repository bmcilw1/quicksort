#!/usr/local/bin/python3

from hypothesis import given
import hypothesis.strategies as st
import quicksort as q

@given(st.lists(st.integers()))
def test_quicksort_sorts(arr):
    sorted = q.quicksort(arr)
    assert all(sorted[i] <= sorted[i+1] for i in range(len(arr)-1))
