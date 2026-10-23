"""
Sayısal verilerle çalışma - Giriş: Sayı gibi görünen her şey sayısal veri midir?
Sayısal veride toplama, ortalama, sıralama, oran anlamlıdır; posta kodunda değildir.
Çalıştır: python kod/04-sayisal-veri/sayisal_mi_kategorik_mi.py
"""
import numpy as np

sicaklik = np.array([12.5, 18.0, 25.0])                        # °C  → sayısal
geyik = np.array([120, 240, 60])                               # adet → sayısal
posta_kodu = np.array([40004, 20002, 10001])                   # ABD posta kodları → kategorik

print("== Sayısal veriler: matematik anlamlı ==")
print(f"  Ortalama sıcaklık          : {sicaklik.mean():.1f} °C")
print(f"  2. alandaki geyik / 1.     : {geyik[1] / geyik[0]:.0f} kat (gerçekten 2 kat fazla geyik)")
print(f"  Sıralama (azdan çoğa)      : {np.sort(geyik)}")

print("\n== Posta kodu: sayı gibi görünüyor ama kategorik ==")
print(f"  40004 / 20002              = {posta_kodu[0] / posta_kodu[1]:.0f}  → Nelson County, Washington DC'nin '2 katı' DEĞİL")
print(f"  Ortalama posta kodu        = {posta_kodu.mean():.0f}  → hiçbir yere karşılık gelmiyor")
print(f"  10001 < 20002 < 40004      → bu sıralama da bir anlam taşımıyor")
