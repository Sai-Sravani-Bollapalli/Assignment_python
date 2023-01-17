option = int(input("Enter any number between (1-5):"))

if (option == 1):
    num1 = int(input("Enter a value:"))
    num2 = int(input("Enter a value:"))
    add = num1 + num2
    if(add >= 0):
        print("Addition of two values:", add )
    else:
        print("NEGATIVE")

elif (option == 2):
    num1 = int(input("Enter a value:"))
    num2 = int(input("Enter a value:"))
    sub = num1 - num2
    if(sub >= 0):
        print("Subtraction of two values:", sub)
    else:
        print("NEGATIVE")

elif (option == 3):
    num1 = int(input("Enter a value:"))
    num2 = int(input("Enter a value:"))
    div = num1 / num2
    if(div >= 0):
        print("Division of two values:", div)
    else:
        print("NEGATIVE")

elif (option == 4):
    num1 = int(input("Enter a value:"))
    num2 = int(input("Enter a value:"))
    mul = num1 * num2
    if(mul >= 0):
        print("Multiplication of two values:", mul)
    else:
        print("NEGATIVE")
    
elif (option == 5):
    mul_num = [int(mul_num) for mul_num in input("Enter two or more values: ").split(",")]
    avg = sum(mul_num) / len(mul_num)
    if(avg >= 0):
        print("Average of the numbers entered:", avg)
    else:
        print("NEGATIVE")
