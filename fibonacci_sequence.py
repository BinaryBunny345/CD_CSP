# Fibonacci Sequence Program

while True:
    user_input = input("How many Fibonacci numbers do you want to show? Enter a whole number from 1 to 20: ")

    try:
        count = int(user_input)
    except ValueError:
        print("You need to type a whole number. Please try again.")
        continue

    if count < 1 or count > 20:
        print("Please stay in the range of 1 to 20. Please try again.")
        continue

    fibonacci = []
    a, b = 0, 1

    for _ in range(count):
        fibonacci.append(a)
        a, b = b, a + b

    print(" ".join(str(number) for number in fibonacci))
    break
