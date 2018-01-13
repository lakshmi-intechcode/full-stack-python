Binary Search
===============

#### Summary

In computer science, a binary search or half-interval search algorithm finds the position of a specified input value (the search "key") within an array **sorted** by key value. For binary search, the array should be arranged in ascending or descending order. 

#### An example
The next best example I can think of is the telephone book, normally called the White Pages or similar but it'll vary from country to country. But I'm talking about the one that lists people by surname and then initials or first name, possibly address and then telephone numbers.

Now if you were instructing a computer to look up the phone number for "John Smith" in a telephone book that contains 1,000,000 names, what would you do? Ignoring the fact that you could guess how far in the S's started (let's assume you can't), what would you do?

A typical implementation might be to open up to the middle, take the 500,000th and compare it to "Smith". If it happens to be "Smith, John", we just got real lucky. Far more likely is that "John Smith" will be before or after that name. If it's after we then divide the last half of the phone book in half and repeat. If it's before then we divide the first half of the phone book in half and repeat. And so on.

This is called a binary search and is used every day in programming whether you realize it or not.

#### Write your Binary Search

Start at the middle of your dataset.
If the number or word you are searching for is lower, stop searching the greater half of the dataset. Find the middle of the lower half and repeat.

Similarly if it is greater, stop searching the smaller half and repeat the process on that half. By continuing to cut the dataset in half, eventually you get your index number. 

This is an O(log n) operation, which is generally the fastest search.

#### Write assert statements to test your code

Write six assert statements to test your code. What if the number isn't in the dataset? What happens to your program? Error check and make sure it doesn't crash.

#### Benchmark

Create a new file, and import the following:

Your benchmark function  
Your linear search
Your binary tree

Using your benchmark function, benchmark your binary search versus the linear search. Which is faster? What is an advantage of both? Be cool and import the benchmark.py and linear.py file and call them that way. No copy paste. Write in comments in your python file.

Now benchmark your binary search against your binary tree's search function. Which is faster?


#### Word List

Import the file "wordlist.txt" and search for some words. Specifically I want the index of 'illuminatingly', 'lexicalisation', and 'unexpectedness'.

Benchmark the binary and linear searches again using this file. 


#### Resources
[Binary Search Algorithm](http://en.wikipedia.org/wiki/Binary_search_algorithm)