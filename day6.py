class Field:
    def __init__(self, x_limit, y_limit):
        self.field = [[{'location_id': '.', 'distance': -1} for i in range(x_limit + 1)] for j in range(y_limit + 1)]
        self.locations = {}
        self.last_location = -1

    def add_location(self, x, y):
        self.last_location += 1
        self.locations = {'id': self.last_location, 'area': 1}
        self.field[y][x] = {'location_id': str(self.last_location), 'distance': 0}

    def _distance(self, point_1, point_2):
        return (point_1[0] - point_2[0]) + (point1[1] - point_2[1])
    def _calculate_area(self, location):
        for y, row in enumerate(self.field):
            for x, item in enumerate(row):
                # TODO: Complete this
                pass


    def __str__(self):
        output = ''
        for row in self.field:
            for item in row:
                output += item['location_id']
            output += '\n'
        return output

def get_data(filename):
    with open(f'data/{filename}', 'r') as f:
        raw_data = f.readlines()
    data = []
    for line in raw_data:
        data.append([int(i) for i in line.strip().split(',')])
    return data

def scale(data):
    x_min, y_min = (min([i[0] for i in data]), min([i[1] for i in data]))
    return [[i[0] - x_min, i[1] - y_min] for i in data]

def part_one(filename):
    data = get_data(filename)
    data = scale(data)
    x_limit, y_limit = (max([i[0] for i in data]), max([i[1] for i in data]))
    field = Field(x_limit, y_limit)
    for item in data:
        field.add_location(item[0], item[1])
    return field

if __name__ == '__main__':
    print(part_one('day6-test.txt'))
