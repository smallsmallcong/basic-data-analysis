import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 500)
y1 = np.sin(x)
y2 = np.sin(3 * x)

fig, ax = plt.subplots(figsize = [20,10])
ax.fill(x, y1, 'b', x, y2, 'r', alpha=0.3)
plt.savefig('sin3.png')
plt.show()