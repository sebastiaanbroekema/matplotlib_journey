import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pypalettes import load_cmap
import numpy as np



cmap = load_cmap("ppalette")
colors = cmap.colors

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/footprint/footprint.csv"
footprint_base = pd.read_csv(url)
label_counties = footprint_base.loc[lambda x: x.populationMillions > 100]
footprint = footprint_base.loc[lambda x: x.populationMillions <= 100 ]


# x = footprint["gdpCapita"]
y = footprint["footprint"]
x = footprint["populationMillions"]
s =  footprint["earthsRequired"]


background_color = "#f1f2f6"
white = "#f1f1f1"
de_emphis = "#a4b0be"

grey = "#2f3542"



fig, ax = plt.subplots()
ax.scatter(x, y, s=s * 1.4, alpha=0.8, color=de_emphis,)

y = label_counties["footprint"]
x = label_counties["populationMillions"]
s =  label_counties["earthsRequired"]
# region = footprint['region']


ax.scatter(x, y, s=s * 1.4, alpha=0.8, color="darkred",)

location = [0, 20_000, 40_000, 60_000, 80_000]
labels = ["", "$20K", "$40K", "$60K", "$80K"]

ax.set_ylim(0, 12.5)
# ax.set_xlim(-1000, 85_000)

# ax.set_xticks(location, labels=labels)


ax.spines[["left", "bottom"]].set_color(grey)

ax.tick_params(length=0)
ax.tick_params(
    axis="both",
    labelsize=10,
    labelcolor=grey,
)


ax.set_facecolor(background_color)
fig.set_facecolor(background_color)


sns.despine()


ax.set_xlabel("GDP per captia", color=grey, loc='left')
ax.set_ylabel("Ecological footprint", color=grey,loc='top')
ax.set_title("High population doesn't always mean a high ecological footprint",color=grey, loc='left')


for i, row in label_counties.iterrows():
    gdp = row.gdpCapita
    footprint_value = row.footprint
    country = row.country
    size = row.populationMillions
    ax.text(
        x=gdp,
        y=footprint_value + (np.sqrt(size)/2) * 0.06,
        s=country,
        ha="center",
        va="center",
        size=7,
        color= grey
    )

plt.show(block=False)


