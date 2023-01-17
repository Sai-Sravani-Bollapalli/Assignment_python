user_input = int(input("Guess the lucky number !"))
lucky_num = 6
while (user_input != lucky_num):
    print("Wrong guess")
    continue
else: 
    print("Right guess")