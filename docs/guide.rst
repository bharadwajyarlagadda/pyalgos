User's Guide
============

Sorting
-------

Insertion Sort
^^^^^^^^^^^^^^

A simple sorting algorithm that builds the final sorted list of items - one item at a time. It can be less efficient on larger lists.

- Best Case: Input is already sorted out. This takes only ``O(n)`` running time. For ex, [1, 2, 3, 4, 5] - in this case it takes only linear time to sort out the items.
- Average/Worst Cases: In both the cases, it takes ``O(pow(n, 2))`` running time to sort out the items. In both these cases, the items in the list are either in a reverse order (or) zig-zag order.

You can use ``Insertion Sort`` from ``pyalgos``.

.. code-block:: python

    from pyalgos.sorting import insertion

    sorted = insertion([3, 4, 2, 7, 5, 1])

    assert sorted == [1, 2, 3, 4, 5, 7]

Selection Sort
^^^^^^^^^^^^^^

A sorting algorithm that build the final sorted list of items. It is inefficient on larger lists.

- Best/Average/Worst Cases: In all these cases, the running time is ``O(pow(n, 2))``.

You can use ``Selection Sort`` from ``pyalgos``.

.. code-block:: python

    from pyalgos.sorting import selection

    sorted = selection([3, 4, 2, 7, 5, 1])

    assert sorted == [1, 2, 3, 4, 5, 7]

