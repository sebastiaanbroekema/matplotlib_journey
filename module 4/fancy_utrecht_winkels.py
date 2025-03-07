import matplotlib.pyplot as plt
import seaborn as sns
from highlight_text import fig_text, ax_text
from drawarrow import fig_arrow
from pypalettes import load_cmap

from mapclassify import Quantiles

import geopandas as gpd
import pandas as pd

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
    "11 to 18 shops",
    "18 to 39 shops",
    "39+ shops",
]

utrecht = utrecht.assign(
    quantile_values=pd.cut(
        utrecht.amount, [1, *quantiles.bins], labels=quantile_labels[1:]
    )
    .astype(str)
    .replace("nan", quantile_labels[0])
)


# second to last is the grey one
# red, orange, yellow, teal, grey, dark blue
# D72000FF, #EE6100, #FFAD0A, #1BB6AF, #9093A2, #132157

colors = ("#9093A2", "#D72000", "#EE6100", "#FFAD0A", "#1BB6AF", "#132157")


color_dict = {i: j for i, j in zip(quantile_labels, colors)}


bar_frame = (
    utrecht.quantile_values.value_counts()
    .reindex(quantile_labels[::-1])
    .reset_index()
    .assign(color=lambda x: x.quantile_values.map(color_dict))
)
total_houses = bar_frame["count"].sum()


utrecht = (
    utrecht.assign(color=lambda x: x.quantile_values.map(color_dict))
)

fig, ax = plt.subplots(figsize=(20,15))

ax.axis("off")

utrecht.plot(
    ax=ax,
    legend=False,
    color=utrecht.color
)


ax_child = ax.inset_axes([0.80, -0.1, 0.3, 0.7])

ax_child.barh(y=bar_frame.quantile_values.astype(str).index, width=bar_frame["count"], color=bar_frame.color)
sns.despine(ax=ax_child, left=True, bottom=True)
ax_child.tick_params(length=0, labelbottom="off", labelsize=12)
ax_child.set_xticklabels([])
for i, count in enumerate(bar_frame["count"]):
    ax_text(
        count,
        i,
        f"{(count/ total_houses) * 100:,.2f}% ",
        va="center",
        ha="right",
        weight="bold",
        size=10,
        color="white",
        ax=ax_child
    )
ax_child.set_yticks([0,1,2,3,4,5], labels=quantile_labels[::-1], fontweight="bold")


# TODO: set title of the child axis later

# fig.savefig('childplot.png')
fig.savefig("utrecht.png")
plt.show(block=False)
