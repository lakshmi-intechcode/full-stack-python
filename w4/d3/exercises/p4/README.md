Threading 101
=============

We're going to give a short introduction to multithreading. Threads deal with the issue of concurrency. Threads usually emulate concurrency. Rather than actually having multiple processes running the same time completely independent of each other, the computer will switch between processes quickly enough where the processes will be 'concurrent enough'. With multiple processors, it is possible to have truly concurrent operations.

Understanding threading will be important to your futures as finance programmers. The issue of concurrency becomes very important when you have writes coming from many places into one--for example, your database. Different databases deal with concurrency differently, and understanding how your database handles these things is a good thing to know. We're going to be using PostgreSQL, which is known for being very good with at concurrency and write heavy apps.

To deal with concurrent reads/writes that you want to have happen sequentially, there are locks. It does what it sounds like. You can set a lock so that none of the other threads can access the data until it's their turn in line. For example, you can have a lock every time a thread is writing to your file, and release the lock once it is done. This way you don't end up having, basically, a merge conflict (kind of like what you see with git). This is, obviously, good for data integrity.

Another way to deal with this issue is to have multiple threads that once done with their operation, send it to a queue. The queue then does the operations in the order they came (the one thing queues do).  
[Read atleast the intro to threads here. Feel free to read through all of it](http://en.wikipedia.org/wiki/Thread_(computing)).

We will be doing some trivial things with threads, so you can see how they work.

We will be using Python's threading library, which is a higher level interface for using threads. It's a little easier to use than Python's thread library, and offers better functionality.

#### Step 1

[Keep this link open in your browser](https://docs.python.org/2/library/threading.html#lock-objects)  

* import the threading library
* make a class myThread (or whatever you want to call it) and have it inherit from ```threading.Thread```.
* the threading library comes with a built in ```__init__```. We're going to overwrite it.
* Inside your ```__init__```, add this line ```threading.Thread.__init__(self)```.
* Give the thread some properties... Let's go with string, counter, and delay.
* Threads also come with a run instance method. 'run' runs once you start the thread (```my_thread.start()```).  
* We're going to overwrite run and give it the print_string method provided. Pass in the properties from myThread into it.
* Create two or more instances of myThread, and then call start on them.
* Run the code and watch it.
* Play with it a bit until you feel like you see what's going on.
* Once you feel like you know what's going on, trace through the code once more and look at the [Python docs]((https://docs.python.org/2/library/threading.html#lock-objects)) again.

#### Step 2

We're going to add a lock to this.

* In the document's main thread (Every process is a thread, even if there is only one), define and instantiate a lock.
* Inside your run method, call ```lock.acquire()``` and ```lock.release()``` around your print_string method.
* Run the code. What happened?

As you can imagine, while doing a read/write, this can be helpful to make sure nothing else is also read/writing to a file or to the database. This is good for the integrity of your data.

#### Step 3

* Call join on one of your threads. What happens?
* Call join on all of your threads. What happens?

If you're having trouble following along with what's happening, make sure to ask us questions. Also, make sure you're playing with your code. Every time you run your code, you're being given information. Use that to your advantage. Imagine you're a detective building a case.