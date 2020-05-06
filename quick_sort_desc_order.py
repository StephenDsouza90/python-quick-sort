def quickSortDescOrder(arr):
    """
    This quick sort function takes an unsorted list of numbers
    and sorts it in a descending order.

    :param arr: A list of unsorted numbers.
    :return arr: A list of sorted numbers in decending order. 
    """

    def partition(arr, startIndex, endIndex):
        """
        This method within the function splits the list 
        into two halfs by using a pivot. The pivot is 
        determined by using a middle number within the list.

        All numbers greater than the pivot are moved to
        the right of the list and all numbers less than
        the pivot are moved to the left of the list.

        At every loop, the index from the left side increaments
        and the index from the right side decrements.
        Once the left side index is equal to or greater than 
        the right side index, the while loop is exited.

        :param arr: List of unsorted numbers to be splited.
        :param startIndex: Index from the left side - starting index.
        :param endIndex: Index from the right side - ending index.
        :return rightIndex: Index used to create a partition between left hand side and right hand side.
        """

        pivot = arr[(startIndex + endIndex) // 2]
        leftIndex = startIndex - 1
        rightIndex = endIndex + 1

        while True:
            leftIndex += 1
            while arr[leftIndex] > pivot:
                leftIndex += 1

            rightIndex -= 1
            while arr[rightIndex] < pivot:
                rightIndex -= 1

            if leftIndex >= rightIndex:
                return rightIndex

            arr[leftIndex], arr[rightIndex] = arr[rightIndex], arr[leftIndex]

    def _quickSort(items, startIndex, endIndex):
        """
        This method within the function splits the list of numbers
        using the partition method to create two subsets of the list.

        The two subsets are then sorted in the same manner, where the 
        left hand side numbers are split from starting index till the split
        index and right hand side numbers are split from the an increament of 
        the split index to the end index.

        :param items: Numbers to be sorted.
        :param startIndex: Index from the left side - starting index.
        :param endIndex: Index from the right side - ending index.
        """

        if startIndex < endIndex:
            splitIndex = partition(items, startIndex, endIndex)
            _quickSort(items, startIndex, splitIndex)
            _quickSort(items, splitIndex + 1, endIndex)

    _quickSort(arr, 0, len(arr) - 1)

    return arr


def main():
    arr = [5, 3, 6, 8, 2]
    quickSortDescOrder(arr)
    print(arr)


if __name__=='__main__':
    main()