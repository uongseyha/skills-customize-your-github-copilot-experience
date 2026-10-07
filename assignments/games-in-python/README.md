
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a word-guessing game in Python. Practice strings, loops, conditionals, user input, and random selection while tracking a player's progress and incorrect guesses.

## 📝 Tasks

### 🛠️ Task 1: Select a Word and Show Progress

#### Description
Complete `choose_secret_word()` and `display_progress()` in `starter-code.py`. Use the provided word list and show which letters the player has guessed.

#### Requirements
Completed program should:

- Randomly select and return one word from `WORDS`.
- Display guessed letters in their correct positions.
- Represent each unguessed letter with an underscore.

### 🛠️ Task 2: Run the Game

#### Description
Complete `play_game()` so the player can guess letters until the word is revealed or the incorrect-guess limit is reached.

#### Requirements
Completed program should:

- Prompt the player for a letter and record each guess.
- Track and display the number of incorrect guesses remaining.
- End when the player guesses the word or reaches `MAX_INCORRECT_GUESSES`.
- Display a win or loss message and reveal the secret word after a loss.
