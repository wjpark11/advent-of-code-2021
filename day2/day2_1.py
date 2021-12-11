with open("day2_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip().split(' ') for input in inputs]

forward = 0
down = 0

for direction in inputs:
    if direction[0] == 'forward':
        forward += int(direction[1])
    elif direction[0] == 'down':
        down += int(direction[1])
    else:
        down -= int(direction[1])

print(forward * down)