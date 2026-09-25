# CD, Loops Notes
import random

count = 1

while count <= 10:
    print(count)
    count += 1

ducks = 1
goose = random.randint(1,11)

while True:
    if ducks == goose:
        break
    print("Duck....")
    ducks += 1             #ducks = ducks + 1
print("GOOSE!!!!!")

# Complex Data Type = Holds other data in it
family = ["Cooper", "Whitaker", "Jennifer", "Jared"]
print(family[3])
#Adding to a list
family.append("Viola") # <= adds the item to the end of the list
family.insert(2, "Cooper")
print(family)
# Remove item from a list
family.pop() # <= if no number given pop removes the last item
print(family)


#print each item in list
for family in families:
    print(family)

# For loops
for num in range(1,25):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)