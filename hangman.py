# CD, Hangman assignment


# Create a list of 10 words on a seperate text file
# Create another file holding win/loss counts
# Read files
# Use split (",") on the content of the words txt document to create your list of words
# Pull win and lose totals from the other txt file and save them as 2 seperate variables
# Build the hangman game
    # Show user hang
    # Under neeth do blanks for the number of letter that you have in the word
    # User guesses letter keep on going
    # Save the correct word as a variable random.choice(name or the list)
    # Number of wrong guesses (0)
    # What letters have been guessed []
# Function to display the hangman (Needs number of wrong guesses)

'''
_______
|     |
|     O
|    /|\
|    / \
|_________

'''

# Function to show the letter and spaces (The correct word, letters that have been guessed)
# Variables for display word (starts as an empty string)
# Loop over the correct word
    # Check if letter has been guessed
        # Then add the letter to the display variable
    # If they haven't guessed the letter
        # Add an underscore to the display word
# Return the finished display word (outside of the loop)

# Main loop of the game (while True)
    # Call function to show hangman
    # Print function call to show display word
    # Create variable and ask user to guess a letter
    # Add the letter to list of guessed letters
    # Check if not letter in word:
        # Increase incorrect guesses
    # Check if (display word) is as the word <= calling funtion
        # Tell user they won!
        # Increase win total
        # Ask if they want to play again
            # Reset random word, rest wrong guess count
    # Check to see if they lost (if they have 6 wrong guesses)
        # Tell them they lost
        # Tell them what the word was
        # Increase the lost count
        # Ask if they want to play

import random 
import os.path

def display_hanging_victim (wrong_guesses):

    print("_______")
    print("|     |")

    if wrong_guesses > 0:
        print("|     0")
    else:
        print("|")
    
    print("|    ", end = '')

    if wrong_guesses == 2:
        print(" |", end = '')
    elif wrong_guesses > 2:
        print("/|", end = '')
    if wrong_guesses > 3:
        print("\\", end = '')

    print("")

    print("|    ", end = '')
    
    if wrong_guesses > 4:
        print("/ ", end = '')
    if wrong_guesses > 5:
        print("\\", end = '')
    
    print("")
    print("|________")
# End of display_hanging_victim function

def record_record (wins, losses):
    with open("stats.txt", "w") as file:
        file.write(str(wins) + "," + str(losses))
# end of record_record function

def display_word_guess (right_answers):
    for character in right_answers:
        print(character, end = ' ')
    print("")
# END OF FUNCTION

# ----------------------------------------- load words and choose random word
word_contents = ""

with open("words.txt", "r") as file:
    word_contents = file.read()
    
word_list = word_contents.split("\n")

random_word_index = random.randint(0, len(word_list) - 1)
word_to_guess = word_list[random_word_index].upper()

# print(word_to_guess)

# ----------------------------------------- load stats
stats_filename = "stats.txt"

if not os.path.exists(stats_filename):
    record_record(0,0)

hangman_record = ""

with open(stats_filename, "r") as file:
    hangman_record = file.read()
    
hangman_scores = hangman_record.split(",")

wins = int(hangman_scores[0])
losses = int(hangman_scores[1])

# print(f"wins: {wins}, losses: {losses}")

# ----------------------------------------- starting the game
number_of_guesses = 0
wrong_guesses = 0
winning = False

guesses = []
solved = []
word = []

for letter in word_to_guess:
    solved.append("_")
    word.append(letter)

# print(solved)
# print(word)

print(f"Your record is {wins} wins and {losses} losses.")
while True:
    display_hanging_victim(wrong_guesses)
    print("")
    display_word_guess(solved)
    print("")

    print("Guessed letters: " + ", ".join(guesses))
    print(f"Wrong guesses remaining: {6 - wrong_guesses}")

    while True:
        guess = input("Guess a letter: ").upper()
        print("")
        print("")
        if guess not in guesses:
            guesses.append(guess)
            break
        else:
            print(f"Sorry, you already guessed '{guess}'. Try again.")

    good_guess = False
    index = 0
    for letter in word:
        if guess == letter:
            solved[index] = letter
            good_guess = True
        index += 1

    if good_guess != True:
        wrong_guesses += 1
        print(f"Sorry, '{guess}' is not in the word.")

    if solved == word:
        winning = True
        wins += 1
        break 

    if wrong_guesses > 5:
        losses += 1
        display_hanging_victim(wrong_guesses)
        break

if winning:
    print(f"\nYou won! You guessed the word: '{word_to_guess}'")
else:
    print(f"\nYou lost, the word was '{word_to_guess}'")

record_record(wins, losses)

print(f"New record update: wins: {wins}, losses: {losses}")