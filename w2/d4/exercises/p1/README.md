Merge Sort
===========

Before you start, watch [this video](https://www.youtube.com/watch?v=EeQ8pwjQxTM) explaining the Merge Sort.

#### Algorithm

To perform the merge sort, first break the list down to sorted lists.

How do we get a sorted list by breaking it down? By making a list containing each individual element. After all, a list with a single value is sorted.

Then, every set of two lists are compared, and merged. For example:
```py
[8, 2, 5, 10, 19, 1] ###starting list

[8] [2] [5] [10] [19] [1] ### fully broken down

[2,8] [5, 10] [1,19] ### each set of two compared and merged

[2,5,8,10] [1,19] ### sets further compared and merged

[1,2,5,8,10,19] ### further compared and merged for the finished product
```
#### Implementation

Write a function `merge_sort()` that takes an unsorted `list` and using the merge sort algorithm, returns a sorted `list`. Do it recursively.

It is probably a good idea to make a helper function for the initial breaking down of the list.