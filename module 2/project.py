import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/newyork-airbnb/newyork-airbnb.csv"
df = pd.read_csv(url)


background_color = "#f1f2f6"
grey = "#2f3542"
color = "#fcb433"

avg_global = df["price"].mean()

df_agg = (
    df.groupby("neighbourhood_group", as_index=False)["price"]
    .mean()
    .sort_values("price")
    .reset_index()
)

x = df_agg["price"]
y = df_agg["neighbourhood_group"]

fig, ax = plt.subplots()

bars = ax.barh(y=y, width=x, color=color, height=0.66)
ax.set_xticks(list(range(0, 201, 20)))


ax.set_title(
    "Want a cheap AirBnB deal?\nThen you should stay in the Bronx.",
    loc="left",
    size=14,
    color=grey,
    fontweight="bold",
)

ax.set_xlabel("Average price in dollars", loc="left", color=grey)

ax.tick_params(length=0)
ax.tick_params(
    labelsize=12,
    labelcolor=grey,
)

ax.axvline(avg_global, color="#e84118")
ax.text(
    x=avg_global + 1,
    y=1,
    s=f"Average price in New York\n${round(avg_global)}",
    color=grey,
)
ax.spines[["left", "bottom"]].set_color(grey)
sns.despine()

ax.set_facecolor(background_color)
ax.bar_label(
    bars, labels=[f"${round(value)}" for value in x], label_type="edge", color=grey
)
ax.text(x=0, y=-1.5, s="Source: insideairbnb.com", color="#7f8fa6")

fig.set_facecolor(background_color)

fig.tight_layout()  # this ensures the figure fits the sandbox
plt.show(block=False)
