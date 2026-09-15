# CD, hello user

while True:
    name = input("What is your name?: ").strip().capitalize()
    if name.isnumeric():
        print("That is a number not a name!")
    else:
        break

print(f"Hello, {name} what are you doing today?!")