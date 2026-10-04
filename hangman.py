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
|    /|\\
|    / \\
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

with open("hangman.txt", "r") as file: