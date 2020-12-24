import matplotlib.pyplot as plt
import numpy as np


x = ["A","B","C","D","E","F","G","H","I","J"]
y = np.random.randint(10,100,10)

y1 = np.random.randint(10,100,10)
y2 = np.random.randint(10,100,10)

plt.xlabel("X-axis",fontdict={"fontsize":15})
plt.ylabel("Y-axis",fontdict={"fontsize":15})
plt.title("Bar Plot",fontdict={"fontsize":20})

# FOR PLOTTING THE VERTICAL BARPLOT
#plt.bar(x,y) 
# fOR PLOTTING THE HORIZONTAL BARPLOT
#plt.barh(x,y) 

# FOR PLOTTING THE VERTICALLY STACKED BARPLOT
#plt.bar(x,y1,width=0.35,color="red",label="Green Flower")
#plt.bar(x,y2,bottom=y1,width=0.35,color="green", label="Red Flower")

#FOR PLOTTING THE HORIZONTALLY STACKED BARPLOT
plt.barh(x,y1,color="red",label="Red Flower")
plt.barh(x,y2,color="blue",left=y1,label="Blue Flower")

#plt.legend()
#plt.show()