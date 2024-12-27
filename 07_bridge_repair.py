from functools import reduce
from itertools import product
import re
from utils.input_data import InputData

TEST_INPUT = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


class BridgeRepair:
    def __init__(self, testing=True):
        self.testing = testing
        self.operations = ["+", "*"]
        self.correct_vals = []
        self.load_data()

    def load_data(self):
        if self.testing:
            self.raw_data = TEST_INPUT.split("\n")
        else:
            self.raw_data = InputData(7).input_data

        self.data = [i.split(":") for i in self.raw_data if i != ""]
        self.data = {int(i[0]): i[1].strip().split(" ") for i in self.data}
        self.data = {k: [int(n) for n in v] for k, v in self.data.items()}

    def test_operations(self, k):
        def _test_combo(vals, ops):
            comb_lists = [
                sub[i] for i in range(len(ops)) for sub in [vals, ops]
            ] + vals[len(ops) :]
            str_rep = reduce(
                (lambda x, y: str(x) + str(y) if y != "||" else x), comb_lists
            )
            clean_list = re.split("(\\*|\\+)", str_rep)
            running_total = reduce(
                (lambda x, y: eval(f"{x}{y}") if y not in ops else f"{x}{y}"),
                clean_list,
            )
            return running_total == k

        v = self.data.get(k)
        n_slots = len(v) - 1
        operations = product(self.operations, repeat=n_slots)
        checks = [_test_combo(v, o) for o in operations]
        return sum(checks) > 0

    def part_1_test(self):
        self.operations = ["+", "*"]
        results = [k for k in self.data if self.test_operations(k)]
        print(f"Part 1: {sum(results)}")


if __name__ == "__main__":
    task = BridgeRepair(testing=True)
    task.part_1_test()
