# Baylee Coons
# Fall 2026 CIS256
# Programming Assignment 4

import random

# list of figure skating words to guess
words = ["axel", "salchow", "loop", "spin", "jump", "ice", "skater"]

def choose_word():
    #picks a random word from the list
    return random.choice(words)

def main():
    word = choose_word()
    guessed_letters = []
    tries = 6
    
    print("Welcome to the Figure Skating Word Guessing Game!")
    
    while tries > 0:
        # build the string showing correctly guessed letters or underscores
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        
        print("\nWord:", display)
        print("Tries left:", tries)
        
        # if there are no underscores left, they won
        if "_" not in display:
            print("Congratulations! You guessed the word!")
            break
            
        guess = input("Guess a letter: ").lower()
        
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        # check if they already tried a specific letter
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
            
        guessed_letters.append(guess)
        
        
        if guess in word:
            print("Good job! That letter is in the word.")
        else:
            tries -= 1
            print("Incorrect! That letter is not in the word.")
            
    if tries == 0:
        print("\nGame over! The word was:", word)

if __name__ == "__main__":
    main()