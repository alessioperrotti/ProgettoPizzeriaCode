import networkx as nx
import matplotlib.pyplot as plt


def create_fsm():
    states = ['q0', 'q1', 'q2', 'q3']
    alphabet = ['0', '1']

    transitions = {
        'q0': {'0': 'q0', '1': 'q1'},
        'q1': {'0': 'q0', '1': 'q2'},
        'q2': {'0': 'q3', '1': 'q1'},
        'q3': {'0': 'q0', '1': 'q1'}
    }

    initial_state = 'q0'
    accepting_state = 'q3'

    return states, alphabet, transitions, initial_state, accepting_state


def visualize_fsm(states, transitions):
    G = nx.DiGraph()

    for state in states:
        G.add_node(state, shape='circle', color='lightblue')
        if state == accepting_state:
            G.nodes[state]['color'] = 'lightgreen'

    for source, transitions in transitions.items():
        for symbol, target in transitions.items():
            G.add_edge(source, target, label=symbol)

    pos = nx.spring_layout(G)

    nx.draw_networkx_nodes(G, pos, node_color=[G.nodes[n]['color'] for n in G.nodes])
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): G[i][j]['label'] for i, j in G.edges})

    plt.axis('off')
    plt.show()


def run_fsm(sequence, initial_state, transitions, accepting_state):
    current_state = initial_state
    occurrences = 0

    for symbol in sequence:
        if symbol in transitions[current_state]:
            current_state = transitions[current_state][symbol]
        else:
            break  # Invalid symbol, reset state

        if current_state == accepting_state:
            occurrences += 1
            current_state = initial_state  # Reset state after recognizing the sequence

    return occurrences


# Definizione e visualizzazione dell'automa
states, alphabet, transitions, initial_state, accepting_state = create_fsm()
visualize_fsm(states, transitions)

# Sequenza di input
input_sequence = "010001100011101"

# Esecuzione dell'automa sulla sequenza di input
occurrences = run_fsm(input_sequence, initial_state, transitions, accepting_state)

# Verifica delle occorrenze della sequenza "100"
print(f"Numero di occorrenze della sequenza '100': {occurrences}")
