def get_data(filename):
    with open(f'data/{filename}', 'r') as f:
        data = f.readlines()
    return data[0]

def reduce_polymer(data):
    changed = True
    while changed:
        prev_len = len(data)
        data = list(data)
        for i, letter in enumerate(data):
            if i == prev_len - 2:
                break
            if letter.lower() != data[i+1].lower():
                continue
            if letter.isupper() and data[i+1].islower():
                data[i] = '.'
                data[i+1] = '.'
            if letter.islower() and data[i+1].isupper():
                data[i] = '.'
                data[i+1] = '.'
        data = ''.join(data)
        data = data.replace('.', '')
        if len(data) == prev_len:
            changed = False
    return data

def part_one(filename):
    data = get_data(filename)
    reduced_data = reduce_polymer(data)
    return len(list(reduced_data))

def part_two(filename):
    data = get_data(filename)
    shortest = 50000
    removed = ''
    for i in 'abcdefghijklmnopqrstuvwxyz':
        modified_polymer = data.replace(i, '').replace(i.upper(), '')
        reduced_polymer = reduce_polymer(modified_polymer)
        if len(list(reduced_polymer)) < shortest:
            shortest = len(list(reduced_polymer))
            removed = i
    return removed, shortest


if __name__ == '__main__':
    print(f'The length of the test polymer is: {part_one("day5-test.txt")}')
    print(f'The length of the polymer is: {part_one("day5-1.txt")}')
    test_removed, test_shortest = part_two('day5-test.txt')
    print(f'The shortest length of the modified test polymer is {test_shortest} with {test_removed} removed.')
    removed, shortest = part_two("day5-1.txt")
    print(f'The shortest length of the modified test polymer is {shortest} with {removed} removed.')
