"""
Mantıksal Regresyon - Sigmoid ile olasılık hesaplama
1) Dersteki -7..7 sigmoid tablosunu üretir
2) Log-odds: sigmoid'in tersinin z'yi geri verdiğini doğrular
3) Şekil 2: z = 2x + 5 doğrusunun sigmoid ile S eğrisine dönüşümü
4) Alıştırma: b=1, w=(2,-1,5), x=(0,10,2) → z ve olasılık
Çalıştır: python kod/02-mantiksal-regresyon/sigmoid.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def log_odds(y):
    """Sigmoid'in tersi: z = ln(y / (1 - y))"""
    return np.log(y / (1 - y))


# 1) Tablo
print("== Sigmoid tablosu ==")
for z in range(-7, 8):
    print(f"  {z:>3} → {sigmoid(z):.3f}")

# 2) Log-odds
print("\n== Log-odds (ters dönüşüm) ==")
for z in (-3.0, 0.0, 1.0, 4.0):
    y = sigmoid(z)
    print(f"  z = {z:>4} → y = {y:.4f} → ln(y/(1-y)) = {log_odds(y):.4f}")

# 3) Şekil 2 noktaları
print("\n== z = 2x + 5 → sigmoid ==")
noktalar = np.array([-7.5, -2.5, 0.0])
for x in noktalar:
    z = 2 * x + 5
    print(f"  x = {x:>5} → z = {z:>5} → y' = {sigmoid(z):.5f}")

# 4) Alıştırma
b, w, x = 1, np.array([2, -1, 5]), np.array([0, 10, 2])
z = b + w @ x
print(f"\n== Alıştırma ==\n  z = 1 + 2·0 + (−1)·10 + 5·2 = {z}\n  y' = sigmoid({z}) = {sigmoid(z):.3f}")

# --- Grafikler ---
img = Path(__file__).resolve().parents[2] / "notlar/02-mantiksal-regresyon/img"
img.mkdir(parents=True, exist_ok=True)

zs = np.linspace(-8, 8, 400)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(zs, sigmoid(zs), color="#1c7ed6", lw=2.5)
ax.axhline(0, color="gray", ls="--", lw=.8); ax.axhline(1, color="gray", ls="--", lw=.8)
ax.scatter([0], [0.5], color="#e03131", zorder=3)
ax.annotate("(0, 0.5)", (0, 0.5), xytext=(1, 0.42))
ax.set(title="Sigmoid: f(x) = 1 / (1 + e⁻ˣ)", xlabel="x", ylabel="f(x)", ylim=(-0.1, 1.1))
ax.grid(alpha=.3); fig.tight_layout(); fig.savefig(img / "sekil1-sigmoid.png", dpi=110); plt.close(fig)

xs = np.linspace(-9, 3, 300)
renkler = ["#f59f00", "#2f9e44", "#ae3ec9"]
fig, axs = plt.subplots(1, 2, figsize=(12, 4.3))
axs[0].plot(xs, 2 * xs + 5, color="#1c7ed6", lw=2)
axs[0].set(title="Doğrusal kısım: z = 2x + 5", xlabel="x", ylabel="z (log-odds)")
zz = np.linspace(-13, 11, 300)
axs[1].plot(zz, sigmoid(zz), color="#1c7ed6", lw=2)
axs[1].set(title="Sigmoid sonrası: y' = 1 / (1 + e⁻ᶻ)", xlabel="z", ylabel="y' (olasılık)")
for x, r in zip(noktalar, renkler):
    z = 2 * x + 5
    axs[0].scatter([x], [z], color=r, s=80, zorder=3, label=f"x={x}, z={z:g}")
    axs[1].scatter([z], [sigmoid(z)], color=r, s=80, zorder=3, label=f"z={z:g} → {sigmoid(z):.5f}")
for ax in axs:
    ax.grid(alpha=.3); ax.legend(loc="upper left")
fig.tight_layout(); fig.savefig(img / "sekil2-dogrusal-sigmoid.png", dpi=110); plt.close(fig)
print("\nGrafikler kaydedildi:", img)
