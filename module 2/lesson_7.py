import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/footprint/footprint.csv"
footprint = pd.read_csv(open_url(url))

x = footprint["gdpCapita"]
y = footprint["footprint"]

fig, ax = plt.subplots()
ax.scatter(x, y, s=100, alpha=0.6)
ax.tick_params(length=0)

sns.despine()
plt.show()




import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/footprint/footprint.csv"
footprint = pd.read_csv(url)

x = footprint["gdpCapita"]
y = footprint["footprint"]

fig, ax = plt.subplots()
ax.scatter(x, y, s=100, alpha=0.6)

ax.tick_params(
  labelsize=12,
  labelcolor="#9f1818",
)

plt.show()