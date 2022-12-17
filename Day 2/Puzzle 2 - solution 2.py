import numpy as np

inputfile = "Puzzle 2 - input 1.txt"

scoreList = []
f = open(inputfile, "r")
sum = 0
for line in f:
    opponent = line[0]
    move = line.strip()[-1]
    if (move == "X"):
        sum += 0
        if (opponent == "A"):
            sum += 3
        elif (opponent == "B"):
            sum += 1
        elif (opponent == "C"):
            sum += 2
    elif (move == "Y"):
        sum += 3
        if (opponent == "A"):
            sum += 1
        elif (opponent == "B"):
            sum += 2
        elif (opponent == "C"):
            sum += 3
    elif (move == "Z"):
        sum += 6
        if (opponent == "A"):
            sum += 2
        elif (opponent == "B"):
            sum += 3
        elif (opponent == "C"):
            sum += 1

print(sum)