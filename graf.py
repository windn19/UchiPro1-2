import itertools

import networkx as nx
import matplotlib.pyplot as plt


cities = {'A': (0, 20),
          'B': (15, 24),
          'C': (16, 41),
          'D': (10, 40)}
graph = nx.Graph()
graph.add_nodes_from(cities)
kilometers = {('A', 'B', 15),
              ('B', 'C', 16),
              ('B', 'D', 25),
              ('C', 'D', 14),
              ('D', 'A', 18)}
graph.add_weighted_edges_from(kilometers)
labels = {e: graph.edges[e]['weight'] for e in graph.edges}
print(labels)
p = nx.spring_layout(graph)
print(p)
nx.draw_networkx_nodes(graph, pos=p, node_size=700)
nx.draw_networkx_edges(graph, pos=p, edgelist=list(labels.keys()))
nx.draw_networkx_labels(graph, pos=p, font_size=12)
edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, p, edge_labels)

plt.show()

