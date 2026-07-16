import random

# List of 5 predefined words
words = ["apple", "tiger", "house", "python", "banana"]

# Choose a random word
word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6
display = ["_"] * len(word)

print("=== Welcome to Hangman ===")

# Game loop
while incorrect_guesses < max_guesses and "_" in display:
    print("\nWord:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Incorrect guesses left:", max_guesses - incorrect_guesses)

    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            # Reveal the guessed letter
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
        else:
            print("Wrong guess!")
            incorrect_guesses += 1

# Game result
if "_" not in display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
