import random

game = True
# chances = 5

random_ans = random.randint(1,10)

user_choice = int(input("Plz choose ur difficulty\n 1.Easy\n 2.Medium\n 3.Hard\n "))

if user_choice == 1:
    chances = 5
elif user_choice == 2:
    chances = 3
else:
    chances = 1
if user_choice == 1:
    print(f"You have {chances} chance")
else:
    print(f"You have {chances} chances")

while game:
    user_ans = int(input("Plz enter a number between 1 to 9 "))


    if user_ans == random_ans:
        print("You guessed it right!")
        break;
    else:
        chances = chances-1
        if user_ans > random_ans:
            print(f"You guessed it too high! You have {chances} chances left.")
        else:
            if chances == 0:
                print(f"The correct answer was {random_ans}, Better luck next time! :(")
                game = False
            else:
                print(f"You guessed it too low! You have {chances} chances left.")

        # print(f"Nope, that's wrong! You have {chances} chances left!")
