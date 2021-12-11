with open("day1_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [int(input.strip()) for input in inputs]

increase = 0
for i in range(len(inputs)-1):
    if inputs[i] < inputs[i+1]:
        increase += 1

print(increase)