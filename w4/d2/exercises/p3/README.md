Unix Ninja 2
============

ARE YOU READY FOR SOME MORE UNIX FUN?!!?!?!!?!!!!!!!!!!!!!??????

type these command into terminal

```bash
$ a=yo
$ b="armen and greg are the greatest, one"
$ echo $a
$ echo $b
```

Isn't that neat? We can store variables in our shell. That seems like it would be useful for if we wanted to write shell scripts...  
Anyways. write the variable b that you just saved to a .txt file. If you don't know how to do that, I recommend referring to yesterday's work. After you finish writing it to a txt file, take the contents of the text file you created, and tweet it.

We're going to have some fun with the text file attached.  
Python is a scripting language. So we can write scripts in it to do a lot of work for us. Write a script that creates 5 files and writes each consecutive line to it's respective file.

Make a sixth file. Have it write all of the lines with the word 'sculpture', and how many times the word appears. You can just make the files .txt, feel free to name them whatever you want.  
You should not be naming these manually. Your script should do all of it.

If I gave you a 100 line text file, it would make 100 folders with .txt files in them, and one file with all of the lines that contain the word 'sculpture', and the word count as the last night.

You will find the [subprocess](https://docs.python.org/3/library/subprocess.html) module helpful for this assignment. What does the shell parameter do?