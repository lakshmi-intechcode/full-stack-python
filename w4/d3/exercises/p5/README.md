Unix Ninja 3
============

Today we're going to take a look at a few more commands.  

#### uniq

Type `$ man uniq` into your terminal and read the man page.

Type `$ uniq text.txt`. What do you get?

Can you get only one of each word?

How about the counts for each word?

Can you combine the two?

#### ps and top

Open a new tab in your terminal and type `$ ps`.

What is that? Let's man it.

While we're at it, let's type `$ man kill`.

Take the PID from one of your terminal processes and type `kill -9 [PID]`. Don't type PID, insert your PID where I typed it.

What does PID stand for?

What happened when you did that?

Remember this command. Sometimes when you're running a local server, it won't close it connection to a port. You can kill the process to open the port again.

Now try `$ top`. What's the difference between ps and top?

#### diff

Type `$ man diff` and read the man page.

Get the diff of text.txt and yo.txt. See how the syntax works. Change the files around, and see how it changes the diff. This may look similar to when you've had a merge conflict, or if you've ever used `git diff`.

#### chmod

Here is some reading on [chmod](http://www.perlfect.com/articles/chmod.shtml).

Read the man on chmod and [chown](http://www.computerhope.com/unix/uchown.htm), as well.

There won't be any exercises on these functions, but you should know them. How do file permissions work in Unix?

#### stdio

Read about [stdio](http://en.wikipedia.org/wiki/Standard_streams). This plays a big role in backend processes. It's a little hard to grasp, so I just want to introduce you to the concept.

#### du

	$ man du
	$ du
	$ du text.txt
	$ du ../

This doesn't matter as much, anymore, since your computer has so much space. Back in the day you had to be much more frugal with disk space. Still, now you know how to know how much space a file or folder is taking.

#### cksum

Read about what a checksum is [here](http://en.wikipedia.org/wiki/Checksum)

The command cksum generates a checksum for any data or file.

Get the checksum of text.txt and compare it to the checksum of yo.txt.

Now duplicate text.txt using cat and compare the checksums again.