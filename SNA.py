import json
import networkx as nx
import pandas as pd


with open('./final.json', 'r') as f:
    emails = json.load(f)

edges = []

# builds list of edges from JSON
for email in emails:
    sender = emails[email]['Sender']
    recipients = emails[email]['Recipients']

    if len(recipients) > 1:
        for r in recipients:
            edge = (sender, r, {'ID' : email + str(recipients.index(r))})
            edges.append(edge)
    else:
        edge = (sender, recipients[0], {'ID' : email})
        edges.append(edge)


# Creating graph
G = nx.Graph()
# Adding edges
G.add_edges_from(edges)


print('Nodes: \t' + str(len(list(G.nodes))))
print('Edges: \t' + str(len(list(G.edges))))
print('Avg Clustering: \t' + str(nx.average_clustering(G)))
print('Connected Components: \t' + str(nx.number_connected_components(G)))
print('Diameter: \t' + str(nx.diameter(G)))
print('Radius: \t' + str(nx.radius(G)))
print('Avg Shortest Path Length: \t' + str(nx.average_shortest_path_length(G)))
# print('Avg Neighbor Degree: \t' + str(nx.average_neighbor_degree(G)))
print('Density: \t' + str(nx.density(G)))


# Calculating centrality
degCent = dict(nx.degree_centrality(G))
evCent = dict(nx.eigenvector_centrality(G))
closeCent = dict(nx.closeness_centrality(G))
btwCent = dict(nx.betweenness_centrality(G))

dfList = []

# Creating list of dictionaries for pd dataframe
for node in list(G.nodes):
    tmp = {}

    tmp['Address'] = node
    tmp['Degree'] = degCent[node]
    tmp['Eigenvector'] = evCent[node]
    tmp['Betweenness'] = btwCent[node]
    tmp['Closeness'] = closeCent[node]

    dfList.append(tmp)

# # Creating dataframe
df = pd.DataFrame.from_dict(dfList)

# print(df.head())
df.to_csv('out.csv', index=False)