inputfile = "Puzzle 20 - input 1.txt"
f = open(inputfile, "r")

encrypted_list = []
index_list = []

for index, line_raw in enumerate(f):
    line = line_raw.strip()
    encrypted_list.append(int(line))
    index_list.append(index)

#print(encrypted_list)
#print(index_list)

print(len(encrypted_list))

for index in range(len(encrypted_list)):
    new_index = (index_list[index] + encrypted_list[index_list[index]]) % (len(index_list) - 1)
    if (new_index > index_list[index]):
        for i in range(index_list[index]+1,new_index+1):
            index_list[index_list.index(i)] = i-1
    if (new_index < index_list[index]):
        for i in range(new_index,index_list[index]):
            index_list[index_list.index(i)] = i+1
    #print(f"{encrypted_list}, {value}, {index_list[index]}, {new_index}")
    encrypted_list.insert(new_index,encrypted_list.pop(index_list[index]))
    index_list[index] = new_index
    #print(encrypted_list)
    if (index%100 == 0):
        print(index)

starting_point = encrypted_list.index(0)

result = encrypted_list[(starting_point+1000)%(len(encrypted_list))] + encrypted_list[(starting_point+2000)%(len(encrypted_list))] + encrypted_list[(starting_point+3000)%(len(encrypted_list))]

print(result)