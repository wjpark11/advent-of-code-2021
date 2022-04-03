from collections import Counter

with open("day6_input.txt", "rt") as f:
    inputs = f.readline()
    inputs = list(map(int,inputs.split(',')))

initial_status = Counter(inputs)

class FishPool:
    def __init__(self, initial: Counter):
        self.pool = initial
        self.pool[6] = 0
        self.pool[7] = 0
        self.pool[8] = 0
        self.pool[0] = 0


    def pass_a_day(self):
        pool = Counter()
        for i in range(8):
            pool[i] = self.pool[i+1]        
        pool[8] = self.pool[0]
        pool[6] += self.pool[0]
        self.pool = pool

    def get_total(self):
        total = 0
        for key in self.pool:
            total += self.pool[key]

        return total

f1 = FishPool(initial_status)
f2 = FishPool(initial_status)

for _ in range(80):
    f1.pass_a_day()

for _ in range(256):
    f2.pass_a_day()



print('latern fishs after 80 days: ', f1.get_total())
print('latern fishs after 256 days: ', f2.get_total())
