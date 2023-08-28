import os
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import re

# Load the CSV file
data_all_groups = pd.read_csv("C:/Users/ylhk/Desktop/optimism_token_transfers_per_group.csv")  # Replace with your actual path

pattern = r'from:\s*"(?P<from_address>0x[a-fA-F0-9]+)".*to:\s*"(?P<to_address>0x[a-fA-F0-9]+)"'

output_directory = "optimism"
os.makedirs(output_directory, exist_ok=True)


def shorten_address(address):
    return address[:6] + '...' + address[-6:]

def plot_graph_for_column(column, index):
    addresses = data_all_groups[column][1].split('<->')
    addresses = [address.strip() for address in addresses]
    G = nx.DiGraph()
    for address in addresses:
        G.add_node(address)
    for row in data_all_groups[column][2:]:
        if isinstance(row, str) and 'from' in row and 'to' in row:
            match = re.search(pattern, row)
            if match:
                from_address = match.group("from_address")
                to_address = match.group("to_address")
                if from_address in addresses and to_address in addresses:
                    G.add_edge(from_address, to_address)
    labels = {node: shorten_address(node) for node in G.nodes()}

    # Create a figure and axis with more control
    fig, ax = plt.subplots(figsize=(14, 10))

    # Check the number of addresses and adjust the layout accordingly
    if len(addresses) >= 30:
        # Divide the addresses based on the given ratios
        first_len = int(len(addresses) * 2/10)
        second_len = int(len(addresses) * 3/10)
        third_len = len(addresses) - first_len - second_len
        shell1 = addresses[:first_len]
        shell2 = addresses[first_len: first_len + second_len]
        shell3 = addresses[first_len + second_len:]
        pos = nx.shell_layout(G, [shell1, shell2, shell3])
    else:
        pos = nx.shell_layout(G)

    nx.draw(G, pos, labels=labels, with_labels=True, node_size=3000, node_color="skyblue", font_size=12, width=2,
            edge_color="gray", arrowsize=20, arrowstyle='-|>', ax=ax)

    # Set the title on the axis, which should provide better control
    ax.set_title(f"Address Relationship for optimism_group{index} with Shell Layout", fontsize=16, pad=20)

    output_path = os.path.join(output_directory, f"optimism_group{index}.png")
    plt.savefig(output_path, bbox_inches='tight')
    plt.close()

# Iterate over all columns and plot graphs
for idx, column in enumerate(data_all_groups.columns, 1):
    plot_graph_for_column(column, idx)
