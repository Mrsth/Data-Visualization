import matplotlib.pyplot as plt
import numpy as np
from numpy import random

x = random.randint(0,100,30)
bins = 30

x_ticks = np.arange(0,100,5)

# Bins is the number of bars required
plt.hist(x, density=True, bins=30, ec="white", width=5 )
plt.xticks(x_ticks)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Histogram chart", fontdict={"fontsize":20, "fontweight":"bold"})
plt.plot()