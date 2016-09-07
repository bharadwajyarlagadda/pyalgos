# -*- coding: utf-8 -*-

import pytest

from .fixtures import parametrize

from pyalgos.sorting import insertion, selection


@parametrize('data,expected', [
    # Case 1
    ([5, 4, 6, 1, 7], [1, 4, 5, 6, 7]),

    # Case 2
    ([14, -1, 3, -6, 19, -100], [-100, -6, -1, 3, 14, 19]),

    # Case 3
    ([1.014, 1.12, 1.011, 1.56, 1.009, 2],
     [1.009, 1.011, 1.014, 1.12, 1.56, 2])
])
def test_insertion_sort(data, expected):
    """Validates the insertion sort on the given list of values."""
    assert insertion(data) == expected


@parametrize('data,exception,error_msg', [
    ((1, 4, 3, 5), ValueError, 'A list of values should be given')
])
def test_insertion_sort_error(data, exception, error_msg):
    """Validates the error if a non-list item is given."""
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
     [1.009, 1.011, 1.014, 1.12, 1.56, 2])
])
def test_selection_sort(data, expected):
    """Validates the selection sort on the given list of values."""
    assert selection(data) == expected


@parametrize('data,exception,error_msg', [
    ((1, 4, 3, 5), ValueError, 'A list of values should be given')
])
def test_selection_sort_error(data, exception, error_msg):
    """Validates the error if a non-list item is given."""
    with pytest.raises(exception) as exc:
        selection(data)

    assert error_msg in str(exc)
