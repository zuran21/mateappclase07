import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 10) 
y = np.exp(x)

plt.plot(x, y)
plt.show()