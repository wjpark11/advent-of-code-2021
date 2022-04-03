with open("day8_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

inputs = [[item.split(' ') for item in input.split(' | ')] for input in inputs]

output_vals = [input[1] for input in inputs]


nums = 0
for output_list in output_vals:
    for output in output_list:
        if len(output) == 2 or len(output) == 3 or len(output) == 4 or len(output) == 7:
            nums += 1

print(nums)