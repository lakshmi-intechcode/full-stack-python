## Vigenere Cipher

#### Yeah crypto!

Remember the Caesar cipher we did? Well we're moving up in the world.

The [Vigenere cipher](http://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher) was formulated in the 1400s and accomplished then using metal discs.

While much more powerful cryptography exists and is used, the Vigenere cipher is still theoretically unbreakable.

Here's a [video that explains it in depth](https://www.youtube.com/watch?v=9zASwVoshiM)

The way it works is simple. You have a string to encrypt, and a key string. Moving one letter at a time simultaneously through both strings, raise the string to encrypt's character by the value of the key string's character, with A equal to 0, B equal to 1, and so on. When you reach the end of the key string, start again at the beginning.

For example, say we want to encrypt "programmingrules" with the key string "ratchet", this is our result

    to_encrypt: programmingrules  
    key string: ratchetratchetra  
    resulting:: grhiyefdigiyyevs  

If you don't see it right away, look at the "a" characters. When a in ratchet occurs, the letter in the result is unchanged. When a is in string to encrypt, the resulting letter is equal to the character in the key string.

The key is merely the word "ratchet" - as the program runs, the word is repeated to match the length of the string you wish to encrypt. This is what is demonstrated above.


#### Requirements

Note that, like the caesar cipher, when we go past 'Z' we start again at 'A'. Leave spaces and symbols untouched and add them to your resulting string. We must also account for both uppercase and lowercase letters and leave them as the user input them.

In Python, we use ord() to get the ASCII numeric value of a character and chr() to convert ASCII value back to a character.

Using an MVC framework, make an app that any user can use. Give them a menu view that lets them choose to encrypt or decrypt, and takes the string and the key. Write the necessary functionality in your model in a vigenere class. There can be a lot here and your code can become a mess fast - stick to one method doing one thing.

No need for any persistence here.

Tie them together with the controller.

# Let's go crypto!