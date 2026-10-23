"""
Mantıksal Regresyon - Giriş: Doğrusal regresyon neden evet/hayır sorularına uymuyor?
Örnek soru: "Bugün yağmur yağacak mı?" (1 = yağar, 0 = yağmaz), özellik: nem (%)
Çalıştır: python kod/02-mantiksal-regresyon/neden_mantiksal.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)
nem = rng.uniform(20, 100, 60)
gercek_olasilik = 1 / (1 + np.exp(-(nem - 65) / 6))
yagmur = (rng.uniform(size=nem.size) < gercek_olasilik).astype(float)  # 0 veya 1

# 1) Doğrusal regresyon
w_d, b_d = np.polyfit(nem, yagmur, 1)

# 2) Mantıksal regresyon (gradyan inişi, log kaybı) — ayrıntıları sonraki derslerde
x = (nem - nem.mean()) / nem.std()          # özellik ölçekleme (normalization)
w = b = 0.0
for _ in range(5000):
    p = 1 / (1 + np.exp(-(w * x + b)))      # sigmoid
    w -= 0.1 * np.mean((p - yagmur) * x)
    b -= 0.1 * np.mean(p - yagmur)

def mantiksal(n):
    return 1 / (1 + np.exp(-(w * (n - nem.mean()) / nem.std() + b)))

xs = np.linspace(0, 120, 300)
print("Nem → doğrusal tahmin / mantıksal olasılık")
for n in (10, 40, 65, 90, 120):
    print(f"  %{n:>3}: {w_d * n + b_d:>6.2f}  /  {mantiksal(n):.2f}")

img = Path(__file__).resolve().parents[2] / "notlar/02-mantiksal-regresyon/img"
img.mkdir(parents=True, exist_ok=True)
fig, axs = plt.subplots(1, 2, figsize=(12, 4.3), sharey=True)
for ax, baslik, ys, renk in [
        (axs[0], "Doğrusal regresyon: 0'ın altına ve 1'in üstüne taşıyor", w_d * xs + b_d, "#e03131"),
        (axs[1], "Mantıksal regresyon: hep 0 ile 1 arasında (olasılık)", mantiksal(xs), "#2f9e44")]:
    ax.axhspan(-0.6, 0, color="#ffe3e3", alpha=.6); ax.axhspan(1, 1.6, color="#ffe3e3", alpha=.6)
    ax.scatter(nem, yagmur, color="#1c7ed6", alpha=.6, zorder=3, label="Veri (1 = yağmur, 0 = yok)")
    ax.plot(xs, ys, color=renk, lw=2.5, label="Model")
    ax.set(title=baslik, xlabel="Nem (%)", xlim=(0, 120), ylim=(-0.6, 1.6))
    ax.grid(alpha=.3); ax.legend(loc="upper left")
axs[0].set_ylabel("Tahmin")
fig.tight_layout(); fig.savefig(img / "dogrusal-vs-mantiksal.png", dpi=110)
print("Grafik kaydedildi:", img)
