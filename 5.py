import numpy as np
import matplotlib.pyplot as plt

x = np.arange(20, 81, 1)

def trapmf(x, a, b, c, d):
    y = np.zeros_like(x, dtype=float)
    for i in range(len(x)):
        if x[i] <= a:
            y[i] = 0
        elif a < x[i] <= b:
            y[i] = (x[i] - a) / (b - a)
        elif b < x[i] <= c:
            y[i] = 1
        elif c < x[i] <= d:
            y[i] = (d - x[i]) / (d - c)
        else:
            y[i] = 0
    return y

# Üyelik fonksiyonlarını oluştur
low = trapmf(x, 20, 25, 35, 40)
med = trapmf(x, 30, 42, 55, 80)

# --- Kesişim (T-norm)
t_min = np.minimum(low, med)
t_algebraic = low * med
t_bounded = np.maximum(0, low + med - 1)

# --- Birleşim (S-norm)
s_max = np.maximum(low, med)
s_algebraic = low + med - (low * med)
s_bounded = np.minimum(1, low + med)

# --- Grafikler
plt.figure(figsize=(12,10))

plt.subplot(3,2,1)
plt.plot(x, low, 'b', label='Low')
plt.plot(x, med, 'orange', label='Med')
plt.title('Üyelik Fonksiyonları (Hazır fonksiyonsuz)')
plt.xlabel('Sıcaklık')
plt.ylabel('Üyelik')
plt.legend()

plt.subplot(3,2,2)
plt.plot(x, t_min, 'r', label='Min (AND)')
plt.plot(x, t_algebraic, 'g', label='Algebraic Product')
plt.plot(x, t_bounded, 'purple', label='Bounded Product')
plt.title('Kesişim (T-Norm)')
plt.xlabel('Sıcaklık')
plt.ylabel('Üyelik')
plt.legend()

plt.subplot(3,2,3)
plt.plot(x, s_max, 'r', label='Max (OR)')
plt.plot(x, s_algebraic, 'g', label='Algebraic Sum')
plt.plot(x, s_bounded, 'purple', label='Bounded Sum')
plt.title('Birleşim (S-Norm)')
plt.xlabel('Sıcaklık')
plt.ylabel('Üyelik')
plt.legend()

plt.tight_layout()
plt.show()
