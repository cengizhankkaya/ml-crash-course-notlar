"""
Sınıflandırma - Tahmin yanlılığı (prediction bias)
tahmin yanlılığı = ortalama(tahmin) − ortalama(gerçek etiket)
Senaryolar:
  1) Normal eğitim                      → yanlılık ≈ 0
  2) Çok güçlü L2 düzenlileştirme        → yanlılık büyür
  3) Önyargılı örnekleme (eğitimde %50 spam, gerçekte %5)
  4) Yetersiz özellik (bilgi taşımayan özellik)
Çalıştır: python kod/03-siniflandirma/tahmin_yanliligi.py
"""
import numpy as np

rng = np.random.default_rng(42)


def veri(n, spam_orani):
    y = (rng.uniform(size=n) < spam_orani).astype(float)
    x = np.c_[rng.normal(2.0 * y, 1.0), rng.normal(1.5 * y, 1.0)]   # 2 bilgilendirici özellik
    return x, y


def egit(x, y, lam=0.0, adim=3000, lr=0.5):
    w, b = np.zeros(x.shape[1]), 0.0
    for _ in range(adim):
        p = 1 / (1 + np.exp(-(x @ w + b)))
        w -= lr * (x.T @ (p - y) / len(y) + 2 * lam * w)
        b -= lr * (np.mean(p - y) + 2 * lam * b)          # güçlü düzenlileştirme yanlılığı da cezalandırırsa
    return w, b


def auc(w, b, x, y):
    """Rastgele bir pozitife rastgele bir negatiften yüksek puan verme olasılığı."""
    puan = x @ w + b
    poz, neg = puan[y == 1], puan[y == 0]
    sira = np.argsort(np.argsort(np.r_[poz, neg])) + 1          # sıralama (rank) ile hızlı AUC
    return (sira[:len(poz)].sum() - len(poz) * (len(poz) + 1) / 2) / (len(poz) * len(neg))


def yanlilik(w, b, x, y):
    p = 1 / (1 + np.exp(-(x @ w + b)))
    return p.mean(), y.mean(), p.mean() - y.mean()


x, y = veri(20000, 0.05)            # gerçek dünya: %5 spam
x_test, y_test = veri(20000, 0.05)

senaryolar = {
    "1) Normal eğitim": (egit(x, y), x_test, y_test),
    "2) Çok güçlü düzenlileştirme (λ=1)": (egit(x, y, lam=1.0), x_test, y_test),
}
x50, y50 = veri(20000, 0.50)          # önyargılı örnekleme: eğitimde yarı yarıya spam
senaryolar["3) Önyargılı örnekleme (eğitim %50 spam)"] = (egit(x50, y50), x_test, y_test)
x_bos = rng.normal(size=(20000, 2))   # etiketle ilgisiz özellikler
senaryolar["4) Yetersiz özellik (bilgisiz)"] = (egit(x_bos, y), rng.normal(size=(20000, 2)), y_test)

print(f"{'Senaryo':<42} {'ort. tahmin':>11} {'ort. etiket':>11} {'yanlılık':>9} {'AUC':>6}")
for ad, ((w, b), xt, yt) in senaryolar.items():
    p_ort, y_ort, fark = yanlilik(w, b, xt, yt)
    print(f"{ad:<42} {p_ort:>11.3f} {y_ort:>11.3f} {fark:>+9.3f} {auc(w, b, xt, yt):>6.3f}")
print("\nNot: 4. senaryoda yanlılık ≈ 0 ama AUC ≈ 0.5 → model işe yaramıyor, sadece ortalamayı tutturuyor.")
