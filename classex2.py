n = int(input("Enter no of items in the list: "))

list1 = []
list2 = []

print("\n taking list1 input")
for i in range(0, n):
    num = int(input(f"Enter the number at position {i+1} in list1 - "))
    list1.append(num)

print("\n\n Taking list 2 input")
for i in range(0, n):
    num = int(input(f"Enter the number at position {i+1} in list2 - "))
    list2.append(num)
if list1==list2:
    print("Lists are equal")
else:
    print("Not equal")