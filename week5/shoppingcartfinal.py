# stores a list of products in a cart with thier prices,     
# user be able to add, remove items,  
# prices listed w/ items in cart, along with total of all items 
# give user a menu  that indicates how to add/remove items, get total costs and quit program  


items_available = []

items_prices = []
items_price = ""

items_in_cart=[]

# choice_numbers = ['add', 'remove', 'view', 'total', 'quit']
cart_wanted = []
new_item = ""
choice = ""
 

print("Welcome to the shopping cart")
print("To use, please add an item, remove an item, view your cart, total cost of cart, or quit")
print("1 - ADD \n2 - REMOVE \n3 - VIEW \n4 - TOTAL \n5 - QUIT")
first_choice = input("please choose 1-5 ")
# choice
if first_choice == "1":
    choice = "add"
elif first_choice == "2":
    choice = "remove"
elif first_choice == "3":
    choice = "view"
elif first_choice == "4":
    choice = "total"
else:
    first_choice == "5"
    choice = "quit"

print (choice)
#start

# while choice != "quit":
#     choice = input("ADD/REMOVE/VIEW/TOTAL/QUIT? ").lower()
#add
    if choice == "add":
        new_item = input("What do you want to buy? ")
        cart_wanted.append(new_item)
        items_price = float(input("How much is that item? "))
        items_prices.append(items_price)
        print(f"{new_item} added to the shopping cart")
#remove     
    elif choice == "remove":
        if len(cart_wanted) == 0:
            print("Your cart is empty")
        else:
            print("Your current items in the cart")            
            for i, item in enumerate(cart_wanted):
                print(f"{i+1}. {item} - ${items_prices[i]:.2f}")
            
            remove_it = input("what do you want to remove? ")
            if remove_it in cart_wanted:
                index = cart_wanted.index(remove_it)
                cart_wanted.pop(index)
                items_prices.pop(index)
                print(f"{remove_it} has been removed from your cart.")
            else:
                print("did you mistype or choose the wrong entry?")
             
#view             
    elif choice == "view":
        for i, item in enumerate(cart_wanted):
            print(f"{i+1}. {item} - ${items_prices[i]:.2f}")
#total    
    elif choice == "total":
        for i, item in enumerate(cart_wanted):
            print(f"{i+1}. {item} - ${items_prices[i]:.2f}")
        total = sum(items_prices)
        print(f"Your total cost ${total:.2f}")
  

#quit
    elif choice != "quit":
        print("invalid choice - please use 1 - ADD \n2 - REMOVE \n3 -VIEW \n4- TOTAL \n5 - QUIT \n? ")
    
    else:
        print("Thanks for shopping where we over charge, under perform, ask people for a TIP")






