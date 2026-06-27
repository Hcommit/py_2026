""""
Develop a function named DivExp which takes TWO parameters a, b and returns a value c (c=a/b). 
Write a suitable assertion for a>0 in function DivExp and raise an exception for when b=0. 
Develop a suitable program which reads two values from the console and calls a function DivExp
"""



def DivExp(a,b):
    assert a>0,"Enter a positive value"
    if(b==0):
        raise ZeroDivisionError("Division with zero not possible")
    c = a/b
    return c
try:
    a = float(input("Enter the value of numerator "))
    b = float(input("Enter the value of denominator "))
    print("The result is ",DivExp(a,b))
except AssertionError as s:
    print("There is an assertion error , ",s)
except ZeroDivisionError as z:
    print("There is a zero division error ,",z)
except ValueError:
    print("Input not in proper format")