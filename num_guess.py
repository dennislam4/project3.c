# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 6/27/2022
# Description: Asks user for an integer that the player will try to guess. If the player
#              guess is higher than the target integer, the program prints "too high" and
#              vice versa. The program repeats until the correct integer is guessed. The
#              program will then print the amount of tries that it took.

integer = int(input("Enter the integer for the player to guess.\n"))
print("Enter your guess.")
tries = 1
while True:
    guess = input()
    guess = int(guess)
    if guess < integer:
        tries = tries + 1
        print("Too low - try again:")
    elif guess > integer:
        tries = tries + 1
        print("Too high - try again:")
    else:
        print("You guessed it in", tries, "tries.")
        break



