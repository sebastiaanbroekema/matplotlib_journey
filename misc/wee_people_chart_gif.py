import copy
import random

import numpy as np
import gif
import matplotlib.pyplot as plt
from highlight_text import ax_text, fig_text
from pyfonts import load_font
from PIL import Image

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
people_set_column = make_column_of_weepeople([f"<{person}>" for person in people_set])
show_order = list(range(100))
random.shuffle(show_order)


highlights = [
    {"color": highlight_color if i < 26 else non_select, "start": char_show[-1]}
    for i, char_show in enumerate(zip(people_set, show_order))
]


def sigmoid(x, k=1, c=0):
    return 1 / (1 + np.exp(-k * (x - c)))


def calc_alpha(current_frame, max_frame, start):
    # delta = (start/max_frame)
    delta = 1 / (max_frame / start)
    print(delta)
    if current_frame < start:
        return 0
    # alpha =   ((delta * (current_frame - start)) / max_frame) * 100
    alpha = (delta * (current_frame - start)) / max_frame
    if alpha > 1:
        return 1
    else:
        return alpha


def calc_alpha_sigmoid(current_frame, start):
    if current_frame < start:
        return 0
    return float(sigmoid((current_frame - start), k=0.5, c=10))


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
        color=non_select,
        alpha=0,
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


frames = [create_frame(x) for x in range(130)]

frames_looping = frames + [frames[-1]] * 10 + frames[::-1]
gif.save(frames_looping, "looping_wee_people.gif", duration=40)

gif.save(frames, "non_looping_wee_people.gif", duration=40)


# Open the existing GIF
with Image.open("non_looping_wee_people.gif") as img:
    # Save the GIF with loop set to 0 (non-looping)
    img.save(
        "non_looping_wee_people_final.gif",
        save_all=True,
        append_images=[img.copy() for _ in range(img.n_frames)],
        loop=1,
        duration=40,
    )
