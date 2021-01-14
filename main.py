import random

lives = 0
comp_number = random.randint(1, 9)
print("The computer has chosen a number")


while lives < 6:
    user_number = int(input("Enter Your Number:"))

    if user_number < comp_number:
        print("Your Number is less than the computer's number")

    elif user_number > comp_number:
        print("Your Number is More than the computer Number")

    elif user_number == comp_number:
        print("Congratulations! You Win!")
        break

    lives += 1

if lives>5:
    print("Sorry, You lose :(")