from search import *

def best_first_tree_search(problem, f, display=False):
        print("previous f",f)
        f = memoize(f,'f')
        print("f",f)
        node = Node(problem.initial)
        frontier = PriorityQueue('min',f)
        frontier.append(node)

        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node
            
            for child in node.expand(problem):
                if child not in frontier:
                    frontier.append(child)
                if child in frontier:
                    if f(child) < frontier[child]:
                        del frontier[child]
                        frontier.append(child)

        return None