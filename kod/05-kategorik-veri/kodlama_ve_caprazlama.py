"""Ek pekiştirme: one-hot, OOV, sabit hashing ve özellik çaprazlama.

Bu bağımsız yapay örnek, resmî kurs alıştırmasının kaydedilmiş sonucu değildir.
Çalıştır: python kod/05-kategorik-veri/kodlama_ve_caprazlama.py
"""
import hashlib
import numpy as np


def one_hot(values, vocabulary):
    """Sözlük dışındaki değerler son OOV sütununa gider."""
    indices = {value: i for i, value in enumerate(vocabulary)}
    result = np.zeros((len(values), len(vocabulary) + 1), dtype=float)
    for row, value in enumerate(values):
        result[row, indices.get(value, len(vocabulary))] = 1.0
    return result


def bucket(value, count):
    """Python hash() yerine süreçler arasında aynı sonucu veren bir hash."""
    digest = hashlib.sha256(value.encode("utf-8")).digest()
    return int.from_bytes(digest[:8], "big") % count


def main():
    channels = ["mağaza", "web", "telefon"]
    values = ["web", "telefon", "yeni kanal"]
    encoded = one_hot(values, channels)
    print("Sütunlar:", channels + ["OOV"])
    print(encoded)
    assert encoded.shape == (3, 4)
    assert np.all(encoded.sum(axis=1) == 1)
    assert encoded[-1, -1] == 1

    deliveries = ["standart", "hızlı", "teslim-al"]
    # Bu hesap bilinen kategorilerin vektörlerini kullanır; OOV'yi çıkarır.
    a = one_hot(["web"], ["web", "mağaza"])[0, :-1]
    b = one_hot(["hızlı"], deliveries)[0, :-1]
    cross = np.outer(a, b).ravel()
    names = [f"{channel}+{delivery}"
             for channel in ["web", "mağaza"] for delivery in deliveries]
    print("\nÇapraz sütunlar:", names)
    print("web+hızlı:", cross)
    assert cross.size == 6 and cross.sum() == 1
    assert names[int(cross.argmax())] == "web+hızlı"

    hashed = {name: bucket(name, 3) for name in ["elma", "armut", "kiraz", "üzüm"]}
    print("\n4 kategori, 3 hash kovası:", hashed)
    assert len(set(hashed.values())) < len(hashed)
    print("En az bir çakışma var. Kova sayısını 20 yapıp yeniden karşılaştır.")


if __name__ == "__main__":
    main()
