import random

MOVES = ['Rock', 'Paper', 'Scissor']

user_score = 0
comp_score = 0

comp_choice = random.randint(0, 2)

while user_score < 3 and comp_score < 3:
    user_choice = int(input("Enter your move: 1.Rock 2.Paper 3.Scissor "))
    user_choice = user_choice-1

    if user_choice not in [0, 1, 2]:
        print("Invalid choice. Please enter a number between 1 and 3.")
        exit()

    if (user_choice == 0 and comp_choice == 2 or user_choice == 1 and comp_choice == 0 or user_choice == 2 and
            comp_choice == 1):
        user_score += 1
        print(f"You win! Computer choice: {MOVES[comp_choice]} ")
        print(f"Current Scores: User: {user_score}     Computer: {comp_score}")
    elif (user_choice == 0 and comp_choice == 1 or user_choice == 1 and comp_choice == 2 or user_choice == 2 and
          comp_choice == 0):
        comp_score += 1
        print(f"You lose! Computer choice: {MOVES[comp_choice]}")
        print(f"Current Scores: User: {user_score}     Computer: {comp_score}")
    else:
        print("It's a tie!")
    comp_choice = random.randint(0, 2)
    print(" ")

if user_score == 3:
    print(f"Game End! Winner is User!")
else:
    print(f"Game End! Winner is Computer!")
