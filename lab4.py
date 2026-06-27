"""""
Develop a program that uses class Student which prompts the user to enter 
marks in three subjects and calculates total marks, percentage and 
displays the score card details. 
[Hint: Use list to store the marks in three subjects and total marks. 
 Use __init__() method to initialize name, 
 USN and the lists to store marks and total, Use getMarks() 
 method to read marks into the list, and display () method to display the score card details.]
"""""


class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.usn = input("Enter USN: ")
        self.marks = []

    def getMarks(self):
        for i in range(3):
            mark = float(input(f"Enter marks for Subject {i+1} : "))
            self.marks.append(mark)

    def display(self):
        total = sum(self.marks)
        percentage = total / 3

        print("\n----- SCORE CARD -----")
        print("Name :", self.name)
        print("USN :", self.usn)
        print("Marks :", self.marks)
        print("Total :", total)
        print("Percentage :", round(percentage, 2), "%")


s = Student()
s.getMarks()
s.display()