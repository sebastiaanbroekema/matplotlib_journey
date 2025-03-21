import matplotlib.pyplot as plt
import seaborn as sns
from highlight_text import fig_text, ax_text
from drawarrow import fig_arrow
import matplotlib.patches as patches
from matplotlib import style
from mapclassify import Quantiles
import geopandas as gpd
import pandas as pd

from pyfonts import load_font

regular = {
    "font": load_font(
        "https://github.com/hafontia-zz/Assistant/blob/master/Fonts/TTF/Assistant-Regular.ttf?raw=true"
    )
}

bold = {
    "font": load_font(
        "https://github.com/hafontia-zz/Assistant/blob/master/Fonts/TTF/Assistant-ExtraBold.ttf?raw=true"
    )
}

style.use("fast")
utrecht = gpd.read_parquet("data/winkels_utrecht.parquet")


# make 5 quantiles
# on cat is 0 shops it's own color
quantiles = Quantiles(utrecht.loc[lambda x: x.amount > 0, "amount"], k=5)

#     Interval        Count
# -------------------------
# [  1.00,   5.00] | 236231
# (  5.00,  10.00] | 176254
# ( 10.00,  18.00] | 199852
# ( 18.00,  39.00] | 208897
# ( 39.00, 514.00] | 198077


quantile_labels = [
    "No shops",
    "1 to 5 shops",
    "6 to 10 shops",
    "11 to 15 shops",
    "16 to 20 shops",
    "20+ shops",
]


quantile_bins = [1, 5, 10, 15, 20, 2500]

utrecht = utrecht.assign(
    quantile_values=pd.cut(
        utrecht.amount, [1, *quantiles.bins], labels=quantile_labels[1:]
    )
    .astype(str)
    .replace("nan", quantile_labels[0])
)

utrecht = utrecht.assign(
    quantile_values=pd.cut(utrecht.amount, quantile_bins, labels=quantile_labels[1:])
    .astype(str)
    .replace("nan", quantile_labels[0])
)

# second to last is the grey one
# red, orange, yellow, teal, grey, dark blue
# D72000FF, #EE6100, #FFAD0A, #1BB6AF, #9093A2, #132157

# colors = ("#9093A2", "#D72000", "#EE6100", "#FFAD0A", "#1BB6AF", "#132157")
# colors = ("#9093A2", "#132157", "#1BB6AF", "#FFAD0A", "#EE6100", "#D72000")
colors = ("#badbdb", "#dedad2", "#e4bcad", "#df979e", "#d7658b", "#c80064")
text_color = "#f1f2f6"
# background="#2f3542"
background = "#1e272e"
background = "#060C0C"

color_dict = {i: j for i, j in zip(quantile_labels, colors)}


bar_frame = (
    utrecht.quantile_values.value_counts()
    .reindex(quantile_labels[::-1])
    .reset_index()
    .assign(color=lambda x: x.quantile_values.map(color_dict))
)
total_houses = bar_frame["count"].sum()


utrecht = utrecht.assign(color=lambda x: x.quantile_values.map(color_dict))


fig, ax = plt.subplots(figsize=(20, 15))

ax.axis("off")
(
    utrecht
    # .sample(frac=0.2)
    .plot(
        ax=ax,
        legend=False,
        color=utrecht.color,
        zorder=-5,
    )
)
rect = patches.Rectangle(
    (0.60, -0.1),
    0.5,
    0.5,
    linewidth=0,
    facecolor=background,
    zorder=0,
    transform=ax.transAxes,
)

ax.add_patch(rect)

ax_child = ax.inset_axes(
    [0.65, 0.2, 0.175, 0.175], zorder=10, transform=fig.transFigure
)

ax_child.barh(
    y=bar_frame.quantile_values.astype(str).index,
    width=bar_frame["count"],
    color=bar_frame.color,
)
sns.despine(ax=ax_child, left=True, bottom=True)
ax_child.tick_params(length=0, labelbottom="off", labelsize=12)
ax_child.set_xticklabels([], **regular)

for i, count in enumerate(bar_frame["count"]):
    ax_text(
        count,
        i,
        f"{(count/ total_houses) * 100:,.2f}% ",
        va="center",
        ha="right",
        weight="bold",
        **bold,
        size=16,
        color=background,
        ax=ax_child,
    )
ax_child.set_yticks(
    [0, 1, 2, 3, 4, 5],
    labels=quantile_labels[::-1],
    fontweight="bold",
    color=text_color,
    **bold,
    size=16,
)


# TODO: set title of the child axis later
# [0.7, 0.2, 0.175, 0.175]
fig_text(
    x=0.7,
    y=0.39,
    ha="center",
    va="bottom",
    s="Share of amount of shops",
    weight="bold",
    size=18,
    zorder=20,
    color=text_color,
    **bold,
)
fig_text(
    x=0.5,
    y=0.88,
    va="bottom",
    ha="center",
    s="How many shops are within a 20 minute roundtrip walk in Utrecht NL",
    weight="bold",
    size=40,
    color=text_color,
    **bold,
)

fig_text(
    x=0.5,
    y=0.10,
    s="sources:\nVisualisation:Sebastiaan Broekema\nOpen street map© for building polygons, KvK for shop locations Walking distances calculated by isochrone distances using open route service.",
    size=16,
    color=text_color,
    ha="center",
    **regular,
)


ax_child.set_facecolor(background)
fig.set_facecolor(background)
ax.set_facecolor(background)
fig.savefig("utrecht.jpeg")
fig.savefig("utrecht1200_dpi.png", dpi=1200)
# plt.show(block=False)
