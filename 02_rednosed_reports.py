from utils.input_data import InputData

raw_input = InputData(2)
input_data = [i.strip().split(" ") for i in raw_input.input_data]
input_data = [[int(j) for j in i] for i in input_data]


def check_set(report):
    delta_vals = [(report[idx + 1] - report[idx]) for idx in range(len(report) - 1)]
    signs = [i < 0 for i in delta_vals]
    monotonic = min(signs) == max(signs)
    delta_size = [not (1 <= abs(i) <= 3) for i in delta_vals]
    btwn_1_3 = sum(delta_size) == 0
    return monotonic & btwn_1_3


keeps = [check_set(i) for i in input_data]

print(f"Total number to keep: {sum(keeps)}")


def remove_one(report):
    for i in range(len(report)):
        test = report[:i] + report[i + 1 :]
        if check_set(test):
            return True
    return False


checked = [True if check_set(i) else remove_one(i) for i in input_data]
print(f"Total number to keep after problem dampener: {sum(checked)}")
