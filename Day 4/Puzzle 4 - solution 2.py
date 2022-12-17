import re

inputfile = "Puzzle 4 - input 1.txt"

f = open(inputfile, "r")
sum = 0
for line in f:
    assignmentsInt = []
    assignments = re.split(",|-",line)
    for a in assignments:
        assignmentsInt.append(int(a))
    #print(assignmentsInt)
    if ((assignmentsInt[0] <= assignmentsInt[2]) and (assignmentsInt[1] >= assignmentsInt[3])):
        sum += 1
    elif ((assignmentsInt[0] >= assignmentsInt[2]) and (assignmentsInt[1] <= assignmentsInt[3])):
        sum += 1
    elif ((assignmentsInt[0] <= assignmentsInt[3]) and (assignmentsInt[0] >= assignmentsInt[2])):
        sum += 1
    elif ((assignmentsInt[1] <= assignmentsInt[3]) and (assignmentsInt[1] >= assignmentsInt[2])):
        sum += 1

print(sum)