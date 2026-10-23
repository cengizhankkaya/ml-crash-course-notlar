"""
Sayısal veri - İlk adımlar: görselleştir, istatistik al, aykırı değerleri bul
Sentetik "ev" verisi, üç tür sorunla:
  oda_sayisi : HATA — birkaç kayıtta fazladan sıfır girilmiş (3 → 30)
  fiyat      : GEÇERLİ ama uç değerler (birkaç lüks konut)
  yas        : İstatistiklerde GİZLENEN anormallik — eksik değerler 0 olarak kodlanmış
Çalıştır: python kod/04-sayisal-veri/ilk_adimlar.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(11)
N = 1000
oda = rng.integers(1, 6, N).astype(float)
oda[rng.choice(N, 6, replace=False)] *= 10                    # yazım hatası: fazladan sıfır
fiyat = rng.lognormal(np.log(250), 0.35, N)                   # bin $
fiyat[rng.choice(N, 8, replace=False)] = rng.uniform(1500, 3000, 8)   # gerçek lüks evler
yas = rng.normal(30, 9, N).clip(1)
yas[rng.choice(N, 120, replace=False)] = 0                    # "bilinmiyor" → 0 diye kaydedilmiş
df = pd.DataFrame({"oda_sayisi": oda, "fiyat": fiyat, "yas": yas})

# 1) Temel istatistikler
pd.options.display.float_format = "{:.1f}".format
print("== describe() ==")
print(df.describe().to_string())
print("\nmedyan:", df.median().round(1).to_dict())

# 2) Yüzdelik farkı kuralı: (25. − 0.) ile (100. − 75.) çok farklıysa → aykırı değer şüphesi
print("\n== Yüzdelik farkı kontrolü ==")
for s in df:
    q = df[s].quantile([0, .25, .5, .75, 1])
    alt, ust = q[.25] - q[0], q[1] - q[.75]
    oran = max(alt, ust) / max(min(alt, ust), 1e-9)
    print(f"  {s:<11}: 0→25: {alt:7.1f} | 75→100: {ust:7.1f} | oran {oran:5.1f}x "
          f"{'⚠️ aykırı değer şüphesi' if oran > 3 else '✓'}")

print("\n== 'yas' istatistiklerde normal görünüyor ama... ==")
print(f"  Tam olarak 0 olan kayıt: {(df.yas == 0).sum()} (%{(df.yas == 0).mean() * 100:.0f}) → eksik veri 0 diye kodlanmış!")

# 3) Ne yapmalı?
temiz = df[df.oda_sayisi <= 10].copy()                        # hata → sil
print(f"\nHatalı oda sayısı silindi: {len(df) - len(temiz)} satır")
ust_sinir = temiz.fiyat.quantile(0.99)
temiz["fiyat_kirpilmis"] = temiz.fiyat.clip(upper=ust_sinir)  # uç değer → kırp (istersen)
print(f"Fiyat 99. yüzdelikte ({ust_sinir:.0f}) kırpıldı: max {temiz.fiyat.max():.0f} → {temiz.fiyat_kirpilmis.max():.0f}")
temiz.loc[temiz.yas == 0, "yas"] = np.nan                     # sahte 0 → eksik
print(f"Sahte 0 yaşlar NaN yapıldı: {temiz.yas.isna().sum()} eksik değer; gerçek ortalama yaş "
      f"{df.yas.mean():.1f} değil {temiz.yas.mean():.1f}")

# --- Grafik ---
img = Path(__file__).resolve().parents[2] / "notlar/04-sayisal-veri/img"
img.mkdir(parents=True, exist_ok=True)
fig, axs = plt.subplots(1, 3, figsize=(15, 4))
axs[0].hist(df.oda_sayisi, bins=60, color="#e03131")
axs[0].set(title="oda_sayisi: 20–50 arası hatalar", xlabel="Oda sayısı", ylabel="Kayıt sayısı", yscale="log")
axs[1].hist(df.fiyat, bins=60, color="#1c7ed6")
axs[1].set(title="fiyat: sağda geçerli uç değerler", xlabel="Fiyat (bin $)", yscale="log")
axs[2].hist(df.yas, bins=60, color="#2f9e44")
axs[2].set(title="yas: 0'da gizli bir sütun!", xlabel="Bina yaşı")
for ax in axs:
    ax.grid(alpha=.3)
fig.tight_layout(); fig.savefig(img / "ilk-adimlar-histogram.png", dpi=110)
print("\nGrafik kaydedildi:", img)
