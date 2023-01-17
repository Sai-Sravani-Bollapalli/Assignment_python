s = "abcSdefPghijQkl"
c1 = c2 = 0
for i in s:
    if i.isupper():
        c1 += 1
    if i.islower():
        c2 +=1
print("No. of Uppercase characters:", c1, " ", "No. of Lowercase characters:", c2)