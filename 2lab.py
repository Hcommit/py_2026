def icecreamparlour():

    menu = {
        "chocolate": 50,
        "vanilla": 45,
        "strawberry": 70,
        "mango": 80
    }

    print("WELCOME TO ICECREAM WORLD")
    print("========= MENU ==========")

    for item, price in menu.items():
        print(f"{item.capitalize()} - Rs {price}")

    total = 0

    while True:
        choice = input("Enter the flavour you want: ").lower()

        if choice in menu:
            total += menu[choice]
            print(f"{choice.capitalize()} added to your order")
        else:
            print("Invalid choice")

        more = input("Do you want to order more (yes/no): ").lower()
        if more != "yes":
            break

    tax = total * 0.08
    final_bill = total + tax

    print("\n\nFINAL BILL\n")
    print(f"Total cost of items: Rs {total}")
    print(f"Tax applied: Rs {tax:.2f}")
    print(f"\nFinal amount to be paid: Rs {final_bill:.2f}")


# Calling the function
icecreamparlour()