inputfile = "Puzzle 21 - input 1.txt"
f = open(inputfile, "r")

data_dict = {}

for index, line_raw in enumerate(f):
    line = line_raw.strip().replace(":","")
    line_list = line.split(" ")
    if (len(line_list) == 2):
        data_dict.update({line_list[0]:int(line_list[1])})
    else:
        data_dict.update({line_list[0]:line_list[1:]})

#print(data_dict)

def monkey_find(key):
    value = data_dict[key]
    #print(value)
    #print(type(value))
    if (type(value) is int):
        return value
    else:
        first_value = monkey_find(value[0])
        second_value = monkey_find(value[2])
    if (value[1] == "+"):
        result = first_value + second_value
    elif (value[1] == "-"):
        result = first_value - second_value
    elif (value[1] == "/"):
        result = first_value / second_value
    elif (value[1] == "*"):
        result = first_value * second_value
    return result

print(monkey_find("root"))