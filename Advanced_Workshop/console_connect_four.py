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
    except InvalidColumnError:
        print(f"This column is not valid, select a valid one: ")
        continue
    except ValueError:
        print(f"Please select a valid digit.")
        continue
    player_num += 1








