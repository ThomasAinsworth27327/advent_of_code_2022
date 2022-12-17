import string
inputfile = "Puzzle 12 - input 1.txt"
f = open(inputfile, "r")
alphabet = list(string.ascii_lowercase)

contour_map = []
position = [0,0]
new_position = [0,0]
end_position = [0,0]
x = 0
y = 0
height = 0
width = 0

for line in f:
    x = 0
    contour_map.append([])
    line_raw = line.strip()
    for character in line_raw:
        if (character == "S"):
            position = [x,y]
            character = "a"
        elif (character == "E"):
            end_position = [x,y]
            character = "z"
        contour_map[y].append(character)
        x += 1
    y += 1

height = len(contour_map)-1
width = len(contour_map[0])-1

options_diff = [[1,0],[0,1],[-1,0],[0,-1]]
route_list = []
route_list.append(tuple(position))
steps = 0
move_up = False
move = False
end_direction = [0,0]
for i in range(len(position)):
    end_direction[i] = 

while True:
    steps += 1
    options = [None,None,None,None]
    if (position[0] != width):
        options[0] = alphabet.index(contour_map[position[1]][position[0]+1]) - alphabet.index(contour_map[position[1]][position[0]])
    if (position[1] != height):
        options[1] = alphabet.index(contour_map[position[1]+1][position[0]]) - alphabet.index(contour_map[position[1]][position[0]])
    if (position[0] != 0):
        options[2] = alphabet.index(contour_map[position[1]][position[0]-1])-alphabet.index(contour_map[position[1]][position[0]])
    if (position[1] != 0):
        options[3] = alphabet.index(contour_map[position[1]-1][position[0]])-alphabet.index(contour_map[position[1]][position[0]])
    test = 1
    move = False
    while True:
        for i in range(len(options)):
            if (options == None):
                pass
            elif (options[i] == test):
                for j in range(len(position)):
                    position[j] = tuple(position)[j] + tuple(options_diff)[i][j]
                print(position)
                if (tuple(position) not in route_list):
                    position = new_position
                    route_list.append(tuple(position))
                    move = True
                    break
                else:
                    for j in range(len(position)):
                        position[j] = tuple(position)[j] - tuple(options_diff)[i][j]
        if (move):
            break
        test -= 1
    if (position == end_position):
        break

print(steps)