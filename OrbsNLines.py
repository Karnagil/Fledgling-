import matplotlib.pyplot as plt
import numpy as np
x=np.random.randint(100, size=(100))
y=np.random.randint(100, size=(100))
colors=np.random.randint(100,size=(100))
dictfont={"family":"serif","color":"blue","size":8}
plt.title("Colors:Rainbow",fontdict=dictfont)
plt.xlabel("@Dresun999",fontdict=dictfont)
sizes=np.random.randint(100,size=(100))
plt.scatter(x,y,c=colors,s=sizes,alpha=0.5,cmap="nipy_spectral")
plt.colorbar()
plt.plot(x,y,c="red", alpha=0.1)
plt.show()