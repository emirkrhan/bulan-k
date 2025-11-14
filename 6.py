import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

x = np.arange(20, 81, 1)

low = fuzz.trapmf(x, [20, 25, 35, 40])
med = fuzz.trapmf(x, [30, 42, 55, 80])

rule1_mamdani = np.fmin(0.4, low)
rule2_mamdani = np.fmin(0.75, med) 

rule1_larsen = 0.4 * low
rule2_larsen = 0.75 * med

plt.figure(figsize=(8,5))
plt.plot(x, low, 'b--', label='Low')
plt.plot(x, med, 'orange', linestyle='--', label='Med')
plt.fill_between(x, rule1_mamdani, alpha=0.4, color='blue', label='Rule1 Mamdani (Low)')
plt.fill_between(x, rule2_mamdani, alpha=0.4, color='orange', label='Rule2 Mamdani (Med)')
plt.title('Mamdani Çıkarımı')
plt.xlabel('Sıcaklık')
plt.ylabel('Üyelik')
plt.legend()
plt.show()

plt.figure(figsize=(8,5))
plt.plot(x, low, 'b--', label='Low')
plt.plot(x, med, 'orange', linestyle='--', label='Med')
plt.fill_between(x, rule1_larsen, alpha=0.4, color='blue', label='Rule1 Larsen (Low)')
plt.fill_between(x, rule2_larsen, alpha=0.4, color='orange', label='Rule2 Larsen (Med)')
plt.title('Larsen Çıkarımı')
plt.xlabel('Sıcaklık')
plt.ylabel('Üyelik')
plt.legend()
plt.show()
