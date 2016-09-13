# -*- coding: utf-8 -*-


def insertion(elements):
    """Returns the sorted values using insertion sort algorithm.

    The best case is when the input is an array that is already sorted. In
    this case, insertion sort has a linear running time O(n).

    The worst case is when the input is an array sorted in reverse order. In
    this case, insertion sort has a quadratic running time O(pow(n,2)).

    Args:
        elements (list): A list of values provided by the user.

    Returns:
        list: A list of elements sorted in ascending order.

    .. versionadded:: 0.1.0

    .. versionchanged:: 0.1.1
        Added validation for checking whether every element in the list is a
        string (when strings are provided in the list).
    """
    if not isinstance(elements, list):
        raise ValueError('A list of values should be given.')

    is_str = all(isinstance(element, str) for element in elements)

    if any(isinstance(element, str) for element in elements) and not is_str:
        # When any of the element in the list is a string, we should then
        # check whether all the other elements are strings or not.
        raise ValueError("int() and str() type can't be specified at the same "
                         "time")

    for pivot in range(1, len(elements)):
        next = pivot
        while next > 0 and elements[next - 1] > elements[next]:
            elements[next], elements[next - 1] = (elements[next - 1],
                                                  elements[next])
            next -= 1

    return elements
