import string

inputfile = "Puzzle 3 - input 1.txt"

f = open(inputfile, "r")
alphabet = list(string.ascii_letters)
sum = 0
i = 0
lineList = []
for foo in range(3):
    lineList.append("")
for line in f:
    lineList[i] = line
    if (i != 2):
        i += 1
    else:
        i = 0
        debug = 0
        for letter in lineList[0]:
            if (letter in lineList[1]):
                if (letter in lineList[2]):
                    debug += 1
                    sum += alphabet.index(letter) + 1
                    if (debug > 1):
                        print("OH NOOOOO")
                    break

print(sum)