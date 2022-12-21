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
    if element[0] -1 < x_range[0]:
        x_range[0] = element[0] - 1
    if element[0] + 1 > x_range[1]:
        x_range[1] = element[0] + 1
    if element[1] - 1 < y_range[0]:
        y_range[0] = element[1] - 1
    if element[1] + 1 > y_range[1]:
        y_range[1] = element[1] + 1
    if element[2] - 1 < z_range[0]:
        z_range[0] = element[2] - 1
    if element[2] + 1 > z_range[1]:
        z_range[1] = element[2] + 1

#print(f"{x_range}, {y_range}, {z_range}")
block_list = []

"""Increase range of each dimension by 1 to ensure that we have a
bounding box of air around the lava"""

for x in range(x_range[0],x_range[1] + 1):
    block_list.append([])
    for y in range(y_range[0],y_range[1] + 1):
        block_list[-1].append([])
        for z in range(z_range[0],z_range[1] + 1):
            # 0 corresponds to air, 1 to lava, 2 to water/steam
            if ([x,y,z] in rock_graph):
                block_list[-1][-1].append(1)
            elif (x == x_range[0] or x == x_range[1] or y == y_range[0] or y == y_range[1] or z == z_range[0] or z == z_range[1]):
                block_list[-1][-1].append(2)
            else:
                block_list[-1][-1].append(0)
#print(block_list)
running = True
while running:
    print("does this happen??")
    num_added_water = 0
    for x in range(len(block_list)):
        for y in range(len(block_list[0])):
            for z in range(len(block_list[0][0])):
                if block_list[x][y][z] == 2:
                    if (x != 0):
                        if (block_list[x-1][y][z] == 0):
                            block_list[x-1][y][z] = 2
                            num_added_water += 1
                    if (y != 0):
                        if (block_list[x][y-1][z] == 0):
                            block_list[x][y-1][z] = 2
                            num_added_water += 1
                    if (z != 0):
                        if (block_list[x][y][z-1] == 0):
                            block_list[x][y][z-1] = 2
                            num_added_water += 1
                    if (x != len(block_list)-1):
                        if (block_list[x+1][y][z] == 0):
                            block_list[x+1][y][z] = 2
                            num_added_water += 1
                    if (y != len(block_list[0])-1):
                        if (block_list[x][y+1][z] == 0):
                            block_list[x][y+1][z] = 2
                            num_added_water += 1
                    if (z != len(block_list[0][0])-1):
                        if (block_list[x][y][z+1] == 0):
                            block_list[x][y][z+1] = 2
                            num_added_water += 1
                elif block_list[x][y][z] == 0:
                    if (x != 0):
                        if (block_list[x-1][y][z] == 2):
                            block_list[x][y][z] = 2
                            num_added_water += 1
                    if (y != 0):
                        if (block_list[x][y-1][z] == 2):
                            block_list[x][y][z] = 2
                            num_added_water += 1
                    if (z != 0):
                        if (block_list[x][y][z-1] == 2):
                            block_list[x][y][z] = 2
                            num_added_water += 1
                    if (x != len(block_list)-1):
                        if (block_list[x+1][y][z] == 2):
                            block_list[x][y][z] = 2
                            num_added_water += 1
                    if (y != len(block_list[0])-1):
                        if (block_list[x][y+1][z] == 2):
                            block_list[x][y][z] = 2
                            num_added_water += 1
                    if (z != len(block_list[0][0])-1):
                        if (block_list[x][y][z+1] == 2):
                            block_list[x][y][z] = 2
                            num_added_water += 1
    print(num_added_water)
    if (num_added_water == 0):
        running = False

#print(block_list)

num_faces = 0

for x in range(len(block_list)):
    for y in range(len(block_list[0])):
        for z in range(len(block_list[0][0])):
            if block_list[x][y][z] == 1:
                if (x != 0):
                    if (block_list[x-1][y][z] == 2):
                        num_faces += 1
                if (y != 0):
                    if (block_list[x][y-1][z] == 2):
                        num_faces += 1
                if (z != 0):
                    if (block_list[x][y][z-1] == 2):
                        num_faces += 1
                if (x != len(block_list)-1):
                    if (block_list[x+1][y][z] == 2):
                        num_faces += 1
                if (y != len(block_list[0])-1):
                    if (block_list[x][y+1][z] == 2):
                        num_faces += 1
                if (z != len(block_list[0][0])-1):
                    if (block_list[x][y][z+1] == 2):
                        num_faces += 1

print(num_faces)