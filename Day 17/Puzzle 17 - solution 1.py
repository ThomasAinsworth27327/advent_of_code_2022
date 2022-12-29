from copy import deepcopy
import time
inputfile = "Puzzle 17 - input 1.txt"
f = open(inputfile, "r")

class chm:
    def __init__(self):
        self.map = [["+"] + ["-"]*7 + ["+"]]
        for _ in range(3):
            self.map.append(["|"] + ["."]*7 + ["|"])
        self.rock = [[["|",".",".","@","@","@","@",".","|"]],
                    [["|",".",".",".","@",".",".",".","|"],["|",".",".","@","@","@",".",".","|"],["|",".",".",".","@",".",".",".","|"]],
                    [["|",".",".","@","@","@",".",".","|"],["|",".",".",".",".","@",".",".","|"],["|",".",".",".",".","@",".",".","|"]],
                    [["|",".",".","@",".",".",".",".","|"],["|",".",".","@",".",".",".",".","|"],["|",".",".","@",".",".",".",".","|"],["|",".",".","@",".",".",".",".","|"]],
                    [["|",".",".","@","@",".",".",".","|"],["|",".",".","@","@",".",".",".","|"]]]
        self.jet_list = []
        #print(self)
    
    def __repr__(self) -> str:
        string = ""
        for index in range(len(self.map)-1,-1,-1):
            for element in self.map[index]:
                string += element
            string += "\n"
        return string
    
    def input_jets(self,file):
        for line_raw in file:
            line = line_raw.strip()
            for character in line:
                self.jet_list.append(character)
        #print(len(self.jet_list))
    
    def add_rock(self,rock_num):
        rock_sel = self.rock[rock_num]
        for line in rock_sel:
            self.map.append(line)
    
    def falling_range(self,character,find_min = True):
        if (find_min):
            min = len(self.map)
        else:
            min = 1
        max = 0
        for ind in range(len(self.map)-1,-1,-1):
            if (character in self.map[ind]):
                if (ind < min):
                    min = ind
                if (ind > max):
                    max = ind
                    if (not find_min):
                        break
            elif ("#" in self.map[ind] and ind > max):
                if (ind > max):
                    max = ind
        return min, max
    
    def move_rock(self,jet_index):
        #print(jet_index)
        if (self.jet_list[jet_index] == ">"):
            direction = 1
        else:
            direction = -1
        min,max = self.falling_range("@", True)
        move = True
        new_position = deepcopy(self.map[min:max+1])
        for ind in range(min,max+1):
            for index in range(len(self.map[ind])):
                space = str(self.map[ind][index])
                if space == "@":
                    adjacent_space = self.map[ind][index+direction]
                    previous_space = self.map[ind][index-direction]
                    if (adjacent_space != "#" and adjacent_space != "|"):
                        new_position[ind-min][index+direction] = "@"
                        if (previous_space != "@"):
                            new_position[ind-min][index] = "."
                    else:
                        move = False
                        break
        if (move):
            self.map[min:] = deepcopy(new_position)
        #print(self)
    
    def gravity(self):
        min,max = self.falling_range("@", True)
        move = True
        new_position = deepcopy(self.map[min-1:max+1])
        for ind in range(min,max+1):
            for index in range(len(self.map[ind])):
                space = self.map[ind][index]
                if space == "@":
                    below_space = self.map[ind-1][index]
                    if (below_space != "#" and below_space != "-"):
                        new_position[ind-min][index] = "@"
                        new_position[ind-min+1][index] = "."
                    else:
                        move = False
                        break
        if (move):
            self.map[min-1:] = deepcopy(new_position)
        #print(self)
        return move
    
    def reset(self):
        min,max = self.falling_range("@", True)
        for ind in range(min,max+1):
            for index in range(len(self.map[ind])):
                space = self.map[ind][index]
                if space == "@":
                    self.map[ind][index] = "#"
        min,max = self.falling_range("#", False)
        #print(f"{max}, {max+4}, {len(self.map)}")
        if (max + 3 + 1 < len(self.map)):
            l = len(self.map)
            for _ in range(max + 3 + 1, l):
                self.map.pop(-1)
        elif (max + 3 + 1 > len(self.map)):
            l = len(self.map)
            for _ in range(l, max + 3 + 1):
                self.map.append(["|"] + ["."]*7 + ["|"])
        #print(self)
    
    def start(self, num_rocks):
        rock_variations = 5
        jet_index = 0
        for rock in range(num_rocks):
            if (rock%75 == 0):
                print(rock)
            move = True

            self.add_rock(rock % rock_variations)

            
            while move:
                self.move_rock(jet_index)
                move = self.gravity()
                jet_index += 1
                jet_index = jet_index % len(self.jet_list)
                if move is False:
                    self.reset()
        min,max = self.falling_range("#", False)
        return max - min + 1




chamber = chm()

chamber.input_jets(f)

print(chamber.start(2022))

#print(chamber)