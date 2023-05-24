# Caldera technical screen May 2023
# https://immense-success-298.notion.site/Chess-Implementation-fa8ee532b0b047b0aa72d0df768e107f

# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
from typing import List, Tuple

letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
letter_int = {x: idx for idx, x in enumerate(letters)}
int_letter = {idx: x for idx, x in enumerate(letters)}


def generate_possible_steps(col: int, row: int) -> List[Tuple[int, int]]:

    possible = []

    # right
    for idx, c in enumerate(range(col, 8)):
        # up
        possible.append((c, row + idx))
        # down
        possible.append((c, row - idx))

    # left
    for idx, c in enumerate(reversed(range(col + 1))):
        # up
        possible.append((c, row + idx))
        # down
        possible.append((c, row - idx))

    filtered = [(c, r) for (c, r) in possible if c >=
                0 and c <= 7 and r >= 0 and r <= 7 and (c != col and r != row)]

    return filtered


def get_is_white(col: str, row: str) -> bool:

    # A, C, E, G
    # even -> white
    # odd -> black

    # B, D, F, H
    # even -> black
    # odd -> white

    if col % 2 == 0:
        return row % 2 == 0
    else:
        return row % 2 != 0


def bishop_path(start: str, end: str) -> List[str]:

    if (start == end):
        return start

    # convert from Letter to int
    # decrement row by 1 to get 0 indexed rows
    start_col = letter_int[start[0]]
    start_row = int(start[1]) - 1

    end_col = letter_int[end[0]]
    end_row = int(end[1]) - 1

    # is possible?
    if not get_is_white(start_col, start_row) == get_is_white(end_col, end_row):
        return "Impossible"

    def find_path(curr_col: int, curr_row: int, target_col: int, target_row: int, path_taken: List[Tuple[int, int]], seen: set[Tuple[int, int]]):

        if len(path_taken) == 5:
            return

        # Determine possible next steps.
        possible_steps = generate_possible_steps(curr_col, curr_row)

        # if can move to target, return with target appended to path
        if (target_col, target_row) in possible_steps:
            path_taken.append((target_col, target_row))
            return path_taken

        for next_step in possible_steps:

            if next_step in seen:
                continue

            next_col = next_step[0]
            next_row = next_step[1]

            path_taken.append(next_step)
            seen.add(next_step)

            sol = find_path(
                next_col,
                next_row,
                target_col,
                target_row,
                path_taken,
                seen
            )

            if sol:
                return sol
            else:
                path_taken.pop()

    seen = set()
    seen.add((start_col, start_row))
    solution = find_path(
        start_col,
        start_row,
        end_col,
        end_row,
        [(start_col, start_row)],
        seen
    )

    chess_notation_string_list_solution = [str(int_letter[c])+str(r + 1)
                                           for (c, r) in solution]

    chess_notation_string_solution = ' '.join(
        [str(e) for e in chess_notation_string_list_solution])

    return chess_notation_string_solution


# "E2", "E3" # Impossible
start = "E2"
end = "E3"
output = bishop_path(start, end)
print("Start: ", start, " End: ", end)
print("output: ", output)

# "F1", "E8" # Possible
start = "F1"
end = "E8"
output = bishop_path(start, end)
print("Start: ", start, " End: ", end)
print("output: ", output)

# "A3", "A3" # Possible
start = "A3"
end = "A3"
output = bishop_path(start, end)
print("Start: ", start, " End: ", end)
print("output: ", output)

# "F7", "H1" # Possible
start = "F7"
end = "H1"
output = bishop_path(start, end)
print("Start: ", start, " End: ", end)
print("output: ", output)
