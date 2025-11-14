import numpy as np
import matplotlib.pyplot as plt

def ucgen_uyelik(a, b, c, x):
    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

x_values = np.linspace(0, 10, 100)
mu_values = np.array([ucgen_uyelik(2, 5, 8, x) for x in x_values])

mu_power = mu_values ** 2

mu_derisme = mu_values ** 2

mu_genisleme = np.sqrt(mu_values)

mu_yogunlasma = np.where(mu_values <= 0.5,
                         2 * (mu_values ** 2),
                         1 - 2 * (1 - mu_values) ** 2)

plt.figure(figsize=(10,6))
plt.plot(x_values, mu_values, label="Orijinal", linewidth=2)
plt.plot(x_values, mu_power, label="Kuvvet (μ^2)")
plt.plot(x_values, mu_derisme, label="Derişme (μ^2)")
plt.plot(x_values, mu_genisleme, label="Genişleme (√μ)")
plt.plot(x_values, mu_yogunlasma, label="Yoğunlaşma")
plt.title("Bulanık Küme Üzerinde İşlemler")
plt.xlabel("x")
plt.ylabel("Üyelik Derecesi (μ)")
plt.legend()
plt.grid(True)
plt.show()
