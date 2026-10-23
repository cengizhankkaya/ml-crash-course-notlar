"""
Mantıksal Regresyon - Log kaybı ve düzenlileştirme
1) Dersteki hassasiyet tablosu (sigmoid 5..10)
2) Log kaybı örnekleri ve kare kaybıyla karşılaştırma
3) Düzenlileştirme olmadan ağırlığın sonsuza gitmesi; L2 ve erken durdurma
Çalıştır: python kod/02-mantiksal-regresyon/log_kaybi.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def log_kaybi(y, p):
    """Ortalama log kaybı: (1/N) Σ −y·log(p) − (1−y)·log(1−p)"""
    p = np.clip(p, 1e-15, 1 - 1e-15)
    return np.mean(-y * np.log(p) - (1 - y) * np.log(1 - p))


# 1) Hassasiyet tablosu
print("== Sigmoid 5..10: 1'e ne kadar yakın? ==")
for z in range(5, 11):
    p = sigmoid(z)
    print(f"  {z:>2} → {p:.7f}   (1 − p = {1 - p:.1e})")

# 2) Log kaybı vs kare kaybı (tek örnek, gerçek etiket y = 1)
print("\n== Gerçek etiket 1, tahmin p ==")
print(f"  {'p':>6} {'kare kaybı':>11} {'log kaybı':>10}")
for p in (0.99, 0.9, 0.7, 0.5, 0.3, 0.1, 0.01):
    print(f"  {p:>6} {(1 - p) ** 2:>11.3f} {log_kaybi(np.array([1.]), np.array([p])):>10.3f}")

# 3) Düzenlileştirme deneyi: tamamen ayrılabilir veri
x = np.array([-3, -2.5, -2, -1.5, -1, 1, 1.5, 2, 2.5, 3.0])
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1.0])


def egit(adim, lr=0.5, lam=0.0):
    w = b = 0.0
    ws, kayiplar = [], []
    for _ in range(adim):
        p = sigmoid(w * x + b)
        kayiplar.append(log_kaybi(y, p) + lam * w ** 2)
        ws.append(w)
        w -= lr * (np.mean((p - y) * x) + 2 * lam * w)   # L2 cezası: λ·w²
        b -= lr * np.mean(p - y)
    return np.array(ws), np.array(kayiplar)


ADIM = 20000
w_yok, k_yok = egit(ADIM)
w_l2, k_l2 = egit(ADIM, lam=0.01)
ERKEN = 50
print(f"\n== Ayrılabilir veri, {ADIM} adım ==")
for n in (10, 100, 1000, 10000, ADIM):
    print(f"  {n:>6}. adım | düzenlileştirme yok: w = {w_yok[n - 1]:6.2f}, kayıp = {k_yok[n - 1]:.5f}"
          f" | L2 (λ=0.01): w = {w_l2[n - 1]:5.2f}")
print(f"  Erken durdurma ({ERKEN}. adımda dur): w = {w_yok[ERKEN - 1]:.2f}, kayıp = {k_yok[ERKEN - 1]:.4f}")

# --- Grafikler ---
img = Path(__file__).resolve().parents[2] / "notlar/02-mantiksal-regresyon/img"
img.mkdir(parents=True, exist_ok=True)

ps = np.linspace(0.001, 0.999, 400)
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(ps, -np.log(ps), color="#e03131", lw=2, label="Log kaybı: −log(p)")
ax.plot(ps, (1 - ps) ** 2, color="#1c7ed6", lw=2, label="Kare kaybı: (1 − p)²")
ax.set(title="Gerçek etiket = 1 iken tahmine göre kayıp", xlabel="Modelin tahmini p", ylabel="Kayıp", ylim=(0, 5))
ax.grid(alpha=.3); ax.legend(); fig.tight_layout()
fig.savefig(img / "log-kaybi-vs-kare.png", dpi=110); plt.close(fig)

fig, axs = plt.subplots(1, 2, figsize=(12, 4.2))
axs[0].plot(w_yok, color="#e03131", label="Düzenlileştirme yok")
axs[0].plot(w_l2, color="#2f9e44", label="L2 (λ = 0.01)")
axs[0].axvline(ERKEN, color="#f59f00", ls="--", label=f"Erken durdurma ({ERKEN}. adım)")
axs[0].set(xscale="log", xlabel="Adım (log)", ylabel="Ağırlık w", title="Ağırlık büyümeye devam ediyor mu?")
xs = np.linspace(-4, 4, 300)
axs[1].scatter(x, y, color="#1c7ed6", zorder=3, label="Veri")
for ad, w_, renk in [("Yok", w_yok, "#e03131"), ("L2", w_l2, "#2f9e44"), ("Erken durdurma", w_yok[:ERKEN], "#f59f00")]:
    axs[1].plot(xs, sigmoid(w_[-1] * xs), color=renk, label=f"{ad} (w = {w_[-1]:.1f})")
axs[1].set(xlabel="x", ylabel="Olasılık", title="Ortaya çıkan modeller")
for ax in axs:
    ax.grid(alpha=.3); ax.legend()
fig.tight_layout(); fig.savefig(img / "duzenlilestirme.png", dpi=110); plt.close(fig)
print("\nGrafikler kaydedildi:", img)
