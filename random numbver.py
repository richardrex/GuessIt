import random
import sys
import time


class bcolors:
    OKBLUE = '\033[94m'


name = input(bcolors.OKBLUE + "Please write your name: ")


def main_menu():
    print("\nHello, ", name.title(), ". Welcome to Guess the Number Game")
    time.sleep(3)
    selection()


def selection():
    print("\nTo start game press 1.\nTo exit press 2")
    menu_selection = input("Please select option: ")
    try:
        menu_selection_int = int(menu_selection)
        print("You have selected: ", menu_selection_int)
    except:
        print("Invalid input")
        selection()
    if menu_selection_int == 1:
        print("You have selected option 1. Have Fun!")
        game()
    elif menu_selection_int == 2:
        play_quit()


def play_quit():
    sys.exit("""Thank you for Playing!
  Hope u enjoyed it 
  Bye!""")


def game():
    k = 0
    while k == 0:
        flag = True
        while flag:
            num = input("Enter your upper bound: ")

            if num.isdigit():
                print("All correct, let's play")
                num = int(num)
                flag = False
            else:
                print("Invalid input, Try again")

        guessing_number = random.randint(0, num)

        guess = None
        count = 1

        while guess != guessing_number:
            guess = input("Please guess number between 0 amd " + str(num) + ": ")
            if guess.isdigit():
                guess = int(guess)

            if guess == guessing_number:
                print("You Win!")
                print("Wanna play again? Y/N")
                b = input()
                if b == "Y" or b == "y":
                    print("Great! Let's go!")
                    game()
                elif b == "N" or b == "n":
                    print("Ow See u next time(")
                    time.sleep(1)
                    play_quit()

            else:
                if guess > guessing_number:
                    print("Lost! Your number is too big.Wanna play again? Y/N")
                    a = input()
                    if a == "N" or a == "n":
                        print("Number was ", str(guess))
                        k = 1
                        play_quit()
                    elif a == "Y" or a == "y":
                        print("Great try again!")
                    else:
                        print("Sorry, Wrong input!")
                if guess < guessing_number:
                    print("Lost! Your namber is too small. Wanna play again? y/N")
                    a = input()
                    if a == "N" or a == "n":
                        print("Number was ", str(guess))
                        k = 1
                        play_quit()
                    elif a == "Y" or a == "y":
                        print("Great try again!")

                    else:
                        print("Sorry, Wrong input!")


main_menu()
