import sys

graph = dict()
heuristic = dict()
stringValues = []
intValues = []

def read_travel_input_file(input_file):
    flag = 0
    current = ''
    previous = ''
    line = input_file.readline()
    while line!="":
        current = line[0] #First letter of the line stored in current variable
        array = line.split(" ") #Each line splited with the space and stored in list
        if (previous == "#" and current != "#"):
            flag = flag + 1
        if flag == 1 and not line.startswith("#"): #read travel graph
            if (array[0] not in graph):
                graph[array[0]] = []
            graph[array[0]].append([array[1], int(array[3][:-1])])
            if (array[2] == "<>"):
                if (array[1] not in graph):
                    graph[array[1]] = []
                graph[array[1]].append([array[0], int(array[3][:-1])])
        elif flag == 2 and not line.startswith("#"): #read given start-end nodes
            start_state = str(array[0])
            end_state = str(array[1][:-1])
        elif flag == 3 and not line.startswith("#"): #read heuristic functions
            heuristic[array[0]] = (int(array[1].strip('\n')))
        previous = line[0] #First letter of the line stored in previous variable
        line = input_file.readline()

    return graph, heuristic, start_state, end_state #return graph list, heuristic list, start node and end node

def read_npuzzle_file(input_file):
    input_file = input_file.readlines()
    for line in input_file:
        if line.startswith('#'):
            continue
        else:
            stringValues.extend(line.split()) #Each element add to the stringValues list
    
    for i in stringValues: 
        intValues.append(int(i)) #Convert each element of stringValues to integer and stored in intValues list
    
    return intValues #return intValues list