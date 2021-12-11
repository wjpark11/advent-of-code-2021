with open("day3_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

oxygen_gen_list = [0 for _ in range(12)]
for bits in inputs:
    idx = 0
    for bit in bits:
        if bit == "1":
            oxygen_gen_list[idx] += 1
        else:
            oxygen_gen_list[idx] -= 1
        idx += 1

oxygen_gen_code = ''.join(["1" if item>=0 else "0" for item in oxygen_gen_list])

oxygen_gen_rating = ''
for i in range(12):
    oxygen_gen_partial = oxygen_gen_code[:i+1]
    oxygen_match_list = [code for code in inputs if code[:i+1]==oxygen_gen_partial]    
    if len(oxygen_match_list) == 1:
        oxygen_gen_rating = oxygen_match_list[0]
        break

co2_scr_code = ''.join(["1" if item < 0 else "0" for item in oxygen_gen_list])

co2_scr_rating = ''
for i in range(12):
    co2_scr_partial = co2_scr_code[:i+1]
    co2_match_list = [code for code in inputs if code[:i+1]==co2_scr_partial]
    print(co2_match_list)
    if len(co2_match_list) == 1:
        co2_scr_rating = co2_match_list[0]
        break

print(oxygen_gen_rating)
print(co2_scr_rating)
# print (int('0b'+oxygen_gen_rating,2) * int('0b'+co2_scr_rating,2))
