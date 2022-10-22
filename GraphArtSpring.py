import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
x1 = np.random.randint(50, size=(50))
y1 = np.random.randint(50, size=(50))
colors = np.random.randint(100, size=(100))
sizes = 20*np.random.randint(100, size=(100))
sizes2 = 20*np.random.randint(200,size=(100))
plt.scatter(x, y,marker='H', c=colors,s=sizes2,cmap='Greens')
plt.scatter(x, y,marker='H', c=colors, s=sizes, cmap='spring')
plt.plot(x,y,"p",ms=9,mec="purple",mfc="red")
plt.title("Graph-Art")
plt.xlabel("@Dresun999")
plt.colorbar()
plt.show()