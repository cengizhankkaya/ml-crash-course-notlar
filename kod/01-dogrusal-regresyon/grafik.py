"""
Doğrusal Regresyon - Giriş: kurstaki Şekil 1, 2 ve 4'ü yeniden çizer.
Çalıştır: python kod/01-dogrusal-regresyon/grafik.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x = np.array([3.50, 3.69, 3.44, 3.43, 4.34, 4.42, 2.37])  # ağırlık (bin pound)
y = np.array([18, 15, 18, 16, 15, 14, 24])                 # mil/galon

b, w = 34, -4.6  # kurstaki model: y' = 34 - 4.6 * x

cikti = Path(__file__).resolve().parents[2] / "notlar/01-dogrusal-regresyon/img"
cikti.mkdir(parents=True, exist_ok=True)

def ciz(dosya, dogru=False, tahmin=False):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.scatter(x, y, color="#d6336c", zorder=3, label="Veri")
    if dogru:
        xs = np.linspace(2, 5, 50)
        ax.plot(xs, b + w * xs, color="#1c7ed6", label="y' = 34 − 4.6·x")
    if tahmin:
        ax.scatter([4], [b + w * 4], s=120, facecolors="none",
                   edgecolors="black", linewidths=2, zorder=4, label="(4, 15.6)")
    ax.set_xlabel("Ağırlık (bin pound)")
    ax.set_ylabel("Mil / galon")
    ax.set_xlim(2, 5); ax.set_ylim(10, 26)
    ax.grid(alpha=0.3); ax.legend()
    fig.tight_layout(); fig.savefig(cikti / dosya, dpi=120); plt.close(fig)

ciz("sekil1-veri.png")
ciz("sekil2-model.png", dogru=True)
ciz("sekil4-tahmin.png", dogru=True, tahmin=True)
print("Grafikler kaydedildi:", cikti)
