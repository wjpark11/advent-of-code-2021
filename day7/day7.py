with open("day7_input.txt", "rt") as f:
    inputs = f.readline()
    inputs = list(map(int,inputs.split(',')))

def total_spent_fuel_constant_rate(initial_list, aligned_position):
    spent_fuel = 0
    for val in initial_list:
        spent_fuel += abs(val - aligned_position)
    return spent_fuel

def total_spent_fuel_real_rate(initial_list, aligned_position):
    spent_fuel = 0
    for val in initial_list:
        position_diff = abs(val - aligned_position) 
        spent_fuel += position_diff*(position_diff+1)/2
    return spent_fuel


def find_min_fuel(inputs, fuel_func):
    max_val = max(inputs)
    min_val = min(inputs)
    min_fuel = fuel_func(inputs, max_val)
    for val in range(min_val, max_val):
        min_fuel = min(min_fuel, fuel_func(inputs, val))        
    return min_fuel



print('solution for part1: ', find_min_fuel(inputs, total_spent_fuel_constant_rate))
print('solution for part2: ', find_min_fuel(inputs, total_spent_fuel_real_rate))
