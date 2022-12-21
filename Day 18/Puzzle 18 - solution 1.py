inputfile = "Puzzle 18 - input 1.txt"
f = open(inputfile, "r")

rock_graph = []

for line_raw in f:
    line = line_raw.strip().split(",")
    line_int = []
    for e in line:
        line_int.append(int(e))
    rock_graph.append(line_int)

"""for l in rock_graph:
    print(l)"""

x_range = [rock_graph[0][0],rock_graph[0][0]]
y_range = [rock_graph[0][1],rock_graph[0][1]]
z_range = [rock_graph[0][2],rock_graph[0][2]]
#print(f"{x_range}, {y_range}, {z_range}")

for element in rock_graph:
    if element[0] < x_range[0]:
        x_range[0] = element[0]
    if element[0] > x_range[1]:
        x_range[1] = element[0]
    if element[1] < y_range[0]:
        y_range[0] = element[1]
    if element[1] > y_range[1]:
        y_range[1] = element[1]
    if element[2] < z_range[0]:
        z_range[0] = element[2]
    if element[2] > z_range[1]:
        z_range[1] = element[2]

#print(f"{x_range}, {y_range}, {z_range}")

num_faces = 0

"""Scanning through x for each y,z"""

for y in range(y_range[0],y_range[1] + 1):
    for z in range(z_range[0],z_range[1] + 1):
        block_list = []
        for x in range(x_range[0],x_range[1] + 1):
            if ([x,y,z] in rock_graph):
                block_list.append(1)
                if (len(block_list) > 1):
                    if (block_list[-2] == 0):
                        num_faces += 2
                else:
                    num_faces += 2
            else:
                block_list.append(0)

"""Scanning through y for each x,z"""

for x in range(x_range[0],x_range[1] + 1):
    for z in range(z_range[0],z_range[1] + 1):
        block_list = []
        for y in range(y_range[0],y_range[1] + 1):
            if ([x,y,z] in rock_graph):
                block_list.append(1)
                if (len(block_list) > 1):
                    if (block_list[-2] == 0):
                        num_faces += 2
                else:
                    num_faces += 2
            else:
                block_list.append(0)

"""Scanning through z for each x,y"""

for x in range(x_range[0],x_range[1] + 1):
    for y in range(y_range[0],y_range[1] + 1):
        block_list = []
        for z in range(z_range[0],z_range[1] + 1):
            if ([x,y,z] in rock_graph):
                block_list.append(1)
                if (len(block_list) > 1):
                    if (block_list[-2] == 0):
                        num_faces += 2
                else:
                    num_faces += 2
            else:
                block_list.append(0)

print(num_faces)