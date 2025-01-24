import matplotlib.pyplot as plt
import numpy as np
from pypalettes import load_cmap
from highlight_text import ax_text


data = np.random.randn(20, 20)
colors = load_cmap("Acadia").colors

fig, ax = plt.subplots()


props = [{"color": color, "weight": "bold"} for color in colors][:4]


ax_text(
    0.1, 0.5, "<Yellow> <Dark Green> <Blue> and <Red psych>", highlight_textprops=props
)

plt.show()


# =====


colors = load_cmap("Acadia")
fig, ax = plt.subplots()


props = [{"color": color, "weight": "bold"} for color in colors][:4]


ax_text(
    0.1, 0.5, "<Yellow> <Dark Green> <Blue> and <Red psych>", highlight_textprops=props
)

plt.show()


# =====

# The colors used are defaults from matplotlib: "red", "purple", "white", and "black".
# Only the red text is bold.
# The bbox style around the second set of enclosed annotations is"edgecolor": "black", "facecolor": "purple", "linewidth": 2, "pad": 5.
# For the line break, use two line feeds (\n).


fig, ax = plt.subplots()

ax_text(
    0.1,
    0.5,
    size=14,
    s="<red medium text> and\n\n<Darkblue and purple>",
    highlight_textprops=[
        {"color": "red", "weight": "bold"},
        {
            "color":"white",
            "size": 30,
            "bbox": {
                "edgecolor": "black",
                "facecolor": "purple",
                "linewidth": 2,
                "pad": 5,
            },
        },
    ],
)

plt.show()

#======


# Yellow is the first color (colors[0]), 
# Darkblue the second one (colors[1]), 
# and Green the last one (colors[2]).





import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pypalettes import load_cmap
from highlight_text import ax_text

url = "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/refs/heads/master/static/data/iris.csv"
iris = pd.read_csv(url)

colors = load_cmap("Acadia", keep_first_n=3).colors

x = iris["sepal_length"]
y = iris["sepal_width"]
c = iris["species"]








fig, ax = plt.subplots()
ax.spines[["top", "right"]].set_visible(False)
sns.scatterplot(
    x=x, y=y, hue=c, s=100, legend=False, palette=colors,
)

# Yellow is the first color (colors[0]), 
# Darkblue the second one (colors[1]), 
# and Green the last one (colors[2]).

ax_text(4.25, 4, "<Setosa> is yellow", highlight_textprops=[{"color":colors[0], "weight":"bold"}])
ax_text(5.5, 2, "<Versicolor> is darkblue", highlight_textprops=[{"color":colors[1], "weight":"bold"}])
ax_text(7, 3.5, "<The other one> is that color", highlight_textprops=[{"color":colors[2], "weight":"bold"}])
plt.show(block=False)








##=====

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/storms/storms.csv"
storms = pd.read_csv(url)
df = storms.groupby("status", as_index=False)["n"].sum()
df = df.sort_values("n")

labels = df["status"]
y = df["n"]

color_mapping = {
  True: "#339f62",
  False: "lightgrey"
}
colors = (df["status"] == "hurricane").map(color_mapping)

fig, ax = plt.subplots()
ax.bar(labels, y, color=colors)

ax_text(
    0.5, 2000, 

    "<Hurricains> second most occoring\ndisater", 
    highlight_textprops=[{"color":color_mapping[True],"weight":"bold"}],
    size=14
    )

plt.show(block=False)