with open("day3_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

gamma_list = [0 for _ in range(12)]
for bits in inputs:
    idx = 0
    for bit in bits:
        if bit == "1":
            gamma_list[idx] += 1
        else:
            gamma_list[idx] -= 1
        idx += 1

gamma_code = ''.join(["1" if item>0 else "0" for item in gamma_list])
epsilon_code = ''.join(["0" if item>0 else "1" for item in gamma_list])

gamma_rate = int('0b'+gamma_code,2)
epsilon_rate = int('0b'+epsilon_code,2)

print(gamma_rate * epsilon_rate)


    



