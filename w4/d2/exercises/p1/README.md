ORM Save
========

You're going to write the save function for your Baby ORM. After this, your Baby ORM is complete and usable!

#### Pseudocode

Before we write any real code, we're going to write pseudocode. Read through the rest of this README, and pseudocode the two methods. Please include it in comments in your file.

#### The Save Method

You want to be able to take any number or arguments from whatever table is supplied, and either create the row, if it doesn't exist, or update the row, if it does exist. The save method should not take parameters, and is an instance method.
```py
user = Users(name="Cassie") # new instance
user.save() # creates new row in table, stores id, returns True on success

cassie = Users.get(name="Cassie") # existing row instance
cassie.hair = "purple"
cassie.save() # updates row, returns True
```

#### The Create Method

The create function is a class method, that creates a new row and returns the instance.
```py
user = Users.create(name="Greg") # returns newly created instance of User class
```
Think about the simplest way you can accomplish this.


Recommendations
---------------

If you haven't already become familiar, google the following:
```py
setattr()
hasattr()
__name__
type(self)
__dict__
vars()
**kwargs
```
Map this out before starting. Plan for what you need to solve this.
Go back to your game plan to make sure you're on track. Was your pseudocode accurate? If not, adjust it.