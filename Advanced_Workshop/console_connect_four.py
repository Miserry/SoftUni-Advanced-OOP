# Place player marker. Check if column available.
# TODO define winning conditions

class InvalidColumnError(Exception):
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
    #TODO
    rows_count = len(ma)
    for row_index in range(rows_count - 1, -1, -1):
        current_element =  ma[row_index][selected_col_index]
        if current_element == 0:
            ma[row_index][selected_col_index] = player_num
            return


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
        place_player_choice(matrix, col_num, player_num)
        print_matrix(matrix)
    except InvalidColumnError:
        print(f"This column is not valid, select a valid one: ")
        continue
    except ValueError:
        print(f"Please select a valid digit.")
        continue
    player_num += 1








