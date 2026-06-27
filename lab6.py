""""
You're managing an ice cream parlour. Write a program that shows the menu, takes customer orders, 
Asks "Do you want to order more?" after each order and calculates total bill with 8% tax.

"""



def icecream_parlour():

    menu = {
        "vanilla": 30,
        "chocolate": 40,
        "strawberry": 35,
        "butterscotch": 45,
        "mango": 50
    }

    total = 0

    print("----- ICE CREAM MENU -----")

    for item, price in menu.items():
        print(item, ":", price)

    while True:

        choice = input("\nEnter ice cream flavor: ").lower()

        if choice in menu:

            total += menu[choice]
            print(f"{choice} added to order")

        else:
            print("Ice cream not available!")

        more = input("Do you want more ice cream? (yes/no): ").lower()

        if more != "yes":
            break

    discount = 0

    if total > 100:
        discount = total * 0.10

    final_bill = total - discount

    print("\n----- BILL -----")
    print("Total Bill :", total)
    print("Discount   :", discount)
    print("Final Bill :", final_bill)


icecream_parlour()