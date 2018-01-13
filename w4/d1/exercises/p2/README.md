Baby ORM - Querying
===================

Are you ready for this? Today we're going to build the first half of our own ORM, or Object-relational mapper. Read more about ORM [here](http://en.wikipedia.org/wiki/Object-relational_mapping)

This is to prepare you for how you will be interacting with the DB in Django and many other web frameworks. This will also be your first foray in to meta-programming - as in code that writes code for you. In this case, our Python code will build and execute the SQL queries for us.

To put it simply, the ORM treats a table in our SQL database like a Python class, and each row in that table can be an instance of that class. While we have been building classes for our database to provide an easy to use interface, this takes it one step further and gives uniform database methods to every model class.

For example, to get all rows from the Users table:  

In SQL:  
```sql
SELECT * FROM Users;
```
In Baby ORM:  
```py
Users.all()
```
To get all users named Greg:  

In SQL:  
```sql
SELECT * FROM Users WHERE name = 'Greg';
```
In Baby ORM:  
```py
Users.filter(name="Greg")
```
Get the idea?

#### Round 1: Create your Model class that all other models will inherit from

We've already created the skeleton you will need in orm_class.py. Don't touch the methods yet - just initialize the Model class.

Remember we want any model class, with any attributes to be able to inherit from this class and read from the appropriate database table.

You will need to use \*\*kwargs, known as keyword arguments. This allows you to pass any number of arguments with values, such as `name='Greg'` and the class or function will treat it like a dictionary.

In conjunction with the kwargs, you will also need to use the setattr() function.

Google these for further explanation.

#### Round 2: Write your all() method

The all() class method should return all rows in the database for a table whose name matches the class. The rows should be instances of the class - not just sqlite's return value.

In a class method, the keyword "self" refers to the class.

You'll probably want to look up how to get the name of the class that self refers to. Remember that it could be anything the user decides, so long as it inherits from your Model class. You'll also need to get the column names from sqlite cursor.

Test this and all your methods against the included babyorm.db - there is data in the Users table and Stocks table. Check out the create_db.py file to see the schema.

#### Round 3: Write your get() method

Finally we start doing some heavy lifting. get() should take a simple equality condition as an argument and return just 1 row as an object from that table. Limit the return to 1 in SQL, not in your program.

#### Round 4: Write your filter() method

Like get(), filter should also take a simple equality condition as an argument. However it should return all rows from the table that match the condition as objects of the class.

#### Refactor

Assumably if you are reading this your code is working - how did you do on OO? Are your class methods big balls of mud? Were you able to reuse some of the code between `.all()`, `.filter()`, and `.get()`?

Refactor so every single step that the methods use is also a function. Name everything well so your code is easy to read.