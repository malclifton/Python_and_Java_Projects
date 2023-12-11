#Assignment 2 Program 2
#Write a program that performs depth-first search (DFS) and breadth-first search (BFS) on a
#given graph. Allow users to input graphs and start traversal from a specified node.
#Create a class Graph in that define the function dfs(start_node) to perform the depth first search
#and print the values of the graph after DFS.
#Create another function bfs(start_node) to perform breadth first search of the original graph and
#print it’s value.
#Take input from the user the start node value

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def breadthfirstsearch(self, s):
        visited = set()
        queue = [s]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(neighbor for neighbor in self.graph.get(node, []) if neighbor not in visited)

    def depthfirstsearch(self, start_node, visited=None):
        if visited is None:
            visited = set()
        print(start_node, end=" ")
        visited.add(start_node)
        for neighbor in self.graph.get(start_node, []):
            if neighbor not in visited:
                self.depthfirstsearch(neighbor, visited)

graph = Graph()

edges = input("Enter the values for your edges (e.g., 1 2, 2 3): ").split(',')
for edge in edges:
    u, v = map(int, edge.split())
    graph.add_edge(u, v)
start = int(input("Enter the start node for traversal: "))
print("Breadth First Search:")
graph.breadthfirstsearch(start)
print("\nDepth First Search:")
graph.depthfirstsearch(start)
