### Hangman
We all know the classic game hangman, today we'll be making it. With the wonderful bonus that we are programmers and we can make it as hard or as easy as we want. The wordlist.txt comprises of words spanning 3 - 15+ letter words in length so there is plenty of scope to make this interesting!

For those that don't know the rules of hangman, it's quite simple. There is 1 player and another person (in this case a computer) that randomly chooses a word and marks correct/incorrect guesses.

The steps of a game go as follows:
  - Computer chooses a word from wordlist.txt
  - The word is stripped of punctuation (e.g. "administrator's" would be "administrators")
  - The word is then populated with underscores in place of where the letters should. ('hello' would be '_ _ _ _ _')
  - Player then guesses if a word from the alphabet [a-z] is in that word
  - If that letter is in the word, the computer replaces all occurences of '_' with the correct letter
  - If that letter is NOT in the word, the computer draws part of the gallow and eventually all of the hangman until he is hung
  - This carries on until either:
      - The player has correctly guessed the word without getting hung OR
      - The player has been hung


### Bonus Features
  - I want to chose a difficulty level
      -  Easy ==> words of length 3-5
      -  Medium ==> words of length 5-7
      -  Expert ==> words of length 8+
  - Our users now want to load hangman with their own custom .txt file. How can we do this?
