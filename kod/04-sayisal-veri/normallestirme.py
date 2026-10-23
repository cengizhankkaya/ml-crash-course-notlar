"""
Sayısal veri - Normalleştirme
1) Dört teknik: doğrusal ölçekleme, z-puanı, log ölçekleme, kırpma
2) net_worth'de doğrusal ölçeklemenin sorunu
3) Gradyan inişi: normalleştirme yoksa yavaş yakınsama / NaN tuzağı
4) Alıştırma: veri merkezi sıcaklığı (31–45 kırp, 1000'leri sil)
Çalıştır: python kod/04-sayisal-veri/normallestirme.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)


def dogrusal(x):          # x' = (x − min) / (max − min)
    return (x - x.min()) / (x.max() - x.min())


def z_puani(x):           # x' = (x − μ) / σ
    return (x - x.mean()) / x.std()


def log_olcek(x):         # x' = ln(x)
    return np.log(x)


def kirp(x, alt=None, ust=None):
    return np.clip(x, alt, ust)


# Örnek veriler
yas = rng.uniform(0, 100, 5000)                                 # yassı → doğrusal
normal = rng.normal(200, 30, 5000)                              # çan → z-puanı
puan_sayisi = rng.lognormal(3, 1.4, 5000).round() + 1            # ağır kuyruk → log
oda_kisi = np.r_[np.abs(rng.normal(1.8, 0.7, 4950)), rng.uniform(4, 17, 50)]   # uzun kuyruk → kırp

print("== 1) Dört teknik ==")
print(f"  Doğrusal  (yaş)        : [{yas.min():.0f}, {yas.max():.0f}] → [{dogrusal(yas).min():.1f}, {dogrusal(yas).max():.1f}]")
z = z_puani(normal)
print(f"  Z-puanı   (μ=200, σ=30) : ortalama {normal.mean():.0f}, std {normal.std():.0f} → ortalama {z.mean():.2f}, std {z.std():.2f}")
print(f"  Log       (kitap satışı): ln(100) = {np.log(100):.1f}, ln(1.000.000) = {np.log(1e6):.1f} "
      f"→ 10.000 kat fark sadece {np.log(1e6) / np.log(100):.0f} kata iniyor")
k = kirp(oda_kisi, ust=4.0)
print(f"  Kırpma    (oda/kişi)    : max {oda_kisi.max():.1f} → {k.max():.1f}; tam 4.0 olan değer sayısı: {(k == 4.0).sum()}")
zk = kirp(z_puani(oda_kisi), -3, 3)
print(f"  Z-puanı + kırpma ±3     : z aralığı [{z_puani(oda_kisi).min():.1f}, {z_puani(oda_kisi).max():.1f}] → [{zk.min():.1f}, {zk.max():.1f}]")

print("\n== 2) net_worth: doğrusal ölçekleme neden kötü? ==")
net = np.r_[rng.lognormal(11, 1, 9990), rng.uniform(5e8, 5e10, 10)]   # birkaç milyarder
d = dogrusal(net)
print(f"  Kişilerin %{np.mean(d < 0.001) * 100:.2f}'i 0.001'in altına sıkıştı → model aralarındaki farkı neredeyse göremez")

print("\n== 3) Gradyan inişi: C ∈ [-1, 1], D ∈ [5.000, 1.000.000.000] ==")
n = 500
C = rng.uniform(-1, 1, n)
D = rng.uniform(5_000, 1e9, n)
y = 3 * C + 2 * (D / 1e9) + rng.normal(0, .1, n)


def egit(X, y, lr, adim=500):
    w, b = np.zeros(X.shape[1]), 0.0
    with np.errstate(all="ignore"):
        for i in range(adim):
            e = X @ w + b - y
            w -= lr * 2 * X.T @ e / len(y)
            b -= lr * 2 * e.mean()
            mse = np.mean((X @ w + b - y) ** 2)
            if not np.isfinite(mse):
                return f"{i + 1}. adımda NaN/sonsuz oldu 💥"
    return f"MSE = {mse:.4f}"


ham = np.c_[C, D]
norm = np.c_[z_puani(C), z_puani(D)]
print(f"  Ham özellikler, lr=0.1          : {egit(ham, y, 0.1)}")
print(f"  Ham özellikler, lr=1e-19        : {egit(ham, y, 1e-19)}  (patlamasın diye minicik lr → hiç öğrenemiyor)")
print(f"  Z-puanı ile normalleştirilmiş, lr=0.1: {egit(norm, y, 0.1)} ✅")

print("\n== 4) Alıştırma: veri merkezi sıcaklığı ==")
t = rng.uniform(15, 30, 10_000)
t[rng.choice(10_000, 40, replace=False)] = rng.uniform(31, 45, 40)    # gerçek sıcak günler
t[::1000] = 1000                                                       # sensör hatası
temiz = t[t != 1000]                                                   # 1000'ler hata → sil
temiz = kirp(temiz, ust=30)                                            # 31–45 gerçek → kırp
print(f"  1000 değerli {np.sum(t == 1000)} satır silindi, {np.sum((t > 30) & (t < 100))} sıcak gün 30'da kırpıldı → "
      f"aralık [{temiz.min():.1f}, {temiz.max():.1f}]")

# --- Grafik ---
img = Path(__file__).resolve().parents[2] / "notlar/04-sayisal-veri/img"
img.mkdir(parents=True, exist_ok=True)
paneller = [
    ("Doğrusal ölçekleme: yaş (yassı)", yas, dogrusal(yas), "#1c7ed6"),
    ("Z-puanı: μ=200, σ=30 (çan)", normal, z_puani(normal), "#2f9e44"),
    ("Log ölçekleme: puan sayısı (ağır kuyruk)", puan_sayisi, log_olcek(puan_sayisi), "#ae3ec9"),
    ("Kırpma: oda / kişi, üst sınır 4.0", oda_kisi, kirp(oda_kisi, ust=4.0), "#f59f00"),
]
fig, axs = plt.subplots(2, 4, figsize=(17, 6.5))
for j, (baslik, once, sonra, renk) in enumerate(paneller):
    aralik = (0, np.percentile(once, 99)) if j == 2 else None   # ağır kuyrukta kuyruğun ucu görünmez
    axs[0, j].hist(once, bins=60, range=aralik, color=renk, alpha=.8)
    axs[0, j].set(title=f"{baslik}\nÖNCE")
    axs[1, j].hist(sonra, bins=60, color=renk, alpha=.8)
    axs[1, j].set(title="SONRA")
    for ax in axs[:, j]:
        ax.grid(alpha=.3)
axs[0, 2].set_title(axs[0, 2].get_title() + " (99. yüzdeliğe kadar)")
fig.tight_layout(); fig.savefig(img / "normallestirme.png", dpi=100)
print("\nGrafik kaydedildi:", img)
