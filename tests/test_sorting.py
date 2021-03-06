# -*- coding: utf-8 -*-

import pytest

from .fixtures import parametrize

from pyalgos import insertion, selection, merge


@parametrize('data,expected', [
    # Case 1
    ([5, 4, 6, 1, 7], [1, 4, 5, 6, 7]),

    # Case 2
    ([14, -1, 3, -6, 19, -100], [-100, -6, -1, 3, 14, 19]),

    # Case 3
    ([1.014, 1.12, 1.011, 1.56, 1.009, 2],
     [1.009, 1.011, 1.014, 1.12, 1.56, 2]),

    # Case 4
    (['z', 'c', 'y', 'a'], ['a', 'c', 'y', 'z']),

    # Case 5
    ((14, -1, 3, -6, 19, -100), (-100, -6, -1, 3, 14, 19)),

    # Case 6
    (('z', 'c', 'y', 'a'), ('a', 'c', 'y', 'z')),

    # Case 7
    ([1], [1])
])
def test_insertion_sort(data, expected):
    """Validates the insertion sort on the given list of values."""
    assert insertion(data) == expected


@parametrize('data,exception,error_msg', [
    ({'a': 1}, ValueError, 'A list/tuple of values should be given'),
    ([1, 2, 3, 'hello'],
     ValueError,
     "int() and str() type can't be specified at the same time")
])
def test_insertion_sort_error(data, exception, error_msg):
    """Validates the error based on the given values."""
    with pytest.raises(exception) as exc:
        insertion(data)

    assert error_msg in str(exc)


@parametrize('data,expected', [
    # Case 1
    ([5, 4, 6, 1, 7], [1, 4, 5, 6, 7]),

    # Case 2
    ([14, -1, 3, -6, 19, -100], [-100, -6, -1, 3, 14, 19]),

    # Case 3
    ([1.014, 1.12, 1.011, 1.56, 1.009, 2],
     [1.009, 1.011, 1.014, 1.12, 1.56, 2]),

    # Case 4
    (['z', 'c', 'y', 'a'], ['a', 'c', 'y', 'z']),

    # Case 5
    ((14, -1, 3, -6, 19, -100), (-100, -6, -1, 3, 14, 19)),

    # Case 6
    (('z', 'c', 'y', 'a'), ('a', 'c', 'y', 'z')),

    # Case 7
    ([1], [1])
])
def test_selection_sort(data, expected):
    """Validates the selection sort on the given list of values."""
    assert selection(data) == expected


@parametrize('data,exception,error_msg', [
    ({'a': 1}, ValueError, 'A list/tuple of values should be given'),
    ([1, 2, 3, 'hello'],
     ValueError,
     "int() and str() type can't be specified at the same time")
])
def test_selection_sort_error(data, exception, error_msg):
    """Validates the error based on the given values."""
    with pytest.raises(exception) as exc:
        selection(data)

    assert error_msg in str(exc)


@parametrize('data,expected', [
    # Case 1
    ([5, 4, 6, 1, 7], [1, 4, 5, 6, 7]),

    # Case 2
    ([14, -1, 3, -6, 19, -100], [-100, -6, -1, 3, 14, 19]),

    # Case 3
    ([1.014, 1.12, 1.011, 1.56, 1.009, 2],
     [1.009, 1.011, 1.014, 1.12, 1.56, 2]),

    # Case 4
    (['z', 'c', 'y', 'a'], ['a', 'c', 'y', 'z']),

    # Case 5
    ((14, -1, 3, -6, 19, -100), (-100, -6, -1, 3, 14, 19)),

    # Case 6
    (('z', 'c', 'y', 'a'), ('a', 'c', 'y', 'z')),

    # Case 7
    ([1], [1])
])
def test_merge_sort(data, expected):
    """Validates the selection sort on the given list of values."""
    assert merge(data) == expected


@parametrize('data,exception,error_msg', [
    ({'a': 1}, ValueError, 'A list/tuple of values should be given'),
    ([1, 2, 3, 'hello'],
     ValueError,
     "int() and str() type can't be specified at the same time")
])
def test_merge_sort_error(data, exception, error_msg):
    """Validates the error based on the given values."""
    with pytest.raises(exception) as exc:
        merge(data)

    assert error_msg in str(exc)
