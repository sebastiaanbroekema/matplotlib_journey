import matplotlib.pyplot as plt
import seaborn as sns
from highlight_text import fig_text, ax_text
from drawarrow import fig_arrow
from pypalettes import load_cmap


import pandas as pd

url = url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/mariokart/mariokart.csv"
df = pd.read_csv(url)

cmap = load_cmap("Bay").colors[::-1]

marker = {
    "No": 3,
    "Yes": -3
}

color_mapping = {
    "No": cmap[1],
    "Yes": cmap[0]
}

# color by short cut or not?
first_last = (
    df.loc[lambda x: x.type == "Three Lap"]
    .groupby("track")
    .agg({"time":["first","last"]})
)

first_last

plot_frame = (
    df.loc[lambda x: 
           (x.type == "Three Lap") & 
        #    (x.track == "Wario Stadium")
        (x.track == "Luigi Raceway")
           ]
    .assign(
        location = lambda x: 3 / (x.time / x.time.min()),
        marker_position = lambda x: x.shortcut.map(marker),
        swarm = 0,
        color = lambda x: x.shortcut.map(color_mapping),
        )
)

# short cut and no short cut 
# strip plot? would be fun a real race feel to the plot

fig, ax = plt.subplots()
x = plot_frame['location']
y = plot_frame["marker_position"]
swarm = plot_frame["swarm"]
color = plot_frame['color']

sns.swarmplot(x=x, y = swarm, orient="h",hue=color,palette=cmap[:2],dodge=True)
ax.set_xlim(0,3)
ax.set_ylim(-5,5)
ax.axhspan(-1, 1, alpha=1, color="k")
ax.axhline(0, color='white', linestyle = "--")
ax.axis('off')


plt.show(block=False)