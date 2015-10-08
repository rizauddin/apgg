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
    
def generate_graph(id, total_edges=10, directed=False):
    '''Generate a graph with weight using student id.
    Parameters:
        id: Student id
        total_edges: The maximum number of edges.
        directed: Set to True to generate a directed graph.
    Returns:
        A directed/undirected graph with total_edges number of edges.
    '''

    strid = str(id)
    
    #remove duplicates
    vertices = list(set(map(int, strid)))
    
    #initialize undirected or directed graph
    G = nx.DiGraph(id=strid) if directed else nx.Graph(id=strid)
    
    #function to generate weight for an edge
    getweight = lambda a, b: a*b
    
    num_edges = 0
    for vertex in vertices:
        
        #enough edges. stop
        if num_edges == total_edges:
            break
            
        #neglect 0 and 1
        if vertex > 1:
            #generate adjacent vertices
            adjacent_vertices = range(vertex)
            
            #remove zero
            adjacent_vertices = adjacent_vertices[1:]
            
            #add edge incident to vertex and adjacent_vertices 1-by-1
            for adjacent_vertex in adjacent_vertices:
                
                #swap the direction if the current number of edge is odd
                if num_edges % 2:
                    vertex, adjacent_vertex = adjacent_vertex, vertex
                
                #add an edge
                G.add_edge(vertex, adjacent_vertex, 
                           weight=getweight(vertex, adjacent_vertex))
                
                #enough edges. stop
                num_edges += 1      
                if num_edges == total_edges:
                    break
            
    return G

def draw(G, weight='weight'):
    #Draw graph G
	
    # positions for all nodes
    pos = nx.random_layout(G)

    # draw the graph
    nx.draw(G,pos=pos, with_labels=True, with_edge_labels=True)
    edge_weight=dict([((u,v,),int(d[weight])) 
                      for u,v,d in G.edges(data=True)])
    edge_labels=nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=edge_weight)
