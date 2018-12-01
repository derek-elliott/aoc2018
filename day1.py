class Frequency:
    def __init__(self):
        self.frequency = 0
    def increment(self, i):
        self.frequency = self.frequency + i
    def decrement(self, i):
        self.frequency = self.frequency - i
    def __str__(self):
        return str(self.frequency)
    def __repr__(self):
        return str(self.frequency)

def get_steps(filename):
    with open(f'data/{filename}', 'r') as f:
        raw_steps = f.readlines()
    steps = []
    for i in raw_steps:
        steps.append([i[0], int(i[1:])])
    return steps

def part_one():
    freq = Frequency()
    steps = get_steps('day1-1.txt')
    ops = {'+': freq.increment, '-': freq.decrement}
    for i in steps:
        ops[i[0]](i[1])
    return freq

def part_two():
    freq = Frequency()
    steps = get_steps('day1-1.txt')
    ops = {'+': freq.increment, '-': freq.decrement}
    current = 0
    already_seen = []
    while current not in already_seen:
        for i in steps:
            if current in already_seen:
                break
            already_seen.append(int(str(freq)))
            ops[i[0]](i[1])
            current = int(str(freq))
    return freq



if __name__ == '__main__':
    print(f'Part 1: {part_one()}\nPart 2: {part_two()}')
