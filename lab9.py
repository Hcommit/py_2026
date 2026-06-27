""""
You are developing multiplicationTable.py for a primary school teacher 
who wants to generate a multiplication table for numbers up to N. 
Develop a program that creates an NxN Multiplication table taking the value N
 through command line arguments and it should write multiplication table to the Excel spreadsheet.

"""


import sys
from openpyxl import Workbook

# Check if user provided N as command-line argument
if len(sys.argv) != 2:
    print("Usage: python multiplicationTable.py N")
    sys.exit(1)

# Read N from command-line
n = int(sys.argv[1])

# Create a new workbook and select the active sheet
wb = Workbook()
ws = wb.active
ws.title = f"Multiplication Table"

# Fill multiplication table
for i in range(1, n + 1):
    for j in range(1, n + 1):
        ws.cell(row=i, column=j, value=i*j)

# Save workbook to Excel file
fileName = f"MultiplicationTable.xlsx"
wb.save(fileName)
print(f"Multiplication table saved to {fileName}")