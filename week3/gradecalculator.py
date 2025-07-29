grade = int(input("What is your grade percent? "))

if grade >= 93:
    letter = "A"
elif grade >= 90:
    letter = "A-"
elif grade >= 87:
    letter = "B+"
elif grade >= 83:
    letter = "B"
elif grade >= 80:
    letter = "B-"
elif grade >= 77:
    letter = "C+"
elif grade >= 73:
    letter = "C"
elif grade >= 70:
    letter = "C-"
elif grade >= 67:
    letter = "D+"
elif grade >= 63:
    letter = "D"
elif grade >= 60:
    letter = "D-"
else: 
    letter = "F"

print("your grade is a " + (letter))
print (f"your grade is a {letter}")

if grade >= 70:
    print ("congrates you passed the course")
else:
    print("You will need to repeat this course, please request a tutor if you have questions")

grade % 10
print (f"{grade}")




