# added names, location, and friends to personalize it. instead of leaving it some random "someone someplace didn't happen event"



print("Please enter the following information:")
first_name = input("what is your first name? ")
last_name = input("what is your last name? ")
location = input("where do you live? ")
task = input("What is a chore you hate to do? ")
friend_name = input("name one of your friends: ")
exclamation = input ("What is something to exclaim? ")
adjective = input ("Any adjective: ")
animal = input ("Favorite animal: ")
verb_1 = input ("Any verb: ")
verb_2 = input ("Any other verb: ")
verb_3 = input ("And a different verb: ")
activity = input ("what is your hobby? ")

print("\n")
print("\n")
print("A clever story")
print("\n")
print("-" * 50)
story = f"""When I, {first_name.capitalize()} {last_name.capitalize()}, returned to {location} last weekend to do some {task}.  I called {friend_name.capitalize()} in hopes to {activity}. 
    But instead ended up telling {friend_name.capitalize()} the following life experience."""
print(story)
print("\n")
story = f"""The other day, I was really in trouble. It all started when I saw a very
    {adjective.lower()} {animal.lower()} {verb_1} down the hallway. {exclamation.title()}! I yelled. But all
    I could think to do was to {verb_2} over and over. Miraculously,
    that caused it to stop, but not before it tried to {verb_3} 
    right in front of my family."""
print(story)
print("-" * 50)

