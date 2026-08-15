'''Hangman game'''

import random

'''List of predefined words'''

pre = ["apple", "tiger", "house", "money", "car"]

'''Random Word'''

word = random.choice(pre)

'''Storing guessed letters'''

guessed_letter = []

'''Number of chances'''

chance = 6

print("Welcome to Hangman!!!")

'''Keep playing till chances end'''

while chance > 0:

    display = ""

    # Display the word
    for letter in word:
        if letter in guessed_letter:
            display = display + letter + " "
        else:
            display = display + "_ "

    print("\nWord:", display)
    print("Lives Left:", chance)

    # If the word is completed
    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed_letter:
        print("You already guessed this letter!")
        continue

    guessed_letter.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        chance = chance - 1
        print("Wrong Guess!!")


if chance == 0:
    print("GAME OVER!")
    print("The word was:", word)
    



        


