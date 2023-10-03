import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import seaborn as sns
import string

from networkx.drawing.nx_agraph import graphviz_layout

def make_color_map_without_replacement(G):
    color_map = []
    for node in G.nodes():
        if node == 'start':
            color_map.append('white')
        # 1st tertile
        elif node in ['A', 'A3', 'A22', 'A211', 'A12', 'A111',
                      'D', 'D3', 'D22', 'D211', 'D12', 'D111',
                      'C3', 'C2', 'C32', 'C311', 'C22', 'C211', 'C12', 'C121', 'C11', 'C111'
                      'B3', 'B2', 'B32', 'B311', 'B22', 'B211', 'B12', 'B121', 'B11', 'B111']:
            color_map.append('blue')
        else:
            color_map.append('white')
    return color_map

def make_size_map_without_replacement(G):
    size_map = []
    for node in G.nodes():
        if node == 'start':
            size_map.append(4000)
        if len(node) == 1:
            size_map.append(2500)
        if len(node) == 2:
            size_map.append(1000)
        if len(node) == 3:
            size_map.append(500)
        if len(node) == 4:
            size_map.append(250)
    return size_map

def make_lw_map_without_replacement(G):
    lw_map = []
    for node in G.nodes():
        if node == 'start':
            lw_map.append(0)
        else:
            lw_map.append(2)
    return lw_map

def plot_4_marbles_without_replacement():
    # Define the nodes and their hierarchy
    letters = string.ascii_uppercase[:4]
    nodes = [('start', letter) for letter in letters]
    indeces_1 = [1, 2, 3]
    indeces_2 = [1, 2]
    indeces_3 = [1]
    for parent, child in zip(letters, letters):
        for idx_1 in indeces_1:
            nodes.append((parent, f"{parent}{idx_1}"))
            for idx_2 in indeces_2:
                nodes.append((f"{parent}{idx_1}", f"{parent}{idx_1}{idx_2}"))
                for idx_3 in indeces_3:
                    nodes.append((f"{parent}{idx_1}{idx_2}", f"{parent}{idx_1}{idx_2}{idx_3}"))

    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges based on the hierarchy
    for parent, child in nodes:
        G.add_edge(parent, child, weight=100)

    pos = graphviz_layout(G, prog="twopi", args='')
                          #args='-Gsplines=true -Gnodesep=0.6 -Goverlap=scalexy')

    color_map = make_color_map_without_replacement(G)
    size_map = make_size_map_without_replacement(G)
    lw_map = make_lw_map_without_replacement(G)


    # Plot the circular tree layout
    plt.figure(figsize=(12, 12))
    nodes = nx.draw_networkx_nodes(G, 
                                   pos=pos, 
                                   label=False,
                                   node_size=size_map,
                                   node_color=color_map,
                                   node_shape='o',
                                   linewidths=lw_map, 
                                   edgecolors='black')
    edges = nx.draw_networkx_edges(G, pos=pos)
    #labels = nx.draw_networkx_labels(G, 
    #                                 pos=pos)

    plt.axis("equal")
    plt.show()
    
def make_color_map_with_replacement(G):
    color1 = 'blue'
    color2 = 'white'
    color_map = []
    for node in G.nodes():
        if node == 'start':
            color_map.append(color2)
        # 1st tertile
        elif node.startswith('C') and (node.endswith('1') or
                                       node.endswith('2') or
                                       node.endswith('3')):
            color_map.append(color1)
        elif node in ['A','B','L'] or ((node.startswith('A') or
                                       node.startswith('B') or
                                       node.startswith('L')) and 
                                       (node.endswith('1') or
                                        node.endswith('2') or
                                        node.endswith('3'))):
            color_map.append(color1)
        # 2nd tertile
        elif (node.startswith('J') or node.startswith('K')) and (node.endswith('1') or node.endswith('2')):
            color_map.append(color1)
        elif node in ['H','I'] or ((node.startswith('H') or
                                   node.startswith('I')) and 
                                   (node.endswith('1') or
                                    node.endswith('2'))):
            color_map.append(color1)
        # 3rd tertile
        elif (node.startswith('G') or node.startswith('F') or node.startswith('E')) and node.endswith('1'):
            color_map.append(color1)
        elif node == 'D' or (node.startswith('D') and node.endswith('1')):
            color_map.append(color1)
        else:
            color_map.append(color2)
    return color_map
    
def make_size_map_with_replacement(G):
    size_map = []
    for node in G.nodes():
        if node == 'start':
            size_map.append(5000)
        if len(node) == 1:
            size_map.append(2000)
        if len(node) == 2:
            size_map.append(1000)
        if len(node) == 3:
            size_map.append(200)
    return size_map

def plot_4_marbles_with_replacement():

    # Define the nodes and their hierarchy
    letters = string.ascii_uppercase[:12]
    nodes = [('start', letter) for letter in letters]
    indeces_1 = [1, 2, 3, 4]
    indeces_2 = [1, 2, 3, 4]
    for parent, child in zip(letters, letters):
        for idx_1 in indeces_1:
            nodes.append((parent, f"{parent}{idx_1}"))
            for idx_2 in indeces_2:
                nodes.append((f"{parent}{idx_1}", f"{parent}{idx_1}{idx_2}"))

    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes and edges based on the hierarchy
    for parent, child in nodes:
        G.add_edge(parent, child, weight=100)

    pos = graphviz_layout(G, prog="twopi", args='')
                          #args='-Gsplines=true -Gnodesep=0.6 -Goverlap=scalexy')

    color_map = make_color_map_with_replacement(G)
    size_map = make_size_map_with_replacement(G)


    # Plot the circular tree layout
    plt.figure(figsize=(20, 20))
    nodes = nx.draw_networkx_nodes(G, 
                                   pos=pos, 
                                   label=True,
                                   node_size=size_map,
                                   node_color=color_map,
                                   node_shape='o',
                                   linewidths=2, 
                                   edgecolors='black')
    #labels = nx.draw_networkx_labels(G, 
    #                                 pos=pos)
    edges = nx.draw_networkx_edges(G, pos=pos)

    plt.axis("equal")

    #plt.axhline(pos['start'][1], color='black')
    #plt.axvline(pos['start'][0], color='black')
    # Calculate the range for each line segment
    # Set the angle and length of the lines
    angle_1 = 90  # Angle in degrees for the first line
    angle_2 = 210  # Angle in degrees for the second line
    angle_3 = 330  # Angle in degrees for the third line
    length = 20 + max(max(pos[node][0] - pos['start'][0]  for node in pos), 
                  max(pos[node][1] - pos['start'][1]  for node in pos))

    # Calculate the line coordinates
    x_start = pos['start'][0]
    y_start = pos['start'][1]
    x_end_1 = x_start + length * np.cos(np.deg2rad(angle_1))
    y_end_1 = y_start + length * np.sin(np.deg2rad(angle_1))
    x_end_2 = x_start + length * np.cos(np.deg2rad(angle_2))
    y_end_2 = y_start + length * np.sin(np.deg2rad(angle_2))
    x_end_3 = x_start + length * np.cos(np.deg2rad(angle_3))
    y_end_3 = y_start + length * np.sin(np.deg2rad(angle_3))

    # Line 1: 60 degrees
    plt.plot([x_start, x_end_1], [y_start, y_end_1], 'k-', linewidth=2)

    # Line 2: 180 degrees
    plt.plot([x_start, x_end_2], [y_start, y_end_2], 'k-', linewidth=2)

    # Line 3: 300 degrees
    plt.plot([x_start, x_end_3], [y_start, y_end_3], 'k-', linewidth=2)

    plt.show()