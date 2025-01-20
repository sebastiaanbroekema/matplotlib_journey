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


x = footprint_base["gdpCapita"]
y = footprint_base["footprint"]
s = footprint_base["populationMillions"]


background_color = "#f1f2f6"
white = "#f1f1f1"
de_emphis = "#a4b0be"
emphis = "#ffa502"
grey = "#2f3542"



fig, ax = plt.subplots()


scatter = ax.scatter(x, y, s=s * 1.4, alpha=0, color=de_emphis,)

x = footprint["gdpCapita"]
y = footprint["footprint"]
s = footprint["populationMillions"]
region = footprint['region']

ax.scatter(x, y, s=s * 1.4, alpha=0.8, color=de_emphis,)

x = label_counties["gdpCapita"]
y = label_counties["footprint"]
s = label_counties["populationMillions"]
region = label_counties['region']

ax.scatter(x, y, s=s * 1.4, alpha=0.8, color=emphis,)

location = [0, 20_000, 40_000, 60_000, 80_000]
labels = ["", "$20K", "$40K", "$60K", "$80K"]

ax.set_ylim(0, 10)
ax.set_xlim(0, 80_000)

ax.set_xticks(location, labels=labels)


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
ax.set_ylabel("Footprint (Global Hectares per person)", color=grey,loc='top')
ax.set_title("GDP has a greater impact on ecological footprint than population size",color=grey, loc='left')


for i, row in label_counties.iterrows():
    gdp = row.gdpCapita
    footprint_value = row.footprint
    country = row.country
    size = row.populationMillions
    ax.text(
        x=gdp,
        y=footprint_value + (np.sqrt(size)/2) * 0.05,
        s=country,
        ha="center",
        va="center",
        size=10,
        color= grey
    )


# produce a legend with a cross-section of sizes from the scatter
handles, labels = scatter.legend_elements(prop="sizes", num=5, alpha=0.8, color= de_emphis)
legend2 = ax.legend(handles, labels, loc="lower right", title="Population size in millions", facecolor=background_color, frameon=False,labelspacing=1.25)




for text in legend2.get_texts():
    text.set_color(grey)

plt.tight_layout()
plt.show(block=False)


"""
My take on the another final boss from Overall theme and style.

I chose to also color emphisese the text labelled countries. Which also led to the Title i chose for the graph.
I am happy with the overall fibe. There are just some issues with the resulting graph I cannot currently cannot seem to fix. Mostly to do with the legend.
Personally I would like to place the legend outside of the graph. I made the legend with the `legend_elements` method of the pathcollection returned by `ax.scatter` I would like to have some more elements under 100 miloen population size and less above.

"""