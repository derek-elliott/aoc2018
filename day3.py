class Instruction:
    def __init__(self, id, left_corner, dims):
        self.id = id
        self.coords = [[j, i] for i in range(left_corner[0] + 1, left_corner[0] + dims[0] + 1)
                              for j in range(left_corner[1] + 1, left_corner[1] + dims[1] + 1)]

    def __str__(self):
        return f'Instruction #{self.id}: \ncoords: {self.coords}'

class Canvas:
    def __init__(self, bounds):
        self.canvas = [[[] for i in range(bounds[0])] for j in range(bounds[1])]
        self.overlap = set()
    def add_claim(self, coords, id):
        self.canvas[coords[0] - 1][coords[1] - 1].append(id)
        if len(self.canvas[coords[0] - 1][coords[1] - 1]) > 1:
            for id in self.canvas[coords[0] - 1][coords[1] - 1]:
                self.overlap.add(id)
    def get_overlap(self):
        return sum([1 for line in self.canvas for list in line if len(list) > 1])
    def __str__(self):
        print_string = ''
        for line in self.canvas:
            for position in line:
                if len(position) > 1:
                    print_string += '#'
                elif len(position) == 1:
                    print_string += str(position[0])
                else:
                    print_string += '.'
            print_string += '\n'
        return(print_string)

def get_data(filename):
    with open(f'data/{filename}', 'r') as f:
        data = f.readlines()
    instructions = []
    for i in data:
        split_line = i.split()
        id = split_line[0].replace('#', '')
        left_corner = split_line[2].replace(':', '').split(',')
        dims = split_line[3].split('x')
        instructions.append(Instruction(int(id), [int(i) for i in left_corner], [int(i) for i in dims]))
    return instructions

def day_three(filename, bounds=[1000,1000], print_canvas=False):
    data = get_data(filename)
    canvas = Canvas(bounds)
    for instruction in data:
        for item in instruction.coords:
            canvas.add_claim(item, instruction.id)
    if print_canvas:
        print(canvas)

    non_overlap_id = 0
    for i in data:
        if i.id not in canvas.overlap:
            non_overlap_id = i.id
            break
    return [canvas.get_overlap(), non_overlap_id]


if __name__ == '__main__':
    test_run = day_three("day3-test.txt", bounds=[11, 9], print_canvas=True)
    real_run = day_three("day3-1.txt")
    print(f'Number of overlapping square inches in test file: {test_run[0]}\nId with no overlap: {test_run[1]}')
    print(f'Number of overlapping square inches in real file: {real_run[0]}\nId with no overlap: {real_run[1]}')
