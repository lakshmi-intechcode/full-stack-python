Employees and Departments
=========================

#### Database Creation - One to Many Relationship

Using the Django ORM, create tables with these values and relationships:

An employee has a name and a birthdate.  
An employee belongs to a department.

A department has a name and a budget.  
A department has many employees.

Don't forget to makemigrations and migrate your db.

#### Build it out

Now we've got some additional requirements.

An employee can be a manager.  
A manager has a team of employees.  
Employees can belong to multiple teams.  
An employee can be in multiple departments.  

After you make each change, makemigrations and migrate again to test it. What happens? What do the migration files look like inside?

Continue to sandbox and see how your relationships work. If you are having trouble seeing the relationships, think about adding a `__str__` method to each of your tables, so that you get easier to read feedback.  

Resources
---------

[Django's ORM Docs](https://docs.djangoproject.com/en/dev/topics/db/models/)  
[Many to many example](https://docs.djangoproject.com/en/dev/topics/db/examples/many_to_many/)