"""
Sayısal veriler - Model veriyi nasıl alır? Özellik vektörü
Veri kümesinde 5 sütun (a–e) var, ama modelin özellikleri yalnızca b ve d.
  Adım 1: Satırdan yalnızca özellik sütunlarını seç (ham değerler)
  Adım 2: Değerleri modelin daha iyi öğreneceği temsillere dönüştür
          b → normalleştirme (z-puanı), d → gruplandırma (one-hot kovalar)
Çalıştır: python kod/04-sayisal-veri/ozellik_vektoru.py
"""
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "a": ["kırmızı", "mavi", "yeşil", "mavi", "kırmızı"],     # kullanılmıyor
    "b": [1200.0, 3400.0, 2850.0, 990.0, 4100.0],             # sayısal özellik (ör. m²)
    "c": ["2021-03-01", "2022-07-15", "2020-11-30", "2023-01-09", "2021-12-24"],  # kullanılmıyor
    "d": [3.0, 27.0, 14.0, 41.0, 8.0],                        # sayısal özellik (ör. bina yaşı)
    "e": [0, 1, 1, 0, 1],                                     # etiket
})
print("== Veri kümesi ==")
print(df.to_string(), "\n")

satir = 2   # kurstaki "3. satır" (0'dan sayınca 2)

# Şekil 1 — model hücreleri böyle ALMAZ
print(f"Şekil 1 (yanlış fikir): model 3b ve 3d hücrelerini alır → {df.loc[satir, 'b']}, {df.loc[satir, 'd']}")

# Şekil 2 — ham değerlerden oluşan özellik vektörü (gerçeğe yakın ama gerçekçi değil)
ham = df.loc[satir, ["b", "d"]].to_numpy(dtype=float)
print(f"Şekil 2 (ham özellik vektörü): {ham}")

# Şekil 3 — dönüştürülmüş özellik vektörü (gerçekçi)
b_z = (df["b"] - df["b"].mean()) / df["b"].std(ddof=0)         # normalleştirme (z-puanı)
kovalar = [0, 10, 20, 50]                                     # d için kovalar: 0–10, 10–20, 20–50
d_kova = pd.cut(df["d"], bins=kovalar, right=False, labels=["0–10", "10–20", "20–50"])
d_onehot = pd.get_dummies(d_kova, dtype=float)

vektor = np.r_[b_z[satir], d_onehot.loc[satir].to_numpy()]
print(f"Şekil 3 (dönüştürülmüş özellik vektörü): {np.round(vektor, 3)}")
print(f"  ↳ b = {df.loc[satir, 'b']:.0f} → z-puanı {b_z[satir]:.3f}")
print(f"  ↳ d = {df.loc[satir, 'd']:.0f} → '{d_kova[satir]}' kovası → one-hot {d_onehot.loc[satir].to_numpy()}")

print("\n== Tüm örneklerin özellik vektörleri (modelin gördüğü tablo) ==")
X = pd.concat([b_z.rename("b_normal"), d_onehot.add_prefix("d_")], axis=1)
print(X.round(3).to_string())
print("\nHepsi kayan nokta (float) mu?", all(np.issubdtype(t, np.floating) for t in X.dtypes))
