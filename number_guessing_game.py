# CD, number guessing game assignment

import random

random_number = random.randint(1,100)

print("Hello, welcome to Cora's Guessing Game. You have six tries to guess the correct number between 1-100.....READY SET GO!")

guess_number = 1

while guess_number <= 6:
    
    while True:
        try:
            guess = int(input(f"What is your guess #{guess_number}? "))
            break
        except:
            print("Please enter a number for your guess.")

    if guess == random_number:
        print(f"Correct! You got the answer in {guess_number} tries! ")
        break
    elif guess < random_number:
        print("Too low!")
    else:
        print("Too high!")
    guess_number += 1

if guess_number > 6:
    print(f"Awwww TOO BAD SO SAD, you're out of guesses. The correct answer was {random_number}!")