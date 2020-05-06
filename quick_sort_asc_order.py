import random

def quickSortAscOrder(arr):
    """
    """

    def partition(arr, lowIndex, highIndex):
        """
        """

        pivot = arr[(lowIndex + highIndex) // 2] # random.choice(arr) 
        leftIndex = lowIndex - 1
        rightIndex = highIndex + 1

        while True:
            leftIndex += 1
            while arr[leftIndex] < pivot:
                leftIndex += 1

            rightIndex -= 1
            while arr[rightIndex] > pivot:
                rightIndex -= 1

            if leftIndex >= rightIndex:
                return rightIndex

            arr[leftIndex], arr[rightIndex] = arr[rightIndex], arr[leftIndex]

    def _quickSort(items, lowIndex, highIndex):
        """
        """

        if lowIndex < highIndex:
            splitIndex = partition(items, lowIndex, highIndex)
            _quickSort(items, lowIndex, splitIndex)
            _quickSort(items, splitIndex + 1, highIndex)

    _quickSort(arr, 0, len(arr) - 1)

    return arr


def main():
    arr = [5, 3, 6, 8, 2]
    quickSortAscOrder(arr)
    print(arr)


if __name__=='__main__':
    main()