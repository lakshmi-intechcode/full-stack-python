## Your Own Private Bank


Welcome back! In this challenge you'll be creating a rich Python terminal app emulating bank software.

#### Step 1: Database

Our DB schema for this challenge is simple. For now, we only need two tables - Users and accounts. A user can have many accounts. Users should have at minimum a username to log in to the app, a time when they were created, and a permissions level. An account should have a number and a balance. Design the schema in SQL designer if it helps you.

There's a file called create_db.py - write your sql that creates the db in there to keep everything organized.

#### Step 2: Our program models

We need two different classes for users - a client, and a banker. A client should be able to view all their accounts, deposit and withdraw funds to and from their OWN accounts, and transfer money from their OWN accounts to another user account. A banker should be able to create accounts, deposit and withdraw funds from ANY user account, and transfer money between ANY two user accounts. A banker should not have any accounts (no co-mingling of funds) and a person should not see the superuser options that bankers have. How you want to design this is up to you. See [inheritance](http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/)

I also strongly recommend that you have another class (see [static methods](https://julien.danjou.info/blog/2013/guide-python-static-class-abstract-methods)) or a module that handles only reading and writing to the database.

#### Step 3: Controller and Views

Stick to the MVC pattern - No spaghetti code! Keep your code dry. There's a lot of user choice options which could be a lot of if/else statements - can you think of a better way?

Present a nice clean interface to the user for the options they are allowed to perform. Some extra account details would be nice to display - some ideas are how long the user has been a member of the bank, which banker created their account, etc.