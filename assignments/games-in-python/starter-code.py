"""Starter code for the Hangman Game Challenge."""

import random

WORDS = ["python", "hangman", "challenge", "programming", "computer"]
MAX_INCORRECT_GUESSES = 6


# Task 1: Choose a word
def choose_secret_word():
	"""Return a randomly selected word from WORDS."""
	# TODO: Use random.choice to select and return a word.
	pass


# Task 2: Show the player's progress
def display_progress(secret_word, guessed_letters):
	"""Return the word with unguessed letters shown as underscores."""
	# TODO: Build and return a string such as "_ a _ g m a n".
	pass


# Task 3: Play a round of Hangman
def play_game():
	"""Run the game until the player wins or runs out of guesses."""
	secret_word = choose_secret_word()
	guessed_letters = set()
	incorrect_guesses = 0

	# TODO: Loop while the word is not fully guessed and guesses remain.
	# Inside the loop:
	# - Display the current progress and remaining incorrect guesses.
	# - Ask the player to enter a letter.
	# - Add the guess to guessed_letters and update incorrect_guesses.
	pass

	# TODO: Display whether the player won or reveal the secret word.


if __name__ == "__main__":
	play_game()
