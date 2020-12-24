import matplotlib.pyplot as plt
import numpy as np

x = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday"]
y = [100,200,300,400,500,600,700]
explode = [0,0,0,0.1,0,0,0.1]

#plt.pie(y, labels=x, autopct="%1.1f%%", shadow=True)
#plt.title("Week piechart",fontdict={"fontsize":20, "fontweight":"bold"})
#plt.plot()


plt.pie(y, labels=x, explode=explode, autopct="%1.1f%%", shadow=True)
plt.title("Week piechart", fontdict={"fontsize":20, "fontweight":"bold"})
plt.plot()

