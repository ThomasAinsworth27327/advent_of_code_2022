inputfile = "Puzzle 15 - input 1.txt"
f = open(inputfile, "r")

rock_graph = [["."]*500]
#print(f"{len(rock_graph)}, {len(rock_graph[0])}")
x = 0
y = 0
sand_source = [500,0]
sensor_list = []
beacon_distance = []
beacon_list = []
x_range = [0,0]
for line_raw in f:
    line_short = line_raw.replace(",","")
    line_short = line_short.replace(":","")
    line = line_short.strip().split(" ")
    sx,sy = [0,0]
    sensor = True
    bx,by = [0,0]
    for element in line:
        if (sensor):
            if ("x=" in element):
                sx = int(element[2:])
            if ("y=" in element):
                sy = int(element[2:])
                sensor = False
        else:
            if ("x=" in element):
                bx = int(element[2:])
            if ("y=" in element):
                by = int(element[2:])
                sensor = False
    sensor_list.append([sx,sy])
    beacon_distance.append(abs(bx-sx)+abs(by-sy))
    if ([bx,by] not in beacon_list):
        beacon_list.append([bx,by])
    if (sx - (abs(bx-sx)+abs(by-sy)) < x_range[0]):
        x_range[0] = sx - (abs(bx-sx)+abs(by-sy))
    if (bx - (abs(bx-sx)+abs(by-sy)) < x_range[0]):
        x_range[0] = bx - (abs(bx-sx)+abs(by-sy))
    if (sx + (abs(bx-sx)+abs(by-sy)) > x_range[1]):
        x_range[1] = sx + (abs(bx-sx)+abs(by-sy))
    if (bx + (abs(bx-sx)+abs(by-sy)) > x_range[1]):
        x_range[1] = bx + (abs(bx-sx)+abs(by-sy))

print(sensor_list)
print(beacon_distance)
print(beacon_list)
print(x_range)

line_check = 2000000
no_beacon = 0

for x in range(x_range[0],x_range[1] + 1):
    if ([x,line_check] in beacon_list):
        pass
    else:
        for index,sensor in enumerate(sensor_list):
            if (abs(sensor[0] - x) + abs(sensor[1] - line_check) <= beacon_distance[index]):
                #print(f"{x}, {sensor}, {beacon_distance[index]}")
                no_beacon += 1
                #if (no_beacon % 10000 == 0):
                    #print(f"{no_beacon}, {x}, {sensor}, {beacon_distance[index]}")
                break

print(no_beacon)