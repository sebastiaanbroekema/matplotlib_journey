import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns




# Use the ax.text() function.
# Choose valid positions so that the text does not overlap with the lines.
# Remove the label parameter from ax.plot() since it is no longer needed.


url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/walks/walks.csv"
df = pd.read_csv(url)

x = list(range(len(df)))
y1 = df["Walk_1"]
y2 = df["Walk_2"]
y3 = df["Walk_3"]

colors = ["#F56455", "#15134B", "#87C785"]

fig, ax = plt.subplots()
ax.plot(x, y1, color=colors[0], label="Walk1")
ax.plot(x, y2, color=colors[1], label="Walk2")
ax.plot(x, y3, color=colors[2], label="Walk3")
# ax.legend()
ax.spines[["top", "right"]].set_visible(False)
ax.set_xlim(0, 200)

ax.text(125, -25, 'Walk 1', color=colors[0])
ax.text(160, -10, 'Walk 3', color=colors[-1])
ax.text(180, 0, 'Walk 2', color=colors[1])

plt.show()


#====

# Use the ax.text() function and set the text to bold with weight="bold".
# Choose valid positions so that the text does not overlap with the points.
# Add legend= in sns.scatterplot() to remove the legend.




url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/footprint/footprint.csv"
df = pd.read_csv(url)
df["is_Europe"] = df["region"].isin(["EU-27"])

x = df["gdpCapita"]
y = df["footprint"]
c = df["is_Europe"]

colors = ["lightgrey", "#2a9d8f"]

fig, ax = plt.subplots()
ax.set_xlim(-2000, 80000)
ax.set_ylim(0, 8.5)
ax.spines[["top", "right"]].set_visible(False)
sns.scatterplot(
  x=x, y=y, hue=c, ax=ax,
  palette=colors, s=150, legend=False
)

ax.text(54500, 5, 'European country', color = colors[-1], weight="bold")
ax.text(14000, 5, 'Non European country', color = colors[0], weight="bold")
plt.show()


#====


# Use the ax.text() function.
# Choose valid positions so that the texts do not overlap with lines or areas.
# Add legend= in sns.kdeplot() to remove the legend.


url = "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/refs/heads/master/static/data/iris.csv"
iris = pd.read_csv(url)

x = iris["sepal_width"]
c = iris["species"]
colors = ["#14213d", "#fca311", "#0077b6"]



fig, ax = plt.subplots()
sns.kdeplot(
  x=x, hue=c, ax=ax,
  palette=colors,
  fill=True,
  legend=False
)

ax.text(3.1, 0.40, 'verginica', color=colors[-1], weight='bold' )

ax.text(2.3, 0.20, 'Versicolor', color=colors[1], weight='bold',ha='right' )

ax.text(3.8, 0.25, 'Setosa', color=colors[0], weight='bold' )

plt.show()


#======

    # Remove the x-axis tick labels with ax.set_xticks([]).
    # Remove the bottom spine.
    # Add individual labels using ax.text().
    # Pro tip: Create a dictionary with text_arg = dict(weight="bold", ha="center") and then pass it to each ax.text() call using the ** operator.

text_arg = dict(weight="bold", ha="center")

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/footprint/footprint.csv"
df = pd.read_csv(url)
df = df[df["region"].isin(
   ["Africa", "EU-27", "Asia-Pacific"]
)]

x = df["region"]
y = df["lifexp"]

colors = ["#ef476f", "#06d6a0", "#118ab2"]






fig, ax = plt.subplots()

sns.swarmplot(
  x=x, y=y, hue=x,
  palette=colors,
  size=10,
  ax=ax
)
ax.spines[["top", "right","bottom"]].set_visible(False)
ax.set_xlabel("")

# africa 70, 0
# Asia-Pacific 63 1
# Europa 70 , 2

ax.text(0,68, 'Africa',color = colors[0], **text_arg)
ax.text(1,63, 'Asia-Pacific',color = colors[1], **text_arg)
ax.text(2,70, 'Europa',color = colors[2], **text_arg)

# ax.get_xaxis().set_visible(False)
ax.grid(axis="y")
ax.set_xlabel()
ax.set_xticks([])
plt.show()

#====


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from pypalettes import load_cmap

np.random.seed(0)
data = np.random.uniform(low=0, high=20, size=(20, 20))
cmap = load_cmap("Sunset", cmap_type="continuous", reverse=True)

fig, ax = plt.subplots(figsize=(7, 7), layout="tight")
sns.heatmap(data, cmap=cmap, cbar=False, ax=ax, annot=True)

value_ranges = [0, 5, 10, 15, 20]
labels = ["0-5", "5-10", "10-15", "15-20"]

rectangle_width = 1.5
rectangle_height = 1.5
legend_x_start = 6
legend_x_step = 2
legend_y = -2.5

for i in range(len(labels)):
    value = (value_ranges[i] + value_ranges[i + 1]) / 2 / value_ranges[-1]
    color = cmap(value)
    ax.add_patch(
        plt.Rectangle(
            (legend_x_start - i * legend_x_step, legend_y),
            rectangle_width,
            rectangle_height,
            facecolor=color,
            edgecolor="black",
            lw=0.6,
            clip_on=False,
        )
    )
    ax.text(
        legend_x_start - i * legend_x_step + 0.7,
        legend_y - 0.5,
        labels[i],
        fontsize=12,
        ha="center",
        va="center",
    )

plt.show()