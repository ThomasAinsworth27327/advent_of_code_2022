inputfile = "Puzzle 15 - input 2.txt"
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

#print(sensor_list)
#print(beacon_distance)
#print(beacon_list)
#print(x_range)

line_check = 20
no_beacon = 0
x_range = [0,line_check]
y_range = [0,line_check]
tuning_frequency = "ERROR"

for y in range(y_range[0],y_range[1] + 1):
    x = x_range[0]
    while (True):
        scanned = False
        for index,sensor in enumerate(sensor_list):
            if (abs(sensor[0] - x) + abs(sensor[1] - y) <= beacon_distance[index]):
                scanned = True
                #print(f"{sensor} // {[y,x]} // {beacon_distance[index]} // {beacon_distance[index] - (abs(sensor[0] - x) + abs(sensor[1] - y)) + 1}")
                x += beacon_distance[index] - (abs(sensor[0] - x) + abs(sensor[1] - y)) + 1
                break
        if (y % 1000 == 0):
            print(f"{x} {y}")
        if (not scanned):
            tuning_frequency = x*4000000 + y
            break
        if (x > x_range[1]):
            break
    if (not scanned):
        break

print(tuning_frequency)