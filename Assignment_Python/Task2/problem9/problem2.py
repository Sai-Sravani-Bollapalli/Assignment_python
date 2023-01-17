number = input("Guess the lucky number")
answer = "6"
while number != answer: 
    reguess = input("want to guess again: ")
    if reguess == answer:
        print("Right guess") 
        break   
    if reguess != "no":
        continue
    else:
        break
else:
        print("Right guess")


