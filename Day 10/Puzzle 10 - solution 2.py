inputfile = "Puzzle 10 - input 1.txt"
f = open(inputfile, "r")

cycle_count = 0
addr = 1
addr_val = 1
x = 1
signal_strength = 0
crt_screen = [""]
line_num = 0

for line in f:
    #print(line.strip())
    line_list = line.strip().split(" ")
    if (line_list[0] == "noop"):
        addr = 1
    elif (line_list[0] == "addx"):
        addr_val += int(line_list[1])
        addr = 2
    for i in range(addr):
        cycle_count += 1
        if ((cycle_count > 1) and ((cycle_count-1) % 40 == 0)):
            line_num += 1
            crt_screen.append("")
        if (((cycle_count-1) % 40 <= x + 1) and ((cycle_count-1) % 40 >= x - 1)):
            crt_screen[line_num] = crt_screen[line_num] + "#"
        else:
            crt_screen[line_num] = crt_screen[line_num] + "."
        #print(f"{crt_screen}, {cycle_count}, {x}")
        if ((i == 1) and (addr == 2)):
            x = addr_val

for line in crt_screen:
    print(line)