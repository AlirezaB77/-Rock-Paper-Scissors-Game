import random

def user_choice():
    print("\n 1.Rock \n 2.Paper \n 3.Scissors")
    user_select = int(input("Enter the number : "))
    while user_select > 3 or user_select < 1:
        print("Please select Number 1, 2 or 3")
        user_select = int(input("Enter the number : "))
    item = {1: 'Rock', 2: "Paper", 3: "Scissors"}
    return item[user_select]

def system_choice():
    return random.choice(['Rock', "Paper", "Scissors"])

user_win = [['Rock', "Scissors"], ["Scissors", "Paper"], ["Paper", 'Rock']]

def detect_winner(user_choice, system_choice):
    if system_choice == user_choice:
        return "Draw"
    elif [user_choice, system_choice] in user_win:
        return "User wins"
    else:
        return "System wins"

def play_game():
    user_input = user_choice()
    sys_input = system_choice()
    print(f'You chose {user_input} and system chose {sys_input}')
    game_result = detect_winner(user_input, sys_input)
    print(game_result)

if __name__ == "__main__":
    play_game()