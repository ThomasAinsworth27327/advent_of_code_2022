import string
import math
inputfile = "Puzzle 12 - input 2.txt"
f = open(inputfile, "r")
alphabet = list(string.ascii_lowercase)

contour_map = []
position = 0
new_position = 0
end_position = 0
x = 0
number_lines = 0
line_width = 0

for line in f:
    line_raw = line.strip()
    line_width = len(line)
    for character in line_raw:
        if (character == "S"):
            position = x
            character = "a"
        elif (character == "E"):
            end_position = x
            character = "z"
        contour_map.append(character)
        x += 1
    number_lines += 1

print(contour_map)

input_graph = []
for character_number in range(len(contour_map)):
    input_graph.append([])
    for i in range(len(contour_map)):
        input_graph[len(input_graph)-1].append(0)
    if (character_number % line_width != line_width - 1):
        new_point = character_number + 1
        result = 2 + alphabet.index(contour_map[character_number]) - alphabet.index(contour_map[new_point])
        if (result > 0):
            input_graph[len(input_graph)-1][new_point] = 1
    if (character_number % line_width != 0):
        new_point = character_number - 1
        result = 2 + alphabet.index(contour_map[character_number]) - alphabet.index(contour_map[new_point])
        if (result > 0):
            input_graph[len(input_graph)-1][new_point] = 1
    if (character_number + line_width < len(contour_map)):
        new_point = character_number + line_width
        result = 2 + alphabet.index(contour_map[character_number]) - alphabet.index(contour_map[new_point])
        if (result > 0):
            input_graph[len(input_graph)-1][new_point] = 1
    if (character_number - line_width >= 0):
        new_point = character_number - line_width
        result = 2 + alphabet.index(contour_map[character_number]) - alphabet.index(contour_map[new_point])
        if (result > 0):
            input_graph[len(input_graph)-1][new_point] = 1

#print(input_graph)

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
            if (node == vert):
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

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                sptSet[v] == False and
                dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist, vert)

# Driver program
g = Graph(len(contour_map))
g.graph = input_graph

g.dijkstra(position, end_position)

# This code is contributed by Divyanshu Mehta