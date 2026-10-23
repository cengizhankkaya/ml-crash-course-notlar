"""
Sınıflandırma - Doğruluk, geri çağırma (recall), FPR, kesinlik (precision), F1
1) Metrik fonksiyonları (NaN durumu dahil)
2) Doğruluk tuzağı: %1 pozitifli veride "hep negatif" diyen model
3) FPR'nin az negatifle oynaklığı
4) Eşik ↑ → kesinlik ↑, geri çağırma ↓ (grafik)
5) Alıştırmaların çözümü
Çalıştır: python kod/03-siniflandirma/metrikler.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def bol(a, b):
    return a / b if b else float("nan")       # 0'a bölme → NaN


def metrikler(TP, FP, FN, TN):
    return {
        "doğruluk": bol(TP + TN, TP + TN + FP + FN),
        "geri çağırma (TPR)": bol(TP, TP + FN),
        "FPR": bol(FP, FP + TN),
        "kesinlik": bol(TP, TP + FP),
    }


def f1(TP, FP, FN):
    k, g = bol(TP, TP + FP), bol(TP, TP + FN)
    return bol(2 * k * g, k + g)


def yazdir(baslik, m):
    print(f"\n== {baslik} ==")
    for ad, v in m.items():
        print(f"  {ad:<20}: {v:.3f}")


# 2) Doğruluk tuzağı
yazdir("1.000 e-posta, 10 spam; model HER ZAMAN 'spam değil' diyor",
       metrikler(TP=0, FP=0, FN=10, TN=990))

# 3) FPR oynaklığı
print("\n== Yalnızca 4 gerçek negatif varken FPR ==")
for fp in range(3):
    print(f"  {fp} yanlış alarm → FPR = {bol(fp, 4):.0%}")

# 5) Alıştırmalar
print("\n== Alıştırmalar ==")
print(f"  1) TP=5, TN=6, FP=3, FN=2 → geri çağırma = 5/(5+2) = {bol(5, 7):.3f}")
print(f"  2) TP=3, TN=4, FP=2, FN=1 → kesinlik    = 3/(3+2) = {bol(3, 5):.3f}")
print(f"     (aynı model için F1 = {f1(3, 2, 1):.3f})")

# 4) Eşik taraması
rng = np.random.default_rng(1)
poz = np.clip(rng.normal(0.6, 0.18, 100), 0.001, 0.999)
neg = np.clip(rng.normal(0.4, 0.18, 300), 0.001, 0.999)
y = np.r_[np.ones(100), np.zeros(300)]
puan = np.r_[poz, neg]
esikler = np.linspace(0.02, 0.98, 97)
sonuc = {k: [] for k in ("doğruluk", "geri çağırma (TPR)", "FPR", "kesinlik", "F1")}
for e in esikler:
    t = puan > e
    TP, FP = np.sum(t & (y == 1)), np.sum(t & (y == 0))
    FN, TN = np.sum(~t & (y == 1)), np.sum(~t & (y == 0))
    for k, v in metrikler(TP, FP, FN, TN).items():
        sonuc[k].append(v)
    sonuc["F1"].append(f1(TP, FP, FN))
en_iyi = esikler[np.nanargmax(sonuc["F1"])]
print(f"\n== 100 pozitif / 300 negatif: F1'i en yüksek yapan eşik ≈ {en_iyi:.2f} ==")
for e in (0.3, 0.5, 0.7):
    i = int(np.argmin(np.abs(esikler - e)))
    print(f"  eşik {e}: " + ", ".join(f"{k} = {sonuc[k][i]:.2f}" for k in sonuc))

img = Path(__file__).resolve().parents[2] / "notlar/03-siniflandirma/img"
img.mkdir(parents=True, exist_ok=True)
renk = {"doğruluk": "#868e96", "geri çağırma (TPR)": "#2f9e44", "FPR": "#e03131", "kesinlik": "#1c7ed6", "F1": "#ae3ec9"}
fig, ax = plt.subplots(figsize=(9, 4.5))
for k, v in sonuc.items():
    ax.plot(esikler, v, lw=2.5 if k in ("geri çağırma (TPR)", "kesinlik") else 1.5,
            ls="--" if k == "F1" else "-", color=renk[k], label=k)
ax.axvline(en_iyi, color="#ae3ec9", ls=":", lw=1)
ax.set(xlabel="Eşik", ylabel="Değer", ylim=(0, 1.02),
       title="Eşik ↑ → kesinlik ↑, geri çağırma ↓ (100 pozitif / 300 negatif)")
ax.grid(alpha=.3); ax.legend(loc="center left")
fig.tight_layout(); fig.savefig(img / "metrikler-esik.png", dpi=110)
print("Grafik kaydedildi:", img)
