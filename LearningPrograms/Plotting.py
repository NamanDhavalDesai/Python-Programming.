import numpy as np
import matplotlib.pyplot as plt
x=np.random.normal(100,10,250)
y=range(1,251)
z=list()
for i in y:
    z.append(i*i)
#Exponential graph
plt.subplot(6,2,1)
plt.plot(y,z)
#Scatter plot
plt.subplot(6,2,2)
plt.scatter(x,y,s=2)
#Bar graph
plt.subplot(6,2,5)
plt.bar(x,y,width=0.1)
#Histogram
plt.subplot(6,2,6)
plt.hist(x)
plt.subplot(6,2,9)
plt.hist(x,bins=25)
#Pie chart
plt.subplot(6,2,10)
y=np.array([35,25,25,15])
c=['blue','yellow','indigo','red']
e=[0.15,0,0,0]
plt.pie(y,labels=['MI','CSK','KKR','RCB'],explode=e,shadow=True)
plt.show()