
s1 = "kishore lalwani"

# removing all the spaces from string so that output should not be a space in case user provides two spaces between words.
s2 = s1.replace(" ", "")

# Empty Dictionary
found_dict = {}

# for iterating the string
for ch in s2:
    # it will break the loop once we get the repeated char which is present in the dictionary
    if ch in found_dict:
        print(ch)
        break

    # it will update the char in dictionary
    else:
        found_dict[ch] = 0



#----------------------------------------------------------------------------------------------------------




#Function for finding first repeating character


def FirstRepatingCharInString(str1):

    str2=str1.replace(" ", "")
    found_dict1 = {}

    for ch in str2:

        if ch in found_dict1:
            return ch

        else:
            found_dict1[ch] = 0


print(FirstRepatingCharInString("kishore lalwani"))


