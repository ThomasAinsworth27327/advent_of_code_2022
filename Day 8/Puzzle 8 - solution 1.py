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

visible_sum = 0
for x in range(0,len(tree_grid),1):
    for y in range(0,len(tree_grid[x]),1):
        if ((x == 0) or (x == len(tree_grid)-1) or (y == 0) or (y == len(tree_grid[x])-1)):
            visible_sum += 1
            #print(str(tree_grid[x][y]) + " at x,y: " + str(x) + "," + str(y) + " sum: " + str(visible_sum))
        else:
            visible_list = [True,True,True,True]
            for x1 in range(0,x,1):
                if (tree_grid[x1][y] >= tree_grid[x][y]):
                    visible_list[0] = False
            for x1 in range(x+1,len(tree_grid),1):
                if (tree_grid[x1][y] >= tree_grid[x][y]):
                    visible_list[1] = False
            for y1 in range(0,y,1):
                if (tree_grid[x][y1] >= tree_grid[x][y]):
                    visible_list[2] = False
            for y1 in range(y+1,len(tree_grid[x]),1):
                if (tree_grid[x][y1] >= tree_grid[x][y]):
                    visible_list[3] = False
            if (True in visible_list):
                visible_sum += 1
            #print(str(tree_grid[x][y]) + " at x,y: " + str(x) + "," + str(y) + " sum: " + str(visible_sum) + " list " + str(visible_list))


print(visible_sum)