"""
Doğrusal Regresyon - Gradyan İnişi (Gradient Descent)
1) Dersteki 6 yinelemelik tabloyu birebir üretir (öğrenme oranı 0.01)
2) Modeli yakınsayana kadar eğitir ve np.polyfit sonucuyla karşılaştırır
3) Kayıp eğrisini, eğitim anlık görüntülerini ve kayıp yüzeyini çizer
Çalıştır: python kod/01-dogrusal-regresyon/gradyan_inisi.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x = np.array([3.50, 3.69, 3.44, 3.43, 4.34, 4.42, 2.37])  # ağırlık (bin pound)
y = np.array([18, 15, 18, 16, 15, 14, 24], dtype=float)    # mil/galon


def mse(w, b):
    return np.mean((w * x + b - y) ** 2)


def gradyan(w, b):
    """MSE'nin w ve b'ye göre türevleri (eğimleri)."""
    hata = (w * x + b) - y                # y' - y
    dw = np.mean(2 * hata * x)            # ∂MSE/∂w
    db = np.mean(2 * hata)                # ∂MSE/∂b
    return dw, db


def gradyan_inisi(ogrenme_orani, yineleme, w=0.0, b=0.0):
    gecmis = []                           # (w, b, kayıp) her adımda
    for _ in range(yineleme):
        gecmis.append((w, b, mse(w, b)))  # 1) kaybı hesapla
        dw, db = gradyan(w, b)            # 2) eğimi (yönü) bul
        w -= ogrenme_orani * dw           # 3) negatif eğim yönünde küçük adım at
        b -= ogrenme_orani * db
    return np.array(gecmis)               # 4) tekrarla


# --- 1) Dersteki tablo ---
print("== Ders tablosu (öğrenme oranı = 0.01) ==")
print(f"{'Yineleme':>8} {'Ağırlık':>8} {'Yanlılık':>9} {'Kayıp (MSE)':>12}")
for i, (w, b, k) in enumerate(gradyan_inisi(0.01, 6), start=1):
    print(f"{i:>8} {w:>8.2f} {b:>9.2f} {k:>12.2f}")

# --- 2) Yakınsayana kadar eğit ---
ORAN, ADIM = 0.05, 3000
g = gradyan_inisi(ORAN, ADIM)
w_son, b_son, k_son = g[-1]
w_ref, b_ref = np.polyfit(x, y, 1)
print(f"\n== {ADIM} yineleme sonra (öğrenme oranı = {ORAN}) ==")
print(f"Gradyan inişi : w = {w_son:.3f}, b = {b_son:.3f}, MSE = {k_son:.3f}")
print(f"np.polyfit    : w = {w_ref:.3f}, b = {b_ref:.3f}, MSE = {mse(w_ref, b_ref):.3f}")
for n in (1, 10, 100, 400, 1000, 2000):
    print(f"  {n:>5}. yineleme kaybı: {g[n - 1, 2]:.2f}")

# --- 3) Grafikler ---
img = Path(__file__).resolve().parents[2] / "notlar/01-dogrusal-regresyon/img"
img.mkdir(parents=True, exist_ok=True)
xs = np.linspace(2, 5, 50)

# Kayıp eğrisi + 3 anlık görüntü (Şekil 12-15)
anlar = [2, 400, 1500]
fig, axs = plt.subplots(len(anlar), 2, figsize=(10, 10))
for satir, n in zip(axs, anlar):
    w, b, k = g[n - 1]
    satir[0].plot(np.arange(1, ADIM + 1), g[:, 2], color="#1c7ed6")
    satir[0].scatter([n], [k], color="#e03131", zorder=3, s=50)
    satir[0].set(yscale="log", xlabel="Yineleme", ylabel="Kayıp (MSE, log)",
                 title=f"{n}. yineleme — kayıp = {k:.2f}")
    satir[0].grid(alpha=.3)
    for xi, yi in zip(x, y):
        satir[1].plot([xi, xi], [yi, w * xi + b], color="#1c7ed6", lw=1.2)
    satir[1].scatter(x, y, color="#d6336c", zorder=3)
    satir[1].plot(xs, w * xs + b, color="#e03131")
    satir[1].set(xlim=(2, 5), ylim=(0, 30), xlabel="Ağırlık (bin pound)",
                 ylabel="Mil / galon", title=f"Model: y' = {b:.2f} + ({w:.2f})x")
    satir[1].grid(alpha=.3)
fig.tight_layout(); fig.savefig(img / "sekil12-15-kayip-egrisi.png", dpi=110); plt.close(fig)

# Kayıp yüzeyi (Şekil 16-18): kontur + gradyan inişinin izlediği yol
W, B = np.meshgrid(np.linspace(-8, 7, 300), np.linspace(-2, 45, 300))
K = np.mean((W[..., None] * x + B[..., None] - y) ** 2, axis=-1)
fig = plt.figure(figsize=(12, 5))
ax3 = fig.add_subplot(1, 2, 1, projection="3d")
ax3.plot_surface(W, B, K, cmap="viridis", alpha=.8, linewidth=0)
iz = g[::25]
ax3.plot(iz[:, 0], iz[:, 1], iz[:, 2], "k.-", ms=3)
ax3.set(xlabel="Ağırlık (w)", ylabel="Yanlılık (b)", zlabel="Kayıp", title="Kayıp yüzeyi (dışbükey)")
ax3.view_init(elev=30, azim=-60)
ax = fig.add_subplot(1, 2, 2)
cs = ax.contour(W, B, K, levels=np.logspace(0, 3, 15), cmap="viridis")
ax.plot(g[:, 0], g[:, 1], "k.-", ms=2, lw=.8, label="Gradyan inişi yolu")
ax.scatter([w_ref], [b_ref], color="#e03131", marker="*", s=200, zorder=3,
           label=f"En düşük kayıp ({w_ref:.2f}, {b_ref:.2f})")
ax.set(xlabel="Ağırlık (w)", ylabel="Yanlılık (b)", title="Yukarıdan bakış (kontur)")
ax.legend(loc="upper right"); ax.grid(alpha=.3)
fig.tight_layout(); fig.savefig(img / "sekil16-18-kayip-yuzeyi.png", dpi=110); plt.close(fig)
print("\nGrafikler kaydedildi:", img)
