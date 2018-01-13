Insertion Sort
==============

Wikipedia on [insertion sort](http://en.wikipedia.org/wiki/Insertion_sort).

![insert sort gif](http://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

#### Algorithm

Insertion sort is a common sorting algorithm that, while still its worst case is still O(n**2), it is much more efficient than Bubble sort on average.

According to wikipedia, when people manually sort something, like a deck of cards for example, most use a method similar to insertion sort.

The algorithm is simple - here it is in pseudocode.
```
from i = 1 to length of array:
	j = i
	while j > 0 and array[j-1] > array[j]:
		swap array[j] and array[j-1]
		j = j - 1
```
#### Implementation

Write a function `insertion_sort()` that takes an unsorted `list` and returns a sorted `list`, using the insertion sort algorithm.