User's Guide
============

Sorting
-------

Insertion Sort
^^^^^^^^^^^^^^

A simple sorting algorithm that builds the final sorted list of items - one item at a time. It can be less efficient on larger lists.

- Best Case: Input is already sorted out. This takes only ``O(n)`` running time. For ex, [1, 2, 3, 4, 5] - in this case it takes only linear time to sort out the items.
- Average/Worst Cases: In both the cases, it takes ``O(pow(n, 2))`` running time to sort out the items. In both these cases, the items in the list are either in a reverse order (or) zig-zag order.

You can use ``Insertion Sort`` from ``pyalgos`` for both list of integers and list of strings.

.. code-block:: python

    from pyalgos.sorting import insertion

    numbers_sorted = insertion([3, 4, 2, 7, 5, 1])
    alphabets_sorted = insertion(['a', 'z', 'y', 'b', 'w'])

    assert numbers_sorted == [1, 2, 3, 4, 5, 7]
    assert alphabets_sorted == ['a', 'b', 'w', 'y', 'z']

.. note:: You can provide either list/tuple of values.


Selection Sort
^^^^^^^^^^^^^^

A sorting algorithm that build the final sorted list of items. It is inefficient on larger lists.

- Best/Average/Worst Cases: In all these cases, the running time is ``O(pow(n, 2))``.

You can use ``Selection Sort`` from ``pyalgos`` for both list of integers and list of strings.

.. code-block:: python

    from pyalgos.sorting import selection

    numbers_sorted = selection([3, 4, 2, 7, 5, 1])
    alphabets_sorted = selection(['a', 'z', 'y', 'b', 'w'])

    assert numbers_sorted == [1, 2, 3, 4, 5, 7]
    assert alphabets_sorted == ['a', 'b', 'w', 'y', 'z']

.. note:: You can provide either list/tuple of values.
