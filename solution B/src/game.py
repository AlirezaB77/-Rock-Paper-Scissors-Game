import random

class RockPaperScissors:
    def __init__(self) -> None:
        self.choise = {1: 'Rock', 2: "Paper", 3: "Scissors"}
        self.user_win_conditions = [['Rock', "Scissors"], ["Scissors", "Paper"], ["Paper", 'Rock']]

    def user_choice(self):
        while True:
            try:
                print("\n 1.Rock \n 2.Paper \n 3.Scissors")
                user_select = int(input("Enter the number : "))
                if 1 <= user_select <= 3:
                    user_select = self.choise[user_select]
                    return user_select
                else:
                    print("Please select Number 1, 2 or 3")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def system_choice(self):
        return random.choice(['Rock', "Paper", "Scissors"])

    def detect_winner(self,user_choice, system_choice):
        user_win = [['Rock', "Scissors"], ["Scissors", "Paper"], ["Paper", 'Rock']]
        if system_choice == user_choice:
            return "Draw"
        elif [user_choice, system_choice] in self.user_win_conditions:
            return "User wins"
        else:
            return "System wins"

    def play_game(self):
        user_input = self.user_choice()
        sys_input = self.system_choice()
        print(f'You chose {user_input} and system chose {sys_input}')
        game_result = self.detect_winner(user_input, sys_input)
        print(game_result)

if __name__ == "__main__":
    game = RockPaperScissors()
    game.play_game()