
import matplotlib.pyplot as plt



# barh

x = [10, 20, 30, 40]
labels = ["France", "Japan", "Italy", "Spain"]


fig, ax = plt.subplots()

ax.barh(y=labels, width=x, height=0.5, color='dodgerblue')

plt.show()


# scatter plot

x = [10, 20, 30, 40]
y = [30, 20, 80, 10]

    # The points are "white".
    # The point size is 100.
    # The point edges are "red".
    # The edge width is thick.


fig, ax = plt.subplots()

ax.scatter(x,y, color="white", s=100, edgecolors="red", linewidth=3)

plt.show()





# # lineplot
#     The line is "green".
#     The line width is thick.

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 4]



fig, ax = plt.subplots()

ax.plot(x, y, color="green", linewidth=3)

plt.show()


# hist



x = [
   10, 12, 11, 13,
   15, 17, 12, 16,
   15, 21, 9, 14,
   14, 15, 13
]


fig, ax = plt.subplots()

ax.hist(x, bins=5,edgecolor='k', color='orange')

plt.show()