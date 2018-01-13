Debugging Challenge
===================

So you and your buddies made a sweet MMORPG. You don't have any players yet, and you wanted to test the database, so you hired someone to write code to seed it.

It _should_ be all done - you'll just have to make the migrations, migrate the DB, and run the seed file successfully. But _should_ is a bad word in programming. Turns out, this guy had no idea how to do it and his code is a mess.

To run the seed, you should just have to instantiate the class once like so:
```
SeedDatabase(players = 50, heroes = 150, teams = 20)
```
It takes three keyword arguments - number of players to create, number of heroes to create, number of teams to create. In the database, Players have many Heroes. Heroes have many Teams and Teams have many Heroes.

#### Goal

Using the error statements and your knowledge of Python and Django, go through and debug the code. When you are done, go in the Django shell and test your relations. Read through the docs from Django on [Many to Many](https://docs.djangoproject.com/en/1.4/topics/db/examples/many_to_many/) and [One to Many](https://docs.djangoproject.com/en/1.4/topics/db/examples/many_to_one/) relationships if you haven't already.