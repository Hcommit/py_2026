def divExp(a,b):
    assert a>0,"Enter a positve number "
    if(b==0):
        raise ZeroDivisionError ("Division with zero not possible")
    c=a/b
    return c
try:
    a=float(input("Enter the first number - "))
    b=float(input("Enter the second number - "))
    print("The result is ",divExp(a,b))
except AssertionError as s:
    print("This is an assertion error : ",s)
except ZeroDivisionError as z :
    print("There is a zero division error : ",z)
except ValueError:
    print("number is not in proper format :")
    print("Enter a number ")

