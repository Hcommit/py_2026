print(" Welcome to Mustafa central shopping mall ")
discount =0
total=0
items=int(input("Enter no of items purchased"))
for i in range(1,items+1):
    price= float(input(f"Enter price of item{i} - "))
    print(f"prince of item {i} : Rs {price}")
    total =total + price
if(total>100):
    discount=total*0.1
print("================================")
print(" Final bill ")
print("Total cost of items - Rs ", total)
print("Discount applied - Rs ",discount)
print(" The customer has to pay Rs - " ,total-discount)
print("=========================")
print("Happy shopping")