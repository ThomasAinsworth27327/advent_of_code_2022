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

def monkey_find(key, find_human = False):
    value = data_dict[key]
    #print(value)
    #print(type(value))
    if find_human:
        if (type(value) is int):
            return False
        if (value is None):
            return True
    if (type(value) is int):
        return value
    else:
        first_value = monkey_find(value[0], find_human)
        second_value = monkey_find(value[2], find_human)
    if find_human:
        result = first_value or second_value
    else:
        if (value[1] == "+"):
            result = first_value + second_value
        elif (value[1] == "-"):
            result = first_value - second_value
        elif (value[1] == "/"):
            result = first_value / second_value
        elif (value[1] == "*"):
            result = first_value * second_value
    return result

def equation_find(key):
    value = data_dict[key]
    #print(value)
    #print(type(value))
    if (type(value) is int):
        return value
    else:
        first_value = monkey_find(value[0])
        second_value = monkey_find(value[2])
    return [first_value,value[1],second_value]

me = "humn"
data_dict[me] = None
monkey1 = monkey_find(data_dict["root"][0],True)
monkey2 = monkey_find(data_dict["root"][2],True)

if (monkey1):
    monkey2_element = 0
    monkey1 = monkey_find(data_dict["root"][2])
else:
    monkey2_element = 2
    monkey1 = monkey_find(data_dict["root"][0])

shout = 2**32
index = 32

while True:
    data_dict[me] = shout
    monkey2 = monkey_find(data_dict["root"][monkey2_element])
    if (monkey1 == monkey2):
        print("")
        print(f"Result is: {shout}")
        break
    shout += 1
    if (shout % 1000 == 0):
        print(f"Running value: {shout}", end="\r")