## Optimizing Queries and Data Comparisons

This challenge will take what we already know about SQL and Python and add the necessary tools to optimize how we make queries and compare data.

#### Setup

In create_db.py, initialize and create a new database "schedules.db" and give it the necessary tables to hold the following:

Students have a name, and a major.
Classes have a title, and a field of study.

Major and field of study are the same, ie. Economics is a major and a field of study.

Students have many classes.
Classes have many students.

Write a seed_db() function that takes the existing data in create db and randomly fills the database with it.


#### Query

Write a function shared_classes() in Python that takes two student names. It should return the classes they take together, if any. How you want to do this is open ended.

What is the Big O time complexity of your algorithm for loading the students and comparing their classes? Write it down, and benchmark your code.

#### First Optimization - the Index

Read [how indexes work](http://www.programmerinterview.com/index.php/database-sql/what-is-an-index/) here. What type of data structure does sqlite3 use to hold indexes?

Now, add an index to one or more of your tables on columns you think would be appropriate.

Benchmark again - what is your speed now?

#### Second Optimization - use a Set

Are you comparing the data returned from the DB in Python? If so, you probably aren't using the right data type. We haven't covered Sets yet - read about them [here](https://docs.python.org/3.4/library/stdtypes.html#set)

A set is very similar to a dictionary, only it does not store values. Only keys. The syntax is like so:
```
{'Programming', 'Calculus', 'Literature'}
```
Use sets to store the returned class data about both students and use set's built in methods to find the intersection if it exists.

The Big O complexity of this operation is `O(len(x) * len(y))`. If you did the most simple comparison with arrays, it was probably `O(len(x) * len(y)**2)`.

Read about sets. Why is this? Here's a [list](https://wiki.python.org/moin/TimeComplexity) of all Python datatype method's time complexity.

#### Third Optimization - a better (longer!) Query

Instead of doing all your comparisons on the Python side, can we pull the information straight out of the database with a more advanced query?

Before you write the query to replace your original answers- let's write a new function that takes a Major and number of students, and returns classes where that number of students or more in that class have that major.

Now, write your enhanced query to find the intersect without any Python data parsing.

Benchmark this function against your first two.

Sandbox!! You will want to get familiar with the following SQL commands: GROUP BY, HAVING, IN.