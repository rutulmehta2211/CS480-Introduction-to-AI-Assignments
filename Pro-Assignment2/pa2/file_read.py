import sys

letters_dict = dict()
new_dict = dict()
x_dict = dict()
o_dict = dict()

def read_input_file(input_file):
    input_file = input_file.readlines()

    for i, line in enumerate(input_file,start=1):
        for j, letter in enumerate(line.split(),start=1):
            letters_dict[(i, j)] = letter.upper()

    new_dict = {key: value for (key,value) in letters_dict.items() if value!='-'}
    x_dict = {key: value for (key,value) in letters_dict.items() if value=='X'}
    o_dict = {key: value for (key,value) in letters_dict.items() if value=='O'}

    return letters_dict,new_dict,x_dict,o_dict

