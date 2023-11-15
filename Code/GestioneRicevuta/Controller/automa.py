import networkx as nx
import matplotlib.pyplot as plt

# Definizione dell'automa
states = ['q0', 'q1', 'q2', 'q3', 'q4']
alphabet = ['a', 'b', 'c', 'n']

transitions = {
    'q0': {'a': 'q1', 'c': 'q1'},
    'q1': {'b': 'q2'},
    'q2': {'c': 'q3'},
    'q3': {'b': 'q4'},
    'q4': {'b': 'q4', 'n': 'q0'}
}

initial_state = 'q0'
final_state = 'q4'

# Creazione del grafo
G = nx.DiGraph()

for state in states:
    G.add_node(state, shape='circle', color='lightblue')
    if state == final_state:
        G.nodes[state]['color'] = 'lightgreen'

for source, transitions in transitions.items():
    for symbol, target in transitions.items():
        G.add_edge(source, target, label=symbol)

# Creazione del layout del grafo
pos = nx.spring_layout(G)

# Disegno del grafo
nx.draw_networkx_nodes(G, pos, node_color=[G.nodes[n]['color'] for n in G.nodes])
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): G[i][j]['label'] for i, j in G.edges})

plt.axis('off')
plt.show()
