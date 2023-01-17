counter = 1
answer = "6"
while counter <= 5:
    print("Nunber of Guessings: ", counter)
    counter +=1
    number = input("Guess the lucky number: ")
    if number == answer:
        print("Good guess!")
        break
    elif number != answer:
        print("Try again!")
else:
    print("Sorry but that was not very successful")
         