""""
Develop Student Grade Tracker: Accept multiple students’ names and marks. 
Store them in a list of tuples or dictionaries. Display summary reports (average, topper, etc.).

"""


students = []
total = 0
n = int(input("Enter number of students: "))

for i in range(n):

    print(f"\nEnter details of Student {i+1}")

    name = input("Enter name: ")
    marks = float(input("Enter marks: "))

    student = { "name": name, "marks": marks}
    students.append(student)
    total += marks


topper = students[0]

print("\n----- STUDENT DETAILS -----")

for j in range(n):

    print(students[j])



avg = total / n

for i in students:

    if i["marks"] > topper["marks"]:
        topper = i

print("\n----- SUMMARY REPORT -----")
print("Total Marks =", total)
print("Average Marks =", avg)
print("Topper =", topper["name"])
print("Topper Marks =", topper["marks"])