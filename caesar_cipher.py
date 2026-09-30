# CD, Caesar Cipher assignment

#ENCRYPTING
# FOR LOOP
# Looking at suggested outputs
# Start without function
# Start with letter 1 and all 3 variables
# Build a working loop that will print out every single letter your user 
# Build conditional inside of loop to see if specific letter is a character, and if it convert to number, incerease by whatever number your user gave you, convert it back to letter, print it
# Needs to have variable where I save all variables as I change or don't change them ONLY LETTERS
# If pass end of the alphabet check before converting it back to character do SUBTRACTION to take us back to the begining of the alphabet

#DECRYPTING
# Number given by user HAS TO BE NEGATIVE


# NEEDED INFORMATION (ALL ONE LINE)
#    number += 2
#    print(f"The letter {lower_start} is the number {ord(lower_start)}")
#    print(f"The letter {chr(number)} is the {number}")
#    print(f"The letter {lower_end} is the number {ord(lower_end)}")


suggested_output = input("Would you like to (E)ncrypt or (D)ecrypt a message? ")
message = input("What is your message: ")
shift = input("How many times would you like to shift: ")

for letter in message:
    if letter.isalpha():
        print(message)
    elif letter.isnumeric():
        print(f"Please print a valid message ")
