def endOverlap(a, b):
    store = ''
    store2 = ''
    for i in range(0, len(a)):
        if b.startswith(a[-i:]):
            # store += a[-i:]
            store = a[-i:]
    for i in range(0, len(b)):
        if a.startswith(b[-i:]):
            # store2 += b[-i:]
            store2 = (b+a[i:])
    if len(store) >= len(store2):
        return store
    else:
        return store2
    # return max(len(store), len(store2))

# print(endOverlap("ACGCATC", "CATGAC"))

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


node, edge = de_bruijn_ize("CCGGTTAAACGTC", 3)
print(node,edge)
print(nodes("CCGGTTAAACGTC",3))
print(edges("CCGGTTAAACGTC",3))