"""Ek pekiştirme: hedef kodlamada eğitim içi cross-fitting.

Yalnız NumPy gerekir. Bu örnek bir üretim encoder'ı veya kurs çözümü değildir.
Çalıştır: python kod/05-kategorik-veri/ortalama_kodlama.py
"""
import numpy as np


def fit_mapping(categories, targets, smoothing=2.0):
    mean = float(targets.mean())
    mapping = {}
    for category in np.unique(categories):
        subset = targets[categories == category]
        mapping[category] = (subset.sum() + smoothing * mean) / (len(subset) + smoothing)
    return mapping, mean


def transform(categories, mapping, fallback):
    return np.array([mapping.get(category, fallback) for category in categories])


def cross_fit(categories, targets, folds):
    encoded = np.empty(len(targets))
    for fold in np.unique(folds):
        held_out = folds == fold
        mapping, mean = fit_mapping(categories[~held_out], targets[~held_out])
        encoded[held_out] = transform(categories[held_out], mapping, mean)
    return encoded


def main():
    categories = np.array(["a", "b", "a", "c", "b", "c", "a", "nadir"])
    targets = np.array([0., 1., 1., 0., 0., 1., 0., 1.])
    folds = np.array([0, 1, 2, 3, 0, 1, 2, 3])
    encoded = cross_fit(categories, targets, folds)
    print("Eğitim satırları, kendi parçalarının etiketleri kullanılmadan kodlandı:")
    for category, target, value in zip(categories, targets, encoded):
        print(f"  kategori={category:5s} etiket={target:.0f} kod={value:.4f}")

    # Bir satırın etiketini değiştirmek, kendi parçasının kodlarını değiştiremez.
    changed = targets.copy()
    changed[0] = 1.0
    changed_encoding = cross_fit(categories, changed, folds)
    assert np.allclose(encoded[folds == folds[0]], changed_encoding[folds == folds[0]])

    # Yeni veriler tam eğitim kümesinden öğrenilen eşlemeyi kullanır.
    mapping, fallback = fit_mapping(categories, targets)
    new_categories = np.array(["a", "b", "görülmedi"])
    new_encoded = transform(new_categories, mapping, fallback)
    print("\nYeni kategori kodları:", {str(k): float(v) for k, v in zip(new_categories, new_encoded)})
    assert new_encoded[-1] == targets.mean()
    assert np.all((encoded >= 0) & (encoded <= 1))
    print("Kontrol: aynı parçanın etiketleri sızmadı; yeni kategori eğitim ortalamasını aldı.")


if __name__ == "__main__":
    main()
