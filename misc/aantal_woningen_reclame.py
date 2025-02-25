
import matplotlib.pyplot as plt
from highlight_text import fig_text, ax_text
from drawarrow import fig_arrow

from pywaffle import Waffle


color = "#9c88ff"

background_color = "#dcdde1"

title = "Tussen 2018 en 2023 is €4,2 miljard reclameruimte ingekocht voor ongezonde voeding.\nDaar had je <30215 nieuwbouw huurwoningen> voor kunnen bouwen"
verantwoording = "Bron: uitgaven reclameruimte Pointer https://pointer.kro-ncrv.nl/nog-steeds-miljarden-euros-naar-junkfoodadvertenties-ondanks-afspraken-terugdringen-overgewicht\nBron:gemiddelde bouwkosten CBS https://www.cbs.nl/nl-nl/cijfers/detail/83673NED\nDe Cijfers voor reclame gaan alleen over conventionele reclame en niet over influencer gemedieerde reclame."

# https://opendata.cbs.nl/statline/#/CBS/nl/dataset/81955NED/table?fromstatweb
# nieuwegein heeft 34 390	

# 139_000 bouwkosten huur woning gemiddeld
# 209_000 bouwkosten koopwoning gemiddeld

# 4_200_000_000 

# 30215 huur woningen
# 20095 koop woningen


fig, ax = plt.subplots(figsize=(15,10))

fig.subplots_adjust(0.2, top=0.85, bottom=0.1)


Waffle.make_waffle(
    ax=ax,  # pass axis to make_waffle
    rows=50, 
    interval_ratio_x=1.5,
    interval_ratio_y=1.5,
    values=[3021],
    colors=[color]
    # icons='house',
    # font_size=5
)

fig_text(x=0.2, y=0.925, s = title, size=16, weight="bold", highlight_textprops=[{"color":color}])
fig_text(x=0.2, y=0.05, s=verantwoording, size=6)
fig_arrow((0.1,0.1),(0.2, 0.25), radius=-0.05, color=color)
fig_text(x=0.1, y=0.09, s="1 blokje is 10 woningen", size=12, color=color, weight="bold", ha='center')
fig.set_facecolor(background_color)
ax.set_facecolor(background_color)

plt.show(block=False)