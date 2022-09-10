from random import randint

def endOverlap(a, b):
    store = ''
    store2 = ''
    for i in range(0, len(a)):
        if b.startswith(a[-i:]):
            # store += a[-i:]
            store = a[-i:]+b
            print("this",a[:]+b[i:])
            # print(b[i:])
    for i in range(0, len(b)):
        if a.startswith(b[-i:]):
            # store2 += b[-i:]
            store2 = (b+a[i:])
            print("this",store2)
    if len(store) >= len(store2):
        return store
    else:
        return store2
    # return max(len(store), len(store2))

endOverlap("ATGAT","CATGA")

# CATGACGCATC

def de_bruijn_ize(st, k):
    edges = []
    nodes = set()
    for i in range(len(st) - k + 1):
        edges.append((st[i:+k-1], st[i+1:i+k]))
        nodes.add(st[i:i+k-1])
        nodes.add(st[i+1:i+k])
    return nodes, edges
def edges(st,num):
    i = 0
    edge_list = []
    while i +num <= len(st):
        sub = st[i:i+num]
        edge_list.append(sub)
        i+=1
    print(*edge_list)
def nodes(st,num):
    i = 0
    edge_list = []
    while i+num-1 <= len(st):
        sub = st[i:i+(num-1)]
        edge_list.append(sub)
        i+=1
    print(*edge_list)


# node, edge = de_bruijn_ize("CCGGTTAAACGTC", 3)
# print(node,edge)
# print(nodes("CCGGTTAAACGTC",3))
# print(edges("CCGGTTAAACGTC",3))


# composition = kmers

def deBruijnGraph(kmers):
    k = len(kmers[0])
    graph = {}
    for i in range(len(kmers)):
        try:
            graph[kmers[i][:-1]].append(kmers[i][1:])
        except:
            graph[kmers[i][:-1]] = [kmers[i][1:]]
    return graph

# graph = deBruijnGraph(sequence_reads)
# print(graph)
# print (*(sorted([key + ' -> ' + ','.join(sorted([v for v in value]))
#                  for key, value in graph.items()])),sep ='\n')
# output = out_string.split('->')

# print("here", endOverlap("CATGA", "ATGAT"))

def find_eulerian_tour(graph): # euluerian cycle problem
    vertices = graph

    print("vertices ", vertices)
    start=[]


    maxGraph=max(graph.keys(), key=int)
    start_vertex=randint(0,int(maxGraph))
    # Choose a starting vertex v and follow a trail of edges from that vertex until returning to v.
    start.append(vertices.keys()[start_vertex])
    print(start)

    stack = [start[0]] # a list containing the vertices in the current tour with unused edges
    tour = [] # a list containing the final tour

    while stack:
        v = stack[-1] # select the starting vertex
        if vertices[v]: # if there are unused edges from the starting vertex
            w = vertices[v][0] # select the vertex connected by the first unused edge
            stack.append(w) # add the new vertex to the stack, to become the new starting vertex
            print("stack ", stack)
            del vertices[v][0]    # delete edge v-w from the graph
        else:
            # if there are no unused edges from the starting vertex, remove it from the stack
            # and add it to the final tour
            tour.append(stack.pop())
    print("--------------------------")
    return tour

# print(find_eulerian_tour())
# def find_eulerian_tour(graph): # euluerian cycle problem
#     vertices = graph
#
#     print "vertices ", vertices
#     start=[]
#
#
#     maxGraph=max(graph.keys(), key=int)
#     start_vertex=randint(0,int(maxGraph))
#     # Choose a starting vertex v and follow a trail of edges from that vertex until returning to v.
#     start.append(vertices.keys()[start_vertex])
#     print start
#
#     stack = [start[0]] # a list containing the vertices in the current tour with unused edges
#     tour = [] # a list containing the final tour
#
#     while stack:
#         v = stack[-1] # select the starting vertex
#         if vertices[v]: # if there are unused edges from the starting vertex
#             w = vertices[v][0] # select the vertex connected by the first unused edge
#             stack.append(w) # add the new vertex to the stack, to become the new starting vertex
#             print("stack ", stack)
#             del vertices[v][0]    # delete edge v-w from the graph
#         else:
#             # if there are no unused edges from the starting vertex, remove it from the stack
#             # and add it to the final tour
#             tour.append(stack.pop())
#     print ("--------------------------")
#     return tour

