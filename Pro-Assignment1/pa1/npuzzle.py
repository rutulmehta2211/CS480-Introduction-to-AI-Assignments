from search import *
from file_read import *

input_file = sys.argv[1]
input_file = open(input_file)

search_algo_str = sys.argv[2]

intValues = read_npuzzle_file(input_file)
print(intValues)