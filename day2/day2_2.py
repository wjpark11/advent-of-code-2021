with open("day2_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip().split(' ') for input in inputs]

position = 0
depth = 0
aim = 0

for direction in inputs:
    if direction[0] == 'forward':
        position += int(direction[1])
        depth += aim * int(direction[1])
    elif direction[0] == 'down':
        aim += int(direction[1])
    else:
        aim -= int(direction[1])

print(position * depth)