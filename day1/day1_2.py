with open("day1_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [int(input.strip()) for input in inputs]

increase = 0
for i in range(len(inputs)-3):
    if inputs[i]+inputs[i+1]+inputs[i+2] < inputs[i+1]+inputs[i+2]+inputs[i+3]:
        increase += 1

print(increase)