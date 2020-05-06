# Quick Sort - Descending Order

This algorithm is a quick sort recursive function that takes an unsorted list and sorts it in a descending order.

The function internally splits a list of numbers into two halves by using a pivot. In this case, the pivot is determined by using the middle value of the list.

All the numbers greater than the pivot are moved to the left side of the pivot and the numbers less than the pivot are moved to the right side of the pivot.

The list is then sub-divided into two halves, where the left side starts from the beginning index of the list and ends at a split index and the right side starts at one index after the split index till the end index.

The function keeps repeating till all the numbers are sorted in the list.

**Example:**

Unsorted list of numbers [5, 3, 6, 8, 2] will be ordered in descending order as follows. 

Sorted list = [8, 6, 5, 3, 2]

## How to run locally

To run the quick sort for descending order, use the following command.

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