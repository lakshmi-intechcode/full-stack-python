Club Maker
==========

You've been commissioned to build software to manage student clubs on a college campus.

#### The Relationships

Design the schema in SQL designer, then in the Django ORM.

A student can have memberships to many clubs  
A club can have many students  
A student can have many interests  
A club can have many interests  
A student can have a title for each club they belong in  

#### Making Queries

Create queries to show that your database has all of these relationships.

Show all the students that belong to a given club, along with their titles.

Show all of the students that have a given interest.

Given a student, find the clubs that match their interests.

If you are having trouble seeing the relationships while you're in shell, think about adding a `__str__` method to each of your tables, so that you get easier to read feedback.

Resources
---------

[Django's ORM Docs](https://docs.djangoproject.com/en/dev/topics/db/models/)  
[Many to many example](https://docs.djangoproject.com/en/dev/topics/db/examples/many_to_many/)