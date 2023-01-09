from copy import deepcopy
import time
inputfile = "Puzzle 17 - input 1.txt"
f = open(inputfile, "r")

class chm:
    def __init__(self):
        self.clear()
        self.rock = [[["|",".",".","@","@","@","@",".","|"]],
                    [["|",".",".",".","@",".",".",".","|"],["|",".",".","@","@","@",".",".","|"],["|",".",".",".","@",".",".",".","|"]],
                    [["|",".",".","@","@","@",".",".","|"],["|",".",".",".",".","@",".",".","|"],["|",".",".",".",".","@",".",".","|"]],
                    [["|",".",".","@",".",".",".",".","|"],["|",".",".","@",".",".",".",".","|"],["|",".",".","@",".",".",".",".","|"],["|",".",".","@",".",".",".",".","|"]],
                    [["|",".",".","@","@",".",".",".","|"],["|",".",".","@","@",".",".",".","|"]]]
        self.jet_list = []
        self.rock_variations = 5
        #print(self)
    
    def __repr__(self) -> str:
        string = ""
        for index in range(len(self.map)-1,-1,-1):
            for element in self.map[index]:
                string += element
            string += str(index)
            string += "\n"
        return string
    
    def clear(self):
        self.map = [["+"] + ["-"]*7 + ["+"]]
        for _ in range(3):
            self.map.append(["|"] + ["."]*7 + ["|"])
    
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
    
    def list_compare(self,lista,listb):
        if (len(lista) != len(listb)):
            raise ValueError("List lengths do not match!!")
        for ind in range(len(lista)):
            if (lista[ind] != listb[ind]):
                return False
        return True
    
    def repeat(self):
        min,max = self.falling_range("#",False)
        length = 50
        for start_pattern in range(int(max-length*2),0,-1):
            for start_match in range(int(max-length),start_pattern + length,-1):
                repeat_found = self.list_compare(self.map[start_pattern:start_pattern+length],
                                                    self.map[start_match:start_match+length])
                if repeat_found:
                    print("Repeat found!!")
                    return start_match-start_pattern, start_pattern, start_match
        return None, None, None
    
    def rock_step(self, jet_index,rock):
        move = True
        self.add_rock(rock % self.rock_variations)
        while move:
            self.move_rock(jet_index)
            move = self.gravity()
            jet_index += 1
            jet_index = jet_index % len(self.jet_list)
            if move is False:
                self.reset()
        return jet_index
    
    def start(self, num_rocks):
        jet_index = 0
        rock_start = None
        rock_repeat = None
        for rock in range(num_rocks):
            jet_index = self.rock_step(jet_index,rock)
            if (rock % 250 == 0):
                repeat_length, repeat_start, repeat_match = self.repeat()
            if (repeat_length is not None):
                print(f"Cycle detection returns: {repeat_length}, {repeat_start}, {repeat_match}, {rock}")
                break
            if (rock%100 == 0):
                print(rock)
        self.clear()
        jet_index = 0

        for rock in range(num_rocks):
            jet_index = self.rock_step(jet_index,rock)
            min,max = self.falling_range("#", False)
            if (max >= repeat_start and rock_start is None):
                rock_start = rock
            if (max >= repeat_match and rock_repeat is None):
                rock_repeat = rock
                break
        rock_end = rock_repeat
        rocks_cycle = rock_repeat - rock_start
        rocks_remaining = num_rocks-rock_end
        num_repeats = (rocks_remaining) // (rocks_cycle)
        added_height = num_repeats * repeat_length
        for rock in range(rock_end+num_repeats*rocks_cycle+1,num_rocks):
            jet_index = self.rock_step(jet_index,rock)
        min,max = self.falling_range("#", False)
        print(f"{rock_end}, {rocks_cycle}, {rocks_remaining}, {num_repeats}, {rock_end+num_repeats*rocks_cycle}")
        return max - min + 1 + added_height




chamber = chm()

chamber.input_jets(f)

result = chamber.start(1000000000000)

print(result)
print(result-1514285714288)

#print(chamber)