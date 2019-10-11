secret = 17

guess = int(input("Have a guess (between 1 and 30): "))

if guess == secret:
    print("you got it, congrats mate!  It's number 17.")
else:
    print("See. you failed again... The secret number is not " + str(guess))
