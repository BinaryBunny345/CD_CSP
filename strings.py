# CD, Strings Notes

name = input("What is your name:").strip().capitalize()  

age = input('How old are you: ')
print(type(age))

print(age+age)

print(name + " " + "Davis")

#
sentence = "The quick brown fox jumped over the lazy dog."

print(sentence)
print(sentence.replace("dog", "monkey"))
print(len(name)) #<= gets the length of a string
print(f"Your name is {name} that is {len(name)} letters long. Your first initial is {name[0]} I think I will call you {name[0:5]}")