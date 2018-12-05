from tabulate import tabulate

class Guard:
    def __init__(self, id):
        self.id = id
        self.schedule = [0 for i in range(60)]
        self.is_asleep = False
        self.time_asleep = 0
    def set_asleep(self, time_awake):
        for minute in range(self.time_asleep, time_awake):
            self.schedule[minute] += 1
    def __str__(self):
        return ''.join([str(i) if i > 0 else '.' for i in self.schedule])
    def __repr__(self):
        return ''.join([str(i) if i > 0 else '.' for i in self.schedule])

def get_data(filename):
    with open(f'data/{filename}', 'r') as f:
        raw_data = f.readlines()
    cleaned_data = []
    for line in raw_data:
        cleaned_data.append(line.replace('[', '')
                                .replace(']', '')
                                .replace('Guard', '')
                                .replace('up', '')
                                .replace('begins shift', '')
                                .replace('asleep', '')
                                .replace('#', '')
                                .split())
    cleaned_data.sort()
    return cleaned_data

def print_guards(guards):
    rows = []
    headers = ['ID']
    for i in range(60):
    headers.append(str(i))
    for key, value in guards.items():
        rows.append([key, value])
    print tabulate(rows, headers=headers)

def part_one(filename, pretty_print=False):
    data = get_data(filename)
    guards = {}
    last_guard = 0
    for item in data:
        if item[2].isdigit():
            last_guard = int(item[2])
            if not int(item[2]) in guards.keys():
                guards[int(item[2])] = Guard(int(item[2]))
        else:
            if item[2] == 'falls':
                guards[last_guard].time_asleep = int(item[1].split(':')[1])
            elif item[2] == 'wakes':
                guards[last_guard].set_asleep(int(item[1].split(':')[1]))
    if pretty_print:
        print_guards(guards)
    highest_time = 0
    sleepiest_guard = Guard(0)
    for guard in guards.values():
        if sum(guard.schedule) > highest_time:
            highest_time = sum(guard.schedule)
            sleepiest_guard = guard
    return sleepiest_guard.id * sleepiest_guard.schedule.index(max(sleepiest_guard.schedule))

def part_two(filename, pretty_print=False):
    data = get_data(filename)
    guards = {}
    last_guard = 0
    for item in data:
        if item[2].isdigit():
            last_guard = int(item[2])
            if not int(item[2]) in guards.keys():
                guards[int(item[2])] = Guard(int(item[2]))
        else:
            if item[2] == 'falls':
                guards[last_guard].time_asleep = int(item[1].split(':')[1])
            elif item[2] == 'wakes':
                guards[last_guard].set_asleep(int(item[1].split(':')[1]))
    if pretty_print:
        print_guards(guards)
    highest_time = 0
    sleepiest_guard = Guard(0)
    for guard in guards.values():
        if max(guard.schedule) > highest_time:
            highest_time = max(guard.schedule)
            sleepiest_guard = guard
    return sleepiest_guard.id * sleepiest_guard.schedule.index(max(sleepiest_guard.schedule))

if __name__ == '__main__':
    print(f'Hash for sleepiest guard using Stragety 1 based on test data: {part_one("day4-test.txt", True)}')
    print(f'Hash for sleepiest guard using Stragety 1 based on real data: {part_one("day4-1.txt")}')
    print(f'Hash for sleepiest guard using Stragety 2 based on test data: {part_two("day4-test.txt", True)}')
    print(f'Hash for sleepiest guard using Stragety 2 based on real data: {part_two("day4-1.txt")}')
