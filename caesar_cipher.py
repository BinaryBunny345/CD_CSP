# CD, Caesar Cipher assignment

# Notes:
# ord() function returns an integer representing the Unicode code point of a single character
# chr() function converts an integer into its corresponding Unicode character

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
shift = int(input("How many times would you like to shift: "))

def caesar_shift(message, shift):
    min_low = ord("a")
    max_low = ord("z")
    min_upp = ord("A")
    max_upp = ord("Z")
    new_message = ""

    for letter in message:
        if letter.isalpha():
            letterord = ord(letter)
            if shift < 0:
                if letter.isupper():
                    if letterord + shift < min_upp:
                        letterord += 26
                elif letter.islower():
                    if letterord + shift < min_low:
                        letterord += 26

            if shift > 0:
                if letter.isupper():
                    if letterord + shift > max_upp:
                        letterord -= 26
                elif letter.islower():
                    if letterord + shift > max_low:
                        letterord -= 26

            letterord += shift

            new_message = new_message + chr(letterord)
        else:
            new_message = new_message + letter

    return new_message

output_is = ""

if suggested_output == "D":
    shift *= -1
    output_is = "decrypted"

if suggested_output == "E":
    output_is = "encrypted"

print(f"Your {output_is} message is: " + caesar_shift(message, shift))
