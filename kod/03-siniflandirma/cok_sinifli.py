"""
Sınıflandırma - Çok sınıflı sınıflandırma (A, B, C)
İkili sınıflandırıcılarla iki yaklaşım:
  1) Biri diğerlerine karşı (one-vs-rest): her sınıf için "bu sınıf mı, değil mi?" → en yüksek olasılık kazanır
  2) Aşamalı (dersteki örnek): önce "A+B mi, C mi?", sonra A+B dediklerine "A mı, B mi?"
Çalıştır: python kod/03-siniflandirma/cok_sinifli.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(5)
merkez = {"A": (-2, 0), "B": (2, 0), "C": (0, 3)}
SINIFLAR = list(merkez)
X = np.vstack([rng.normal(m, 1.0, (200, 2)) for m in merkez.values()])
y = np.repeat(np.arange(3), 200)        # 0 = A, 1 = B, 2 = C


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def ikili_egit(X, t, adim=2000, lr=0.5):
    """Basit mantıksal regresyon (gradyan inişi, log kaybı). t: 0/1 etiket."""
    w, b = np.zeros(X.shape[1]), 0.0
    for _ in range(adim):
        p = sigmoid(X @ w + b)
        w -= lr * X.T @ (p - t) / len(t)
        b -= lr * np.mean(p - t)
    return w, b


# 1) Biri diğerlerine karşı
ovr = [ikili_egit(X, (y == k).astype(float)) for k in range(3)]
def ovr_tahmin(X):
    olas = np.column_stack([sigmoid(X @ w + b) for w, b in ovr])
    return olas.argmax(axis=1)

# 2) Aşamalı: (A+B) vs C, sonra A vs B
w1, b1 = ikili_egit(X, (y == 2).astype(float))                  # C mi?
ab = y != 2
w2, b2 = ikili_egit(X[ab], (y[ab] == 1).astype(float))          # B mi? (A+B içinde)
def asamali_tahmin(X):
    c_mi = sigmoid(X @ w1 + b1) > 0.5
    b_mi = sigmoid(X @ w2 + b2) > 0.5
    return np.where(c_mi, 2, np.where(b_mi, 1, 0))


def karisiklik(y, t):
    m = np.zeros((3, 3), int)
    for g, p in zip(y, t):
        m[p, g] += 1          # satır = tahmin, sütun = gerçek (kurstaki düzen)
    return m


X_test = np.vstack([rng.normal(m, 1.0, (200, 2)) for m in merkez.values()])
y_test = np.repeat(np.arange(3), 200)
for ad, f in [("Biri diğerlerine karşı", ovr_tahmin), ("Aşamalı (A+B / C → A / B)", asamali_tahmin)]:
    t = f(X_test)
    print(f"\n== {ad}: doğruluk = {np.mean(t == y_test):.3f} ==")
    m = karisiklik(y_test, t)
    print("            gerçek A  gerçek B  gerçek C")
    for i, s in enumerate(SINIFLAR):
        print(f"  tahmin {s}  " + "  ".join(f"{v:>8}" for v in m[i]))

# --- Grafik: karar bölgeleri ---
img = Path(__file__).resolve().parents[2] / "notlar/03-siniflandirma/img"
img.mkdir(parents=True, exist_ok=True)
xx, yy = np.meshgrid(np.linspace(-6, 6, 300), np.linspace(-4, 7, 300))
izgara = np.c_[xx.ravel(), yy.ravel()]
renk = ["#1c7ed6", "#f59f00", "#2f9e44"]
from matplotlib.colors import ListedColormap
fig, axs = plt.subplots(1, 2, figsize=(12, 5))
for ax, (ad, f) in zip(axs, [("Biri diğerlerine karşı", ovr_tahmin), ("Aşamalı: (A+B vs C) → (A vs B)", asamali_tahmin)]):
    ax.contourf(xx, yy, f(izgara).reshape(xx.shape), levels=[-.5, .5, 1.5, 2.5], cmap=ListedColormap(renk), alpha=.2)
    for k in range(3):
        ax.scatter(*X_test[y_test == k].T, s=10, color=renk[k], label=SINIFLAR[k])
    ax.set(title=f"{ad}\ndoğruluk = {np.mean(f(X_test) == y_test):.3f}", xlabel="Özellik 1", ylabel="Özellik 2")
    ax.legend(loc="upper left"); ax.grid(alpha=.3)
fig.tight_layout(); fig.savefig(img / "cok-sinifli.png", dpi=110)
print("\nGrafik kaydedildi:", img)
