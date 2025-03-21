import matplotlib.pyplot as plt
import seaborn as sns
from highlight_text import fig_text, ax_text
from drawarrow import fig_arrow
from pypalettes import load_cmap
import pandas as pd
from pyfonts import load_font
import string
import random

random.seed(42)

chars = [x for x in "abcdefghijklmnopqrstABCDEFGHIJKLMNOPQRSTUVWXYZ"]

non_select = "#576574"


def generate_population():
    def insert_newlines(input_string):
        return "\n".join(
            [input_string[i : i + 10] for i in range(0, len(input_string), 10)]
        )

    return insert_newlines("".join(random.choices(chars, k=100)))


wee_people = {
    "font": load_font(
        "https://github.com/propublica/weepeople/blob/master/weepeople.ttf?raw=true"
    )
}

df = pd.read_csv("data/gezondheid.csv").iloc[:11]


rokers = df["Rokers (% mensen van 18 jaar of ouder)"]
# 25.7
# 18.2


# generated from generate_population
smokers_2014 = "<AoiMGkPcOM>\n<RrKRZCbDHU>\n<UAEBNs>KhBY\npLJTTTroNO\nUbdJWZOteJ\nUALVcQnrgE\nGQhdUIlVgB\nllaRVLhApH\nJtlSjrCkGG\nZnYKmGLOcH"

smokers_2024 = "<AoiMGkPcOM>\n<RrKRZCbD>HU\nUAEBNsKhBY\npLJTTTroNO\nUbdJWZOteJ\nUALVcQnrgE\nGQhdUIlVgB\nllaRVLhApH\nJtlSjrCkGG\nZnYKmGLOcH"

fig, ax = plt.subplots(figsize=(10, 10))

ax.axis("off")
ax.set_ylim(0, 100)
ax.set_xlim(0, 100)

fig_text(s="If the Netherlands was 100 people", x=0.5, y=0.9, ha="center", size=32)

ax_text(
    25,
    0,
    s=smokers_2014,
    va="bottom",
    ha="center",
    **wee_people,
    size=40,
    highlight_textprops=[
        {"color": "#F79F1F"},
        {"color": "#F79F1F"},
        {"color": "#F79F1F"},
    ],
    color=non_select,
)
ax_text(
    75,
    0,
    s=smokers_2024,
    va="bottom",
    ha="center",
    **wee_people,
    size=40,
    highlight_textprops=[{"color": "#F79F1F"}, {"color": "#F79F1F"}],
    color=non_select,
)
background = "#c8d6e5"
fig.set_facecolor(background)
ax.set_facecolor(background)

plt.show(block=False)
