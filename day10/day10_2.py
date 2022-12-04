with open("day10_input.txt", "rt") as f:
    inputs = f.readlines()
    inputs = [line.strip() for line in inputs]


PAIR_DICT = {"}": "{", ")": "(", "]": "[", ">": "<"}


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
                    return True, is_paired
            if PAIR_DICT[line[idx]] == line[search_idx]:
                is_paired[idx] = True
                is_paired[search_idx] = True
            else:
                return False, is_paired
    return True, is_paired


SCORE_DICT = {"(": 1, "[": 2, "{": 3, "<": 4}


def day10_2(inputs):
    incompletes = [line for line in inputs if is_corrupted(line)[0]]
    scores = []
    for line in incompletes:
        char_list = [line[i] for i, val in enumerate(is_corrupted(line)[1]) if not val]
        score = 0
        for char in char_list:
            score = (score * 5) + SCORE_DICT[char]
        scores.append(score)
        scores.sort()

    return scores[int(len(scores) / 2)]


if __name__ == "__main__":
    print(day10_2(inputs))
