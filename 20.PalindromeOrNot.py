
str1 = input("Enter any string: ")

str2 = str1.lower()

if str2 == str2[::-1]:
    print("{} is a Palindrome".format(str1))
else:
    print("{} is not a Palindrome".format(str1))
