import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url = "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/refs/heads/master/static/data/iris.csv"
iris = pd.read_csv(url)

x = iris["sepal_length"]
y = iris["sepal_width"]

color_mapping = {
"virginica":  "#9e0059", 
"versicolor":  "#390099",
"setosa":  "#ff5400"}

color = iris['species'].map(color_mapping)

fig, ax = plt.subplots()

ax.scatter(x=x, y=y, c=color)


plt.show()

# ===


color_mapping = {
"virginica":  "#78290f", 
"versicolor":  "lightgrey",
"setosa":  "lightgrey"}

color = iris['species'].map(color_mapping)

fig, ax = plt.subplots()

ax.scatter(x=x, y=y, c=color)


plt.show()

# === 


url = "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/storms.csv"
storms = pd.read_csv(url)
df = storms.groupby("status", as_index=False)["n"].sum()
df = df.sort_values("n")

labels = df["status"]
y = df["n"]


color = df['status'].apply(lambda x: "#335c67" if x == "tropical storm" else "lightgrey")

fig, ax = plt.subplots()

ax.bar(x=labels, height=y, color=color)


plt.show()



# == 

pivot_df = storms.pivot_table(
  index="year",  # year is now the index
  columns="status",  # column are the kind of storm
  values="n",  # df content is taken from the 'n' column
)

columns = ['hurricane', 'tropical depression', 'tropical storm', 'tropical wave']
colors = [ '#0077b6', 'lightgrey','lightgrey','lightgrey']


fig, ax = plt.subplots()


for column, color in zip(columns,colors):
    ax.plot(pivot_df.index, pivot_df[column], color=color)


plt.show()




# === 

df = pd.DataFrame({
  "sizes": [20, 40, 20, 20],
  "labels": ["A", "B", "C", "D"]
})

values = df["sizes"]
labels = df["labels"]


color_mapping={
True: "#4b6c96", 
False: "#f2ebeb"}


fig, ax = plt.subplots()


ax.pie(x=values, labels=labels,colors=(labels == "B").map(color_mapping), explode=[0.1]*len(labels))
ax.pie(x=[1], labels=[''],colors=['white'],radius=0.7)

plt.show()



#===

df = pd.DataFrame({
  "A": [5, 12, 23, 9, 41],
  "B": [8, 17, 31, 4, 29],
})

y = df.index


fig, ax = plt.subplots()



ax.scatter(x=df['A'], y=y,color='Red')
ax.scatter(x=df['B'], y=y, color='Blue')
ax.hlines(y=y, xmin=df['A'], xmax=df['B'],color='k',zorder=-1)
ax.legend(labels=["A", "B"])


plt.show()



# == 

np.random.seed(0)
x = np.random.normal(size=1000)


# 1 are "darkgray", and "skyblue"

hist, bin_edges = np.histogram(x, bins=40)



threshold = 1
lower_color = "lightblue"
upper_color = "darkgray"

# create a list of colors
colors = []
for bin_edge in bin_edges:
    if bin_edge < threshold:
        colors.append(lower_color)
    else:
        colors.append(upper_color)

# make the plot
fig, ax = plt.subplots()
ax.bar(
    bin_edges[:-1], 
    hist, 
    width=np.diff(bin_edges), 
    color=colors, 
) 
plt.show()