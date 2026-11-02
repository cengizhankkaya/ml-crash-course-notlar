"""Ek pekiştirme: NumPy ile XOR için forward, loss, backward ve güncelleme.

Dört satırlı oyuncak tabloyu öğrenir; genelleme başarısı ölçmez.
Çalıştır: python kod/07-sinir-aglari/ileri_geri_yayilim.py
"""
import numpy as np


def ileri(X, W1, b1, W2, b2):
    h = np.tanh(X @ W1 + b1)
    logits = h @ W2 + b2
    # Büyük logit'lerde de taşmayı önleyen sigmoid yazımı.
    p = np.exp(-np.logaddexp(0, -logits))
    return h, logits, p


def kayip(X, y, W1, b1, W2, b2):
    _, logits, _ = ileri(X, W1, b1, W2, b2)
    return np.mean(np.logaddexp(0, logits) - y * logits)


def gradyanlar(X, y, W1, b1, W2, b2):
    h, _, p = ileri(X, W1, b1, W2, b2)
    dz2 = (p - y) / len(X)
    dW2 = h.T @ dz2
    db2 = dz2.sum(axis=0)
    dz1 = (dz2 @ W2.T) * (1 - h**2)
    return X.T @ dz1, dz1.sum(axis=0), dW2, db2


def main():
    rng = np.random.default_rng(7)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
    y = np.array([[0], [1], [1], [0]], dtype=float)
    W1, b1 = rng.normal(0, 0.5, (2, 4)), np.zeros(4)
    W2, b2 = rng.normal(0, 0.5, (4, 1)), np.zeros(1)
    params = [W1, b1, W2, b2]
    baslangic = kayip(X, y, *params)

    # Bir parametrenin analitik türevini merkezi sonlu farkla denetle.
    analitik = gradyanlar(X, y, *params)[0][0, 0]
    onceki, eps = W1[0, 0], 1e-5
    W1[0, 0] = onceki + eps
    arti = kayip(X, y, *params)
    W1[0, 0] = onceki - eps
    eksi = kayip(X, y, *params)
    W1[0, 0] = onceki
    sayisal = (arti - eksi) / (2 * eps)
    np.testing.assert_allclose(analitik, sayisal, rtol=1e-5, atol=1e-8)
    print(f"Gradyan kontrolü: analitik={analitik:.8f}, sayısal={sayisal:.8f}")

    for _ in range(6000):
        grads = gradyanlar(X, y, *params)
        for param, grad in zip(params, grads):
            param -= 0.1 * grad

    son = kayip(X, y, *params)
    _, _, p = ileri(X, *params)
    assert np.isfinite(son) and son < baslangic
    np.testing.assert_array_equal((p >= 0.5).astype(int), y.astype(int))
    print(f"Kayıp: {baslangic:.4f} -> {son:.4f}")
    print("XOR tablosu (yalnız eğitim örnekleri):")
    for x, hedef, olasilik in zip(X.astype(int), y.ravel(), p.ravel()):
        print(f"  {x.tolist()} hedef={int(hedef)}, P(1)={olasilik:.4f}")
    print("Bu sonuç ayrı bir test kümesindeki genelleme ölçümü değildir.")


if __name__ == '__main__':
    main()
