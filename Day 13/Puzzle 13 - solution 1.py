import ast
inputfile = "Puzzle 13 - input 1.txt"
f = open(inputfile, "r")


def list_compare(left_list, right_list):
    result = None
    #print(f"{left_list}//// {right_list}")
    if (len(left_list) < len(right_list)):
        num_checks = len(left_list)
    else:
        num_checks = len(right_list)
    for j in range(num_checks):
        #print(f"Line 14: {j} {left_list} // {right_list}")
        if ((type(left_list[j]) is list) or (type(right_list[j]) is list)):
            if (type(left_list[j]) is int):
                left_int = [left_list[j]]
            else:
                left_int = left_list[j]
            if (type(right_list[j]) is int):
                right_int = [right_list[j]]
            else:
                right_int = right_list[j]
            result_int = list_compare(left_int, right_int)
            if (result_int is not None):
                result = result_int
                break
        else:
            if (left_list[j] > right_list[j]):
                result = False
                #print(f"Line 31 False: {j}, {left_list} // {right_list}")
                break
            elif (left_list[j] < right_list[j]):
                #print(f"Line 34 True: {j}, {left_list} // {right_list}")
                result = True
                break
    if result is None:
        if (len(left_list) > len(right_list)):
            #print(f"Line 10 False: {left_list} // {right_list}")
            result = False
        elif (len(left_list) < len(right_list)):
            #print(f"Line 38 True: {left_list} // {right_list}")
            result = True
    return result

number_rounds = 20
worry_level_divider = 3
line_list = []

for line in f:
    line_raw = line.strip()
    if line_raw == "":
        continue
    else:
        line_list.append(ast.literal_eval(line_raw))

#print(line_list)
index_pass = []


for i in range(int(len(line_list)/2)):
    index_pass.append(True)
    left_list = line_list[i*2]
    right_list = line_list[i*2+1]
    index_pass[i] = list_compare(left_list, right_list)

sum = 0
for i in range(len(index_pass)):
    if (index_pass[i]):
        sum += i + 1

print(index_pass)
print(sum)
