import numpy as np
import matplotlib.pyplot as plt

array=np.linspace(1,100,10)
randarray=np.random.rand(len(array))*10

plt.figure(figsize=(10,6))
plt.plot(array,randarray,marker='o', color='r',linewidth=2)
plt.xlabel("Data counts")
plt.ylabel("Data values")
plt.title("This is the new title")
# plt.savefig('testFigure.png',dpi=100,bbox_inches='tight')