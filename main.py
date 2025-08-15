import csv, networkx as nx

file_nodes = []
graph = nx.Graph()

with open('index.csv') as index:
    reader = csv.reader(index)

    for row in reader:
        entity = row[0]
        kind = row[1]

        if len(row) > 2:
            file_nodes.append((entity, f"data/{row[2]}"))

        graph.add_node(entity, kind=kind)

for region, path in file_nodes:
    with open(path) as file:
        reader = csv.reader(file)

        for row in reader:
            treaty = row[0]
            partner = row[1]

            graph.add_edge(region, partner, treaty=treaty)

nx.write_gexf(graph, "regionweb.gexf")