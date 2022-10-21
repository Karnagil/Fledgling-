import matplotlib.pyplot as plt
import numpy as np
import random

x1=np.array([0,0,5,8,8,5,0])
y1=np.array([0,8,8,6,2,0,0])
x2=np.array([1.5,1.5,5,6.5,6.5,5,1.5])
y2=np.array([2,6,6,5,3,2,2])

dict1={"family":"serif","color":"red","size":10}
dict2={"family":"serif","color":"crimson","size":10}
dict3={"family":"font","color":"DarkBlue","size":10}
dict4={"family":"font","color":"yellow","size":10}
plt.title("\"D\" is for DRESUN999",fontdict=dict1)
plt.xlabel("@DRESUN999: The Programmer", fontdict=dict2)
plt.ylabel("@DRESUN999",fontdict=dict3)
plt.plot(x1,y1,"r",x2,y2,"y")
plt.show()