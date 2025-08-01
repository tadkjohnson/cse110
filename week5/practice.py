# # First, I'm going to set up an empty list called, friends.
# # Notice that I call it friends (with an s) not friend. This will help me
# # remember throughout my code that it is a list of potentially many friends
# # rather than a single friend.
# friends = []

# # This will be used in my loop to get the name of each friend that I want
# # to put in the list. I can start it will any value, as long as that value
# # is not "end", otherwise, it won't ever go into the loop I made to gather
# # the names.
# name = None

# while name != "end":
#     name = input("Type the name of a friend: ")

#     # Without this if statement, I would put "end" into my list as well
#     if name != "end":
#         friends.append(name)

# print()
# print("Your friends are:")

# # Now I'm going to loop through them each one at a time to display them.
# # Notice that the list is called "friends" (with an s) but as I go through
# # it I'm going to refer to each individual name as "friend" (no s)
# for friend in friends:
#     print(friend)
# # 

items = ['Apple', 'Banana', 'Cherry', 'Date']

# Display numbered menu starting from 1
for idx, item in enumerate(items, start=1):
    print(f"{idx}. {item}")

choice = input("Enter the item number: ").strip()

if choice.isdigit():
    index = int(choice) - 1  # Convert to zero-based index
    if 0 <= index < len(items):
        selected = items[index]
        print(f"You chose: {selected}")
    else:
        print("That number is out of range.")
else:
    print("That wasn't a valid number.")

