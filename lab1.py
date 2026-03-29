print("Coffee Kutira Restuarant")
print("1.ADD--2.SUBSTRACT--3.MULTIPLY--4.DEVIDE")

while True:
    choice=int(input("Enter your choice - "))
    if(choice==1):
        food_cost=float(input("Enter total cost of food - "))
        tax=float(input("Enter tax - "))
        print("Total cost = ",food_cost+tax)
    elif(choice==2):
        original_amount=float(input("Enter the orignal amount="))
        discounted_bill=float(input("Enter the discounted bill payed - "))
        print("Discount given - ",original_amount-discounted_bill)
    elif(choice==3):
        price=float(input("Cost of item - "))
        quantity=int(input("total no of article purchased - "))
        total_price=price*quantity
        print("Total price to be payed - ",total_price)
    elif(choice==4):
        total_bill=float(input("Enter total bill - "))
        pax=int(input("Enter total no of poeple - "))
        if(pax!=0):
            share=total_bill/pax
            print("Share per person - ",share)
        else:
            print("No of poeple cannot be zero")
else:
    print("Invalid choice")