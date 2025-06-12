import matplotlib.pyplot as plt
import seaborn as sns
from highlight_text import fig_text, ax_text
from drawarrow import fig_arrow
from pypalettes import load_cmap


import geopandas as gpd


wegen_net = gpd.read_file("data/01-06-2025/Wegvakken/Wegvakken.dbf")

wegen_net.to_parquet("data/wegennet.parquet")

wegen_net.GME_NAAM.sort_values().unique()

utrecht = wegen_net.loc[lambda x: x.GME_NAAM == "Utrecht"]

neonpink = "#FF10F0"

fig, ax = plt.subplots(figsize=(7, 7))
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

(utrecht.plot(color=neonpink, ax=ax, linewidth=0.4))

background = "#232023"

fig.set_facecolor(background)
ax.set_facecolor(background)
ax.axis("off")

fig_text(0.5, 0.93, s="Utrecht", color=neonpink, va="center", ha="center", size=40)


fig_text(
    0.6,
    0.1,
    s="Visualisation: Sebastiaan Broekema\n Source:Nationaal Wegen Bestand",
    color=neonpink,
)

plt.savefig("Utrecht_netwerk.png", dpi=600)
