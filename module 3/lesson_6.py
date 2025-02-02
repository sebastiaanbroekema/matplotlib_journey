import matplotlib.pyplot as plt
import pandas as pd
from drawarrow import ax_arrow,fig_arrow





fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [3, 2, 1])


ax_arrow((2,2), (3,1), color='purple')

plt.show(block=False)


#===

fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [3, 2, 1])


ax_arrow((2,2), (3,1), color='red',radius=0.5 ,double_headed=True, fill_head=False)

plt.show(block=False)






fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [3, 2, 1])


ax_arrow((1,3), (3,1), color='red',radius=0.2, head_width=15, head_length=10 )

plt.show(block=False)





fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [3, 2, 1])

fig_arrow((0.1, 0.9), (0.9, 0.9) )

plt.show(block=False)