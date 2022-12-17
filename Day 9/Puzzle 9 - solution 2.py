inputfile = "Puzzle 9 - input 1.txt"
f = open(inputfile, "r")

def listDiff(list1,list2):
    result = list()
    for e1, e2 in zip(list1,list2):
        result.append(e1-e2)
    return result

string_grid = [["s"]]
start_coord = [0,0]
rope_coord = []
number_knots = 10
for i in range(number_knots):
    rope_coord.append([0,0])
tail_coord_list = []
tail_coord_list.append(tuple(start_coord))
tail_places = 1
steps = 0
#print(len(rope_coord)-1)
for line in f:
    #print(line.strip())
    line_list = line.strip().split(" ")
    if (line_list[0] == "R"):
        direction = 1
        head_element = 0
    elif (line_list[0] == "L"):
        direction = -1
        head_element = 0
    elif (line_list[0] == "U"):
        direction = 1
        head_element = 1
    else:
        direction = -1
        head_element = 1
    for foo in range(int(line_list[1])):
        rope_coord[0][head_element] = rope_coord[0][head_element] + direction
        for j in range(1,len(rope_coord),1):
            list_diff = listDiff(rope_coord[j-1], rope_coord[j])
            for k in range(len(rope_coord[j])):
                if any(abs(diff) > 1 for diff in list_diff):
                    if list_diff[k] != 0:
                        rope_coord[j][k] = rope_coord[j][k] + int(list_diff[k] / abs(list_diff[k]))
            if (j == len(rope_coord)-1):
                #print(rope_coord[j])
                if all(tuple(rope_coord[j]) != element for element in tail_coord_list):
                    tail_coord_list.insert(0,tuple(rope_coord[j]))
                    tail_places += 1
            #print("tail_coord:" + str(rope_coord[1]) + " head_coord:" +  str(rope_coord[0]) + " tail_coord_list:" +  str(tail_coord_list))
            steps += 1

#print(tail_coord_list)
print(tail_places)