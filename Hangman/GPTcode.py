import random

def hangman():
    word_list = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grape","hangman","mango","litchi",""]
    word = random.choice(word_list).lower()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess! Attempts remaining:", attempts)
            if attempts == 0:
                print("You ran out of attempts. The word was:", word)
                break
        else:
            print("Correct guess!")

        masked_word = ""
        for letter in word:
            if letter in guessed_letters:
                masked_word += letter + " "
            else:
                masked_word += "_ "

        print(masked_word.strip())

        if "_" not in masked_word:
            print("Congratulations! You guessed the word:", word)
            break

hangman()
