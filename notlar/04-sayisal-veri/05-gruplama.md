# 4.5 Gruplama (Binning)

> Kaynak: [MLCC — Binning](https://developers.google.com/machine-learning/crash-course/numerical-data/binning)

Sürekli bir değeri aralıklara ayırıp her aralığı bir kategori gibi temsil ederiz. Böylece doğrusal model, her aralık için ayrı etki öğrenebilir. Bu, ölçeklemeden farklıdır: aynı aralıktaki değerlerin ayrıntısı kaybolur.

## Küçük örnek

Sıcaklık sınırları `10` ve `25` olsun:

| Aralık | Değer | One-hot vektör |
|---|---|---|
| x < 10 | 7 | [1, 0, 0] |
| 10 ≤ x < 25 | 18 | [0, 1, 0] |
| 25 ≤ x | 31 | [0, 0, 1] |

Model bu gösterimle soğuk ve sıcak günlere farklı ağırlıklar verebilir. Ancak 12 ile 24 artık aynı gösterime sahiptir.

## Sınırları seçmek

- **Eşit genişlik:** Her aralık aynı sayısal genişliktedir; örnek sayıları dengesiz olabilir.
- **Yüzdeliklere göre:** Her aralık yaklaşık aynı sayıda eğitim örneği içerir; aralık genişlikleri değişir. Tekrarlanan değerler tam eşitliği engelleyebilir.
- Çok fazla aralık, az örnekli kategoriler ve aşırı öğrenme oluşturabilir.

Veriden öğrenilen sınırları yalnız eğitim kümesinden hesapla; doğrulama, test ve üretimde aynı sınırları uygula. Sınır üzerindeki değerlerin hangi aralığa girdiğini açık tanımla.

## ✅ Kendimi test

**S:** Gruplama ile normalleştirme aynı mı?

**C:** Hayır. Gruplama değerleri kategorilere indirger; ölçekleme sayısal temsili dönüştürür.

**S:** Her örneğe ayrı aralık vermek neden sorunlu?

**C:** Aralık başına genellenebilir örüntü öğrenmeye yetecek veri kalmaz.

## 🔑 Anahtar terimler

`binning` · `bucketing` · `quantile` · `one-hot encoding`

💻 Ek tekrar örneği: [veri_donusumleri.py](../../kod/04-sayisal-veri/veri_donusumleri.py)
