#list1=[1,2,3,2,4]
n = int(input("Enter no of items in the list: "))

list1 = []

for i in range(0, n):
    num = int(input(f"Enter the number at position {i+1} - "))
    list1.append(num)

if list1 == list1[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")