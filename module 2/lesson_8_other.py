import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from pypalettes import load_cmap

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/natural-disasters/natural-disasters.csv"
df = pd.read_csv(url)

columns = df.drop(columns="Year").sum().sort_values().index.to_list()
x = df["Year"]
y = np.stack(df[columns].values, axis=-1)

fig, ax = plt.subplots(figsize=(10, 5))

colors = load_cmap("Antique").colors

ax.stackplot(x, y, colors=colors, labels=columns, baseline='wiggle')
ax.set_xlim(1960, 2023)
ax.spines[["top", "left"]].set_visible(False)
ax.yaxis.tick_right()
ax.text(
   x=1960,
   y=380,
   s="Evolution of natural disasters between 1960 and 2023",
   size=12,
)
ax.text(x=1960, y=355, s="Data source: EM-DAT")
ax.legend(reverse=True, loc="center left")
# ax.set_xticks([1960, 1980, 2000, 2020])
# ax.set_yticks([100, 200, 300, 400])
ax.tick_params(length=0, pad=5)

plt.show()