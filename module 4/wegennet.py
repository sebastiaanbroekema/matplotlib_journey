import matplotlib.pyplot as plt
import seaborn as sns
from highlight_text import fig_text, ax_text
from drawarrow import fig_arrow
from pypalettes import load_cmap
from pyfonts import load_google_font

import geopandas as gpd


COORDINATES = """
52° 5' 34.3536'' N 
  5° 6' 16.1280'' E
"""

gemeenten = gpd.read_parquet('data/gemeenten_zonder_water.parquet')

utrecht_gemeente = gemeenten.loc[lambda x: x.gemeentenaam == "Utrecht"].geometry.iloc[0]

bold = load_google_font("Economica", weight="bold")
regular = load_google_font("Economica")

# wegen_net = gpd.read_file("data/01-06-2025/Wegvakken/Wegvakken.dbf")

# wegen_net.to_parquet("data/wegennet.parquet")

wegen_net = gpd.read_parquet("data/wegennet.parquet")

wegen_net.GME_NAAM.sort_values().unique()

utrecht = (
    wegen_net.loc[lambda x: x.geometry.within(utrecht_gemeente, align=False)]
)

neonpink = "#FF10F0"

fig, ax = plt.subplots(figsize=(7, 7))
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

(utrecht.plot(color=neonpink, ax=ax, linewidth=0.4))

background = "#232023"

fig.set_facecolor(background)
ax.set_facecolor(background)
ax.axis("off")

fig_text(0.5, 0.93, s="Utrecht", color=neonpink, va="center", ha="right", size=40,  font=bold)
fig_text(0.51, 0.93, s=COORDINATES, color=neonpink, va="center", ha="left", size=16,  font=bold)

fig_text(
    0.6,
    0.1,
    s="Visualisation: Sebastiaan Broekema\nSource: Nationaal Wegen Bestand",
    color=neonpink,
    font=bold
)

plt.savefig("Utrecht_netwerk.png", dpi=600)
plt.close()