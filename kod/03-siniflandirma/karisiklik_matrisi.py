"""
Sınıflandırma - Eşikler ve karışıklık matrisi
1) Karışıklık matrisini (TP, FP, FN, TN) hesaplar
2) Widget'taki gibi üç oyuncak veri kümesi: ayrık, ayrışmamış, dengesiz
3) Eşik yükseldikçe TP/FP/FN/TN nasıl değişir? (test sorularının cevabı)
Çalıştır: python kod/03-siniflandirma/karisiklik_matrisi.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def karisiklik_matrisi(y, puan, esik):
    """Keras gibi: puan > eşik ise pozitif (eşitlikte negatif)."""
    tahmin = puan > esik
    gercek = y == 1
    return {"TP": int(np.sum(tahmin & gercek)), "FP": int(np.sum(tahmin & ~gercek)),
            "FN": int(np.sum(~tahmin & gercek)), "TN": int(np.sum(~tahmin & ~gercek))}


def yazdir(m):
    print(f"                    Gerçek pozitif   Gerçek negatif")
    print(f"  Tahmin pozitif    TP = {m['TP']:>3}         FP = {m['FP']:>3}    | toplam {m['TP'] + m['FP']}")
    print(f"  Tahmin negatif    FN = {m['FN']:>3}         TN = {m['TN']:>3}    | toplam {m['FN'] + m['TN']}")
    print(f"  Sütun toplamı      {m['TP'] + m['FN']:>3}               {m['FP'] + m['TN']:>3}")


rng = np.random.default_rng(1)


def veri(n_poz, n_neg, poz_ort, neg_ort, yayilim):
    poz = np.clip(rng.normal(poz_ort, yayilim, n_poz), 0.01, 0.99)
    neg = np.clip(rng.normal(neg_ort, yayilim, n_neg), 0.01, 0.99)
    return np.r_[np.ones(n_poz), np.zeros(n_neg)], np.r_[poz, neg]


kumeler = {
    "Ayrık": veri(50, 50, 0.75, 0.25, 0.12),
    "Ayrışmamış": veri(50, 50, 0.55, 0.45, 0.2),
    "Dengesiz": veri(5, 95, 0.7, 0.3, 0.15),
}

# 1) Örnek matris
y, puan = kumeler["Ayrık"]
for esik in (0.5, 0.95):
    print(f"\n== Ayrık veri, eşik = {esik} ==")
    yazdir(karisiklik_matrisi(y, puan, esik))

y, puan = kumeler["Dengesiz"]
print(f"\n== Dengesiz veri: {int(y.sum())} pozitif / {int((1 - y).sum())} negatif, eşik = 0.5 ==")
yazdir(karisiklik_matrisi(y, puan, 0.5))

# 2) Eşik yükselince ne olur?
print("\n== Eşik 0.3 → 0.7 (ayrışmamış veri) ==")
y, puan = kumeler["Ayrışmamış"]
a, b = karisiklik_matrisi(y, puan, 0.3), karisiklik_matrisi(y, puan, 0.7)
for k in ("TP", "FP", "FN", "TN"):
    print(f"  {k}: {a[k]:>3} → {b[k]:>3}  ({'artar' if b[k] > a[k] else 'azalır'})")

# --- Grafik ---
img = Path(__file__).resolve().parents[2] / "notlar/03-siniflandirma/img"
img.mkdir(parents=True, exist_ok=True)
esikler = np.linspace(0, 1, 101)
renk = {"TP": "#2f9e44", "FP": "#e03131", "FN": "#f59f00", "TN": "#1c7ed6"}
fig, axs = plt.subplots(2, 3, figsize=(15, 7.5))
for j, (ad, (y, puan)) in enumerate(kumeler.items()):
    ax = axs[0, j]
    bins = np.linspace(0, 1, 21)
    ax.hist(puan[y == 0], bins=bins, color="#1c7ed6", alpha=.6, label="Gerçek negatif")
    ax.hist(puan[y == 1], bins=bins, color="#2f9e44", alpha=.6, label="Gerçek pozitif")
    ax.axvline(0.5, color="k", ls="--", lw=1, label="eşik 0.5")
    ax.set(title=f"{ad}: modelin puanları", xlabel="Puan (P(pozitif))", ylabel="Örnek sayısı")
    ax.legend(fontsize=8); ax.grid(alpha=.3)
    ax = axs[1, j]
    sayilar = {k: [karisiklik_matrisi(y, puan, e)[k] for e in esikler] for k in renk}
    for k, v in sayilar.items():
        ax.plot(esikler, v, color=renk[k], lw=2, label=k)
    ax.set(title=f"{ad}: eşiğe göre TP / FP / FN / TN", xlabel="Eşik", ylabel="Sayı")
    ax.legend(fontsize=8); ax.grid(alpha=.3)
fig.tight_layout(); fig.savefig(img / "esik-karisiklik.png", dpi=105); plt.close(fig)
print("\nGrafik kaydedildi:", img)
