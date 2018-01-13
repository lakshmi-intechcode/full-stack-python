Todos App with Baby ORM
=======================

Now we'll put your fully fledged ORM to good use. Create a terminal app that creates a todo list using ARGV, and saves the lists using your baby ORM.

For example:
```
python3 todolist.py add do laundry  
python3 todolist.py add buy groceries
python3 todolist.py list
python3 todolist.py complete <task id>
python3 todolist.py delete <task id>
```
#### Design and create your database

Design the schema you'll need and create the DB. Of course, import and integrate the baby ORM.

#### Outline your models and methods

Look at example above - we have the commands add, complete, delete, and list. These aren't just for the user - these are actual backend functionality in your code. Create a skeleton of methods for any db classes you might need.

#### Implement functionality

add() should append an item to the list.

list() should display the list of tasks and their id. If it is completed, it should be noted as such.
```
python3 todolist.py list
$ My Todo List
$ 1. do laundry
$ 2. buy groceries
```
delete() should take the id of the task and remove it from the database.

complete() should take the id of the task and mark it complete.