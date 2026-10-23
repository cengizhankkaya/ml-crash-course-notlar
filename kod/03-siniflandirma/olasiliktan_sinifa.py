"""
Sınıflandırma - Giriş: Mantıksal regresyonun olasılığını bir sınıfa çevirmek
Örnek: e-postanın spam olma olasılığı → "spam" / "spam değil"
Çalıştır: python kod/03-siniflandirma/olasiliktan_sinifa.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
# Bir mantıksal regresyon modelinin 10 e-posta için verdiği spam olasılıkları
olasilik = np.round(np.sort(rng.uniform(0, 1, 10)), 2)
ESIK = 0.5


def siniflandir(p, esik=ESIK):
    return np.where(p >= esik, "spam", "spam değil")


print(f"Eşik = {ESIK}")
for p, s in zip(olasilik, siniflandir(olasilik)):
    print(f"  P(spam) = {p:.2f} → {s}")

for esik in (0.3, 0.5, 0.8):
    print(f"Eşik {esik}: {np.sum(olasilik >= esik)} / {olasilik.size} e-posta spam sayılır")

img = Path(__file__).resolve().parents[2] / "notlar/03-siniflandirma/img"
img.mkdir(parents=True, exist_ok=True)
fig, ax = plt.subplots(figsize=(9, 2.8))
renk = np.where(olasilik >= ESIK, "#e03131", "#2f9e44")
ax.scatter(olasilik, np.zeros_like(olasilik), c=renk, s=140, zorder=3)
for i, p in enumerate(olasilik):
    ax.annotate(f"{p:.2f}", (p, 0), xytext=(0, 12 if i % 2 == 0 else -20),
                textcoords="offset points", ha="center", fontsize=9)
ax.axvline(ESIK, color="black", ls="--")
ax.text(ESIK / 2, -0.6, "spam değil", ha="center", color="#2f9e44", fontsize=12)
ax.text((1 + ESIK) / 2, -0.6, "spam", ha="center", color="#e03131", fontsize=12)
ax.text(ESIK + 0.01, 0.75, f"eşik = {ESIK}", ha="left")
ax.set(xlim=(0, 1), ylim=(-1, 1), yticks=[], xlabel="Modelin tahmini: P(spam)",
       title="Olasılıktan sınıfa: eşiğin üstü 'spam', altı 'spam değil'")
ax.grid(alpha=.3, axis="x")
fig.tight_layout(); fig.savefig(img / "olasiliktan-sinifa.png", dpi=110)
print("Grafik kaydedildi:", img)
