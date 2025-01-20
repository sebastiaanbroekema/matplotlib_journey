
import matplotlib.pyplot as plt

fig, ax = plt.subplots()


plt.show()



# ex 2



x = [1,2,3,4,5]
y = [2,3,1,4,5]


fig, ax = plt.subplots()

ax.plot(x, y)
# ax.text(1, 5, "My name")
fig.text(0.1, 0.9, 'my name' )
ax.text(1.5, 2.5, "friend name")
plt.show()