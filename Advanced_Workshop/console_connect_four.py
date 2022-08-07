# TODO define winning conditions

class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


# print matrix
def print_matrix(ma):
    for element in matrix:
        print(element)


def validate_col_choice(selected_col, max_col_index):
    # verify if player choice is valid
    if not (0 <= selected_col <= max_col_index):
        raise InvalidColumnError


def place_player_choice(ma, selected_col_index, player_num):
    # Place player marker. Check if column available.
    rows_count = len(ma)
    for row_index in range(rows_count - 1, -1, -1):
        current_element =  ma[row_index][selected_col_index]
        if current_element == 0:
            ma[row_index][selected_col_index] = player_num
            return row_index, selected_col_index
    raise FullColumnError

def is_winner(ma, row, col, player_num, slots_count = 4):
    is_right = all[ma[row][col+index] == player_num for index in range(slots_count)]
    is_left = all[ma[row][col-index] == player_num for index in range(slots_count)]



rows = 6
cols = 7

# create a matrix
matrix = [[0 for _ in range(cols)]for row_num in range(rows)]

print_matrix(matrix)

player_num = 1
while True:
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        # Read column choice from input
        col_num = int(input(f"Player {player_num}, choose a column: ")) - 1
        validate_col_choice(col_num, cols - 1)
        row, col = place_player_choice(matrix, col_num, player_num)
        if is_winner(matrix, row, col, player_num):
            print(f"Player {player_num} has won the game!")
            break
        elif board_full():
            break
        print_matrix(matrix)
    except InvalidColumnError:
        print(f"This column is not valid, select a valid one: ")
        continue
    except ValueError:
        print(f"Please select a valid digit.")
        continue
    except FullColumnError:
        print(f"The column is full, please choose another one.")
        continue
    player_num += 1








