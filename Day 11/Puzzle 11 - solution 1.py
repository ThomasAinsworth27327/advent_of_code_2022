import math
inputfile = "Puzzle 11 - input 1.txt"
f = open(inputfile, "r")

number_rounds = 20
worry_level_divider = 3
monkey_behaviour = []
monkey_business_list = []

for line in f:
    line_raw = line.strip().split(" ")
    line_list = []
    for e in line_raw:
        line_list.append(e.strip(",:"))
    #print(line_list)
    if (line_list[0] == "Monkey"):
        monkey_behaviour.append([[],[],[],[],[]])
        monkey_business_list.append(0)
        monkey = int(line_list[1])
    elif (line_list[0] == "Starting"):
        for item in line_list[2:]:
            monkey_behaviour[monkey][0].append(int(item))
    elif (line_list[0] == "Operation"):
        for operation in line_list[-3:]:
            try:
                monkey_behaviour[monkey][1].append(int(operation))
            except:
                monkey_behaviour[monkey][1].append(operation)
        if (monkey_behaviour[monkey][1][0] != "old"):
            print("Old not first in operation!!!")
    elif (line_list[0] == "Test"):
        monkey_behaviour[monkey][2].append(int(line_list[-1]))
    elif (line_list[0] == "If"):
        if (line_list[1] == "true"):
            monkey_behaviour[monkey][3].append(int(line_list[-1]))
        elif (line_list[1] == "false"):
            monkey_behaviour[monkey][4].append(int(line_list[-1]))
        else:
            print("THIS SHOULDN'T HAPPEN 1")

for i in range(number_rounds):
    for monkey in range(len(monkey_behaviour)):
        num_remove = len(monkey_behaviour[monkey][0])
        for item in monkey_behaviour[monkey][0]:
            monkey_business_list[monkey] += 1
            if (monkey_behaviour[monkey][1][2] == "old"):
                if (monkey_behaviour[monkey][1][1] == "*"):
                    intermediate_worry = item * item
                elif (monkey_behaviour[monkey][1][1] == "/"):
                    intermediate_worry = item / item
                elif (monkey_behaviour[monkey][1][1] == "+"):
                    intermediate_worry = item + item
                elif (monkey_behaviour[monkey][1][1] == "-"):
                    intermediate_worry = item - item
            else:
                if (monkey_behaviour[monkey][1][1] == "*"):
                    intermediate_worry = item * monkey_behaviour[monkey][1][2]
                elif (monkey_behaviour[monkey][1][1] == "/"):
                    intermediate_worry = item / monkey_behaviour[monkey][1][2]
                elif (monkey_behaviour[monkey][1][1] == "+"):
                    intermediate_worry = item + monkey_behaviour[monkey][1][2]
                elif (monkey_behaviour[monkey][1][1] == "-"):
                    intermediate_worry = item - monkey_behaviour[monkey][1][2]
            new_worry = math.trunc(intermediate_worry / worry_level_divider)
            if (new_worry % monkey_behaviour[monkey][2][0] == 0):
                monkey_behaviour[monkey_behaviour[monkey][3][0]][0].append(new_worry)
            else:
                monkey_behaviour[monkey_behaviour[monkey][4][0]][0].append(new_worry)
        for remove in range(num_remove):
            monkey_behaviour[monkey][0].pop(0)

monkey_business_list.sort()
print(monkey_business_list)
print(monkey_business_list[-1] * monkey_business_list[-2])