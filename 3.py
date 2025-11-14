import numpy as np
import matplotlib.pyplot as plt

def uyelik_hesapla(a, b, u):
    """
    Bu fonksiyon YAKIN kümesinin üyelik değerini hesaplar.
    a: tam yakınlığın bittiği nokta (örnek: 200)
    b: uzaklığın başladığı nokta (örnek: 500)
    u: verilen mesafe
    """
    if u < a:
        return 1
    elif a <= u <= b:
        return (b - u) / (b - a)
    else:
        return 0

mesafe = np.linspace(-500, 500, 1001)

yakin = [uyelik_hesapla(200, 500, abs(u)) for u in mesafe]

plt.figure(figsize=(10, 5))
plt.plot(mesafe, yakin, color='orange', linewidth=2)
plt.title("YAKIN Bulanık Kümesi - Fonksiyonla Hesaplama", fontsize=14)
plt.xlabel("Mesafe")
plt.ylabel("Yakınlık (üyelik değeri)")
plt.grid(True)

plt.axvline(x=-500, color='gray', linestyle='--', linewidth=0.8)
plt.axvline(x=-200, color='gray', linestyle='--', linewidth=0.8)
plt.axvline(x=200, color='gray', linestyle='--', linewidth=0.8)
plt.axvline(x=500, color='gray', linestyle='--', linewidth=0.8)

plt.show()

u = float(input("Bir mesafe gir (örnek 250): "))
uyelik = uyelik_hesapla(200, 500, abs(u))
print(f"{u} mesafesi için yakınlık derecesi: {uyelik:.2f}")
