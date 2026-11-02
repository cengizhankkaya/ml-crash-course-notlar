"""Ek pekiştirme: eğitim ve sunum dönüşümünün aynı olması.

Gerçek servis veya resmî Colab sonucu değildir; elle seçilmiş sayılar kullanır.
Çalıştır: python kod/10-uretim-ml-sistemleri/egitim_sunum_farki.py
"""
from math import exp


def tahmin(ham_deger, ortalama, std):
    if std <= 0:
        raise ValueError("Standart sapma pozitif olmalı.")
    z = (ham_deger - ortalama) / std
    logit = 0.8 * z - 0.2  # Öğrenme yapılmıyor; örnek ağırlıklar sabit.
    return z, 1 / (1 + exp(-logit))


def main():
    # Bu değerler modelle birlikte saklanmış eğitim istatistiklerini temsil eder.
    kayitli_donusum = {"ortalama": 100.0, "std": 20.0}
    hatali_donusum = {"ortalama": 80.0, "std": 20.0}
    print("Ham değer | doğru z / olasılık | hatalı z / olasılık")
    for x in (80.0, 100.0, 120.0):
        z, p = tahmin(x, **kayitli_donusum)
        yanlis_z, yanlis_p = tahmin(x, **hatali_donusum)
        print(f"{x:9.1f} | {z:6.2f} / {p:.4f} | {yanlis_z:7.2f} / {yanlis_p:.4f}")
    print("Aynı ham değer + farklı dönüşüm = farklı model girdisi ve tahmin.")


if __name__ == "__main__":
    main()
