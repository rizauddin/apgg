#!/usr/bin/env python
"""
Generate a graph with weight.
Draw a graph with matplotlib.
You must have matplotlib for this to work.
"""
__author__ = """Rizauddin Saian (rizauddin@perlis.uitm.edu.my)"""

import networkx as nx
import numpy as np
try:
    import matplotlib.pyplot as plt
except:
    raise

def generate_graph(id):
    strid = str(id)
    num = [int(i) for i in strid]
    G = nx.Graph(id=strid)
    for i in xrange(len(strid)):
        size = num[i]
        if size:
            randnums = np.random.random_integers(0, 9, size=size)
            for r in randnums:
                G.add_edge(i,r,weight=np.random.randint(1,100))
    return G

def draw(G):
    #pos=nx.spring_layout(G) # positions for all nodes
    pos = nx.random_layout(G)
    
    # nodes
    nx.draw_networkx_nodes(G,pos,node_size=600,alpha=0.8)

    # edges
    nx.draw_networkx_edges(G,pos,width=3,alpha=0.5,edge_color='b')

    # labels
    nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
    
    plt.axis('off')
    plt.show()
