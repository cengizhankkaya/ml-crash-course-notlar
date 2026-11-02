"""Ek tekrar örneği: gruplama, eksik değer göstergesi ve polinom özellikleri.

Sentetik veri kullanır; resmî Colab alıştırmasının sonucu değildir.
Çalıştır: python kod/04-sayisal-veri/veri_donusumleri.py
"""
import numpy as np


def main():
    temperatures = np.array([7.0, 10.0, 18.0, 25.0, 31.0])
    bins = np.digitize(temperatures, bins=[10.0, 25.0], right=False)
    one_hot = np.eye(3, dtype=int)[bins]
    print("Sıcaklıklar:", temperatures)
    print("Aralık numaraları:", bins)
    print("One-hot:\n", one_hot)

    train = np.array([2.0, 4.0, 6.0, np.nan])
    median = np.nanmedian(train)
    # Test/üretim istatistikleri kullanılmıyor; eğitim medyanı korunuyor.
    serving = np.array([np.nan, 0.0, 8.0])
    missing = np.isnan(serving)
    filled = np.where(missing, median, serving)
    print("Eğitim medyanı:", median)
    print("Üretim [değer, eksik]:\n", np.column_stack([filled, missing]))

    x = np.linspace(-2.0, 2.0, 9)
    design = np.column_stack([np.ones_like(x), x, x**2])
    y = 1 + 2*x + 3*x**2
    coefficients, *_ = np.linalg.lstsq(design, y, rcond=None)
    print("[bias, x ağırlığı, x² ağırlığı]:", coefficients.round(6))
    print("Gürültüsüz sentetik veri MSE:", np.mean((design @ coefficients-y)**2))


if __name__ == "__main__":
    main()
