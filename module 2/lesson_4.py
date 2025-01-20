import matplotlib.pyplot as plt
from pypalettes import load_cmap
import pandas as pd

cmap = load_cmap('FireNation')





import matplotlib.pyplot as plt
from pypalettes import load_cmap

year = [2010, 2011, 2012, 2013]
y1 = [3, 4, 2, 5]
y2 = [1, 5, 3, 2]
y3 = [8, 2, 4, 6]
y4 = [8, 12, 4, 1]


fig, ax = plt.subplots()



ax.stackplot(year, y1, y2, y3, y4, colors=cmap.colors)


plt.show()




url = "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/refs/heads/master/static/data/iris.csv"
iris = pd.read_csv(url)


x = iris["sepal_length"]
y = iris["sepal_width"]
c = pd.Categorical(iris["species"]).codes



fig, ax = plt.subplots()

ax.scatter(x=x, y=y, c=c, cmap=load_cmap("Alosa_fallax"))


plt.show()





# Althoff


url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-07-14/astronauts.csv"
df = pd.read_csv(url)

x = df["year_of_birth"]
y = df["year_of_mission"]


fig, ax = plt.subplots()

cmap = load_cmap("Althoff", cmap_type="continuous")

ax.hist2d(x,y, 
# cmap=cmap, 
bins=20)


plt.show()


cmap = load_cmap("Aluterus_scriptus", 
# reverse=True, 
cmap_type="continuous")


fig, ax = plt.subplots()

ax.hist2d(
    x,y, cmap=cmap, bins=20
)


plt.show()



fig, ax = plt.subplots()

ax.vlines()

plt.show()


# copilot please create a bundled cord diagram