inputfile = "Puzzle 16 - input 2.txt"
f = open(inputfile, "r")

valve_dict = {}

pressure_max = 0
starting_point = 0

for line in f:
    line_raw = line.strip().split(" ")
    valve_dict.update({line_raw[1]:[]})
    pressure_release = int(line_raw[4][5:-1])
    valve_dict[line_raw[1]].append(pressure_release)
    tunnels_list = []
    for cave in line_raw[8+1:]:
        tunnels_list.append(cave.strip(","))
    valve_dict[line_raw[1]].append(tunnels_list)

for key,value in valve_dict.items():
    pressure_release = value[0]
    if (pressure_release > pressure_max):
        pressure_max = pressure_release

input_graph = []
for cave in valve_dict.keys():
    input_graph.append([])
    for i in range(len(valve_dict)):
        input_graph[-1].append(0)
    for adjacent_caves in valve_dict[cave][1]:
        input_graph[-1][list(valve_dict).index(adjacent_caves)] = 1


"""for line in input_graph:
    print(line)"""

# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]

    def printSolution(self, dist, vert):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            if (node == vert or vert is None):
                print(node, "\t\t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = 1e100

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src, vert):

        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        path = [[]] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            if (u is None):
                print(sptSet)
            sptSet[u] = True
            path[u].append(u)

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                sptSet[v] == False and
                dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
                    path[v] = list(tuple(path[u]))

        #self.printSolution(dist, vert)
        return dist, path

# Driver program
g = Graph(len(valve_dict))
g.graph = input_graph

def pathing_function(start_node, valve_opened, steps, max_steps, valve_dict):
    start_index = list(valve_dict.keys()).index(start_node)
    dist_list, path_list_index = g.dijkstra(start_index,None)
    
    #print(dist_list)
    #print(path_list_index)

    # This code is contributed by Divyanshu Mehta

    path_weight = []
    path_pressure = []
    path_length = []
    path_length_list = []
    path_weighted_length = []
    path_list = []

    for path in path_list_index:
        path_list.append([])
        path_weight.append(0)
        path_pressure.append(0)
        path_length.append(0)
        path_length_list.append([])
        for cave_index in path:
            cave = list(valve_dict.keys())[cave_index]
            path_list[-1].append(cave)
        for cave_index in path[1:]:
            cave = list(valve_dict.keys())[cave_index]
            valve_pressure = valve_dict[cave][0]
            #print(valve_pressure)
            if valve_pressure == 0 or cave in valve_opened:
                path_length[-1] += 1
                path_weight[-1] += 1 * path_pressure[-1]
                path_length_list[-1].append(1)
            else:
                path_length[-1] += 2
                path_length_list[-1].append(2)
                path_weight[-1] += 2 * path_pressure[-1]
                path_pressure[-1] += valve_pressure
        path_weight[-1] += path_pressure[-1]
        if (steps + path_length[-1] <= max_steps and (path_length[-1] != 0)):
            path_weighted_length.append(path_pressure[-1]/path_length[-1])
        else:
            path_weighted_length.append(0)


    print(path_list)
    print(path_length)
    print(path_weight)
    print(path_weighted_length)

    max_weighted_length = max(path_weighted_length)
    path_to_take = path_weighted_length.index(max_weighted_length)
    return path_length[path_to_take], path_list[path_to_take], path_length_list[path_to_take]


valve_opened = []
node = "AA"
steps = 0
max_steps = 30
pressure_release_total = 0
pressure_release_culmulative = 0

while(steps < max_steps):
    #print(steps)
    steps_forward, path_list, steps_list = pathing_function(node, valve_opened, steps, max_steps, valve_dict)
    #print(path_list)
    #print(steps_list)
    if ((steps + steps_forward <= max_steps) and (steps_forward != 0)):
        for ind, valve in enumerate(path_list[1:]):
            pressure_release_culmulative += pressure_release_total * steps_list[ind]
            #print(pressure_release_culmulative)
            if (valve not in valve_opened and valve_dict[valve][0] != 0):
                pressure_release_total += valve_dict[valve][0]
                valve_opened.append(valve)
        node = path_list[-1]
    else:
        #print(steps)
        break

print(valve_opened)
print(pressure_release_total)
print(pressure_release_culmulative)
