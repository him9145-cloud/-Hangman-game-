# IMPORT LIBRARIES
import random

# List of words
words = [
    "apple", "banana", "orange", "computer", "python",
    "hangman", "student", "college", "machine", "science",
    "football", "cricket", "basketball", "programming"
]

def checkName(name):
    if name == "":
        print("Sorry, you did not enter your name")
        return 0
    else:
        print("\n--------------------------------------\n")
        return 1

def hangman():
    # Select a random word
    word = random.choice(words).lower()

    alphabets = "abcdefghijklmnopqrstuvwxyz"
    chance = 10
    guess_made = ""

    while len(word) > 0:
        main = ""

        for letter in word:
            if letter in guess_made:
                main += letter
            else:
                main += "_ "

        if main.replace(" ", "") == word:
            print("Word is:", word)
            print("You Win!")
            break

        print(f"Guess the word: {main}")
        guess = input("Enter a letter: ").lower()

        if len(guess) == 1 and guess in alphabets:
            guess_made += guess
        else:
            print("Enter a valid single character.")
            continue

        if guess not in word:
            chance -= 1

            if chance == 9:
                print("9 turns left")

            elif chance == 8:
                print("8 turns left")
                print("      O")

            elif chance == 7:
                print("7 turns left")
                print("      O")
                print("      |")

            elif chance == 6:
                print("6 turns left")
                print("      O")
                print("      |")
                print("     /")

            elif chance == 5:
                print("5 turns left")
                print("      O")
                print("      |")
                print("     / \\")

            elif chance == 4:
                print("4 turns left")
                print("     \\O")
                print("      |")
                print("     / \\")

            elif chance == 3:
                print("3 turns left")
                print("     \\O/")
                print("      |")
                print("     / \\")

            elif chance == 2:
                print("2 turns left")
                print("     \\O/ |")
                print("      |")
                print("     / \\")

            elif chance == 1:
                print("1 turn left")
                print("Last breathing...")
                print("     \\O/ __|")
                print("      |")
                print("     / \\")

            elif chance == 0:
                print(f"You lost! The word was '{word}'")
                print("Game Over")
                print("      O____|")
                print("     /|\\")
                print("     / \\")
                break

name = input("Hey there! What is your name: ")

if checkName(name):
    print(name + ", let's play Hangman!")
    hangman()