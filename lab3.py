""""
You're working as a cashier at a shopping mall. 
Write a program that asks customers how many items they want to buy. For each item, 
input the price, Calculate total bill and apply 10% discount if total > Rs. 100. 
Display itemized receipt
"""


print(" Welcome to Mustafa central shopping mall ")

discount =0

total=0
items=int(input("Enter no of items purchased"))
price_lst = []
for i in range(items):
    price= float(input(f"Enter price of item{i+1} - "))
    price_lst.append(price)
    total =total + price
    
if(total>100):
    discount=total*0.1
print("================================")
print("\n")
for j in range(items):
    print(f" item {j+1} - Rs {price_lst[j]}")
print(" Final bill ")
print("Total cost of items - Rs ", total)
print("Discount applied - Rs ",discount)
print(" The customer has to pay Rs - " ,total-discount)
print("=========================")
print("Happy shopping")