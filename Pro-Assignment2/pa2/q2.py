from games import *
from file_read import *

input_file = sys.argv[1]
input_file = open(input_file)

letters_dict, new_dict, x_dict, o_dict = read_input_file(input_file)

nterm = 0
nterm_win = 0
nterm_loss = 0
nterm_draw = 0

term = 0
term_win = 0
term_loss = 0
term_draw = 0

ttt = TicTacToe()
state = ttt.initial

for i in new_dict:
    move = i
    state = ttt.result(state, move)
    if not ttt.terminal_test(state):
        nterm+=1
        if(state.utility == 1):
            nterm_win+=1
        elif(state.utility == 0):
            nterm_draw+=1
        else:
            nterm_loss+=1
    else:
        term+=1
        if(state.utility == 1):
            term_win+=1
        elif(state.utility == 0):
            term_draw+=1
        else:
            term_loss+=1

while len(state.moves):
    player = state.to_move
    move = alpha_beta_search(state,ttt)
    state = ttt.result(state, move)
    if not ttt.terminal_test(state):
        nterm+=1
        if(state.utility == 1):
            nterm_win+=1
        elif(state.utility == 0):
            nterm_draw+=1
        else:
            nterm_loss+=1
    else:
        term+=1
        if(state.utility == 1):
            term_win+=1
        elif(state.utility == 0):
            term_draw+=1
        else:
            term_loss+=1

print('How many terminal states are there?')
print(term)
print('In how many of those terminal states does X win?')
print(term_win)
print('In how many of those terminal states does X lose?')
print(term_loss)
print('In how many of those terminal states does X draw?')
print(term_draw)
print('How many non-terminal states are there?')
print(nterm)
print('In how many of those non-terminal states does X have a guranteed win?')
print(nterm_win)
print('In how many of those non-terminal states does X have a guranteed loss?')
print(nterm_loss)
print('In how many of those non-terminal states does X have a guranteed draw?')
print(nterm_draw)
