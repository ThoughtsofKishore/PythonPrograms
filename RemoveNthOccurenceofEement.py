

l1 = ["geeks", "for", "geeks", "and", "geeks", "or", "geeks", "kishore", "geeks"]

n = int(input("Enter the nth[1-5] number geek you want to remove from list:"))

count = 0

for i in range(len(l1)):
    if l1[i] == "geeks":
        count += 1
        if count == n:
            l1.pop(i)
            break

print(l1)

