# QuickSort - Descending Order

This algorithm is based on QuickSort which is a sorting algorithm that sorts a list by breaking it into smaller lists that can be sorted more efficiently recursively. In this algorithm, we sort the list in descending order.

**How it works**

The function internally splits a list of numbers into two partitions by using a pivot. In this case, the pivot is selected at random from the given items in the list. The split is done such that all the numbers greater than the pivot are moved to the left side of the pivot and the numbers less than the pivot are moved to the right side of the pivot. This is done with the help of a left and right pointers that scans elements and if it meets the above condition, it re-positions these elements to the left or right accordingly.

This function repeats recursively for each new partition that's created at the left and right until no more partitions can be made. At this point the list is then sorted.

**Example:**

Input List = [5, 3, 6, 8, 2]

Resulting list sorted in descending order = [8, 6, 5, 3, 2]

**Time Complexity Analysis**

Best-case: A best-case scenario is when the list of N numbers has been evenly partitioned in each recursive step. In this case the pivot selected will be exactly in the middle. Because of the even partitioning, the data size for the next recursive calls are cut in half giving us a perfect "log n" time complexity to sort the data.

Worst-case: A worst-case scenario is when the pivot is either the smallest or the largest value that is selected. This causes the partition to be very badly uneven where either the left or the right partition will have just one item. This causes the data size for each recursive step to be of size n-1, n-2 and so giving us a total of O(n^2) quadratic time complexity.

Average-case: Since we don't make any assumptions about the data, it's not easy to select the pivot which will give us the best-case time complexity all the time. But to come close to the best case, we can select a pivot at random which with high probability can give us a partition which is closer to being even but maybe not equally even, but will not always give the worst case scenario. This is the average case. In this case, using a random pivot selection in each recursive step, the pivot will lie b/w 25% and 75% of the list resulting in a close to even partitioning. This also leads to an unbalanced division but can still yield a good log of N where N is still better than the worst case.

## How to run locally

To run the QuickSort for descending order, use the following command.

```bash

>> python quick_sort_desc_order.py

Enter a list of numbers:

5 3 6 8 2

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