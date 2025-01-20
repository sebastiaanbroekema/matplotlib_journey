import matplotlib.pyplot as plt

y = [
   "Apple",
   "Banana",
   "Cherry",
   "Date",
   "Elderberry",
   "Fig"
]
values = [12, 8, 15, 6, 10, 4]

fig, ax = plt.subplots()

ax.barh(y=y, width=values)
ax.bar(x=y, height=values)
# ax.set_axis_off()

plt.show()





x = [1, 2, 3, 4, 5, 6]
y = [12, 8, 15, 6, 10, 4]
y2 = [12, 8, 15, 6, 10, 4][::-1]

fig, ax = plt.subplots()

ax.fill_between(x=x, y1=y, y2=y2)

plt.show()


# stemplots


y = [12, 8, 15, 6, 10, 4]
x = ['a', 'b', 'c', 'd', 'e', 'f']

fig, ax = plt.subplots()

ax.stem(y, x)

plt.show()



x = [
   10, 12, 11, 13,
   15, 17, 12, 16,
   15, 21, 9, 14,
   14, 15, 13
]


fig, ax = plt.subplots()

ax.hist(x, bins=20)
plt.show()



x = [1, 2, 3, 4, 5, 6]
y = [12, 8, 15, 6, 10, 4]
s = [1, 200, 300, 400, 200, 100000]


fig, ax = plt.subplots()

ax.scatter(x,y, s)

plt.show()



x = [16, 8, 6, 20, 15]
labels = ["Nike", "Adidas", "Asics", "Puma", "Jordan"]


fig, ax = plt.subplots()

ax.pie(x=x, labels=labels)

plt.show()

x = [16, 8, 6, 20, 15]

fig, ax = plt.subplots()

ax.boxplot(x)

plt.show()

x = [
   [16, 8, 6, 20, 15],
   [1, 4, 12, 5, 13],
   [20, 9, 3, 17, 9],
]


fig, ax = plt.subplots()

ax.imshow(x)

plt.show()


import numpy as np

x = np.random.normal(size=10000)
y = np.random.normal(size=10000)

fig, ax = plt.subplots()

ax.hist2d(x,y)

plt.show()