import matplotlib.pyplot as plt
import numpy as np

fig,ax = plt.subplots(2,2)

x = np.linspace(0,2,10)
y = np.linspace(0,2,10)

ax[0,0].plot(x,y*1, color="green", linewidth=2, label="green")
ax[0,0].plot(x,y*2, color="red", linewidth=2, label="red")
ax[0,0].plot(x,y*3, color="blue", linewidth=2, label="blue")
ax[0,0].plot(x,y*4, color="brown", linewidth=2, label="brown")

ax[0,1].plot(x,y-0, color="green", linewidth=2, label="green")
ax[0,1].plot(x,y-10, color="blue", linewidth=2, label="blue")
ax[0,1].plot(x,y-20, color="red", linewidth=2, label="red")
ax[0,1].plot(x,y-30, color="brown", linewidth=2, label="brown")

ax[1,0].plot(x,y**2, color="green", linewidth=2, label="green")
ax[1,0].plot(x,y**3, color="red", linewidth=2, label="red")
ax[1,0].plot(x,y**4, color="blue", linewidth=2, label="blue")
ax[1,0].plot(x,y**5, color="brown", linewidth=2, label="brown")

ax[1,1].plot(x,y**2, color="green", linewidth=2, label="green")
ax[1,1].plot(x,y**3, color="blue", linewidth=2, label="blue")
ax[1,1].plot(x,y**4, color="red", linewidth=2, label="red")
ax[1,1].plot(x,y**5, color="brown", linewidth=2, label="brown")

ax[0,0].legend(fontsize = 'x-small')
ax[0,1].legend(fontsize='x-small')
ax[1,0].legend(fontsize='x-small')
ax[1,1].legend(fontsize='x-small')

plt.plot()