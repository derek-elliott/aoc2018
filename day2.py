from collections import defaultdict

def get_data(filename):
    with open(f'data/{filename}', 'r') as f:
        raw_data = f.readlines()
    return raw_data

def get_letter_counts(box_id):
    letter_counts = defaultdict(int)
    for i in box_id:
        letter_counts[i] += 1
    return letter_counts

def check_counts(letter_counts):
    counts = [0, 0]
    for key in letter_counts:
        if letter_counts[key] == 2:
            counts[0] += 1
        if letter_counts[key] == 3:
            counts[1] += 1
    return [1 if counts[0] > 0 else 0, 1 if counts[1] > 0 else 0]

def part_one():
    data = get_data('day2-1.txt')
    twos = 0
    threes = 0
    for i in data:
        count = check_counts(get_letter_counts(i))
        twos += count[0]
        threes += count[1]
    return twos * threes

def part_two():
    data = get_data('day2-1.txt')
    for i, val_one in enumerate(data):
        for val_two in data[i:]:
            intersection = [j for j, k in zip(val_one, val_two) if j == k]
            if len(intersection) == len(val_one) - 1:
                return ''.join(intersection)

if __name__ == '__main__':
    hash = part_one()
    intersect = part_two()
    print(f'The hash is: {hash}')
    print(f'Intersect of the correct boxes are: {intersect}')
