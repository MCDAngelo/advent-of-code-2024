import re
from itertools import zip_longest
from utils.input_data import InputData

raw_input = InputData(4).input_data


def find_xmas(s):
    term = "XMAS"
    l_to_r = re.findall(term, s)
    r_to_l = re.findall(term[::-1], s)
    combined = l_to_r + r_to_l
    return combined


def search_list(l):
    raw_results = [find_xmas(i) for i in l]
    clean_results = [i for i in raw_results if len(i) > 0]
    n_terms_found = sum([len(i) for i in clean_results])
    return n_terms_found


def transpose_input(list_of_strings):
    transposed_input = list(map(list, zip_longest(*list_of_strings, fillvalue="")))
    transposed_strings = ["".join(line) for line in transposed_input]
    return transposed_strings


def shift_by_n(orig, shift):
    filler = [""] * abs(shift)
    filled = filler + orig
    return filled


# rows first:
n_in_rows = search_list(raw_input)
print(f"Row count: {n_in_rows}")

# columns second:
element_wise = [[c for c in line] for line in raw_input]
transposed_strings = transpose_input(element_wise)

n_in_cols = search_list(transposed_strings)
print(f"Column count: {n_in_cols}")


# diagonals:
diag_left = [shift_by_n(i, idx + 1) for idx, i in enumerate(element_wise)]
diag_left_strings = transpose_input(diag_left)
n_in_diag_left = search_list(diag_left_strings)
print(f"Diagonals left count: {n_in_diag_left}")

diag_right = [shift_by_n(i[::-1], idx + 1) for idx, i in enumerate(element_wise)]
diag_right_strings = transpose_input(diag_right)
n_in_diag_right = search_list(diag_right_strings)
print(f"Diagonals right count: {n_in_diag_right}")

print(f"Total for part 1: {n_in_rows + n_in_cols + n_in_diag_left + n_in_diag_right}")

# Part 2
remove_x = [i.replace("X", ".") for i in raw_input]
indices = [
    [(x, y) for x, l in enumerate(sub) if l == "A"] for y, sub in enumerate(raw_input)
]
indices_set = set([i for j in indices for i in j])


def find_x_mas(words, a_coords):
    a_x = a_coords[0]
    a_y = a_coords[1]

    if a_x in [0, X_MAX] or a_y in [0, Y_MAX]:
        return False

    top_left = words[a_y - 1][a_x - 1]
    bottom_right = words[a_y + 1][a_x + 1]
    bottom_left = words[a_y + 1][a_x - 1]
    top_right = words[a_y - 1][a_x + 1]
    if any(e in [top_left, bottom_right, top_right, bottom_left] for e in [".", "A"]):
        return False
    if (top_left == bottom_right) or (top_right == bottom_left):
        return False
    return True


Y_MAX = len(remove_x) - 1
X_MAX = max([len(i) for i in remove_x]) - 1


x_mas_locations = [find_x_mas(remove_x, a_coords) for a_coords in indices_set]
print(f"Part 2: number of X-MAS = {sum(x_mas_locations)}")
