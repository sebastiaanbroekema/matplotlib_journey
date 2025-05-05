# source https://data.openstate.eu/dataset/verkiezingsuitslagen-tweede-kamerverkiezingen-2023
# source https://data.opendatasoft.com/explore/dataset/georef-netherlands-gemeente%40public/export/?disjunctive.prov_code&disjunctive.prov_name&disjunctive.gem_code&disjunctive.gem_name

# https://python-cartogram.readthedocs.io/quickstart.html#fine-tuning-the-distortions
import matplotlib.pyplot as plt
import seaborn as sns
from highlight_text import fig_text, ax_text
from drawarrow import fig_arrow
from pypalettes import load_cmap
from pyfonts import load_font

import geopandas as gpd

from cartogram import Cartogram


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

# kleuren nodig voor
# PVV (Partij voor de Vrijheid)               257
# GROENLINKS / Partij van de Arbeid (PvdA)     31
# VVD                                          31
# Nieuw Sociaal Contract                       15
# Staatkundig Gereformeerde Partij (SGP)        8


# colors based on nos.nl colors
color_mapping = {
    "PVV (Partij voor de Vrijheid)": "#70d4ff",
    "GROENLINKS / Partij van de Arbeid (PvdA)": "#a90000",
    "VVD": "#4c44ff",
    "Nieuw Sociaal Contract": "#f7c106",
    "Staatkundig Gereformeerde Partij (SGP)": "#f08836",
}


uitslag = gpd.read_file("data/2023tk.geo.json")
agg_cols = [
    "Geldige stemmen",
    "Opgeroepen",
    "Ongeldig",
    "Blanco",
    "Geldige stempassen",
    "Geldige volmachtbewijzen",
    "Geldige kiezerspassen",
    "Toegelaten kiezers",
    "Meer getelde stembiljetten",
    "Minder getelde stembiljetten",
    "Meegenomen stembiljetten",
    "Te weinig uitgereikte stembiljetten",
    "Te veel uitgereikte stembiljetten",
    "Geen verklaring",
    "Andere verklaring",
    "Te veel briefstembiljetten",
    "Geen briefstembiljetten",
    "Opkomst",
    "Opkomstpercentage",
    "VVD",
    "D66",
    "GROENLINKS / Partij van de Arbeid (PvdA)",
    "PVV (Partij voor de Vrijheid)",
    "CDA",
    "SP (Socialistische Partij)",
    "Forum voor Democratie",
    "Partij voor de Dieren",
    "ChristenUnie",
    "Volt",
    "JA21",
    "Staatkundig Gereformeerde Partij (SGP)",
    "DENK",
    "50PLUS",
    "BBB",
    "BIJ1",
    "Piratenpartij - De Groenen",
    "BVNL / Groep Van Haga",
    "Nieuw Sociaal Contract",
    "Splinter",
    "LP (Libertaire Partij)",
    "LEF - Voor de Nieuwe Generatie",
    "Samen voor Nederland",
    "Nederland met een PLAN",
    "PartijvdSport",
    "Politieke Partij voor Basisinkomen",
]

politieke_partijen = [
    "VVD",
    "D66",
    "GROENLINKS / Partij van de Arbeid (PvdA)",
    "PVV (Partij voor de Vrijheid)",
    "CDA",
    "SP (Socialistische Partij)",
    "Forum voor Democratie",
    "Partij voor de Dieren",
    "ChristenUnie",
    "Volt",
    "JA21",
    "Staatkundig Gereformeerde Partij (SGP)",
    "DENK",
    "50PLUS",
    "BBB",
    "BIJ1",
    "Piratenpartij - De Groenen",
    "BVNL / Groep Van Haga",
    "Nieuw Sociaal Contract",
    "Splinter",
    "LP (Libertaire Partij)",
    "LEF - Voor de Nieuwe Generatie",
    "Samen voor Nederland",
    "Nederland met een PLAN",
    "PartijvdSport",
    "Politieke Partij voor Basisinkomen",
]


amount_of_votes_total = [
    "< >", #padding for plotting
    "<23,5 % of total vote>", #PVV
    "<15,8 % of total vote>", # GL PVDA
    "<15,2 % of total vote>", # VVD
    "<12,8 % of total vote>", # NSC
    "<  2,1 % of total vote>" # SGP
]

uitslag = (
    uitslag.groupby("gmcode")[agg_cols]
    .sum()
    .reset_index()
    .assign(winnaar=lambda x: x[politieke_partijen].idxmax(axis=1))
)

# data prep run one time only

# gemeenten = (
#     gpd
#     .read_file('data/wijkenbuurten_2024_v1.gpkg')
# )

# gemeenten_zonder_water = (
#     gemeenten
#     .loc[lambda x: x.water == "NEE"]
#     .dissolve(by='gemeentecode')
#     .reset
# )

# gemeenten_zonder_water.reset_index().to_parquet('data/gemeenten_zonder_water.parquet')
# gmcode voor de uitslagen


gemeenten = gpd.read_parquet("data/gemeenten_zonder_water.parquet")[
    ["geometry", "gemeentecode"]
]


results = gemeenten.merge(uitslag, left_on="gemeentecode", right_on="gmcode").assign(
    color=lambda x: x.winnaar.map(color_mapping)
)


# results_cartogram = Cartogram(results, "Geldige stemmen")
# results_cartogram.to_parquet('data/cartogram.parquet')

results_cartogram = gpd.read_parquet('data/cartogram.parquet')



fig, axs = plt.subplots(figsize=(20,15), ncols=2, )


fig.subplots_adjust(top=0.95, bottom=0.05)

fig_text(
    x=0.5, 
    y=0.95, 
    s="Land does not vote, people do\n<Looking at the results of the 2023 Dutch parliamentary elections using a cartogram>",
    size=40,
    ha='center',
    highlight_textprops=[{"size":30}],
    **bold
    )

fig_text(
    x=0.33, 
    y = 0.85, 
    s="Geographically accurate map\nof Dutch Municipalities",
    size=28,
    ha='center',
    **regular
    )

fig_text(
    x=0.75, 
    y = 0.85, 
    s="Geographically distored map\nby total number of votes cast",
    size=28,
    ha='center',
    **regular
    )

background='#636e72'
fig.set_facecolor(background)


ax1 = axs[0]

ax1.axis("off")
ax1.set_facecolor(background)
results.plot(color=results.color, ax=ax1, 
            #  edgecolor=results.color
            edgecolor='k'
             )


ax2 = axs[1]

ax2.axis("off")
results_cartogram.plot(
    ax=ax2, color=results_cartogram.color, 
    # edgecolor=results_cartogram.color
    edgecolor='k'
)




fig_text(
    x = 0.25,
    y = 0.1,
    s = "source: https://data.openstate.eu\nVisualisation: Sebastiaan Broekema",
    ha='center',
    size=16,
    **regular
)


legend_text = "\n".join(
    [f'<{x}>' for x in color_mapping.keys()]
)

color_dict = [{"color":x} for _, x in color_mapping.items()]

legend_text = f"<Party with the most votes in the municipality>\n{legend_text}"


props = [bold] + color_dict

ax2.set_facecolor(background)
fig_text(
    x = 0.38,
    y = 0.3,
    s = legend_text,
    ha='left',
    highlight_textprops=props,
    size=20,
    **regular
)
# legend table

legend_table_text = "\n".join(amount_of_votes_total)
fig_text(
    x = 0.63,
    y = 0.3,
    s = legend_table_text,
    ha='left',
    highlight_textprops=props,
    size=20,
    **regular
)




fig.savefig("cartogram.png", dpi = 300)
# plt.show(block=False)


