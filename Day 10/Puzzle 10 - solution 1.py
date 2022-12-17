inputfile = "Puzzle 10 - input 1.txt"
f = open(inputfile, "r")

cycle_count = 0
addr = 1
addr_val = 1
x = 1
signal_strength = 0

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
        if ((cycle_count == 20) or (((cycle_count-20)%40) == 0)):
            signal_strength += cycle_count * x
        if ((i == 1) and (addr == 2)):
            x = addr_val

print(signal_strength)