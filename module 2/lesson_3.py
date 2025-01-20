import matplotlib.pyplot as plt
import pandas as pd


x = [10, 20, 30, 40]
labels = ["France", "Japan", "Italy", "Spain"]
colors = ["dodgerblue", "firebrick", "dodgerblue","dodgerblue" ]

fig, ax = plt.subplots()

ax.barh(labels, width=x, color=colors)



plt.show()


# 



y = [10, 20, 30, 40, 50, 60, 70]


labels = [
   "France", "Japan", "Italy", "Spain",
   "Germany", "Brazil", "India"
]
continents = [
   "Europe", "Asia", "Europe", "Europe",
   "Europe", "South America", "Asia"
]

color_dict = {
    "Europe": "dodgerblue", "Asia": 'firebrick', "South America": "olivedrab"
}

colors = [color_dict[x] for x in continents]


fig, ax = plt.subplots()

ax.barh(labels, width=y, color=colors, height=0.75)


plt.show()

# donut chart



sizes = [25, 35, 20, 20]
labels = ["A", "B", "C", "D"]
colors = ["dodgerblue", "firebrick", 'olivedrab', 'orchid']



fig, ax = plt.subplots()

ax.pie(x=sizes, labels=labels, colors=colors)
ax.pie(x=[1], labels=[""], radius=0.66, colors='white')

plt.show()
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-14/astronauts.csv"

df = pd.read_csv(url)

x = df["year_of_birth"]
y = df["year_of_mission"]


fig, ax = plt.subplots()

ax.hist2d(x, y , cmap="viridis")

plt.show()




url = "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/refs/heads/master/static/data/iris.csv"
df = pd.read_csv(url)

# with the "sepal_length" column on the x-axis 
# and the "sepal_width" column on the y-axis. 
# Use the "petal_length" column to determine the color of the points.

x = df['sepal_length']
y = df['sepal_width']
c = df['petal_length']


fig, ax = plt.subplots()

ax.scatter(x,y, c=c, cmap='viridis', s=250)


plt.show()



fig, ax = plt.subplots()
c = pd.Categorical(df["species"]).codes
ax.scatter(x,y, c=c, cmap="viridis", s=250)


plt.show()