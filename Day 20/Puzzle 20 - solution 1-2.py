inputfile = "Puzzle 20 - input 1.txt"
f = open(inputfile, "r")

class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = self
        self.ind = 0

class CLL:
    def __init__(self):
        self.head = None
        self.count = 0
     
    def __repr__(self):
        string = ""
          
        if(self.head == None):
            string += "Circular Linked List Empty"
            return string
          
        string += f"Circular Linked List:\n{self.head.data}, {self.head.ind}"      
        temp = self.head.next
        while temp != self.head:
            string += f" -> {temp.data}, {temp.ind}"
            temp = temp.next
        return string
     
    def append(self, data):
        self.insert(data, self.count)
        return
     
    def data_index(self, index):
        if (index > self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
             
        if self.head == None:
            raise ValueError(f"There is no data in this linked list. Please add some first.")
         
        temp = self.head
        for _ in range(index):
            temp = temp.next
             
        return temp.data
     
    def insert(self, data, index):
        if (index > self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
             
        if self.head == None:
            if (type(data) == Node):
                self.head = data
            else:
                self.head = Node(data)
                self.head.ind = 0
            self.count += 1
            return
         
        temp = self.head
        for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
            temp = temp.next
             
        aftertemp = temp.next #New node goes between temp and aftertemp
        if (type(data) == Node):
            temp.next = data
        else:
            temp.next = Node(data)
            temp.next.ind = index
        temp.next.next = aftertemp
        if(index == 0):
            self.head = temp.next
        self.count += 1
        return
     
    def remove(self, index):
        if (index >= self.count) | (index < 0):
            raise ValueError(f"Index out of range: {index}, size: {self.count}")
         
        if self.count == 1:
            self.head = None
            self.count = 0
            return
         
        before = self.head
        for _ in range(self.count - 1 if index - 1 == -1 else index - 1):
            before = before.next
        after = before.next.next
        
        return_node = before.next

        before.next = after
        if(index == 0):
            self.head = after
        self.count -= 1
        return return_node
     
    def index(self, data):
        temp = self.head
        for i in range(self.count):
            if(temp.data == data):
                return i
            temp = temp.next
        return None

    def ret_index(self,index):
        temp = self.head
        for i in range(self.count):
            if(temp.ind == index):
                return i
            temp = temp.next
        return None

     
    def size(self):
        return self.count
     
    def display(self):
        print(self)

encrypted_list = CLL()
index_list = []

for index, line_raw in enumerate(f):
    line = line_raw.strip()
    encrypted_list.append(int(line))
    index_list.append(index)

#print(encrypted_list)
#print(index_list)
#encrypted_list.display()

#print(encrypted_list.size())

#for index in range(encrypted_list.size()):
#    print(encrypted_list.ret_index(index))

for index in range(encrypted_list.size()):
    element_index = encrypted_list.ret_index(index)
    element = encrypted_list.remove(element_index)
    new_index = (element_index + element.data) % (encrypted_list.size())
    #print(f"{encrypted_list}, {value}, {index_list[index]}, {new_index}")
    encrypted_list.insert(element,new_index)
    #print(encrypted_list)
    if (index%100 == 0):
        print(index)

starting_point = encrypted_list.index(0)

result = encrypted_list.data_index((starting_point+1000)%(encrypted_list.size())) + encrypted_list.data_index((starting_point+2000)%(encrypted_list.size())) + encrypted_list.data_index((starting_point+3000)%(encrypted_list.size()))

print(result)