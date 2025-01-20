import matplotlib.pyplot as plt


x = [10, 20, 30, 40]
y = [30, 20, 80, 10]

fig, ax = plt.subplots()


ax.scatter(x,y, color = (0.9,0.5,0.4))

plt.show()





x = [
   10, 12, 11, 13,
   15, 17, 12, 16,
   15, 21, 9, 14,
   14, 15, 13
]


fig, ax = plt.subplots()

ax.hist(x, color = "#f5f5dc")
# ax.hist(x, color = "beige")

plt.show()


y = [10, 20, 30, 40]
labels = ["France", "Japan", "Italy", "Spain"]



fig, ax = plt.subplots()

ax.barh(y=labels, width=y, color='dodgerblue')

plt.show()


import matplotlib.colors as mcolors

x = [10, 20, 30, 40]
labels = ["France", "Japan", "Italy", "Spain"]


fig, ax = plt.subplots()

hsv_color = (0.55, 0.50, 0.43)
rgb_color = mcolors.hsv_to_rgb(hsv_color)

ax.barh(labels, width=x, color=rgb_color)

plt.show()