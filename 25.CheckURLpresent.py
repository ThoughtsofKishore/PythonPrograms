
import re

str1 = "ABCDEhttps://rahulshettyacademy.com/angularpractice/"

#http://urlrgex.com
str2 = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str1)

print(str2)
