with open("day3_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

filtered_list = inputs
for idx in range(12):
    digit = '0'
    occur_list = [1 if input[idx]=='1' else -1 for input in filtered_list]
    if sum(occur_list) >= 0:
        digit = '1'
    else:
        digit = '0'
    filtered_list = [item for item in filtered_list if item[idx]==digit]
    if len(filtered_list) == 1:
        oxygen_gen_rating = int('0b'+''.join(filtered_list[0]),2)


filtered_list = inputs
for idx in range(12):
    digit = '0'
    occur_list = [1 if input[idx]=='1' else -1 for input in filtered_list]
    if sum(occur_list) < 0:
        digit = '1'
    else:
        digit = '0'
    filtered_list = [item for item in filtered_list if item[idx]==digit]    
    if len(filtered_list) == 1:
        co2_scr_rating = int('0b'+''.join(filtered_list[0]),2)

print(oxygen_gen_rating*co2_scr_rating)
