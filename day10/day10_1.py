from collections import Counter

with open("day10_input.txt", "rt") as f:
    inputs = f.readlines()
    lines = [line.strip() for line in inputs]


PAIR_DICT = {
    "}" : "{",
    ")" : "(",
    "]" : "[",
    ">" : "<"
}

def is_corrupted(line: str) -> tuple:
    for i in range(len(line)):
        if line[i] in ")]}>":
            pair = PAIR_DICT[line[i]]
            pair_point = -1
            j = i
            while pair_point != 0:
                j -= 1
                if line[j] == pair:
                    pair_point += 1
                elif line[j] == line[i]:
                    pair_point -= 1
                elif j == -1:
                    return False, line[i]    
            chunk = line[j:i+1]
            print(chunk)
            counter = Counter(chunk)
            if counter['{'] != counter['}']\
                or counter['['] != counter[']']\
                or counter['<'] != counter['>']\
                or counter['('] != counter[')']:
                return False, line[i]
    return True, ""

SCORE_DICT = {
    ')' :3, ']': 57, '}': 1197, '>': 25137
}


print(is_corrupted('[(()[<>])]({[<{<<[]>>('))
# score = 0
# for line in lines:
#     if not is_corrupted(line)[0]:
#         score += SCORE_DICT[is_corrupted(line)[1]]

# print(f"total syntax error score: {score}")
                

