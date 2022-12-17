import re
inputfile = "Puzzle 6 - input 1.txt"

f = open(inputfile, "r")
characters_read = 0
num_characters = 5
characters = [""] * num_characters

for line in f:
    for character in line:
        match = 0
        characters_read += 1
        characters =  [character] + characters[:num_characters-1]
        for i in range(len(characters)):
            for i2 in range(len(characters)):
                if (i != i2):
                    if characters[i] == characters[i2]:
                        match = 1
        if "" in characters:
            match = 1
        if (match == 0):
            break

print(characters_read)
print(characters)