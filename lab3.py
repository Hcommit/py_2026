print(" HI , WELCOME TO Gary Icecream Parlour ")
print("++++++++++++         MENU        +++++++++++++++")
print(" 1 . VANILLA SCOOP = 40 Rs ")
print(" 2 . CHOCOLATE SCOOP = 50 Rs ")
print(" 3 . STRAWBERRY SCOOP = 50 Rs ")
print(" 4 . MANGO SCOOP = 60 Rs ")

final_bill = 0
order_more = "yes"

while order_more == "yes":
    choice = int(input("Enter your preferred icecream (1-4): "))
    quantity = int(input("Enter number of scoops: "))
    
    if choice == 1:
        print(f"You want {quantity} x Vanilla")
        total_bill = 40 * quantity
    elif choice == 2:
        print(f"You want {quantity} x Chocolate")
        total_bill = 50 * quantity
    elif choice == 3:
        print(f"You want {quantity} x Strawberry")
        total_bill = 50 * quantity
    elif choice == 4:
        print(f"You want {quantity} x Mango")
        total_bill = 60 * quantity
    else:
        print("INVALID CHOICE - choose 1 to 4 only")
        total_bill = 0   # avoid error

    final_bill += total_bill
    
    order_more = input("Add more? (yes/no): ").lower()

print("+++++++ FINAL BILL +++++++++++")
print("Cost of icecream =", final_bill)

tax = final_bill * 0.08
print("8% tax =", tax)

print("TOTAL AMOUNT TO BE PAID =", final_bill + tax)
print("ENJOY your sweet treat!")