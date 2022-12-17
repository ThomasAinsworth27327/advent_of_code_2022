inputfile = "Puzzle 14 - input 1.txt"
f = open(inputfile, "r")

rock_graph = [["."]*500]
#print(f"{len(rock_graph)}, {len(rock_graph[0])}")
x = 0
y = 0
sand_source = [500,0]
for line in f:
    line_raw = line.strip().split(" -> ")
    line_list = []
    for xy in line_raw:
        line_list.append(xy.split(","))
    x_old = None
    #print(line_list)
    for y_str,x_str in line_list:
        x = int(x_str)
        y = int(y_str)
        if(len(rock_graph) <= x):
            for i in range(x-len(rock_graph)+1):
                rock_graph.append(["."]*len(rock_graph[0]))
        if(len(rock_graph[0]) <= y):
            #print(f"{x}, {y}, {len(rock_graph)}, {len(rock_graph[0])}")
            for i in range(len(rock_graph)):
                for j in range(y-len(rock_graph[i])+1):
                    rock_graph[i].append(".")
        if (x_old is not None):
            #print(f"{x_old}, {y_old} to {x}, {y}")
            rock_graph[x][y] = "X"
            if (x == x_old):
                direction = int((y-y_old)/abs(y-y_old))
                for j in range(y_old,y+direction,direction):
                    rock_graph[x][j] = "#"
            else:
                direction = int((x-x_old)/abs(x-x_old))
                for i in range(x_old,x+direction,direction):
                    rock_graph[i][y] = "#"
        x_old = x
        y_old = y

rock_graph[sand_source[1]][sand_source[0]] = "+"

for i in range(len(rock_graph[0])):
    no_rock = True
    for j in range(len(rock_graph)):
        if (rock_graph[j][1] != "."):
            no_rock = False
            break
    if (no_rock):
        sand_source[0] -= 1
        for j in range(len(rock_graph)):
            del rock_graph[j][0]
    else:
        break

for j in range(len(rock_graph)):
    rock_graph[j].append(".")

rock_graph.append(["."]*len(rock_graph[0]))
rock_graph.append(["#"]*len(rock_graph[0]))

for line in rock_graph:
    simplified_line = ""
    for character in line:
        simplified_line += character
    print(simplified_line)

new_sand = True
settled_sand = 0

while True:
    if (new_sand):
        new_sand = False
        sand_position = list(tuple(sand_source))
    if (sand_position[0] == len(rock_graph[0]) - 1):
        #print(f"{sand_position} // {len(rock_graph[0])}")
        for j in range(len(rock_graph)):
            if (j != len(rock_graph) - 1):
                rock_graph[j].append(".")
            else:
                rock_graph[j].append("#")
    if (0 == sand_position[0]):
        sand_source[0] += 1
        sand_position[0] += 1
        for j in range(len(rock_graph)):
            if (j != len(rock_graph) - 1):
                rock_graph[j].insert(0,".")
            else:
                rock_graph[j].insert(0,"#")
    if ((len(rock_graph) <= sand_position[1] + 1)):
        #print(f"{sand_position} // {sand_source}")
        break
    elif ((rock_graph[sand_position[1] + 1][sand_position[0]] == ".")):
        sand_position[1] += 1
    elif (rock_graph[sand_position[1] + 1][sand_position[0] - 1] == "."):
        sand_position[1] += 1
        sand_position[0] -= 1
    elif (rock_graph[sand_position[1] + 1][sand_position[0] + 1] == "."):
        sand_position[1] += 1
        sand_position[0] += 1
    elif (sand_position == list(sand_source)):
        settled_sand += 1
        break
    else:
        rock_graph[sand_position[1]][sand_position[0]] = "O"
        settled_sand += 1
        new_sand = True

for line in rock_graph:
    simplified_line = ""
    for character in line:
        simplified_line += character
    print(simplified_line)
print(settled_sand)