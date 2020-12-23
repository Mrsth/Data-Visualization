import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,2,100)
y = np.linspace(0,2,100)


plt.plot(x, y, color="red", linewidth=4, label = "Facebook")
plt.plot(x, y**2, color="green", linewidth=4, label = "Instagram")
plt.plot(x, y**3, color="blue", linewidth=4, label = "Youtube")


plt.annotate("Facebook", xy = (1.9,7.5), xytext = (1.25,8),
             arrowprops = {"facecolor": "blue", "shrink":0.05})
plt.annotate("Instagram", xy=(2,4), xytext=(1.25,6),
             arrowprops = {"facecolor":"green", "shrink":0.05})
plt.annotate("Youtube", xy=(2,2), xytext=(1,3),
             arrowprops = {"facecolor":"red", "shrink":0.05})

plt.title("Line plot and annotation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.legend()
plt.show()