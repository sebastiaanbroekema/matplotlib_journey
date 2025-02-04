import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from pypalettes import load_cmap



url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/netflix/netflix.csv"
df = pd.read_csv(url)

cast = df.cast.str.split(',').explode()

# 'show_id', 'title', 'director', 'cast', 'country', 'date_added',
#        'release_year', 'rating', 'duration', 'listed_in', 'description']

df = df.drop('cast',axis=1).join(cast, how='outer')


grouped = (
    df
    .groupby(["director","cast"])
    .title
    .count()
    .loc[lambda x: x > 2]
    .sort_values(ascending=False)
    .reset_index()
)

cmap = load_cmap("Acadia").colors

graph = nx.from_pandas_edgelist(grouped, "director", "cast", ["title"])
color_dict = {
    True:cmap[0],
    False:cmap[1]
}
director_list = grouped.director.unique().tolist()
color = [color_dict[x in director_list] for x in list(graph.nodes)]
layout = nx.kamada_kawai_layout(graph)
layout2 = nx.shell_layout(graph)
layout3 = nx.spiral_layout(graph)



fig, ax = plt.subplots()



nx.draw(graph,layout , ax=ax, node_color=color, node_size = 5, edge_color = 'grey')

plt.show(block=False)







(
df.groupby(["cast","country"])
.duration.sum()
.sort_values(ascending=False)
.iloc[:10]
.plot(kind='bar')
)

plt.show()