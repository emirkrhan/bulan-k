import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,10,0.1)
z=[]

for i, tutx in enumerate(x):
    z.insert(i, 1/(1+10*(tutx-5)**2))

plt.plot(x, z)
plt.show()

