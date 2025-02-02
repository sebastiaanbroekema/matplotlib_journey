import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pypalettes import load_cmap
from matplotlib.axes import Axes

# =====
url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/economic/economic.csv"
df = pd.read_csv(url)

fig, axs = plt.subplots(ncols=3, nrows=3, layout="tight")

for country, ax in zip(df["country"].unique(), axs.flat):
    ax.text(x=0.5, y=0.5, s=country.title(), ha="center", va="center")

plt.show()


# =====

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/economic/economic.csv"
df = pd.read_csv(url)

fig, axs = plt.subplots(
    ncols=3,
    nrows=3,
    layout="tight",
)

for country, ax in zip(df["country"].unique(), axs.flat):
    x = df.loc[df["country"] == country, "date"]
    y = df.loc[df["country"] == country, "consumer confidence"]
    ax.plot(x, y)
    ax.set_ylim(-60, 130)
    ax.set_xticks(["2020-01-01", "2022-01-01", "2024-01-01"], labels=[2020, 2022, 2024])
    ax.grid(axis="y")
    ax.tick_params(length=0)
    ax.text("2024-01-01", 130, country, ha="right")
    sns.despine()
plt.show()


fig, axs = plt.subplots(ncols=3, nrows=3, layout="tight")

for country, ax in zip(df["country"].unique(), axs.flat):
    x = df.loc[df["country"] == country, "consumer confidence"]
    sns.kdeplot(x, fill=True, color="purple", ax=ax)
    ax.set_yticks([])
    ax.set_ylabel("")
    ax.set_xlabel("")
    ax.spines[["top", "left", "right"]].set_visible(False)
    ax.set_xlim(-60, 130)
    ax.set_ylim(0, 0.1)
    ax.tick_params(length=0)
    ax.text(x=-60, y=0.06, s=f"Consumer confidence in\n{country}", size=7)
plt.show()


colors = load_cmap("Antique").colors
background_color = "#f2f2f2"


fig, axs = plt.subplots(nrows=3, ncols=3, layout="tight")

fig.set_facecolor(background_color)


def background_plot(ax: Axes, df: pd.DataFrame) -> Axes:
    for country in df["country"].unique():
        country_filter = df.country.apply(lambda x: x == country)
        date = df.loc[country_filter, "date"]
        confidence = df.loc[country_filter, "consumer confidence"]
        ax.plot(date, confidence, color="grey")
    return ax


ax: Axes
for country, ax, color in zip(df["country"].unique(), axs.flat, colors):
    country_filter = df.country.apply(lambda x: x == country)
    date = df.loc[country_filter, "date"]
    confidence = df.loc[country_filter, "consumer confidence"]

    ax.plot(date, confidence, color=color)
    ax.set_xticks(["2020-01-01", "2022-01-01", "2024-01-01"], labels=[2020, 2022, 2024])
    ax = background_plot(ax, df[~country_filter])
    ax.set_facecolor(background_color)
    ax.set_ylim(-60, 130)
    ax.text(
        "2024-01-01",
        110,
        country.title(),
        ha="right",
        color=color,
        size=16,
        weight="bold",
    )
    sns.despine()


plt.show(block=False)


# ======

colors = load_cmap("Antique").colors
background_color = "#f2f2f2"

fig, axs = plt.subplots(ncols=3, nrows=3, layout="tight")
fig.set_facecolor(background_color)

for color, country, ax in zip(colors, df["country"].unique(), axs.flat):
    other_df = df[df["country"] != country]
    for other_country in other_df["country"].unique():
        x = other_df.loc[other_df["country"] == other_country, "date"]
        y = other_df.loc[other_df["country"] == other_country, "consumer confidence"]
        ax.plot(x, y, alpha=0.2, color="grey", linewidth=0.5)

    x = df.loc[df["country"] == country, "date"]
    y = df.loc[df["country"] == country, "consumer confidence"]
    ax.plot(x, y, color=color)
    ax.set_ylim(-60, 130)
    ax.set_xlim("2020-01-01", "2024-01-01")
    ax.set_xticks(["2020-01-01", "2022-01-01", "2024-01-01"], labels=[2020, 2022, 2024])
    ax.text(
        x="2024-01-01", y=112, s=country.title(), ha="right", color=color, weight="bold"
    )
    ax.spines[["top", "right", "bottom"]].set_visible(False)
    ax.tick_params(length=0, labelsize=6)
    ax.grid(axis="y", linewidth=0.5, alpha=0.5)
    ax.set_facecolor(background_color)

plt.show()
