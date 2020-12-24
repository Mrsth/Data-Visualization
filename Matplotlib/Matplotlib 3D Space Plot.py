import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [10,20,30,40,50]
z = [80,90,60,40,70]

x1 = np.linspace(0,2,10)
y1 = np.linspace(10,20,10)
z1 = np.linspace(30,40,10)

sizes = np.random.randint(10,100,5)

plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
ax.scatter(x1,y1,z1, s=sizes)
#ax.plot(x,y,z)

ax.set_title("3D Scatter Plot", fontdict={"fontsize":20, "fontweight":"bold"})
ax.set_xlabel("X-axis", fontdict={"fontsize":15})
ax.set_ylabel("Y-axis", fontdict={"fontsize":15})
ax.set_zlabel("Z-axis", fontdict={"fontsize":15})

plt.show()