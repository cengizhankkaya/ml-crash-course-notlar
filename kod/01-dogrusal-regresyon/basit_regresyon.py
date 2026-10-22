"""
Doğrusal Regresyon - Giriş
Kurstaki ağırlık → yakıt verimliliği verisine en iyi doğruyu uyduruyoruz.
"""
import numpy as np

# Özellik (x): ağırlık (bin pound), Etiket (y): mil/galon
x = np.array([3.50, 3.69, 3.44, 3.43, 4.34, 4.42, 2.37])
y = np.array([18, 15, 18, 16, 15, 14, 24])

# En küçük kareler ile w (eğim) ve b (yanlılık) hesapla
w, b = np.polyfit(x, y, deg=1)
print(f"Öğrenilen model: y' = {b:.2f} + ({w:.2f}) * x")

# Kurstaki örnek model ile karşılaştır
def tahmin(x, b, w):
    return b + w * x

print(f"Kurs modeli (b=34, w=-4.6) → 4.0 için: {tahmin(4.0, 34, -4.6):.1f} mpg")
print(f"Bizim model               → 4.0 için: {tahmin(4.0, b, w):.1f} mpg")
