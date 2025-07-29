# stores a list of products in a cart with thier prices,     
# user be able to add, remove items,  
# prices listed w/ items in cart, along with total of all items 
# give user a menu  that indicates how to add/remove items, get total costs and quit program  


items_available = []

items_prices = []
items_price = ""

items_in_cart=[]


cart_wanted = []
new_item = ""
choice = ""

print("Welcome to the shopping cart")
print("To use, please ADD an item, REMOVE an item, VIEW your cart, TOTAL cost of cart, or QUIT")

while choice != "quit":
    choice = input("ADD/REMOVE/VIEW/TOTAL/QUIT? ").lower()

    if choice == "add":
        new_item = input("What do you want to buy? ")
        cart_wanted.append(new_item)
        items_price = float(input("How much is that item? "))
        items_prices.append(items_price)
        print(f"{new_item} added to the shopping cart")
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
             
    elif choice == "view":
        for i, item in enumerate(cart_wanted):
            print(f"{i+1}. {item} - ${items_prices[i]:.2f}")
    
    elif choice == "total":
        for i, item in enumerate(cart_wanted):
            print(f"{i+1}. {item} - ${items_prices[i]:.2f}")
        total = sum(items_prices)
        print(f"Your total cost ${total:.2f}")
  
  
    # elif choice == "shipping":
    #     shipping =input(f"Your total is ${total:.2f} do you want to ship it directly to you for {len(cart_wanted) * 25} or pick it up in person SHIP/PICK ").lower()
    #     if shipping == "ship":
    #         cart_wanted.append(shipping)
    #         items_prices.append(len(cart_wanted) * 100)         
    #     else:
    #         print("We will store it in a secure vault for your pick up, open hours from 730am- 930am")


    elif choice != "quit":
        print("invalid choice - please use ADD, REMOVE, VIEW, TOTAL, or QUIT.")
    
    else:
        print("Thanks for shopping where we over charge, under perform, ask people for a TIP")






