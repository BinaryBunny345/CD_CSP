# CD, Conditionals Notes

# conditional

time = 1416
day = "Tuesday"

if time < 1200 and time > 500:
    print("Good Morning!")
    if day != "Saturday" or day != "Sunday":
        print("Are you ready for school?")
elif time < 1700:
    print("Good Afternoon!")
    if day != "Saturday" and day != "Sunday":
        print("How has school been?")
elif time < 2000:
    print("Good Evening!")
else:
    print("Good Night!")

print("Code is done")