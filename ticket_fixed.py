# CD, Fixed Vibe Code

age = input("Enter your age: ")

try:
    age = int(age)
except:
    print("Invalid age.")
    exit()

if age < 0:
    print("Invalid age.")
    exit()

matinee = input("Is this a matinee? (yes/no): ").lower()

if age < 5:
    price = 0
elif age <= 12:
    price = 8
elif age < 65:
    price = 12
else:
    price = 9

if matinee == "yes":
    price = price - 3

if price < 0:
    price = 0

print(f"Ticket price: ${price:.2f}")