"""
Sınıflandırma - ROC eğrisi ve AUC
1) ROC'u sıfırdan çizer: her eşikte (FPR, TPR)
2) AUC'yi iki yoldan hesaplar: eğri altı alan ve "pozitif > negatif" olasılığı
3) Mükemmel / iyi / zayıf / rastgele / şanstan kötü modeller
4) Bir eğri üzerinde A, B, C eşiklerini seçer
Çalıştır: python kod/03-siniflandirma/roc_auc.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)


def roc(y, puan):
    esikler = np.r_[np.inf, np.sort(np.unique(puan))[::-1], -np.inf]
    P, N = np.sum(y == 1), np.sum(y == 0)
    fpr = np.array([np.sum((puan >= e) & (y == 0)) / N for e in esikler])
    tpr = np.array([np.sum((puan >= e) & (y == 1)) / P for e in esikler])
    return fpr, tpr, esikler


def auc_alan(fpr, tpr):
    return float(np.sum(np.diff(fpr) * (tpr[1:] + tpr[:-1]) / 2))   # yamuk kuralı


def auc_siralama(y, puan):
    """Rastgele bir pozitifin rastgele bir negatiften yüksek puan alma olasılığı (eşitlik = yarım)."""
    poz, neg = puan[y == 1][:, None], puan[y == 0][None, :]
    return float(np.mean((poz > neg) + 0.5 * (poz == neg)))


def model(ayrim, n=500):
    """ayrim: pozitiflerin ortalama puan avantajı (0 = rastgele, <0 = ters)."""
    y = np.r_[np.ones(n), np.zeros(n)]
    puan = np.r_[rng.normal(ayrim, 1, n), rng.normal(0, 1, n)]
    return y, puan


modeller = {
    "Mükemmel": (np.r_[np.ones(500), np.zeros(500)], np.r_[rng.uniform(.6, 1, 500), rng.uniform(0, .4, 500)]),
    "İyi": model(2.1),
    "Zayıf": model(0.55),
    "Rastgele": model(0.0),
    "Şanstan kötü": model(-0.7),
}

print(f"{'Model':<14} {'AUC (alan)':>10} {'AUC (sıralama)':>15}")
egriler = {}
for ad, (y, puan) in modeller.items():
    fpr, tpr, esik = roc(y, puan)
    egriler[ad] = (fpr, tpr, esik, y, puan)
    print(f"{ad:<14} {auc_alan(fpr, tpr):>10.3f} {auc_siralama(y, puan):>15.3f}")

# A, B, C noktaları "İyi" model üzerinde
fpr, tpr, esik, y, puan = egriler["İyi"]
i_b = int(np.argmin(fpr ** 2 + (1 - tpr) ** 2))              # (0,1)'e en yakın
i_a = int(np.argmax(np.where(fpr <= fpr[i_b] / 3, tpr, -1)))  # daha düşük FPR
i_c = int(np.argmax(tpr >= min(0.99, tpr[i_b] + (1 - tpr[i_b]) * .7)))  # daha yüksek TPR
noktalar = {"A": i_a, "B": i_b, "C": i_c}
print("\n'İyi' model üzerinde üç eşik:")
for ad, i in noktalar.items():
    print(f"  {ad}: eşik = {esik[i]:.2f}, FPR = {fpr[i]:.2f}, TPR = {tpr[i]:.2f}")

# --- Grafikler ---
img = Path(__file__).resolve().parents[2] / "notlar/03-siniflandirma/img"
img.mkdir(parents=True, exist_ok=True)
renk = {"Mükemmel": "#2f9e44", "İyi": "#1c7ed6", "Zayıf": "#f59f00", "Rastgele": "#868e96", "Şanstan kötü": "#e03131"}
fig, axs = plt.subplots(1, 2, figsize=(13, 5.5))
ax = axs[0]
for ad, (fpr_, tpr_, *_r) in egriler.items():
    ax.plot(fpr_, tpr_, color=renk[ad], lw=2, label=f"{ad} (AUC = {auc_alan(fpr_, tpr_):.2f})")
ax.plot([0, 1], [0, 1], "k:", lw=1)
ax.set(xlabel="Yanlış pozitif oranı (FPR)", ylabel="Doğru pozitif oranı (TPR)", title="ROC eğrileri", aspect="equal")
ax.grid(alpha=.3); ax.legend(loc="lower right")

ax = axs[1]
ax.fill_between(fpr, tpr, color="#1c7ed6", alpha=.15)
ax.plot(fpr, tpr, color="#1c7ed6", lw=2, label=f"İyi model (AUC = {auc_alan(fpr, tpr):.2f})")
ax.plot([0, 1], [0, 1], "k:", lw=1)
for ad, i in noktalar.items():
    ax.scatter([fpr[i]], [tpr[i]], s=90, zorder=3, color="#e03131")
    ax.annotate(f"{ad}\neşik {esik[i]:.2f}", (fpr[i], tpr[i]), xytext=(10, -28), textcoords="offset points")
ax.scatter([0], [1], marker="*", s=200, color="#2f9e44", zorder=3, label="Mükemmel nokta (0, 1)")
ax.set(xlabel="FPR", ylabel="TPR", title="Aynı modelde üç farklı eşik", aspect="equal")
ax.grid(alpha=.3); ax.legend(loc="lower right")
fig.tight_layout(); fig.savefig(img / "roc-auc.png", dpi=110)
print("Grafik kaydedildi:", img)
