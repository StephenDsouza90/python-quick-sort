# QuickSort - Descending Order

This algorithm is based on QuickSort which is a sorting algorithm that sorts a list by breaking it into smaller lists that can be sorted more efficiently recursively. In this algorithm, we sort the list in descending order.

**How it works**

The function internally splits a list of numbers into two partitions by using a pivot. In this case, the pivot is selected at random from the given items in the list. The split is done such that all the numbers greater than the pivot are moved to the left side of the pivot and the numbers less than the pivot are moved to the right side of the pivot. This is done with the help of a left and right pointers that scans elements and if it meets the above condition, it re-positions these elements to the left or right accordingly.

This function repeats recursively for each new partition that's created at the left and right until no more partitions can be made. At this point the list is then sorted.

**Example:**

Input List = [5, 3, 6, 8, 2]

Resulting list sorted in descending order = [8, 6, 5, 3, 2]

**Time Complexity Analysis**

Best-case: A best-case scenario is when the list of N numbers has been evenly divided (total n is even) or close to evenly divided (total n is odd) while the value of the pivot is a middle value. The sub-arrays are divided into size of log2 n which means the list has been cut in half to solve the problem. Therefore, the best-case is O(n log n), where n is the number of elements in the list and log n is the half of size N.  

Average-case: An average-case scenario is when the list has been divided by 3/4 and 1/4 because the pivot lies between 75% and 25% of the list. This leads to an unbalanced division, however still using a log4/3 and on average the processing time is O(n log n).  

Worst-case: A worst-case scenario is when the list has been divided in an unbalanced way because the pivot occours at the extreme left or extreme right of the list. This leads one sub-array being larger than the other at every recursive call leading to n - 1, n - 2 and so on. This makes the problem longer to solve, hence the worst-case is O(n^2) because at every call, n is being sorted.

## How to run locally

To run the QuickSort for descending order, use the following command.

```bash

>> python quick_sort_desc_order.py

[8, 6, 5, 3, 2]

```

## Testing

To run tests locally, use the following command. For this to work, install the `nose` library.

```bash

>> python -m "nose" tests

```

## Install dependencies

The dependencies are saved in the requirements.txt file. It can be installed via the following command:

```bash

>> pip install -r requirements.txt

```