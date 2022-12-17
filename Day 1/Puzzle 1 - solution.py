import numpy as np

inputfile = "Puzzle 1 - input 1.txt"

f = open(inputfile, "r")
sum = 0
caloriesList = []
for line in f:
    if (line != "\n"):
        sum += int(line)
    else:
        caloriesList.append(sum)
        sum = 0

maxCalories = max(caloriesList)
caloriesListSorted = np.sort(caloriesList)
print(caloriesList.index(maxCalories))
print(maxCalories)
print(caloriesListSorted)

finalSum = caloriesListSorted[-1] + caloriesListSorted[-2] + caloriesListSorted[-3]

print(finalSum)