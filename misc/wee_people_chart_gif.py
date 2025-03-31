"""
Script  to generate waffle charts based on the wee people font.
The code generates gifs from the charts based on the gif module
which basically just
# https://source.opennews.org/articles/our-font-made-people/
https://github.com/propublica/weepeople?tab=readme-ov-file#wee-people

"""

import random

import numpy as np
import gif
import matplotlib.pyplot as plt
from highlight_text import ax_text, fig_text
from pyfonts import load_font
from PIL import Image

# make the charts reproducable
# can there be any other number
random.seed(42)

# since wee people is a font we need a character set to choose from
chars = [x for x in "abcdefghijklmnopqrstABCDEFGHIJKLMNOPQRSTUVWXYZ"]

# graph colors
non_select_color = "#576574"
highlight_color = "#F79F1F"
background = "#c8d6e5"


def make_column_of_weepeople(people_preped):
    result = []
    # i want columns of width 10 so a new item every 10 length
    for i in range(0, len(people_preped), 10):
        result.append("".join(people_preped[i : i + 10]))
    return "\n".join(result)


def generate_population(chars: list = chars) -> list:
    return random.choices(chars, k=100)


def sigmoid(x, k=1, c=0):
    return 1 / (1 + np.exp(-k * (x - c)))


def calc_alpha_sigmoid(current_frame, start):
    if current_frame < start:
        return 0
    return float(sigmoid((current_frame - start), k=0.5, c=10))


wee_people = {
    "font": load_font(
        "https://github.com/propublica/weepeople/blob/master/weepeople.ttf?raw=true"
    )
}

people_set = generate_population()
# prep every person with <> for texthighlight function
people_set_column = make_column_of_weepeople([f"<{person}>" for person in people_set])

# generated the randomly orderd list in which the wee people will appear in the graph
show_order = list(range(100))
random.shuffle(show_order)

# wil lbe used in every frame to create the highlight_textprops
highlights = [
    {"color": highlight_color if i < 26 else non_select_color, "start": char_show[-1]}
    for i, char_show in enumerate(zip(people_set, show_order))
]


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

    fig_text(
        s="Source: Centraal Bureau voor de Statistiek\nVisualisation: Sebastiaan Broekema",
        x=0.2,
        y=0.05,
    )
    highlights_props = [
        {"alpha": calc_alpha_sigmoid(i, x.get("start")), "color": x.get("color")}
        for x in highlights
    ]
    ax_text(
        50,
        0,
        s=people_set_column,
        va="bottom",
        ha="center",
        **wee_people,
        size=40,
        highlight_textprops=highlights_props,
        color=non_select_color,
        alpha=0,
    )

    if i > 110:
        ax_text(
            x=50,
            y=81,
            s="26 of them would have been <smokers> in 2014",
            ha="center",
            va="top",
            size=18,
            highlight_textprops=[{"color": highlight_color}],
        )
    if i < 105:
        ax_text(
            x=50,
            y=81,
            s="How many of them would have been <smokers> in 2014?",
            ha="center",
            va="top",
            size=18,
            highlight_textprops=[{"color": highlight_color}],
        )

    fig.set_facecolor(background)
    ax.set_facecolor(background)


frames = [create_frame(x) for x in range(130)]
# looping variant in which the wee people wil disapear again in reverse order of appearance
frames_looping = frames + [frames[-1]] * 10 + frames[::-1]
gif.save(frames_looping, "looping_wee_people.gif", duration=40)

# add final frame in the front (so the final frame is the complete graph)
gif.save([frames[-1]] + frames, "temp.gif", duration=40)


# open the resulting gif and make it non looping
with Image.open("temp.gif") as img:
    img.save(
        "non_looping_wee_people_final.gif",
        save_all=True,
        append_images=[img.copy() for _ in range(img.n_frames)],
        loop=1,
        duration=40,
    )
