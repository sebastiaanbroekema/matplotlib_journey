import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from drawarrow import ax_arrow
from highlight_text import ax_text

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


fig, ax = plt.subplots()

rund = slacht.loc[lambda x: x.Slachtdieren == "Rundvee (totaal)"]

mond_en_klauw_zeer = rund.loc[lambda x: x.Perioden == 2001, "AantalSlachtingen"].iloc[0]

ax.plot(rund.Perioden, rund.AantalSlachtingen)

ax.set_ylim(0, rund.AantalSlachtingen.max() + 0.05 * rund.AantalSlachtingen.max())

ax.set_xticks([1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025])
ax.ticklabel_format(scilimits=(0,0),style="plain")

ax_arrow((1995, 2028300 / 2), (2001, mond_en_klauw_zeer), radius=0.2)
ax_text(x= 1995, y= 2028300 / 2, s="Mond\nen\nKlauw zeer", ha="center")



sns.despine()
plt.show(block=False)
