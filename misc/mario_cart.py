import matplotlib.pyplot as plt
import seaborn as sns
from highlight_text import fig_text, ax_text
from drawarrow import ax_arrow
from pypalettes import load_cmap


import pandas as pd

url = url = (
    "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/mariokart/mariokart.csv"
)
df = pd.read_csv(url)

cmap = load_cmap("Bay").colors[::-1]

marker = {"No": 3, "Yes": -3}

color_mapping = {"No": cmap[1], "Yes": cmap[0]}

# color by short cut or not?
first_last = (
    df.loc[lambda x: x.type == "Three Lap"]
    .groupby("track")
    .agg({"time": ["first", "last"]})
)

first_last

plot_frame = df.loc[
    lambda x: (x.type == "Three Lap")
    &
    #    (x.track == "Wario Stadium")
    (x.track == "Luigi Raceway")
].assign(
    location=lambda x: 3 / (x.time / x.time.min()),
    marker_position=lambda x: x.shortcut.map(marker),
    swarm=0,
    color=lambda x: x.shortcut.map(color_mapping),
)

# short cut and no short cut
# strip plot? would be fun a real race feel to the plot

x = plot_frame["location"]
y = plot_frame["marker_position"]
swarm = plot_frame["swarm"]
color = plot_frame["color"]


fig, ax = plt.subplots()
sns.swarmplot(x=x, y=swarm, orient="h", hue=color, palette=cmap[:2], legend=False)
ax.set_xlim(0, 3.05)
ax.set_ylim(-5, 5)
ax.axhspan(-1, 1, alpha=1, color="#c8d6e5", zorder=0)
ax.axhline(1.05, color="red", linestyle="--")
ax.axhline(-1.05, color="red", linestyle="--")

ax.vlines(
    [1, 2, 3], ymin=-1, ymax=1, colors=["white", "white", "white"], linestyles="--"
)

ax.hlines(
    y=[-1.2] * 3,
    xmin=[0.05, 1.05, 2.05],
    xmax=[0.95, 1.95, 2.95],
    colors=["#A3CB38"] * 3,
)
ax.axis("off")

ax_text(s="first lap", x=0.5, y=-1.3, ha="center")
ax_text(s="second lap", x=1.5, y=-1.3, ha="center")
ax_text(s="third lap", x=2.5, y=-1.3, ha="center")

fig_text(
    0.125, 0.8, "Non-shortcut users eat dust on Luigi Raceway\nfastest <shortcut> user is 5× faster than the slowest <non-shortcut> user.", weight="bold", size=14,
    highlight_textprops=[{"color":cmap[1]},{"color":cmap[0]}]
)

ax_text(
    s="Slowest <non-shortcut record> just past halfway on lap 1\n as the fastest shortcut record finishes",
    x=0.4,
    y=1.5,
    ha="center",
    va="bottom",
    size=12,
    highlight_textprops=[{"color": cmap[0]}],
)


ax_arrow(
    tail_position=(0.4, 1.5),
    head_position=(0.570720, 0),
    color=cmap[0],
    head_width=4,
    zorder=20,
    fill_head=False,
)

ax_arrow(
    tail_position=(2.5, 1.5),
    head_position=(3, 0),
    color=cmap[1],
    head_width=4,
    zorder=20,
    fill_head=False,
)

ax_text(
    s="Fastes <shortcut> record finishes compleet track in 25.3 seconds",
    x=2.5,
    y=1.5,
    ha="center",
    va="bottom",
    size=12,
    highlight_textprops=[{"color": cmap[1]}],
)



plt.show(block=False)
