import matplotlib.pyplot as plt
import random
x = [0,6,3]
y = [0,0,3]
rpx=[3]
rpy=[1]
for i in range(1,1000000):
    v1=random.randint(1,len(rpx))
    v2=random.randint(1,3)
    midx=(x[v2-1]+rpx[v1-1])/2
    midy=(y[v2-1]+rpy[v1-1])/2
    rpx.append(midx)
    rpy.append(midy)

x=[*x, *rpx]
y=[*y, *rpy]
plt.scatter(x, y,s=1)
plt.show()