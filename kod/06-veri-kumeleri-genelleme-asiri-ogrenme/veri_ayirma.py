"""Ek pekiştirme: veri ayrımı, eksik değerler, ölçekleme ve örnek ağırlıkları.

Yapay bağımsız satırlar kullanılır; gerçek veri veya Colab sonucu içermez.
Çalıştır: python kod/06-veri-kumeleri-genelleme-asiri-ogrenme/veri_ayirma.py
"""
import numpy as np


def main():
    rng = np.random.default_rng(42)
    values = rng.normal(50, 10, 100)
    values[[4, 17, 28, 51, 79]] = np.nan
    order = rng.permutation(len(values))
    train_ids, validation_ids, test_ids = np.split(order, [70, 85])
    assert not set(train_ids) & set(validation_ids)
    assert not set(train_ids) & set(test_ids)
    assert not set(validation_ids) & set(test_ids)
    assert len(set(order)) == len(values)

    train = values[train_ids]
    median = np.nanmedian(train)
    completed_train = np.where(np.isnan(train), median, train)
    mean = completed_train.mean()
    std = completed_train.std()
    if std == 0:
        std = 1.0

    print(f"Yalnız eğitimden: medyan={median:.3f}, ortalama={mean:.3f}, std={std:.3f}")
    for name, indices in [("eğitim", train_ids), ("doğrulama", validation_ids), ("test", test_ids)]:
        raw = values[indices]
        missing = np.isnan(raw)
        completed = np.where(missing, median, raw)
        features = np.column_stack(((completed - mean) / std, missing.astype(float)))
        assert np.isfinite(features).all()
        print(f"{name:10s}: şekil={features.shape}, eksik={missing.sum()}, "
              f"ölçekli ortalama={features[:, 0].mean():.3f}")
        if name == "eğitim":
            assert np.isclose(features[:, 0].mean(), 0)

    # Tam sayılı bu örnek, ağırlıklı sınıf oranını elle kontrol etmeyi kolaylaştırır.
    negative_count, positive_count, factor = 900, 100, 10
    kept_negative = negative_count // factor
    weighted_negative = kept_negative * factor
    weighted_positive = positive_count
    print("\nAlt örnekleme: 900 negatif -> 90; her tutulan negatifin ağırlığı 10.")
    print("Ağırlıklı pozitif oranı:", weighted_positive / (weighted_negative + weighted_positive))
    assert weighted_negative == negative_count
    assert weighted_positive / (weighted_negative + weighted_positive) == 0.1


if __name__ == "__main__":
    main()
