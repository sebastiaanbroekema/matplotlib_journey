import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [3, 2, 1])

fig.text(0.5, 0.5, 'I am in the middle of the figure')
ax.text(1.5, 1.5, 'i am in the middle of the axis\nor i would be if the limits were at 0')


plt.show()



fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [3, 2, 1])


ax.title('i am a title', color='red', loc='center')
ax.text(x=1.05, y=3, s="first dot")
ax.text(x=2.05, y=2, s="second dot")
ax.text(x=3.05, y=1, s="third dot")

plt.show()

    # Use ha="right" to set the horizontal alignment.
    # Use a fixed x-axis value (for example, x=3) for the location.
    # Use annotations of varying lengths (long, medium, and short text).


fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [3, 2, 1])


for i in range(1,4):
    ax.text(3,i, 'string' * (i**i),ha='right')


plt.show()


    # Set the size to 16.
    # Set the color to "purple".
    # Set the weight to "bold".


text_dict = dict(
    size=16,
    color = 'purple',
    weight = "bold"
)

fig, ax = plt.subplots()

ax.plot([1, 2, 3], [3, 2, 1])

for i,j in zip(range(1,4), range(4,1, -1)):
    ax.text(i,j,f'text_{i}_{j}', **text_dict)

ax.set_xlim(1,4)
ax.set_ylim(1,4)


plt.show()





url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/natural-disasters/natural-disasters.csv"
df = pd.read_csv(url)

fig, ax = plt.subplots()
ax.plot(df["Year"], df["Earthquake"])

ax.set_ylim(0, 45)
ax.spines[["top", "right"]].set_visible(False)
ax.axhline(25, color='#bc1f1f')

ax.text(1970, 25.5, 'threshold mc threshold 25')

plt.show()


