class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign


def read_players():
    first_player_name = input(f"Player 1 name: ")
    second_player_name = input(f"Player 2 name: ")

    while True:
        first_player_sign = input(f"{first_player_name} you would like to play with X or O?").upper()
        if first_player_sign == "X" or first_player_sign == "O":
            break

    second_player_sign = "O" if first_player_sign == "X" else "X"


    return first_player_name, second_player_name

first_player, second_player = read_players()
