#!/usr/bin/env python
'''
Generate a graph with weight using student id
with a fix predefined number of edges.
Draw a graph with matplotlib.
Must have matplotlib and NetworkX for this to work.
'''
__author__ = """Rizauddin Saian (rizauddin@perlis.uitm.edu.my)"""

try:
    import matplotlib.pyplot as plt
    import networkx as nx
except:
    raise

def generate_flow(id):
    '''Generate a network flow with capacity using student id.
    's': source
    't': sink
    
    Parameters:
        id: Student id
    Returns:
        A directed network flow.
    '''
    strid = str(id)

    # In Python 3, map returns an iterable object of type map, 
    # and not a subscriptible.
    # Need to force a list.
    nodes = list(map(lambda n: float(n) if float(n) else 1.0, strid))
    #nodes = map(lambda n: float(n) if float(n) else 1.0, strid)

    L = nx.DiGraph()

    L.add_edge('s','a', capacity=nodes[0])
    L.add_edge('s','b', capacity=nodes[1])
    L.add_edge('a','c', capacity=nodes[2])
    L.add_edge('b','c', capacity=nodes[3])
    L.add_edge('b','d', capacity=nodes[4])
    L.add_edge('d','e', capacity=nodes[5])
    L.add_edge('e','f', capacity=nodes[5])
    L.add_edge('f','t', capacity=nodes[5])
    L.add_edge('c','t', capacity=nodes[6])
    L.add_edge('e','t', capacity=nodes[7])
   
    return L

def generate_graph(id=2015234031):
    '''Parameters:
        id: Student id
    Returns:
        A graph.
    '''
    #Generating edges. Assign to next vertex if v_i=id_i
    edges = []
    for v, id in enumerate(map(int, str(2013567257))):
        if v == id:
            edges.append((v, v+1))
        else:
            edges.append((v, id))
    
    #initialize graph
    G = nx.Graph()

    #function to generate weight for an edge
    getweight = lambda a, b: a*b if a*b else 1
    
    for u, v in edges:
        #add an edge
        G.add_edge(u, v, weight=getweight(u, v))
        
    return G
   

def draw(G, weight='weight'):
    '''Draw graph G
    '''
    
    # positions for all nodes
    pos = nx.random_layout(G)

    # draw the graph
    nx.draw(G,pos=pos, with_labels=True, with_edge_labels=True)
    edge_weight=dict([((u,v,),int(d[weight])) 
                      for u,v,d in G.edges(data=True)])
    edge_labels=nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=edge_weight)
