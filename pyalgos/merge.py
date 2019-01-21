# -*- coding: utf-8 -*-


def merge(elements):
    """Returns the sorted values using merge sort algorithm.

    The time complexity will always be O(n * log(n)).

    Args:
        elements (list/tuple): A list/tuple of values provided by the user.

    Returns:
        list/tuple: A list/tuple of elements sorted in ascending order.

    .. versionadded:: 0.2.0
    """
    if not isinstance(elements, (list, tuple)):
        raise ValueError('A list/tuple of values should be given.')

    # Get the instance of the data structure given.
    instance = type(elements)

    if instance is tuple:
        # Convert the tuple of elements to list of elements. We need to
        # convert the tuple to list because a tuple is immutable. You cannot
        # swap the elements of a tuple.
        elements = list(elements)

    is_str = all(isinstance(element, str) for element in elements)

    if any(isinstance(element, str) for element in elements) and not is_str:
        # When any of the element in the list is a string, we should then
        # check whether all the other elements are strings or not.
        raise ValueError("int() and str() type can't be specified at the same "
                         "time")

    if len(elements) <= 1:
        # A list of size 1 is already sorted.
        return elements

    # Using "//" gives you int() value.
    mid_position = len(elements) // 2

    # Recursively sort both sub-lists
    left = merge(elements[:mid_position])
    right = merge(elements[mid_position:])

    # Merge the sorted sub-lists.
    sorted = []

    while left and right:
        if left[0] <= right[0]:
            # When the first element of left sub-list is less than first
            # element of right sub-list, append the first item of left
            # sub-list to the sorted list and remove that element from left
            # sub-list.
            sorted.append(left[0])
            left.pop(0)
        else:
            # When the first element of right sub-list is less than first
            # element of left sub-list, append the first item of right
            # sub-list to the sorted list and remove that element from right
            # sub-list.
            sorted.append(right[0])
            right.pop(0)

    # There is a possibility that the left sub-list might have elements left
    # in it. Append the elements from left sub-list to the sorted list.
    while left:
        sorted.append(left[0])
        left.pop(0)

    # There is a possibility that the right sub-list might have elements left
    # in it. Append the elements from right sub-list to the sorted list.
    while right:
        sorted.append(right[0])
        right.pop(0)

    if instance is tuple:
        # Convert the data structure back to tuple if the user has provided a
        # tuple of values.
        sorted = tuple(sorted)

    return sorted
