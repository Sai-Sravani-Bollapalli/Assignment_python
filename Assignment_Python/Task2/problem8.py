user_input = input("Enter something:")
c1 = c2 = 0
for i in user_input:
    if i.isdigit():
        c1 += 1
    elif i.isalpha():
        c2 += 1
print("Letters", c2, "     ", "Digits", c1)

