inputfile = "Puzzle 8 - input 1.txt"
f = open(inputfile, "r")

tree_grid = []
line_number = 0

for line_raw in f:
    tree_grid.append([])
    line = line_raw.strip()
    for tree in line:
        tree_grid[line_number].append(int(tree))
    line_number += 1

#print(tree_grid)

visible_max = 0
for x in range(0,len(tree_grid),1):
    for y in range(0,len(tree_grid[x]),1):
        visible_distance = [1,1,1,1]
        for x1 in range(x-1,0,-1):
            if (tree_grid[x1][y] < tree_grid[x][y]):
                #print("x1 " + str(x1) + " " + str(tree_grid[x1][y]))
                visible_distance[0] += 1
            else:
                break
        for x1 in range(x+1,len(tree_grid)-1,1):
            if (tree_grid[x1][y] < tree_grid[x][y]):
                #print("x1 " + str(x1) + " " + str(tree_grid[x1][y]))
                visible_distance[1] += 1
            else:
                break
        for y1 in range(y-1,0,-1):
            if (tree_grid[x][y1] < tree_grid[x][y]):
                #print("y1 " + str(y1) + " " + str(tree_grid[x][y1]))
                visible_distance[2] += 1
            else:
                break
        for y1 in range(y+1,len(tree_grid[x])-1,1):
            if (tree_grid[x][y1] < tree_grid[x][y]):
                #print("y1 " + str(y1) + " " + str(tree_grid[x][y1]))
                visible_distance[3] += 1
            else:
                break
        visible_mult = 1
        for value in visible_distance:
            visible_mult = visible_mult * value
        #print(str(visible_distance) + " = " + str(visible_mult) + " last max = " + str(visible_max) + " at x,y " + str(x) + "," + str(y) + " value " + str(tree_grid[x][y]))
        if visible_mult > visible_max:
            visible_max = visible_mult


print(visible_max)