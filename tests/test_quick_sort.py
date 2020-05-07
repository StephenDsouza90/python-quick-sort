import nose.tools as nt

from quick_sort_desc_order import quickSortDescOrder


class Tests(object):

    def test_quick_sort_in_descending_order(self):
        # Testing when a list is unsorted
        actual = quickSortDescOrder([5, 3, 6, 8, 2])
        expected = [8, 6, 5, 3, 2]
        nt.assert_equals(expected, actual)

        # Testing when a list is sorted by ascending order
        actual = quickSortDescOrder([2, 3, 5, 6, 8])
        expected = [8, 6, 5, 3, 2]
        nt.assert_equals(expected, actual) 

        # Testing when a list is sorted by descending order
        actual = quickSortDescOrder([8, 6, 5, 3, 2])
        expected = [8, 6, 5, 3, 2]
        nt.assert_equals(expected, actual)       