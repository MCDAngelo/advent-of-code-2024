import re
from utils.input_data import InputData


def mul(x, y):
    return x * y


inputs = InputData(3)
matches = [re.findall(r"mul\(\d+,\d+\)", i) for i in inputs.input_data]
expressions = [eval(i) for sub in matches for i in sub]
print(f"Part 1: The sum is: {sum(expressions)}")

full_input = ("").join(inputs.input_data)
split1 = full_input.split("do()")
split2 = [i.split("don't()")[0] for i in split1]
matches = [re.findall(r"mul\(\d+,\d+\)", i) for i in split2]
expressions = [eval(i) for sub in matches for i in sub]

print(f"Part 2: {sum(expressions)}")
