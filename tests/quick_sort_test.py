import nose.tools as nt

from quick_sort_desc_order import quickSortDescOrder
from quick_sort_asc_order import quickSortAscOrder


class Tests(object):

    def test_quick_sort_random_list_in_descending_order(self):
        actual = quickSortDescOrder([5, 3, 6, 8, 2])
        expected = [8, 6, 5, 3, 2]
        nt.assert_equals(expected, actual)

    def test_quick_sort_random_list_in_ascending_order(self):
        actual = quickSortAscOrder([5, 3, 6, 8, 2])
        expected = [2, 3, 5, 6, 8]
        nt.assert_equals(expected, actual)
