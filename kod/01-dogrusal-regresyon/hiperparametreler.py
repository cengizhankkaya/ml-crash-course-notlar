"""
Doğrusal Regresyon - Hiperparametreler
1) Öğrenme oranı: çok küçük / ideal / sınırda / çok büyük
2) Grup boyutu: tam grup, SGD (1 örnek), mini grup (100 örnek)
3) Dönem (epoch): güncelleme sayılarını ders tablosuyla doğrular
Çalıştır: python kod/01-dogrusal-regresyon/hiperparametreler.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

img = Path(__file__).resolve().parents[2] / "notlar/01-dogrusal-regresyon/img"
img.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------
# 1) ÖĞRENME ORANI — kurstaki 7 araba
# ---------------------------------------------------------------
x = np.array([3.50, 3.69, 3.44, 3.43, 4.34, 4.42, 2.37])
y = np.array([18, 15, 18, 16, 15, 14, 24], dtype=float)
L_MIN = np.mean((np.polyval(np.polyfit(x, y, 1), x) - y) ** 2)  # ulaşılabilecek en düşük MSE


def egit(lr, adim, xx=x, yy=y):
    w = b = 0.0
    kayip, ws = [], []
    for _ in range(adim):
        e = w * xx + b - yy
        kayip.append(np.mean(e ** 2)); ws.append(w)
        w -= lr * np.mean(2 * e * xx)
        b -= lr * np.mean(2 * e)
    return np.array(kayip), np.array(ws)


def yakinsama_adimi(lr, sinir=200_000):
    k, _ = egit(lr, sinir) if lr < 0.07 else (np.array([np.inf]), None)
    idx = np.argmax(k < L_MIN * 1.01)
    return int(idx) if k[idx] < L_MIN * 1.01 else None


# Kararlılık sınırı: lr < 2 / (MSE'nin en büyük eğriliği)
H = 2 * np.array([[np.mean(x * x), np.mean(x)], [np.mean(x), 1]])
sinir = 2 / np.linalg.eigvalsh(H).max()
print(f"== Öğrenme oranı (bu veri için kararlılık sınırı ≈ {sinir:.4f}) ==")
for lr in (0.005, 0.01, 0.02, 0.04, 0.05, 0.069, 0.08):
    n = yakinsama_adimi(lr)
    print(f"  lr = {lr:<6} → " + (f"{n:>6} yinelemede yakınsadı" if n else "   ASLA yakınsamaz (ıraksar)"))

print("\nGradyan 2.5, öğrenme oranı 0.01 → parametre değişimi:", 2.5 * 0.01)

fig, axs = plt.subplots(1, 3, figsize=(15, 4.2))
for lr, renk, ad in [(0.005, "#adb5bd", "0.005 — çok küçük"),
                     (0.02, "#74c0fc", "0.02 — küçük"),
                     (0.05, "#2f9e44", "0.05 — iyi")]:
    k, _ = egit(lr, 3000)
    axs[0].plot(k, color=renk, label=ad)
axs[0].axhline(L_MIN, ls="--", color="k", lw=.8, label=f"En düşük kayıp ({L_MIN:.2f})")
axs[0].set(yscale="log", xlabel="Yineleme", ylabel="Kayıp (MSE, log)", title="Uygun / küçük öğrenme oranları")
axs[0].legend(); axs[0].grid(alpha=.3)

k, _ = egit(0.08, 60)
axs[1].plot(k, color="#e03131")
axs[1].set(yscale="log", xlabel="Yineleme", ylabel="Kayıp (MSE, log)",
           title="0.08 — çok büyük: kayıp patlıyor (Şekil 23)")
axs[1].grid(alpha=.3)

for lr, renk in [(0.05, "#2f9e44"), (0.069, "#f08c00")]:
    _, ws = egit(lr, 25)
    axs[2].plot(ws, "o-", ms=3, color=renk, label=f"lr = {lr}")
axs[2].set(xlabel="Yineleme", ylabel="Ağırlık (w)", title="Sınıra yakın oran: ağırlık 'sekiyor' (Şekil 22)")
axs[2].legend(); axs[2].grid(alpha=.3)
fig.tight_layout(); fig.savefig(img / "sekil20-23-ogrenme-orani.png", dpi=110); plt.close(fig)

# ---------------------------------------------------------------
# 2-3) GRUP BOYUTU ve DÖNEM — 1.000 örneklik sentetik veri
# ---------------------------------------------------------------
rng = np.random.default_rng(42)
N = 1000
X = rng.uniform(2, 5, N)
Y = 34 - 4.6 * X + rng.normal(0, 1.5, N)


def mse_tum(w, b):
    return np.mean((w * X + b - Y) ** 2)


def mini_grup_sgd(grup, donem, lr=0.01, tohum=0):
    r = np.random.default_rng(tohum)
    w = b = 0.0
    kayip, guncelleme = [mse_tum(w, b)], 0
    for _ in range(donem):
        sira = r.permutation(N)                 # her dönemde karıştır
        for i in range(0, N, grup):
            j = sira[i:i + grup]
            e = w * X[j] + b - Y[j]
            w -= lr * np.mean(2 * e * X[j])
            b -= lr * np.mean(2 * e)
            guncelleme += 1
            kayip.append(mse_tum(w, b))
    return np.array(kayip), guncelleme, w, b


DONEM = 20
print(f"\n== {N} örnek, {DONEM} dönem ==")
sonuc = {}
for ad, grup in [("Tam grup", N), ("SGD", 1), ("Mini grup SGD", 100)]:
    k, g, w, b = mini_grup_sgd(grup, DONEM)
    sonuc[ad] = (k, grup)
    print(f"  {ad:<14} (grup={grup:>4}): {g:>6} güncelleme, "
          f"dönem başına {N // grup:>4} yineleme, son MSE = {k[-1]:.2f}, y' = {b:.2f} + ({w:.2f})x")

# Gürültü karşılaştırması: üç yöntem de AYNI sayıda güncelleme (3000) yapsın
GUNCELLEME, LR = 3000, 0.03
print(f"\n== Eşit güncelleme ({GUNCELLEME}), lr = {LR} ==")
fig, axs = plt.subplots(1, 3, figsize=(15, 4.2), sharey=True)
for ax, (ad, grup, renk) in zip(axs, [("Tam grup", N, "#1c7ed6"), ("Mini grup SGD", 100, "#2f9e44"), ("SGD", 1, "#e03131")]):
    donem = int(np.ceil(GUNCELLEME * grup / N))
    k, _, w, b = mini_grup_sgd(grup, donem, lr=LR)
    k = k[:GUNCELLEME + 1]
    son = k[-500:]
    print(f"  {ad:<14}: {donem:>4} dönem, son MSE = {k[-1]:.3f}, son 500 adımda dalgalanma (std) = {son.std():.4f}")
    ax.plot(k, color=renk, lw=.7)
    ax.set(yscale="log", xlabel="Güncelleme sayısı", title=f"{ad} — grup = {grup} ({donem} dönem)")
    ax.grid(alpha=.3)
axs[0].set_ylabel("Kayıp (MSE, log)")
fig.tight_layout(); fig.savefig(img / "sekil24-25-grup-boyutu.png", dpi=110); plt.close(fig)
print("\nGrafikler kaydedildi:", img)
