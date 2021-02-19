from games import *
from file_read import *

input_file = sys.argv[1]
input_file = open(input_file)

letters_dict, new_dict, x_dict, o_dict = read_input_file(input_file)

def gen_to_move():
    if(len(x_dict) > len(o_dict)):
        next_move = 'O'
    else:
        next_move = 'X'
    return next_move

def gen_state(to_move='X', x_positions=[], o_positions=[],utility=0, h=3, v=3):
    moves = set([(x, y) for x in range(1, h+1) for y in range(1, v+1)]) - set(x_positions) - set(o_positions)
    moves = list(moves)
    board = {}
    for pos in x_positions:
        board[pos] = 'X'
    for pos in o_positions:
        board[pos] = 'O'
    return GameState(to_move=to_move, utility=utility, board=board, moves=moves)

class SubTicTacToe(TicTacToe):
    def __init__(self, h=3, v=3, k=3):
        self.h = h
        self.v = v
        self.k = k
        self.initial = gen_state(to_move=gen_to_move(), x_positions=list(x_dict),
                      o_positions=list(o_dict),utility=0)

nterm = 0
nterm_win = 0
nterm_loss = 0
nterm_draw = 0

term = 0
term_win = 0
term_loss = 0
term_draw = 0

ttt = SubTicTacToe()
state = ttt.initial
for i in new_dict: 
    if(ttt.terminal_test(state)):
        term+=1
        break
    if not ttt.terminal_test(state):
        player = state.to_move
        move=i
        board = state.board.copy()
        board[move] = state.to_move
        if(ttt.compute_utility(board,move,player) == 1 or ttt.compute_utility(board,move,player) == -1):
            term+=1
            continue
        else:
            while ttt.terminal_test(state):
                state = ttt.result(state,move)
                if(state.utility == 1 or state.utility == -1):
                    term+=1
                else:
                    
            

