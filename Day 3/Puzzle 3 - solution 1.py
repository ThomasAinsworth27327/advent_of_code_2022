import string

inputfile = "Puzzle 3 - input 1.txt"

f = open(inputfile, "r")
alphabet = list(string.ascii_letters)
print(alphabet)
sum = 0
for line in f:
    i = 0
    firstHalf = line[:len(line.strip())//2]
    secondHalf = line[len(line.strip())//2:]
    #print(line + " = " + firstHalf + " + " + secondHalf)
    for letter in firstHalf:
        if (letter in secondHalf):
            i += 1
            sum += alphabet.index(letter) + 1
            if (i > 1):
                print("OH NOOOO")
            break

print(sum)