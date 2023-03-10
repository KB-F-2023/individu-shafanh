from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.costs = {}
        self.heuristics = {}

    def add_node(self, node):
        self.nodes.add(node)
        if node not in self.edges:
            self.edges[node] = []
        if node not in self.costs:
            self.costs[node] = {}
        if node not in self.heuristics:
            self.heuristics[node] = 0

    def add_edge(self, from_node, to_node, cost):
        self.add_node(from_node)
        self.add_node(to_node)
        self.edges[from_node].append(to_node)
        self.costs[from_node][to_node] = cost

#menghitung / generate SLD dari tiap node ke target
    def add_heuristic(self, node, heuristic):
        self.heuristics[node] = heuristic

#menghitung shortest path dengan menggunakan
#nilai heuristic yang ada / hasil generate SLD
# kemudian ditambahkan dengan cost antar node
def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.edges[current]:
            new_cost = cost_so_far[current] + graph.costs[current][next]
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + graph.heuristics[next]
                frontier.put(next, priority)
                came_from[next] = current

    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()

    return path, cost_so_far[goal]

# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 2)
graph.add_edge('C', 'E', 7)
graph.add_edge('D', 'E', 4)


graph.add_heuristic('A', 7)
graph.add_heuristic('B', 6)
graph.add_heuristic('C', 3)
graph.add_heuristic('D', 3)
graph.add_heuristic('E', 1)

start = 'C'
goal = 'E'
path, cost = a_star_search(graph, start, goal)

print("Shortest path from", start, "to", goal, ":", path)
print("Cost of shortest path:", cost)


"""
In this example, the graph has five nodes (A, B, C, D, and E) and 
six edges with their costs. The add_heuristic method is used to add 
the straight-line distance (SLD) heuristic from each node to the goal node (E). 
The a_star_search function takes the graph, start, and goal as inputs and 
returns the shortest path between start and goal as well as the cost of that path.
 The PriorityQueue data structure is used to keep track of the nodes to explore 
 next based on their estimated total cost (new_cost + heuristic).
"""