# 4.3 Sayısal Veri: Programlama Alıştırmaları

> Kaynak: [ML Crash Course — Sayısal veri: Programlama alıştırmaları](https://developers.google.com/machine-learning/crash-course/numerical-data/programming-exercises?hl=tr)

[İlk adımlar](02-ilk-adimlar.md) dersinde öğrenilenleri uygulamak için iki Colab alıştırması:

| # | Alıştırma | Amaç | Colab |
|---|---|---|---|
| 1 | **Veri kümesinin istatistiklerini alma** | Belirgin aykırı değer içeren **sütunları** istatistiklerle bulmak | [Aç](https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/numerical_data_stats.ipynb) |
| 2 | **Veri kümesinin "kötü bölümünü" bulma** | Veride **gizlenmiş kötü değerleri** görsel ve matematiksel yöntemlerle bulmak | [Aç](https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/numerical_data_bad_values.ipynb) |

Colab kurulum gerektirmez, tarayıcıda çalışır (en iyi Chrome ve Firefox'un masaüstü sürümlerinde).

> ⚠️ Hatırlatma: Colab'da kod hücrelerini çalıştırmadan önce **tarayıcı çevirisini kapat**; yoksa kod da çevrilip bozuluyor ([1.5'teki not](../01-dogrusal-regresyon/05-programlama-alistirmasi.md)).

## Bu alıştırmalarda kullanılacak araçlar ([4.2](02-ilk-adimlar.md)'den)
| Ne arıyorum? | Araç |
|---|---|
| Sütun istatistikleri | `df.describe()`, `df.median()`, `df.std()` |
| Aykırı değer şüphesi | (25. − 0.) ile (100. − 75.) yüzdelik farklarını karşılaştırmak |
| Gizli kötü değerler | Histogram / dağılım grafiği; tek bir değerde (0, −1, 999…) anormal yığılma |
| Eksik veri | `df.isna().sum()`, ama "0" veya "−1" diye kodlanmış eksiklere de dikkat |

Benim [ilk_adimlar.py](../../kod/04-sayisal-veri/ilk_adimlar.py) deneyim bu iki alıştırmanın küçük bir provası gibi: Yüzdelik farkı istatistikle iki aykırı sütunu buldu, histogram ise istatistikte görünmeyen "0'da gizli sütunu" ortaya çıkardı.

## 📝 Sonuçlarım
*Colab'da çalıştırınca doldur:*

### Alıştırma 1: İstatistikler
- Hangi sütunlarda belirgin aykırı değer var?
- Hangi istatistik bunu gösterdi?

### Alıştırma 2: Kötü bölüm
- Kötü değerler verinin hangi bölümündeydi?
- Görsel mi, matematiksel mi buldum?
- Ne yaptım (sil / düzelt / kırp)?
