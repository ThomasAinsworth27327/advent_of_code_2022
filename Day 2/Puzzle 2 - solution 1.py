import numpy as np

inputfile = "Puzzle 2 - input 1.txt"

strategyList = [{"X":"A","Y":"B","Z":"C"},
                 {"X":"A","Y":"C","Z":"B"},
                 {"X":"B","Y":"A","Z":"C"},
                 {"X":"B","Y":"C","Z":"A"},
                 {"X":"C","Y":"A","Z":"B"},
                 {"X":"C","Y":"B","Z":"A"},]

scoreList = []
for strategy in strategyList:
    f = open(inputfile, "r")
    sum = 0
    for line in f:
        opponent = line[0]
        move = strategy[line.strip()[-1]]
        if (move == opponent):
            sum += 3
        elif ((opponent == "A") & (move == "B")):
            sum += 6
        elif ((opponent == "B") & (move == "C")):
            sum += 6
        elif ((opponent == "C") & (move == "A")):
            sum += 6
        if (move == "A"):
            sum += 1
        if (move == "B"):
            sum += 2
        if (move == "C"):
            sum += 3
    scoreList.append(sum)


maxScore = max(scoreList)
scoreListSorted = np.sort(scoreList)
print(scoreList.index(maxScore))
print(maxScore)
print(scoreList)
print(scoreListSorted)