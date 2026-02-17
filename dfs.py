graph={1:[2,3,4],
       2:[5,6],
       3:[],
       4:[7,8],
       5:[9,10],
       6:[],
       7:[11,12],
       8:[],
       9:[],
       10:[],
       11:[],
       12:[]}
visited=[] #list for visited nodes
stack=[]
def dfs_stack(visited, graph, node):
    stack.append(node)
    while stack:
        m=stack.pop()
        if m not in visited:
            print(m,end=" ")
            visited.append(m)
            for neighbour in reversed(graph[m]):
                if neighbour not in visited:
                    stack.append(neighbour)
print("following is the dfs using stack")
dfs_stack(visited, graph, 1)