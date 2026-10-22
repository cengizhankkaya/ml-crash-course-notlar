"""
Doğrusal Regresyon - Kayıp (Loss)
1) Kurs modeli için L1, MAE, L2, MSE, RMSE hesaplar
2) Kurstaki tek nokta örneğini (x=2.37) doğrular
3) Aykırı değer varken MSE ve MAE ile eğitilen modelleri karşılaştırır
4) Nottaki grafikleri çizer (Şekil 8, 9-10)
Çalıştır: python kod/01-dogrusal-regresyon/kayip.py
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

x = np.array([3.50, 3.69, 3.44, 3.43, 4.34, 4.42, 2.37])  # ağırlık (bin pound)
y = np.array([18, 15, 18, 16, 15, 14, 24])                 # mil/galon
b, w = 34, -4.6

def tahmin(x, b, w):
    return b + w * x

# --- Kayıp fonksiyonları ---
def l1(y, y_):   return np.sum(np.abs(y - y_))
def mae(y, y_):  return np.mean(np.abs(y - y_))
def l2(y, y_):   return np.sum((y - y_) ** 2)
def mse(y, y_):  return np.mean((y - y_) ** 2)
def rmse(y, y_): return np.sqrt(mse(y, y_))

y_ = tahmin(x, b, w)
print("== Kurs modeli y' = 34 - 4.6x, 7 örnek ==")
for ad, f in [("L1", l1), ("MAE", mae), ("L2", l2), ("MSE", mse), ("RMSE", rmse)]:
    print(f"{ad:5}: {f(y, y_):.3f}")

# --- Kurstaki tek nokta örneği ---
t = round(tahmin(2.37, b, w), 1)
print(f"\n== Tek nokta (x=2.37) ==\nTahmin: {t}  Gerçek: 24  L2: {(24 - t) ** 2:.2f}")

# --- Aykırı değer: MSE vs MAE ---
xa = np.append(x, 3.0)   # 3.000 lb...
ya = np.append(y, 40)    # ...ama 40 mpg → aykırı değer

def egit(kayip_f):
    """Basit ızgara araması: kaybı en küçük yapan (b, w) çiftini bulur."""
    en_iyi = (None, None, np.inf)
    for bb in np.linspace(20, 60, 401):
        for ww in np.linspace(-12, 2, 281):
            k = kayip_f(ya, tahmin(xa, bb, ww))
            if k < en_iyi[2]:
                en_iyi = (bb, ww, k)
    return en_iyi[:2]

b_mse, w_mse = egit(mse)
b_mae, w_mae = egit(mae)
print(f"\n== Aykırı değer (3.0, 40) eklenince ==")
print(f"MSE ile eğitilen: y' = {b_mse:.1f} + ({w_mse:.2f})x  → x=3 için {tahmin(3, b_mse, w_mse):.1f}")
print(f"MAE ile eğitilen: y' = {b_mae:.1f} + ({w_mae:.2f})x  → x=3 için {tahmin(3, b_mae, w_mae):.1f}")

# --- Grafikler ---
img = Path(__file__).resolve().parents[2] / "notlar/01-dogrusal-regresyon/img"
img.mkdir(parents=True, exist_ok=True)
xs = np.linspace(2, 5, 50)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(xs, tahmin(xs, b, w), color="#1c7ed6", label="Model")
for xi, yi in zip(x, y):
    ax.plot([xi, xi], [yi, tahmin(xi, b, w)], color="#f08c00", lw=1.5)
ax.scatter(x, y, color="#d6336c", zorder=3, label="Gerçek değer")
ax.plot([], [], color="#f08c00", label="Kayıp (hata)")
ax.set(xlabel="Ağırlık (bin pound)", ylabel="Mil / galon", xlim=(2, 5), ylim=(10, 26))
ax.grid(alpha=.3); ax.legend(); fig.tight_layout()
fig.savefig(img / "sekil8-kayip.png", dpi=120); plt.close(fig)

fig, axs = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
for ax, (ad, bb, ww) in zip(axs, [("MSE", b_mse, w_mse), ("MAE", b_mae, w_mae)]):
    ax.scatter(x, y, color="#d6336c", zorder=3, label="Veri")
    ax.scatter([3.0], [40], color="black", marker="x", s=80, zorder=3, label="Aykırı değer")
    ax.plot(xs, tahmin(xs, bb, ww), color="#e03131", label=f"{ad} ile eğitilen model")
    ax.set(title=f"{ad}: y' = {bb:.1f} + ({ww:.2f})x", xlabel="Ağırlık (bin pound)", xlim=(2, 5), ylim=(10, 42))
    ax.grid(alpha=.3); ax.legend()
axs[0].set_ylabel("Mil / galon")
fig.tight_layout(); fig.savefig(img / "sekil9-10-mse-mae.png", dpi=120); plt.close(fig)
print("\nGrafikler kaydedildi:", img)
