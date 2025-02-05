import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from drawarrow import fig_arrow
from highlight_text import ax_text, fig_text
from pyfonts import load_font
from pypalettes import load_cmap

cmap = load_cmap("AsteroidCity3")
google_font = "https://github.com/google/fonts/blob/main"
regular = load_font(
    "https://github.com/eifetx/Pixelify-Sans/blob/main/fonts/otf/PixelifySans-Regular.otf?raw=true"
)

bold = load_font(
    "https://github.com/eifetx/Pixelify-Sans/blob/main/fonts/otf/PixelifySans-SemiBold.otf?raw=true"
)

background = "#f5f6fa"


regions = [
    "NA_Sales",
    "EU_Sales",
    "JP_Sales",
    "Other_Sales",
]

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/game-sales/game-sales.csv"
df = pd.read_csv(url)

grouped = df.groupby("Genre")[
    ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]
].sum()


percentage = (
    (
        grouped[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].div(
            grouped.Global_Sales, axis=0
        )
        * 100
    )
    .reset_index()
    .sort_values(by="NA_Sales")
)


text_props = [{"color": color} for color in cmap.colors]


fig, ax = plt.subplots()
fig.subplots_adjust(top=0.725, right=0.725, left=0.2)
ax.set_xlim(0, 100)

percentage.set_index("Genre").plot(
    kind="barh", stacked=True, ax=ax, colormap=cmap, legend=False, zorder=1
)


fig_text(
    0.2,
    0.95,
    "Share of game genre sales between\n<North America>, <Europa>, <Japan>\nand <the rest of the world>",
    highlight_textprops=text_props,
    font=bold,
    size=16,
    ax=ax,
)

# Convert display coordinates to figure coordinates
disp_arrow = ax.transData.transform((75, 0))
fig_coords_arrow = fig.transFigure.inverted().transform(disp_arrow)

fig_arrow((0.73, 0.15), fig_coords_arrow, radius=0.1)
fig_text(
    0.73,
    0.2,
    "The only genre where\nNorth America is not\nnumber one in sale share\n<35%> vs <38%>",
    highlight_textprops=[
        text_props[0],  # | {"font": bold},
        text_props[2],  # | {"font": bold},
    ],
    size=10,
    va="center",
    ha="left",
    font=regular,
)

x_step = [0, 20, 40, 60, 80, 100]
ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False, length=0)
ax.set_xticks(x_step, [f"{x}%" for x in x_step], font=regular)

for label in ax.get_yticklabels():
    label.set_fontproperties(regular)


ax.set_ylabel("")

sns.despine(
    top=False,
    bottom=True,
    left=True,
    trim=True,
    # offset=10,
)

fig.set_facecolor(background)
ax.set_facecolor(background)


for index, row in percentage.reset_index(drop=True).iterrows():
    pos = 0
    copy_ = row.copy()
    if row[0] == "Shooter":
        # pos += row[-2]
        row.iloc[-2] = 0
        # row[-1] = 0
    for item, increment in zip(row.iloc[1:], copy_.iloc[1:]):
        if item:
            _ = ax_text(pos, index, f"{round(item)}%", va="center", font=regular)

        pos += increment

plt.show(block=False)
