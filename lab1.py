""""
You are working as a software developer for "CoffeeKutira Restaurant". 
The restaurant manager has asked you to create a calculator program to help staff quickly calculate various
 bill-related operations for a single item during busy hours. 
 The program should allow staff to choose from 4 operations:
a.
Add - Calculate total bill (food cost + tax)
b.
Subtract - Calculate discount amount (original bill - discounted bill)
c.
Multiply - Calculate total for multiple identical orders
d.
Divide - Split bill among customers
"""

def add():
    food_cost = float(input("Enter total cost of food - "))
    tax = float(input("Enter tax - "))
    print("Total cost =", food_cost + tax)

def subtract():
    original_amount = float(input("Enter the original amount - "))
    discounted_bill = float(input("Enter the discounted bill paid - "))
    print("Discount given -", original_amount - discounted_bill)

def multiply():
    price = float(input("Cost of item - "))
    quantity = int(input("Total no of articles purchased - "))
    print("Total price to be paid -", price * quantity)

def divide():
    total_bill = float(input("Enter total bill - "))
    pax = int(input("Enter total no of people - "))

    if pax != 0:
        print("Share per person -", total_bill / pax)
    else:
        print("No of people cannot be zero")

import sys
print("Coffee Kutira Restaurant")
print("1.ADD--2.SUBTRACT--3.MULTIPLY--4.DIVIDE")

while True:
    choice = int(input("Enter your choice - "))

    if choice == 1:
        add()

    elif choice == 2:
        subtract()

    elif choice == 3:
        multiply()

    elif choice == 4:
        divide()

    else:
        print("Invalid choice")
        print("Exiting loop")
        sys.exit()
        