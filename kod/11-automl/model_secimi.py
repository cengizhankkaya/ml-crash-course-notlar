"""Ek pekiştirme: doğrulama kümesiyle küçük bir aday araması.

Tam bir AutoML sistemi değildir. Yapay veri, NumPy ve sabit tohum kullanır.
Test kümesi aday seçildikten sonra yalnız son değerlendirmeye girer.
Çalıştır: python kod/11-automl/model_secimi.py
"""
import numpy as np


def mse(gercek, tahmin):
    return float(np.mean((gercek - tahmin) ** 2))


def main():
    rng = np.random.default_rng(42)
    x = rng.uniform(-1.0, 1.0, 150)
    y = 1.0 + 2.0 * x - 1.5 * x**2 + rng.normal(0, 0.3, len(x))
    sira = rng.permutation(len(x))
    egitim, dogrulama, test = sira[:90], sira[90:120], sira[120:]

    adaylar = []
    print("Derece | eğitim MSE | doğrulama MSE")
    for derece in (1, 2, 3, 6, 12):
        tasarim = np.polynomial.polynomial.polyvander(x[egitim], derece)
        agirliklar, *_ = np.linalg.lstsq(tasarim, y[egitim], rcond=None)
        egitim_hata = mse(y[egitim], tasarim @ agirliklar)
        dogrulama_tahmin = np.polynomial.polynomial.polyval(x[dogrulama], agirliklar)
        dogrulama_hata = mse(y[dogrulama], dogrulama_tahmin)
        adaylar.append((dogrulama_hata, derece, agirliklar))
        print(f"{derece:6d} | {egitim_hata:10.4f} | {dogrulama_hata:13.4f}")

    _, derece, agirliklar = min(adaylar, key=lambda aday: aday[0])
    test_tahmin = np.polynomial.polynomial.polyval(x[test], agirliklar)
    print(f"Doğrulamada seçilen derece: {derece}")
    print(f"Seçim sonrası ayrılmış test MSE: {mse(y[test], test_tahmin):.4f}")
    print("Test sonucu aday seçiminde kullanılmadı.")


if __name__ == "__main__":
    main()
