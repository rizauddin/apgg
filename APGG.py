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
    for i in range(len(strid)):
        size = num[i]
        if size:
            randnums = np.random.random_integers(0, 9, size=size)
            for r in randnums:
                G.add_edge(i,r,weight=np.random.randint(1,100))
    return G

def draw(G):
    # positions for all nodes
    pos = nx.random_layout(G)

    # draw the graph
    nx.draw(G,pos=pos, with_labels=True, with_edge_labels=True)
    edge_weight=dict([((u,v,),int(d['weight'])) 
                      for u,v,d in G.edges(data=True)])
    edge_labels=nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=edge_weight)
