# CD, password strength checker assignment

# Ask user for password
# Check if password is long enough
# update length variable to True
# For letter in password:
    #if letter.isupper():
        #update uppercase variable to True
# .isslower()
# .isnumeric
# if letter in "!?@#$[]<>:"

characters = False
uppercase = False
lowercase = False
number = False
symbol = False
length = False 
requirements_met = 0

password = input("What is your password? ")

password_length = len(password)
if password_length >= 8:
    length = True
if password_length < 8:
    length = False   

for letter in password:
    if letter.isupper():
        uppercase = True
    if letter.islower():
        lowercase = True
    if letter.isnumeric():
        number = True
    if letter in "!?@#$&[]<>:":
        symbol = True

if length == True:
    requirements_met += 1
if uppercase == True:
    requirements_met += 1
if lowercase == True:
    requirements_met += 1
if number == True:
    requirements_met += 1
if symbol == True:
    requirements_met += 1

if requirements_met == 5:
    password_strength = "Strong"
elif requirements_met <= 4 and requirements_met >= 3:
    password_strength = "Moderate"
else:
    password_strength = "Weak"

print(f"Has at least 8 characters: {length}")
print(f"Has an uppercase letter: {uppercase}")
print(f"Has a lowercase letter: {lowercase}")
print(f"Has a number: {number}")
print(f"Has a symbol: {symbol}")

print(f"Your password strength is: {password_strength}")

if password_strength == "Strong":
    print("Good job, your password is strong.")
else:
    print("To make it Strong:")
    if length == False:
        print("    - Make your password at least 8 characters long")
    if uppercase == False:
        print("    - Add an uppercase letter")
    if lowercase == False:
        print("    - Add a lowercase letter")
    if number == False:
        print("    - Include a number")
    if symbol == False:
        print("    - It must contain a symbol")