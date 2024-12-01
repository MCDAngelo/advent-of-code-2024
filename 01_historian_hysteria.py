import re
from collections import Counter
from utils.input_data import InputData

day_1_input_url = "https://adventofcode.com/2024/day/1/input"
raw_input = InputData(day_1_input_url)
list_input = [re.split(r"\s+", i) for i in raw_input.input_data]

l1 = [int(i[0]) for i in list_input]
l2 = [int(i[1]) for i in list_input]

deltas = [abs(i - j) for i, j in zip(sorted(l1), sorted(l2))]

print(f"Part 1: the total delta is {sum(deltas)}")

l2_counts = Counter(l2)
sim_score = sum([i * l2_counts.get(i, 0) for i in l1])

print(f"Part 2: the similarity score is {sim_score}")
