
def power(a, b):

    if b == 1:
        return a

    return a * power(a, b-1)


result = power(5, 2)
print(result)
