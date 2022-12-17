import re
inputfile = "Puzzle 5 - input 1.txt"

f = open(inputfile, "r")
inputStage = True
sum = 0
for line in f:
    if not ("[" in line):
        listStacks = line.split(" ")
        numStacks = max(listStacks)
        break
#print(numStacks)
stacks = [[] for i in range(int(numStacks))]
f = open(inputfile, "r")
for line in f:
    if (inputStage):
        if ("[" in line):
            listStacks = [line[i+1] for i in range(0, len(line), 4)]
            i = 0
            for element in listStacks:
                if " " not in element:
                    stacks[i].insert(0,element)
                i += 1
        else:
            inputStage = False
    else:
        if (line != "\n"):
            inputList = line.strip().split(" ")
            for i in range(int(inputList[1])):
                stacks[int(inputList[5])-1].insert(len(stacks[int(inputList[5])-1])-i,stacks[int(inputList[3])-1].pop())
result = ""
for i in range(len(stacks)):
    result = result + stacks[i][-1]

print(stacks)
print(result)