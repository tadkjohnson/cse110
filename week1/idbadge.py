# needs first, last, email, phone, job title, and an id number  
# show info in order of  1st line last, first   2nd line job title   3rd line  id   space   line email and line phone number
# last name all caps,  email all lower case, jobtitle first letter cap.  

print("Please enter the following information:")
last_name = input ("What is your last name? ")
first_name = input ("What is your first name? ")
email = input ("What is your email address? ")
title = input ("What is your job title? ")
idn = input ("What is your ID Number? ")
phone_number = input ("What is your phone Number? ")

# print() or ("\n")
print("The ID Card is:")
print("\n")
print("-" * 50)
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(f"{title.title()}")
print(f"ID: {idn}")
print()
print(f"{email.lower()}")
print(f"{phone_number}")
print("-" * 50)



