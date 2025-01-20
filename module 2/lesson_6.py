import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pypalettes import load_cmap


# Create a simple wrapper around the ax.plot() function.

#     Name the function plot_blue_and_thick()
#     Set the color to blue using color="skyblue"
#     Set the line width to large using linewidth=10
#     Call the function with the x and y values.


def plot_blue_and_thick(ax,x,y):

    ax.plot(x,y, color='blue',linewidth = 10)
    return ax



x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 10, 2]

fig, ax = plt.subplots()


ax = plot_blue_and_thick(ax, x,y)

plt.show(block=False)

#===


url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/footprint/footprint.csv"
df = pd.read_csv(url)


# Use the "lifexp" column for the x-axis.
# Use the "gdpCapita" column for the y-axis.
# Use the "region" column to define the colors


fig, ax = plt.subplots()

sns.scatterplot(data=df, x='populationMillions', y='footprint', hue="region")


plt.show()

#==

fig, ax = plt.subplots()

sns.regplot(data=df, x='populationMillions', y='footprint')

sns.despine()
plt.show()



#==
fig, ax = plt.subplots()
sns.stripplot(data=df, x='region',y='populationMillions',hue='populationMillions',size=5,alpha=0.5)

sns.despine()
plt.show()
