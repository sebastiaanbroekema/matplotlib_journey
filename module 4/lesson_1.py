import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns


fig, axs = plt.subplots(ncols=3, layout="tight")

plt.show()




fig, axs = plt.subplots(ncols=2, nrows=3, layout="tight")

plt.show()






x = [1, 2, 3, 4, 5]
y = [10, 37, 26, 34, 1]

fig, axs = plt.subplots(ncols=2, nrows=2, layout='tight')

axs[1,0].plot(x,y)

plt.show()











x = [1, 2, 3, 4, 5]
y = [10, 37, 26, 34, 1]

fig, axs = plt.subplots(
    nrows=2, ncols=2, layout="tight"
)
axs[0, 0].plot(x, y)
axs[1, 0].plot(x, y)
axs[0, 1].plot(x, y, color="red")
axs[1, 1].plot(y, x)

plt.show()




url = "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/refs/heads/master/static/data/iris.csv"
iris = pd.read_csv(url)




x = iris["petal_length"]
y = iris["petal_width"]
c = iris["species"]

fig, axs = plt.subplots(ncols=2, nrows=2, layout='tight')




sns.scatterplot(x=x, y=y, hue=c, ax=axs[0,0])
sns.scatterplot(x=y, y=x, hue=c, ax=axs[1,0])

plt.show()