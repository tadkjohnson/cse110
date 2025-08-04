# ran some diff lists,  added soem commentary, not sure what else i can add to make it have character or expand on the original idea.




items_prices = []
items_price = ""

# items_in_cart=[]

choice_numbers = ['add', 'remove', 'view', 'total', 'quit']
cart_wanted = []
new_item = ""
choice = ""
 

print("Welcome to the shopping cart")
print("To use, please add an item, remove an item, view your cart, total cost of cart, or quit")


 
 
#start

while choice != 5:
    print("\n1 - ADD \n2 - REMOVE \n3 - VIEW \n4 - TOTAL \n5 - QUIT")
    choice = int(input("Please choose 1-5 "))
    if choice == 1:
        new_item = input("What do you want to buy? ")
        cart_wanted.append(new_item)
        items_price = float(input("How much is that item? "))
        items_prices.append(items_price)
        print(f"{new_item} added to the shopping cart")
#remove     
    elif choice == 2:
        if len(cart_wanted) == 0:
            print("Your cart is empty")
        else:
            # len(cart_wanted) > 0:
            print("Your current items in the cart")
            for i, item in enumerate(cart_wanted):
                print(f"{i+1}. {item} - ${items_prices[i]:.2f}")
            remove_want = int(input("What item number do you want to remove? "))
            remove_i = remove_want - 1
            
            if 0 <= remove_i < len(cart_wanted):
                removed_item = cart_wanted.pop(remove_i)
                items_prices.pop(remove_i)
                print(f"{removed_item} has been removed from your cart.")
            else:
                print("Did you mistype or choose the wrong entry?")

      
             
##view             
    elif choice == 3:
        for i, item in enumerate(cart_wanted):
            print(f"{i+1}. {item} - ${items_prices[i]:.2f}")
#total    
    elif choice == 4:
        for i, item in enumerate(cart_wanted):
            print(f"{i+1}. {item} - ${items_prices[i]:.2f}")
        total = sum(items_prices)
        print(f"Your total cost ${total:.2f}")
  

#quit
    elif choice != 5:
        print("invalid choice - please use 1 - ADD \n2 - REMOVE \n3 -VIEW \n4- TOTAL \n5 - QUIT \n? ")
    else:
        print("Thanks for shopping where we over charge, under perform, ask people for a TIP")#






