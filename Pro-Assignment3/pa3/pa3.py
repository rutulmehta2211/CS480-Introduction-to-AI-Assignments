import sys
from logic import *

if __name__ == '__main__':
    
    input_file = sys.argv[1]
    input_file = open(input_file)

    infoValues = []
    queryValues = []

    def read_example_input_file(input_file):
        flag=0
        current=''
        previous=''
        line = input_file.readline()
        while line!="":
            current = line[0]
            if previous=="#" and current!="#":
                flag=flag+1
            if flag == 1 and not line.startswith("#"):
                boardrow = str(line[0])
                boardcolumn = str(line[2])
            elif flag == 2 and not line.startswith("#"):
                infoValues.append(line)
            elif flag == 3 and not line.startswith("#"):
                queryValues.append(line)
            previous = line[0]
            line = input_file.readline()
        return boardrow, boardcolumn, infoValues, queryValues

    def beep(x, y):
        return Expr('B{x}{y}'.format(x=x,y=y))
    
    def mines(x, y):
        return Expr('M{x}{y}'.format(x=x,y=y))
    
    class MinesKB(PropKB):
        def __init__(self, dimrow, dimcolumn):
            super().__init__()
            self.dimrow = dimrow
            self.dimcolumn = dimcolumn

            for y in range(0, dimcolumn):
                for x in range(0, dimrow):
                    mines_in = list()
                    if x > 0: # West room exists
                        mines_in.append(mines(x - 1, y))
                    if y < dimcolumn - 1: # North room exists
                        mines_in.append(mines(x, y + 1))
                    if x < dimrow - 1: # East room exists
                        mines_in.append(mines(x + 1, y))
                    if y > 0: # South room exists
                        mines_in.append(mines(x, y - 1))
                    self.tell(equiv(beep(x, y), new_disjunction(mines_in)))

    boardrow, boardcolumn, infoValues, queryValues = read_example_input_file(input_file)

    mines_kb = MinesKB(int(boardrow), int(boardcolumn))
    
    for t in infoValues:
        mines_kb.tell(expr(t))

    for q in queryValues:
        ans = mines_kb.ask_if_true(expr(q))
        if ans==True:
            print("Yes")
        else:
            print("No")
