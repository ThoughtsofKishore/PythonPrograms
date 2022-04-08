
import re

str1 = "welcome"

str2 = re.compile("[~!@#$%^&*()}{;:',./<>?|]")


if str2.search(str1) == None:
    print("No special Char")
else:
    print("Special Character present")
