import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from drawarrow import ax_arrow
from highlight_text import ax_text, fig_text
from pyfonts import load_font


nosifer = load_font("https://github.com/google/fonts/blob/main/ofl/nosifer/Nosifer-Regular.ttf?raw=true")


perioden = pd.read_csv("data/perioden.csv", sep=";")
label_dieren = pd.read_csv("data/namen_dieren.csv", sep=";", encoding="latin")


slachtdieren = pd.read_csv("data/slacht_data.csv", sep=";")


# geslacht gewicht kg


slacht = (
    slachtdieren.set_index("Perioden")
    .join(perioden.set_index("Key"), how="left")
    .drop(["Description", "Status"], axis=1)
    .reset_index(drop=True)
    .rename(columns={"Title": "Perioden"})
    .set_index("Slachtdieren")
    .join(label_dieren.set_index("Key"), how="left")
    .drop(["Description"], axis=1)
    .reset_index(drop=True)
    .rename(columns={"Title": "Slachtdieren"})
    .drop("ID", axis=1)
    .assign(
        AantalSlachtingen=lambda x: x.AantalSlachtingen_1 * 1000,
        GeslachtGewicht=lambda x: x.GeslachtGewicht_2 * 1000,
        Perioden = lambda x: x.Perioden.astype(int)
    )
    .drop(
        [
            "AantalSlachtingen_1",
            "GeslachtGewicht_2",
        ],
        axis=1,
    )
)


rund = slacht.loc[lambda x: x.Slachtdieren == "Rundvee (totaal)"]
kalf = slacht.loc[lambda x: x.Slachtdieren == "Totaal kalveren"]
rund_volwassen = slacht.loc[lambda x: x.Slachtdieren == "Totaal volwassen runderen"]


fig, ax = plt.subplots()
fig.subplots_adjust(top=0.8,right=0.8)
# https://en.wikipedia.org/wiki/Bovine_spongiform_encephalopathy
mond_en_klauw_zeer = rund.loc[lambda x: x.Perioden == 2001, "AantalSlachtingen"].iloc[0]
ban_britsh_beef = rund.loc[lambda x: x.Perioden == 1996, "AantalSlachtingen"].iloc[0]
ban_britsh_beef_lifted = rund.loc[lambda x: x.Perioden == 2006, "AantalSlachtingen"].iloc[0]

# 2015 afschaffen melk quotum
# meer kalveren, start groei

max_value_plot = rund.AantalSlachtingen.max()

ax.plot(rund.Perioden, rund.AantalSlachtingen, solid_capstyle="round", lw=5)
ax.plot(kalf.Perioden, kalf.AantalSlachtingen, solid_capstyle="round", lw=5)
ax.plot(rund_volwassen.Perioden, rund_volwassen.AantalSlachtingen, solid_capstyle="round", lw=5)


ax.set_ylim(0, max_value_plot + 0.05 * max_value_plot)

ax.set_xticks([1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025])
ax.ticklabel_format(scilimits=(0,0),style="plain")
ax.tick_params(length=0)


ax_arrow((1995, 2028300 / 2), (2001, mond_en_klauw_zeer), radius=0.2)
ax_text(x= 1995, y= 2028300 / 2, s="Mond\nen\nKlauw zeer", ha="center")

# percentage groei krimpt
# slacht[lambda x: x.Slachtdieren == 'Totaal kalveren'].set_index("Perioden").AantalSlachtingen.pct_change() * 100
# Mad cow
ax_arrow((1993, 1500000), (1996, ban_britsh_beef), radius=0.1)

coordinates_pixels = ax.transData.transform((1990, max_value_plot ))
relative_figure_coordinates = fig.transFigure.inverted().transform(coordinates_pixels)

print(relative_figure_coordinates)

fig_text(relative_figure_coordinates[0],0.9,'De slaughter continues\nSlaughtered Cattle and pigs in the Netherlands', font = nosifer, color='red')

sns.despine(trim=True)
plt.show(block=False)
