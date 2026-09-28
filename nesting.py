# CD, Nesting notes

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



siblings = ["Alex", "Katie", "Cassandra", "Billy"]
count = 1
if len(siblings) > 0:
    while count <= len(siblings):
        print(f"{count}. {siblings[count-1]}")
        count += 1
else:
    print("There are no siblings.")