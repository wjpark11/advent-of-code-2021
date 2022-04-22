with open("day9_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [list(map(int,list(line.strip()))) for line in inputs]

w, h = len(inputs[0]), len(inputs)

print(w, h)