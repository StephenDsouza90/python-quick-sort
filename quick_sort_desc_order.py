import random


def partition(arr, startIndex, endIndex):
    """
    The function internally splits a list of numbers into two 
    partitions by using a pivot. In this case, the pivot is 
    selected at random from the given items in the list. 
    
    The split is done such that all the numbers greater than the 
    pivot are moved to the left side of the pivot and 
    the numbers less than the pivot are moved to the right side 
    of the pivot. 
    
    This is done with the help of a left and right pointers that 
    scans elements and if it meets the above condition, 
    it re-positions these elements to the left or right accordingly.

    :param arr: List of remaining numbers to be sorted.
    :param startIndex: Starting index of scan.
    :param endIndex: Ending index of scan.
    :return rightIndex: Index used for creating sub-arrays.
    """

    pivot = random.choice(arr)
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


def quickSortDescOrder(arr):
    """
    This quick sort function takes an unsorted list of numbers
    and sorts it in descending order in-place.

    :param arr: A list of unsorted numbers.
    :return arr: The same list sorted in decending order.     
    """

    def _quickSort(items, startIndex, endIndex):
        """
        This function repeats recursively for each new partition 
        that's created at the left and right until no more partitions 
        can be made. At this point the list is then sorted.

        :param items: List of remaining numbers to be sorted.
        :param startIndex: Index from the left side i.e. starting index.
        :param endIndex: Index from the right side i.e. ending index.
        """

        if startIndex < endIndex:
            splitIndex = partition(items, startIndex, endIndex)
            _quickSort(items, startIndex, splitIndex)
            _quickSort(items, splitIndex + 1, endIndex)

    _quickSort(arr, 0, len(arr) - 1)

    return arr


def main():
    arr = list(map(int, input("\nEnter a list of numbers:\n").split()))
    quickSortDescOrder(arr)
    print(arr)


if __name__=='__main__':
    main()