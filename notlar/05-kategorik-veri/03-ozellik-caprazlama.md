# 5.3 Özellik Çaprazlama ve Pekiştirme

> Kaynaklar: [MLCC — Özellik çaprazlama](https://developers.google.com/machine-learning/crash-course/categorical-data/feature-crosses?hl=tr) · [Etkileşimli alıştırmalar](https://developers.google.com/machine-learning/crash-course/categorical-data/feature-cross-exercises?hl=tr)

**Özellik çaprazlama**, kategorik veya kovalanmış özelliklerin kombinasyonunu yeni bir özellik yapar. Doğrusal model, yalnız tek tek etkileri toplamak yerine belirli bir eşleşmeye ayrı ağırlık verebilir.

## Örnek: kanal × teslimat türü

Kanallar `{web, mağaza}`, teslimat türleri `{standart, hızlı, teslim-al}` olsun. Çapraz sözlükte `2×3=6` olası eşleşme vardır. `web+hızlı` ayrı bir özellik olur; `web` ve `hızlı` sütunlarının yan yana yazılması bu etkileşimle aynı şey değildir.

One-hot vektörleri `a` ve `b` için çapraz vektör, dış çarpımın düzleştirilmesiyle kurulabilir:

$$c_{ij}=a_i b_j$$

Çaprazlama, modelin **parametrelere göre doğrusal** olmasını değiştirmez; girdilerin temsilini zenginleştirir. Sayısal özelliklerde `x²` veya `x₁x₂` gibi polinom dönüşümleri benzer bir amaç taşır.

## Bedeli

Kategori sayıları çarpıldığı için temsil hızla büyür. Çoğu eşleşmenin az gözlemi varsa model bu ağırlıkları güvenilir biçimde öğrenemez. Alan bilgisiyle anlamlı birleşimler seç; faydayı ayrılmış doğrulama verisinde karşılaştır.

## Ek alıştırma

İlgili kodda kanal ve teslimat one-hot vektörlerinden çapraz vektörü üret. Ardından yeni bir teslimat türü eklediğinde kaç yeni sütun gerektiğini kâğıt üzerinde hesapla. Bu, burada eklenen bağımsız bir pekiştirme örneğidir; resmî Playground alıştırmasının sonucu değildir.

**S1:** 4 kategori ile 7 kategoriyi çaprazlarsan boyut kaç olur?

**C:** Tam Kartezyen çarpım için 28.

**S2:** Çaprazlama eğitim hatasını düşürdü ama doğrulama hatasını artırdı. Ne düşünülmeli?

**C:** Yeni temsil ezberlemeyi kolaylaştırmış olabilir; nadir eşleşmeleri, düzenlileştirmeyi ve veri ayrımını incele.

## Anahtar terimler

`feature cross` · `Cartesian product` · `interaction` · `polynomial feature` · `sparsity`

## Resmî tekrar bağlantıları

- [Özellik çaprazlama etkileşimli alıştırmaları](https://developers.google.com/machine-learning/crash-course/categorical-data/feature-cross-exercises?hl=tr)
- [Modül sonu bilgi testi](https://developers.google.com/machine-learning/crash-course/categorical-data/test-your-knowledge?hl=tr)

Bu nottaki sorular ek pekiştirme içindir; resmî testin cevap anahtarı değildir.

---
💻 Ek pekiştirme örneği: [`kodlama_ve_caprazlama.py`](../../kod/05-kategorik-veri/kodlama_ve_caprazlama.py)
