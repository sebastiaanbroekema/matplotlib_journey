import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from highlight_text import ax_text


url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/economic/economic.csv"
df = pd.read_csv(url)
df = df[~df["country"].isin(["europe", "new zealand"])]
df["country"] = df["country"].replace({"united states": "US", "united kingdom": "UK"})
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")


grey_lines_color = "#7c7c7c"
background_color = "#191c3b"
color_mapping = {
    "china": "#e84f4f",
    "switzerland": "#4bcf82",
    "japan": "#de5fee",
    "australia": "#786cf3",
}


countries = ["australia", "japan", "switzerland", "china"][::-1]

time_max = df.date.max()


fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(10, 10),layout="thight")
for country, ax in zip(countries, axs.flat):
    filter_ = df.country == country
    main = df[filter_]
    other = df[~filter_]
    x = main["date"]
    y = main["interest rates"]
    ax.step(x, y, where="post", color=color_mapping[country], zorder=5)

    ax_text(
        x=time_max + pd.Timedelta(days=25),
        y=y.iloc[-1],
        s=country.title(),
        color=color_mapping[country],
        ax=ax,
        va="center",
    )

    for other_countries in other["country"].unique():
        selection = other.loc[lambda x: x.country == other_countries]
        x = selection["date"]
        y = selection["interest rates"]
        ax.step(x, y, where="post", color=grey_lines_color)

        _ = ax_text(
                x=time_max + pd.Timedelta(days=25),
                y=y.iloc[-1],
                s=other_countries.title(),
                color=grey_lines_color,
                ax=ax,
                va="center",
            )


    ax.set_facecolor(background_color)
    ax.set_ylim(-1, 6)
    ax.tick_params(length=0, labelcolor=grey_lines_color, color="white")
    ax.set_xticks(
        ["2020-01", "2021-01", "2022-01", "2023-01", "2024-01"],
        labels=["2020", "2021", "2022", "2023", "2024"],
    )
    ax.spines[["left", "bottom"]].set_color("white")
    sns.despine()

fig.set_facecolor(background_color)
fig.text(
  x=0.13, y=0.92, s="Interest Rates, from 2020 to 2024",
  size=18, color="#e2e2e2"
)


axs[0, 1].spines["left"].set_visible(False)
axs[1, 1].spines["left"].set_visible(False)
axs[0, 1].set_yticks([])
axs[1, 1].set_yticks([])


plt.show(block=False)
