class Student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.usn = input("Enter student USN: ")
        self.marksList = []   # To store marks of 3 subjects
        self.totalList = []   # To store total marks
        self.totalMarks = 0
        self.percentage = 0.0

    def getMarks(self):
        print("\nEnter marks for 3 subjects:")
        for i in range(1, 4):
            mark = float(input("Enter mark for subject " + str(i) + ": "))
            self.marksList.append(mark)

        self.totalMarks = sum(self.marksList)
        self.totalList.append(self.totalMarks)
        self.percentage = self.totalMarks / 3

    def display(self):
        print("\n------ STUDENT SCORE CARD ------")
        print("Name:", self.name)
        print("USN:", self.usn)
        print("Marks in 3 subjects:", self.marksList)
        print("Total Marks:", self.totalList[0])
        print("Percentage:", round(self.percentage, 2), "%")
        print("--------------------------------")


# Create object and call methods
student1 = Student()
student1.getMarks()
student1.display()