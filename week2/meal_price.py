import math

#added senior citizens discount
#added several tip suggestion amounts
#added drink costs that vary for person

cost_child = float(input("what is the price of the child meal? $"))
cost_adult = float(input("what is the price of the adult meal? $"))
cost_senior = float(cost_adult - (cost_adult * .25))

num_child = int(input("how many child meals were purchased? "))
num_adult = int(input("how many adult meals were purchased? "))
num_senior = int(input("how many senior meals were purchased? "))

tally_child = cost_child * num_child
tally_adult = cost_adult * num_adult 
tally_senior = cost_senior * num_senior

drink_child = int(input("how many child drinks were purchased? "))
drink_adult = int(input("how many adult drinks were purchased? "))
drink_senior = int(input("how many senior drinks were purchased? "))

drink_cost_c = 1
drink_cost_a = 2.50
drink_cost_s = 1.50

drinks_total = float((drink_child * drink_cost_c) + (drink_cost_a * drink_adult) + (drink_cost_s * drink_senior))

subtotal = float(tally_child + tally_adult + tally_senior + drinks_total)
tax_rate = float(input("what is the tax rate (entered as a percentage)"))
print()
print()
tax_amount = float(math.ceil(subtotal * tax_rate)/100)
print(f"The total before Tax and Tip is ${subtotal:.2f}")
print(f"Tax charge ${tax_amount:.2f}")
print()
print(f"suggested tip 15% {subtotal * .15:.2f}, which would make your total ${subtotal + (subtotal * .15):.2f}")
print(f"suggested tip 20% {subtotal * .2:.2f}, which would make your total ${subtotal + (subtotal * .2):.2f}")
print(f"suggested tip 25% {subtotal * .25:.2f}, which would make your total ${subtotal + (subtotal * .25):.2f}")
print()
print()
total_bill = float(subtotal + tax_amount)
print(f"Total bill with taxes ${subtotal + tax_amount:.2f}")
print()
customers_tip = float(input("How much do you want to tip? " ))
total_cost = float(customers_tip + total_bill)
print(f"Your total bill with tip was ${total_bill:.2f}")
customers_payment = float(input("how much did you pay $"))
print(f"Your change is ${customers_payment - total_cost:.2f}")

