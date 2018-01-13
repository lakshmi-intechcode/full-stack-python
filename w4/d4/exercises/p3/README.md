Reddit Miner
============

Now that you've completed mining coinmarketcap for data, you've seen that scraping data using HTML can be kind of messy. If they decide to change an id of a div or something, we're screwed. It's extremely useful, but not an exact science by any stretch.

Now we're going to move on to reddit. Reddit is a beast. It's huge and constantly changing. Thank doge that they will serve us json.

What does that mean? Well go to http://www.reddit.com/.json and take a look.

The front page is one massive json object. In fact, every page on reddit is.

Let's parse that beast.

#### Getting the JSON

Using requests, get that big json file and load it.

#### Our database

We're going to build an app that saves every front page post into the database when it is run. For each post, we'll want its title, author, url, subreddit it was posted in, number of upvotes, and the datetime it was posted on Reddit.

Create the necessary table using the django ORM.

#### Getting the correct data

That json return is a little scary. It's huge and complex. How can you search it in the terminal to figure out what fields you need?

Access the correct fields in the object and save them to your db. We don't want duplicate entries - ensure uniqueness in a way that makes sense.

If you run your program again and an entry already exists, update it so we get the most recent score.

#### Indexing

Whatever column you decide to use to ensure uniqueness, we'll want to add an [index](http://en.wikipedia.org/wiki/Database_index) to this field because we're going to be searching it alot. What is the big o when searching by index? What is it without one?

#### The final product

Create a function that just pulls a random row from your reddit frontpage database and prints it to the screen. Since you've got the crontab running, you should soon have a huge database of the top reddit posts and links. In 6 months, repost and reap those sweet sweet internet points. Oh yeah!