#Malia Clifton
#Lab 10
#Problem 1
#Check if the string has balanced parentheses or not.
#Input: “(([])” Output: false    Input: “(){(())}”  Output: true

def is_balanced(user):
    stack = []
    for char in user:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False 
            top = stack.pop()
            if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                return False  
    return not stack  
print("\n")
while True:
    user = input("Enter a string or enter quit: ")
    if user.lower() == "quit":
        break
    result = is_balanced(user)
    if result:
        print("Output: true")
    else:
        print("Output: false")
        
print("\n")

#Problem 2
#There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.
#You are given a 2D integer array of edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
#Input: edges = [[1,2],[2,3],[4,2]] Output: 2    Input: edges = [[1,2],[5,1],[1,3],[1,4]] Output: 1

def findCenter(edges):
    node_count = {}
    for edge in edges:
        for node in edge:
            if node in node_count:
                node_count[node] += 1
            else:
                node_count[node] = 1
    n = len(edges) + 1
    for node, count in node_count.items():
        if count == n - 1:
            return node
     
while True:
    edges = []
    n = int(input("Enter the number of edges: "))
    print("Enter the value of your edges (ex.1,2):")
    for i in range(n):
        u, v = map(int, input().split(","))
        edges.append([u, v])
    center = findCenter(edges)
    print("The center of the given star graph: ", center)
    m= input("Continue? y/n  ")
    if m.lower() == "n":
        break
