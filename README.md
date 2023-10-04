# Hangman Game with Hints

This is a Python implementation of the classic game Hangman with a twist - hints! In this game, you'll be provided with a secret word, and your task is to guess the word one letter at a time. You have limited chances to guess the correct letters, so use your guesses wisely. If you run out of guesses before solving the word, you lose the game.

## How to Play

1. Clone or download this repository to your local machine.
2. Make sure you have Python installed on your computer.
3. Run the Python script hangman.py in your terminal or preferred Python environment.

## Rules

1. You start with 6 guesses and 3 warnings. You lose one guess if you guess a letter that is not in the secret word. If you run out of warnings, you lose one guess.
2. You can enter one letter per turn, and it must be a lowercase letter.
3. You can also type an asterisk (*) to get a hint. A hint will show you words from the wordlist that match the letters you've guessed correctly so far.
4. If you guess a vowel (a, e, i, o, u) that is not in the secret word, you lose two guesses.
5. You win the game if you correctly guess all the letters in the secret word before running out of guesses.
6. After each game, you can choose to play again or exit.

## Game Output

The game will display the following information during each turn:
* The current state of the hangman figure.
* The number of guesses you have left.
* The letters you've guessed so far.
* The secret word with underscores representing unguessed letters.
* A prompt for your next letter guess.

## Hints

If you get stuck, you can use the hint feature by typing an asterisk (*) instead of a letter. The game will display a list of words from the wordlist that match the letters you've guessed correctly so far. This can help you narrow down your guesses and solve the secret word.

## Enjoy the Game!

Have fun playing Hangman with Hints! Test your vocabulary and word-guessing skills, and see if you can outsmart the hangman. Good luck!

