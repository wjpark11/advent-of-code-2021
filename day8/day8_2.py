from typing import List

with open("day8_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [input.strip() for input in inputs]

inputs = [[item.split(' ') for item in input.split(' | ')] for input in inputs]


def decode_signal(signals: list) -> dict:
    decode_dict = dict()
    length5 = []
    length6 = []

    for signal in signals:
        if len(signal) == 2:
            decode_dict[signal] = '1'
            num1 = signal
        elif len(signal) == 3:
            decode_dict[signal] = '7'
        elif len(signal) == 4:
            decode_dict[signal] = '4'
            num4 = signal
        elif len(signal) == 7:
            decode_dict[signal] = '8'
            num8 = signal
        elif len(signal) == 5:
            length5.append(signal)
        else:
            length6.append(signal)

    for signal in length5:
        if len(set(signal) & set(num1)) == 2:
            decode_dict[signal] = '3'
        elif len(set(signal) & set(num4)) == 2:
            decode_dict[signal] = '2'
        else:
            decode_dict[signal] = '5'

    for signal in length6:
        if len(set(signal) & set(num1)) == 1:
            decode_dict[signal] = '6'
        elif len(set(signal) & set(num4)) == 3:
            decode_dict[signal] = '0'
        else:
            decode_dict[signal] = '9'

    return decode_dict
    



def get_numbers(input: List[list]) -> int:
    signals, nums = input
    decode_dict = decode_signal(signals)

    ans_str = ''
    for num in nums:
        ans_str += decode_dict[num]

    ans = int(ans_str)

    return ans



for input in inputs:
    print(decode_signal(input[0]))