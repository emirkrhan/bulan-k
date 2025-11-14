import numpy as np
import matplotlib.pyplot as plt

mesafe = np.linspace(-500, 500, 1001)
uzaklik = np.abs(mesafe)

yakin = np.zeros_like(uzaklik)

for i in range(len(uzaklik)):
    if uzaklik[i] < 200:
        yakin[i] = 1
    elif 200 <= uzaklik[i] <= 500:
        yakin[i] = (500 - uzaklik[i]) / 300
    else:
        yakin[i] = 0

plt.figure(figsize=(10, 5)) 
plt.plot(mesafe, yakin, color='orange', linewidth=2)

plt.title("YAKIN Bulanık Kümesi (mesafe ∈ [-500, 500])", fontsize=14)
plt.xlabel("Mesafe", fontsize=12)
plt.ylabel("Yakınlık (üyelik değeri)", fontsize=12)
plt.grid(True)

plt.axvline(x=-500, color='gray', linestyle='--', linewidth=0.8)
plt.axvline(x=-200, color='gray', linestyle='--', linewidth=0.8)
plt.axvline(x=200, color='gray', linestyle='--', linewidth=0.8)
plt.axvline(x=500, color='gray', linestyle='--', linewidth=0.8)

plt.show()
