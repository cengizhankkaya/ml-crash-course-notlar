# 4.7 Polinom Dönüşümleri

> Kaynak: [MLCC — Polynomial transforms](https://developers.google.com/machine-learning/crash-course/numerical-data/polynomial-transforms)

Doğrusal model, yeni özellikler eklenerek girişle doğrusal olmayan ilişkileri temsil edebilir:

$$\hat y=b+w_1x+w_2x^2$$

Burada model **parametrelere göre doğrusaldır**; girdiye göre eğri çizer. `x²` yeni bir sentetik özelliktir. Sinir ağı kullanmadan da bu ilişki öğrenilebilir.

## Küçük örnek

Örnek veri `y = 1 + 2x + 3x²` ilişkisiyle üretilsin. Tasarım matrisindeki bir satır `[1, x, x²]` olur. `x=2` için satır `[1, 2, 4]`, tahmin `1 + 4 + 12 = 17` olur.

Ek kod, gürültüsüz örnekte katsayıları en küçük karelerle bulur. Bu, polinom gösterimini anlatmak içindir; gerçek veride kusursuz tahmin beklenmez.

## Dikkat

- Yüksek dereceler büyük sayılar ve sayısal kararsızlık üretebilir; ölçeklemeyi değerlendir.
- Daha yüksek derece her zaman daha iyi genelleme sağlamaz. Dereceyi doğrulama verisiyle seç.
- Eğitim aralığı dışına taşan polinom tahminleri hızla büyüyebilir.

## ✅ Kendimi test

**S:** `x²` eklemek modeli parametrelere göre doğrusal olmaktan çıkarır mı?

**C:** Hayır; ağırlıklar hâlâ özelliklerle çarpılıp toplanır.

**S:** Eğitim hatası azaldığında dereceyi artırmak kesin doğru mu?

**C:** Hayır; doğrulama hatası artabilir.

## 🔑 Anahtar terimler

`polynomial transform` · `synthetic feature` · `design matrix` · `extrapolation`

💻 Ek tekrar örneği: [veri_donusumleri.py](../../kod/04-sayisal-veri/veri_donusumleri.py)
