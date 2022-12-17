inputfile = "Puzzle 7 - input 1.txt"
f = open(inputfile, "r")

def dictReturnFunc(dictionary,key_list):
    if (len(key_list) == 1):
        return dictionary[key_list[0]]
    else:
        return dictReturnFunc(dictionary[key_list[0]],key_list[1:])

def key_file_size(dictionary):
    sum = 0
    for key in dictionary:
        if (type(dictionary[key]) is dict):
            sum += key_file_size(dictionary[key])
        else:
            sum += int(dictionary[key])
    return sum

def files_under_threshold(dictionary,threshold):
    sum = 0
    for key in dictionary:
        if (type(dictionary[key]) is dict):
            sum_temp = key_file_size(dictionary[key])
            if (sum_temp < threshold):
                sum += sum_temp
            sum += files_under_threshold(dictionary[key],threshold)
    return sum

file_structure = {"/":{}}

inside_folder = ["/"]
ls = 0

#print(file_structure)

for line in f:
    #print(line.strip())
    line_list = line.strip().split(" ")
    if (line_list[0] == "$"): # Command
        ls = 0
        if (line_list[1] == "cd"):
            if (line_list[2] == "/"):
                inside_folder = ["/"]
            elif (line_list[2] == ".."):
                inside_folder.pop(len(inside_folder)-1)
            else:
                inside_folder.append(line_list[2])
        elif (line_list[1] == "ls"):
            ls = 1
        else:
            print("Something has gone terribly wrong...")
            print(inside_folder)
            print(line)
            print(line_list)
            break
    elif (ls == 1):
        currentDict = dictReturnFunc(file_structure,inside_folder)
        if (line_list[0] == "dir"):
            if (currentDict.get(line_list[1]) is None):
                currentDict[line_list[1]] = {}
        else:
            if (currentDict.get(line_list[1]) is None):
                currentDict[line_list[1]] = line_list[0]
        for i in range(len(inside_folder)-1,-1,-1):
            if (i == 0):
                file_structure[inside_folder[i]] = currentDict
            else:
                outerDict = dictReturnFunc(file_structure,inside_folder[:i])
                outerDict[inside_folder[i]] = currentDict
                currentDict = outerDict
    else:
        print("Does this happen??")

print(file_structure)

result = files_under_threshold(file_structure,100000)

print(result)