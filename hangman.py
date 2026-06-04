import random

# List of predefined words
words = ["python", "computer", "program", "keyboard", "hangman"]

# Select a random word
word = "python"

# Create hidden word display
guessed_word = ["_"] * len(word)

# Variables
incorrect_guesses = 0
max_guesses = 6
guessed_letters = []

print(" Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_guesses and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Guessed Letters:", ", ".join(guessed_letters))
    print(f"Remaining Chances: {max_guesses - incorrect_guesses}")

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check letter in word
    if guess in word:
        print(" Correct Guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print(" Wrong Guess!")
        incorrect_guesses += 1

# Game result
if "_" not in guessed_word:
    print("\n Congratulations! You guessed the word:", word)
else:
    print("\n Game Over!")
    print("The correct word was:", word)