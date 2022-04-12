class Graph:

    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFSUtil(self, temp, v, visited):

        # Mark the current vertex as visited
        visited[v] = True

        # Store the vertex to list
        temp.append(v)

        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if not visited[i]:
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp

        # method to add an undirected edge

    def addEdge(self, v, w):
        self.adj[w].append(v)
        self.adj[v].append(w)

        # Method to retrieve connected components

    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if not visited[v]:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc


def micro_grupos(membros, relacionamentos):
    grafo = Graph(membros+1)
    
    for i in relacionamentos:
        grafo.addEdge(i[0], i[1])

    cc = grafo.connectedComponents()
    print(len(cc) - 1) # Retiro 1 já que a função inicia um nó 0 isolado.


micro_grupos(7, [[1,2],[2,3],[3,1],[3,4],[6,5],[5,7]])