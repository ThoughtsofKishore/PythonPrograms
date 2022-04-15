

def EnterAge(age):

    if age<0:
        raise ValueError("Age should be always positive")

    elif age % 2 == 0:
        print("Age is Even")

    else:
        print("Age is odd")


try:
    age=-2
    EnterAge(age)
except ValueError:
    print("In Exception block. Enter positive value of age")
else:
    print("Program is executed without exception")
finally:
    print("Finally block executed")