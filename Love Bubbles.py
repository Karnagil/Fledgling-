import matplotlib.pyplot as plt
import numpy as np
import random

x=np.random.randint(200,size=(200))
y=np.random.randint(200,size=(200))
colors=np.random.randint(200,size=(200))

dict1={"family":"serif","color":"red","size":10}
dict2={"family":"serif","color":"crimson","size":10}
dict3={"family":"font","color":"DarkBlue","size":10}

plt.title("Love Bubbles ^_^",fontdict=dict1)
plt.xlabel("@DRESUN999: The Programmer",fontdict=dict2)
plt.ylabel("@DRESUN999",fontdict=dict3)
plt.scatter(x,y,c=colors,s=colors,cmap="rainbow",alpha=0.4)
plt.colorbar()
plt.show()