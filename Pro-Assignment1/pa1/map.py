from search import *
from file_read import *
from additional_algo import *

if __name__ == '__main__':
	
    input_file = sys.argv[1]
    input_file = open(input_file)

    search_algo_str = sys.argv[2]
    
    graph, heuristic, start_state, end_state = read_travel_input_file(input_file)
    # print(graph)
    # print(heuristic)
    # print(start_state)
    # print(end_state)
    
    class Problem_Class(Problem):
        def actions(self,state):
            print(graph[state])
            self.action = [i[0] for i in graph[state]]
            # print(self.action)
            return self.action

        def result(self,state,action):
            return action

        def path_cost(self,c,state1,action,state2):
            for i in graph[state1]:
                if(i[0] == state2):
                    return c + i[1]

        def value(self, node):
            if(node.state in heuristic):
                return heuristic[node.state]
            else:
                return float('inf')

        def heuristic(self, node):
            if(node.state in heuristic):
                return heuristic[node.state]
            else:
                return float('inf')

    objProblem = Problem_Class(start_state, end_state)

    h = None
    h = memoize(h or objProblem.heuristic,'h')

    if search_algo_str == "BFTS":
        goal_node = breadth_first_tree_search(objProblem)
    elif search_algo_str == "BFGS":
        goal_node = breadth_first_graph_search(objProblem)
    elif search_algo_str == "DFTS":
        goal_node = depth_first_tree_search(objProblem)
    elif search_algo_str == "DFGS":
        goal_node = depth_first_graph_search(objProblem)
    elif search_algo_str == "UCTS":
        goal_node = best_first_tree_search(objProblem, lambda node:node.path_cost)
    elif search_algo_str == "UCGS":
        goal_node = uniform_cost_search(objProblem)
    elif search_algo_str == "GBFTS":
        goal_node = best_first_tree_search(objProblem, lambda node:h(node))
    elif search_algo_str == "GBFGS":
        goal_node = best_first_graph_search(objProblem, lambda node:h(node))
    elif search_algo_str == "ASTS":
        goal_node = best_first_tree_search(objProblem, lambda node:h(node) + node.path_cost)
    elif search_algo_str == "ASGS":
        goal_node = astar_search(objProblem, lambda node:h(node) + node.path_cost)
    else:
        goal_node = None
        print("Invalid search algorithm string. Please enter valid string")

    if goal_node is not None:
        print("Solution path", goal_node.solution())
        print("Solution cost", goal_node.path_cost)
    else:
        print("No solution was found.")
