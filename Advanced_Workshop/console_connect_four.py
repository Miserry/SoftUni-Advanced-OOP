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


def is_horizontal(ma, row, col, player_num, slots_count):
    count_right = [is_player_num(ma, row, col + index, player_num) for index in range(slots_count)].count(True)
    count_left = [is_player_num(ma, row, col - index, player_num) for index in range(slots_count)].count(True)
    return (count_left + count_right) > slots_count


def is_right_diagonal(ma, row, col, player_num, slots_count):
    right_up_count = [is_player_num(ma, row - index, col + index, player_num) for index in range(slots_count)].count(True)
    left_down_count = [is_player_num(ma, row + index, col - index, player_num) for index in range(slots_count)].count(True)
    return (right_up_count + left_down_count) > slots_count


def is_left_diagonal(ma, row, col, player_num, slots_count):
    left_up_count = [is_player_num(ma, row - index, col - index, player_num) for index in range(slots_count)].count(True)
    right_down_count = [is_player_num(ma, row + index, col + index, player_num) for index in range(slots_count)].count(True)
    return (left_up_count + right_down_count) > slots_count


def is_up(ma, row, col, player_num, slots_count):
    up_count = [is_player_num(ma, row - index, col, player_num) for index in range(slots_count)].count(True)
    return up_count > slots_count


def is_winner(ma, row, col, player_num, slots_count = 4):
    if any(
            [
                is_horizontal(ma, row, col, player_num, slots_count),
                is_right_diagonal(ma, row, col, player_num, slots_count),
                is_left_diagonal(ma, row, col, player_num, slots_count),
                is_up(ma, row, col, player_num, slots_count)
            ]
    ):
        return True
    return False


def is_player_num(ma, row, col, player_num):
    if col < 0:
        return False
    try:
        if ma[row][col] == player_num:
            return True
    except IndexError:
        return False
    return False


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
            print_matrix(matrix)
            print(f"Player {player_num} has won the game!")
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








