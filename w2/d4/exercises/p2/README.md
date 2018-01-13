Quicksort
=========

Wikipedia on [Quicksort](http://en.wikipedia.org/wiki/Quicksort).  

![quicksort gif](http://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)

#### Algorithm

Another divide-and-conquer algorithm, Quicksort works by picking a pivot point, or a value in the array, and reordering all the elements with values less than the pivot to the front of it, and all values greater than the pivot to the back. This is called the partition operation, and upon completion the pivot point is in its correct position.

You then recursively apply the same steps to each sub array - the elements smaller than the last pivot, and the elements larger than the last pivot.

Your base case is when a sub array is length 1 or 0.

#### The Pivot

Unsure of where to set the pivot? Read under the header "Implementation issues" on the Wikipedia.

#### Implementation

Write a function, `quicksort()` that takes an unsorted `list` and returns a sorted `list`. You may want to use some helper functions to partition.