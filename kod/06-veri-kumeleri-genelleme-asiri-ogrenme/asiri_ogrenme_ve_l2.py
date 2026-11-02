"""Ek pekiştirme: polinom kapasitesi, L2 ve doğrulamayla model seçimi.

Amaç: MSE + lambda * sum(w[1:]**2). Sabit terim cezalandırılmaz.
Yapay veri kullanılır; resmî kurs deneyi veya geçmiş kişisel sonuç değildir.
Çalıştır: python kod/06-veri-kumeleri-genelleme-asiri-ogrenme/asiri_ogrenme_ve_l2.py
"""
import numpy as np


def design(x, degree):
    return np.vander(x, degree + 1, increasing=True)


def fit(x, y, degree, strength):
    matrix = design(x, degree)
    if strength == 0:
        return np.linalg.lstsq(matrix, y, rcond=None)[0]
    penalty = np.eye(degree + 1)
    penalty[0, 0] = 0.0
    # Augmented least squares avoids explicitly inverting X.T @ X.
    augmented = np.vstack([matrix, np.sqrt(len(x) * strength) * penalty])
    targets = np.r_[y, np.zeros(degree + 1)]
    return np.linalg.lstsq(augmented, targets, rcond=None)[0]


def mse(x, y, weights):
    return float(np.mean((design(x, len(weights) - 1) @ weights - y) ** 2))


def main():
    rng = np.random.default_rng(7)

    def sample(size):
        x = rng.uniform(-1, 1, size)
        y = np.sin(np.pi * x) + rng.normal(0, 0.2, size)
        return x, y

    train_x, train_y = sample(25)
    validation_x, validation_y = sample(100)
    test_x, test_y = sample(100)
    candidates = []
    print("derece  lambda      eğitim MSE   doğrulama MSE   ağırlık normu")
    for degree in (1, 3, 15):
        for strength in (0.0, 0.0001, 0.01, 0.1):
            weights = fit(train_x, train_y, degree, strength)
            train_loss = mse(train_x, train_y, weights)
            validation_loss = mse(validation_x, validation_y, weights)
            assert np.isfinite([train_loss, validation_loss]).all()
            candidates.append((validation_loss, degree, strength, weights))
            print(f"{degree:6d}  {strength:8g}  {train_loss:12.5f}  "
                  f"{validation_loss:14.5f}  {np.linalg.norm(weights[1:]):14.3f}")

    _, degree, strength, weights = min(candidates, key=lambda item: item[0])
    print(f"\nDoğrulamayla seçilen: derece={degree}, lambda={strength:g}")
    # Test kaybı model seçildikten sonra yalnız seçilen model için hesaplanır.
    print(f"Son değerlendirme, test MSE: {mse(test_x, test_y, weights):.5f}")
    print("En düşük eğitim hatasını veren satırın doğrulama hatasını karşılaştır.")
    print("Bu tek yapay veri deneyi; aynı lambda her veri kümesi için iyi değildir.")

    # Eğitim yapmayan ayrı bir kayıt örneği: en iyi adımı geri seçme fikri.
    validation_history = np.array([0.8, 0.5, 0.35, 0.31, 0.33, 0.38])
    best_epoch = int(validation_history.argmin()) + 1
    print(f"\nTemsili erken durdurma kaydı: {validation_history.tolist()}")
    print(f"En iyi kontrol noktası: {best_epoch}. dönem (son dönem değil).")
    assert best_epoch == 4


if __name__ == "__main__":
    main()
