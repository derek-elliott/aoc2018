class Field:
    def __init__(self, x_limit, y_limit):
        self.field = [[{'location_id': '.', 'distances': [], 'total_distance': 0} for i in range(x_limit + 1)] for j in range(x_limit + 1)]
        self.x_bounds = [0, x_limit]
        self.y_bounds = [0, y_limit]
        self.locations = {}
        self.last_location = -1

    def _distance(self, point_1, point_2):
        return abs(point_1[0] - point_2[0]) + abs(point_1[1] - point_2[1])

    def _fill_area(self, location, id):
        for x, row in enumerate(self.field):
            for y, item in enumerate(row):
                dist = self._distance([x,y], location['center'])
                if item['distances'] == [] or min(item['distances']) > dist:
                    self.field[x][y]['location_id'] = str(id)
                elif min(item['distances']) == dist:
                    self.field[x][y]['location_id'] = '.'
                self.field[x][y]['distances'].append(dist)

    def _calculate_distance_sum(self):
        for x, row in enumerate(self.field):
            for y, item in enumerate(row):
                self.field[x][y]['total_distance'] = sum(item['distances'])

    def add_location(self, x, y):
        self.last_location += 1
        self.locations[str(self.last_location)] = {'center': [x,y], 'area': 1}
        self.field[x][y]['location_id'] =  str(self.last_location)
        self.field[x][y]['distances'].append(0)
        self._fill_area(self.locations[str(self.last_location)], self.last_location)

    def calculate_area(self):
        for x, row in enumerate(self.field):
            for y, item in enumerate(row):
                if item['location_id'] != '.' and self.locations[item['location_id']]['area'] != -1:
                    if x not in self.x_bounds and y not in self.y_bounds:
                        self.locations[item['location_id']]['area'] += 1
                    else:
                        self.locations[item['location_id']]['area'] = -1

    def calculate_max_dist_area(self, max_distance):
        area = 0
        self._calculate_distance_sum()
        for x, row in enumerate(self.field):
            for y, item in enumerate(row):
                if item['total_distance'] < max_distance:
                    area += 1
        return area

    def print_areas(self):
        for id, item in self.locations.items():
            print(f'Field: {id}, Area: {item["area"]}\n')

    def max_area(self):
        max_area = 0
        for item in self.locations.values():
            if item['area'] > max_area:
                max_area = item['area']
        return max_area

    def _print_to_log(self):
        with open('data/day6.log', 'w') as f:
            f.write(str(self))

    def __str__(self):
        output = ''
        for row in self.field:
            output += "\t".join([i["location_id"] for i in row]) + '\n'
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

def day_6(filename, max_distance, pretty_print=False, print_to_log=False):
    data = get_data(filename)
    data = scale(data)
    x_limit, y_limit = (max([i[1] for i in data]), max([i[0] for i in data]))
    field = Field(x_limit, y_limit)
    for item in data:
        field.add_location(item[0], item[1])
    field.calculate_area()
    if pretty_print:
        field.print_areas()
        print(field)
    if print_to_log:
        with open('data/day6.log', 'w') as f:
            f.write(str(field))
    return (field.max_area(), field.calculate_max_dist_area(max_distance))

if __name__ == '__main__':
    # max_dist = 32
    # part_one, part_two = day_6("day6-test.txt", max_dist)
    max_dist = 10000
    part_one, part_two = day_6("day6.txt", max_dist)
    print(f'The max, non infinite, area is {part_one}')
    print(f'The area of the region containing all locations with a sum distance less than {max_dist} is {part_two}')
