import numpy as np
import matplotlib.pyplot as plt
a = np.linspace(0,30,100000)
b = np.exp(-a)
c=np.sin(a)

plt.plot(a,c)
plt.show()
print a