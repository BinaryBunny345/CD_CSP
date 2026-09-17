# CD, your budget code assignment

while True:
    try:
        income =  float(input("What is your monthly income?: "))
        break
    except:
        print("Please enter a valid number for your income:")

while True:
    try:
        rent =  float(input("What is your monthly rent/mortgage?: "))
        break
    except:
        print("Please enter a valid number for your rent/mortgage:")

while True:
    try:
        utilities =  float(input("What is your monthly utilities?: "))
        break
    except:
        print("Please enter a valid number for your utilities:")

while True:
    try:
        groceries =  float(input("What is your monthly grocery expense?: "))
        break
    except:
        print("Please enter a valid number for your grocery expense:")

while True:
    try:
        transportation =  float(input("What is your monthly transportation expense?: "))
        break
    except:
        print("Please enter a valid number for your transportation expense:")

print(f"Your monthly rent/mortgage is ${rent:.2f} {int(rent/income*100)}%")
print(f"Your monthly utilities are ${utilities:.2f} {int(utilities/income*100)}%")
print(f"Your monthly grocery expense is ${groceries:.2f} {int(groceries/income*100)}%")
print(f"Your monthly transportation expense is ${transportation:.2f} {int(transportation/income*100)}%")