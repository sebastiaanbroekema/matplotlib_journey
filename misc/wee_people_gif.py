import matplotlib.pyplot as plt
import seaborn as sns
from highlight_text import fig_text, ax_text
from drawarrow import fig_arrow
from pypalettes import load_cmap
import pandas as pd
from pyfonts import load_font
import string
import random
import copy
import gif

random.seed(42)

chars = [x for x in "abcdefghijklmnopqrstABCDEFGHIJKLMNOPQRSTUVWXYZ"]

non_select = "#576574"
highlight_color = "#F79F1F"


def make_column_of_weepeople(people_preped):
    result = []
    for i in range(0, len(people_preped), 10):  # Step by 10
        # Concatenate the next 10 elements
        result.append("".join(people_preped[i : i + 10]))
    return "\n".join(result)


def generate_population():
    return random.choices(chars, k=100)


def prep_individuals(people_list, num_of_replacements):
    people_list_cp = copy.copy(people_list)
    indices = random.sample(range(len(people_list_cp)), num_of_replacements)
    for index in indices:
        people_list_cp[index] = f"<{people_list_cp[index]}>"
    return people_list_cp


wee_people = {
    "font": load_font(
        "https://github.com/propublica/weepeople/blob/master/weepeople.ttf?raw=true"
    )
}

people_set = generate_population()


smokers_2014_random = make_column_of_weepeople(prep_individuals(people_set, 26))
smokers_2024_random = make_column_of_weepeople(prep_individuals(people_set, 18))

df = pd.read_csv("data/gezondheid.csv").iloc[:11]


rokers = df["Rokers (% mensen van 18 jaar of ouder)"]
# 25.7
# 18.2


# generated from generate_population
smokers_2014 = "<AoiMGkPcOM>\n<RrKRZCbDHU>\n<UAEBNs>KhBY\npLJTTTroNO\nUbdJWZOteJ\nUALVcQnrgE\nGQhdUIlVgB\nllaRVLhApH\nJtlSjrCkGG\nZnYKmGLOcH"

smokers_2024 = "<AoiMGkPcOM>\n<RrKRZCbD>HU\nUAEBNsKhBY\npLJTTTroNO\nUbdJWZOteJ\nUALVcQnrgE\nGQhdUIlVgB\nllaRVLhApH\nJtlSjrCkGG\nZnYKmGLOcH"


smokers_2014 = """<JbmkNLVdtb>
<kDbjJFkHRa>
<RMphYp>eeSH
RNEYrFSITG
MckndkemJq
rjmXJIhNhr
ZJFLSPkbom
jXUoKsWBml
FmGVskZDec
fIQtcrZEYT"""


@gif.frame
def create_frame(i):
    fig, ax = plt.subplots(figsize=(10, 8))

    ax.axis("off")
    ax.set_ylim(0, 90)
    ax.set_xlim(0, 100)

    fig_text(
        s="If the Netherlands was 100 people",
        x=0.5,
        y=0.9,
        ha="center",
        size=32,
        weight="bold",
    )

    fig_text(s="Source: Centraal Bureau voor de Statistiek", x=0.2, y=0.05)

    ax_text(
        50,
        0,
        s=smokers_2014_random,
        va="bottom",
        ha="center",
        **wee_people,
        size=40,
        highlight_textprops=[{"color": highlight_color, "alpha":(100 - i) / 100}] * 26,
        color=non_select,
        alpha=0,
    )
    ax_text(
        50,
        0,
        s=smokers_2014,
        va="bottom",
        ha="center",
        **wee_people,
        size=40,
        # highlight_textprops=[{"color": highlight_color}]*18,
        highlight_textprops=[{"color": highlight_color, "alpha": i / 100}] * 3,
        color=non_select,
        # alpha=(i) / 100,
    )

    ax_text(
        x=50,
        y=81,
        s="26 of them would have been <smokers> in 2014",
        ha="center",
        va="top",
        size=18,
        highlight_textprops=[{"color": highlight_color}],
    )

    background = "#c8d6e5"
    fig.set_facecolor(background)
    ax.set_facecolor(background)


frames = [create_frame(x) for x in range(101)]

frames = frames + [frames[-1]] * 10 + frames[::-1]
gif.save(frames, 'example.gif', duration=50)