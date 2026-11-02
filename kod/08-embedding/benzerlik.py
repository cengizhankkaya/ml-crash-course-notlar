"""Ek pekiştirme: elle belirlenmiş vektörlerle embedding erişimi ve kosinüs.

Bu vektörler eğitilmemiştir; gerçek anlamsal model veya arama sistemi değildir.
Çalıştır: python kod/08-embedding/benzerlik.py
"""
import numpy as np


def kosinus(a, b):
    payda = np.linalg.norm(a) * np.linalg.norm(b)
    if payda == 0:
        raise ValueError('Sıfır vektörü için kosinüs tanımsızdır.')
    return float(np.dot(a, b) / payda)


def main():
    adlar = ['bisiklet', 'scooter', 'kitap', 'defter']
    # Tamamen öğretici koordinatlar; modelin öğrenilmiş çıktıları değil.
    E = np.array([[1.0, 0.2, 0.0], [0.9, 0.3, 0.0],
                  [0.0, 0.1, 1.0], [0.0, 0.2, 0.9]])
    ids = np.array([0, 2, 0])
    one_hot = np.eye(len(E))[ids]
    np.testing.assert_allclose(one_hot @ E, E[ids])
    print(f'Tablo boyutu: {E.shape}; üç indeksin çıktısı: {E[ids].shape}')
    print('One-hot @ E ile E[ids] aynı sonucu verdi.')
    skorlar = [(adlar[i], kosinus(E[0], E[i])) for i in range(1, len(E))]
    for ad, skor in sorted(skorlar, key=lambda item: item[1], reverse=True):
        print(f'  bisiklet / {ad}: kosinüs={skor:.4f}')
    np.testing.assert_allclose(kosinus(E[0], E[1]), kosinus(E[0], 5 * E[1]))
    print('Pozitif ölçekleme kosinüsü değiştirmez; nokta çarpımını değiştirir:')
    print(f'  önce={E[0] @ E[1]:.3f}, sonra={E[0] @ (5 * E[1]):.3f}')
    try:
        kosinus(E[0], np.zeros(3))
    except ValueError as error:
        print(f'Beklenen sınır durumu: {error}')


if __name__ == '__main__':
    main()
