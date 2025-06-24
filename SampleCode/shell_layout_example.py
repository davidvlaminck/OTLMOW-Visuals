# shell_layout_pyvis_example.py

from pyvis.network import Network
import networkx as nx

# 1. Create a graph with two shells:
#    - shell 1: nodes [1, 2, 3]
#    - shell 2: nodes [4, 5, 6, 7]
G = nx.Graph()
G.add_nodes_from([1, 2, 3], shell=0)
G.add_nodes_from([4, 5, 6, 7], shell=1)

# Add some edges between and within shells
edges = [
    (1, 2), (2, 3), (3, 1),            # triangle in shell 1
    (4, 5), (5, 6), (6, 7), (7, 4),    # square in shell 2
    (1, 4), (2, 5), (3, 6)             # cross-shell links
]
G.add_edges_from(edges)

# 2. Compute shell layout positions
pos = nx.shell_layout(G)  # dict: node -> (x, y)

# 3. Create a PyVis network and add nodes/edges at those positions
net = Network(height="600px", width="800px", notebook=False)

# Add each node with fixed x,y (scaled for better spacing)
scale = 200
for node, (x, y) in pos.items():
    net.add_node(
        node,
        label=str(node),
        x=x * scale,
        y=y * scale,
        fixed=True  # ensures PyVis doesn’t re-run its physics
    )

# Add edges
for source, target in G.edges():
    net.add_edge(source, target)

# (Optional) Disable physics entirely since positions are fixed
net.toggle_physics(False)

# Generate and open the visualization
net.show("shell_layout.html", notebook=False)
