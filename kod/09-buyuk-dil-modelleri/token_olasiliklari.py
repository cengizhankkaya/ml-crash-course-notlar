"""Ek pekiştirme: oyuncak logit'lerden sonraki token olasılıkları.

Gerçek tokenizer veya dil modeli içermez; eğitim ya da model indirme yapmaz.
Temperature, dağılımdan örnekleme için ek bir pratik kavramdır.
Çalıştır: python kod/09-buyuk-dil-modelleri/token_olasiliklari.py
"""
import numpy as np


def softmax(logits, sicaklik=1.0):
    if not np.isfinite(sicaklik) or sicaklik <= 0:
        raise ValueError('Sıcaklık sonlu ve sıfırdan büyük olmalıdır.')
    z = np.asarray(logits, dtype=float) / sicaklik
    z = z - np.max(z)
    exp_z = np.exp(z)
    return exp_z / exp_z.sum()


def main():
    adaylar = np.array(['güzel', 'serin', 'kapalı'])
    logits = np.array([2.0, 1.0, 0.0])
    print('Oyuncak bağlam: Bugün hava ...')
    for sicaklik in [0.5, 1.0, 2.0]:
        p = softmax(logits, sicaklik)
        np.testing.assert_allclose(p.sum(), 1.0)
        print(f'T={sicaklik:.1f}: ' + ', '.join(f'{a}={v:.3f}' for a, v in zip(adaylar, p)))
    np.testing.assert_allclose(softmax(logits), softmax(logits + 10000))
    assert softmax(logits, 0.5).max() > softmax(logits, 2).max()
    rng = np.random.default_rng(9)
    print('En yüksek olasılıklı seçim:', adaylar[np.argmax(logits)])
    print('Sabit tohumla 10 örnek:', rng.choice(adaylar, 10, p=softmax(logits)).tolist())
    print('Sıcaklık ağırlıkları güncellemez; örnekleme dağılımını değiştirir.')
    print('Olasılığın yüksek olması, üretilen ifadenin doğru olduğunu kanıtlamaz.')


if __name__ == '__main__':
    main()
