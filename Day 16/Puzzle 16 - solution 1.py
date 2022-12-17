inputfile = "Puzzle 16 - input 2.txt"
f = open(inputfile, "r")

valve_dict = {}

pressure_max = 0

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
        input_graph[len(input_graph)-1].append(0)
    for adjacent_caves in valve_dict[cave][1]:
        input_graph[len(input_graph)-1][list(valve_dict).index(adjacent_caves)] = 1


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

dist_list, path_list = g.dijkstra(0,None)
print(dist_list)
print(path_list)

# This code is contributed by Divyanshu Mehta

path_weight = []
path_length = []
valve_opened = []

for path in path_list:
    path_weight.append(0)
    path_length.append(0)
    for cave_index in path:
        cave = list(valve_dict.keys())[cave_index]
        valve_pressure = valve_dict[cave][0]
        if valve_pressure == 0 or cave in valve_opened:
            path_length[-1] += 1
        else:
            path_length[-1] += 2
            path_weight[-1] += valve_pressure

print(path_weight)
print(path_length)