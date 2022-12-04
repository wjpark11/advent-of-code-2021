with open("day10_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [line.strip() for line in inputs]


PAIR_DICT = {
    "}" : "{",
    ")" : "(",
    "]" : "[",
    ">" : "<"
}

def is_corrupted(line: str) -> tuple:
    is_paired = [False for _ in line]
    for idx in range(len(line)):
        if line[idx] in "({[<":
            pass
        else:
            search_idx = idx - 1
            while is_paired[search_idx]:
                search_idx -= 1
                if search_idx < 0:
                    return True, ""
            if PAIR_DICT[line[idx]] == line[search_idx]:
                is_paired[idx] = True
                is_paired[search_idx] = True
            else:
                return False, line[idx]
    return True, ""

SCORE_DICT = {
    ')' :3, ']': 57, '}': 1197, '>': 25137
}


def day10_1(inputs):
    score = 0
    for line in inputs:
        if not is_corrupted(line)[0]:
            score += SCORE_DICT[is_corrupted(line)[1]]

    return score


if __name__ == "__main__":
    print(day10_1(inputs))
                

