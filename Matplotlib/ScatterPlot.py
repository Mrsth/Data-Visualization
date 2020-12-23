import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0,10,20)
y = np.random.randint(0,50,20)

a = np.random.randint(0,40,20)
b = np.random.randint(0,50,20)

p = np.random.randint(0,70,20)
q = np.random.randint(0,90,20)

sizes = np.abs(np.random.randn(50))*100
colors = np.random.randint(0,50,20)

'''plt.scatter(x,y, color="green", label="Green dots", s=sizes)
plt.scatter(a,b, color="blue", label="Blue dots", s=sizes)
plt.scatter(p,q, color="red", label="Red dots", s=sizes)
plt.legend()
'''

plt.scatter(x,y, c=colors, label="Green dots", s=sizes)
plt.scatter(a,b, c=colors, label="Blue dots", s=sizes)
plt.scatter(p,q, c=colors, label="Red dots", s=sizes)

plt.title("Scatter Plot", fontdict={"fontsize":20})
plt.xlabel("X-axis", fontdict={"fontsize":20})
plt.ylabel("Y-axis", fontdict={"fontsize":20})


plt.show()