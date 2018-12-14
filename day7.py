import re
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.source = []
        self.sink = []
        self.total_vertex = 0

    def add_vertex(self, vertex, depends_on=''):
        if vertex in self.graph.keys():
            self.add_dependency(vertex, depends_on)
            return
        if depends_on != '' and depends_on not in self.graph.keys():
            self.add_vertex(depends_on)
        if depends_on == '':
            self.graph[vertex] = []
        else:
            self.graph[vertex] = [depends_on]
        self.total_vertex += 1

    def add_dependency(self, from_vertex, to_vertex):
        if from_vertex not in self.graph.keys():
            self.add_vertex(from_vertex, to_vertex)
            return
        if to_vertex not in self.graph.keys():
            self.add_vertex(to_vertex)
        self.graph[from_vertex].append(to_vertex)
        self._find_source_sink()

    def schedule(self, workers = 1, pretty_print=False):
        time = 0
        workers = [{'task': '-', 'time_left': 0} for i in range(workers)]
        output = ''
        while len(output) < self.total_vertex:
            proposed_steps = []
            for key, item in self.graph.items():
                if item == []:
                    proposed_steps.append(key)
            proposed_steps.sort()
            for worker in workers:
                worker['time_left'] -= 1
                if worker['time_left'] <= 0:
                    if worker['task'] != '-':
                        output += worker['task']
                    self._clear_dependency(worker['task'])
                    worker['task'] = proposed_steps[0] if proposed_steps != [] else '-'
                    if worker['task'] != '-':
                        proposed_steps.remove(worker['task'])
                        self._remove_node(worker['task'])
                    worker['time_left'] = ord(worker['task']) - 4 if worker['task'] != '-' else -1
            if pretty_print:
                worker_string = ''
                for worker in workers:
                    worker_string += f'{worker["task"]}\t'
                print(f'{time}\t{worker_string}\t{output}')
            time += 1
        return output


    def _find_source_sink(self):
        all_vertex = self.graph.keys()
        self.source = []
        for key, value in self.graph.items():
            if value == []:
                self.source.append(key)
            all_vertex = [vertex for vertex in all_vertex if vertex not in value]
        self.sink = all_vertex

    def _clear_dependency(self, dependency):
        for key, value in self.graph.items():
            if dependency in value:
                self.graph[key] = [dep for dep in value if dep != dependency]

    def _remove_node(self, node):
        self.graph.pop(node, None)

    def __str__(self):
        output = ''
        for key, item in self.graph.items():
            output += f'{key}: {item}\n'
        return output



def get_data(filename):
    with open(f'data/{filename}', 'r') as f:
        raw_data = f.readlines()
    pattern = re.compile('[S,s]tep ([A-Z])')
    data = []
    for row in raw_data:
        result = pattern.findall(row)
        data.append(result)
    return data

def day_seven(filename, workers, pretty_print = False):
    data = get_data(filename)
    graph = Graph()
    for row in data:
        graph.add_vertex(row[1], row[0])
    if pretty_print:
        print(f'Source: {graph.source}, Sink: {graph.sink}')
    return graph.schedule(workers, pretty_print)

if __name__ == '__main__':
    # print(f'Test step order(part one): {day_seven("day7-test.txt", 1)}')
    # print(f'Step order(part_one): {day_seven("day7.txt", 1, pretty_print=False)}')
    print(f'Test step order(part two): {day_seven("day7-test.txt", 2, pretty_print=True)}')
    # print(f'Step order(part two): {day_seven("day7.txt", 5, pretty_print=True)}')
