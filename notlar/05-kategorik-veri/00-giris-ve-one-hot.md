# 5.0 Kategorik Veri, Sözlük ve One-Hot

> Kaynaklar: [MLCC — Kategorik veri](https://developers.google.com/machine-learning/crash-course/categorical-data?hl=tr) · [Sözlük ve one-hot](https://developers.google.com/machine-learning/crash-course/categorical-data/one-hot-encoding?hl=tr)

Bir değerin rakamlardan oluşması, onun sayısal büyüklük olduğu anlamına gelmez. Ürün kodu `120`, ürün kodu `60`ın iki katı değildir. Kategorik özelliklerde önce **hangi kimliğin temsil edildiğini**, sayısal özelliklerde ise **hangi miktarın ölçüldüğünü** sor.

## Sözlükten vektöre

Sözlük, her kategoriye bir sütun ayırır. `one-hot` vektöründe yalnız o kategoriye ait sütun 1, diğerleri 0 olur. Sütun numarası bir konumdur; onu sürekli bir miktar gibi modele vermek yapay bir sıralama yaratabilir.

Bu not için hazırlanmış örnek:

| Sipariş kanalı | mağaza | web | telefon | bilinmeyen |
|---|---:|---:|---:|---:|
| web | 0 | 1 | 0 | 0 |
| telefon | 0 | 0 | 1 | 0 |
| yeni kanal | 0 | 0 | 0 | 1 |

Sözlük eğitimde sabitlenir; tahminde aynı sütun sırası kullanılır. Nadir veya yeni kategoriler için **OOV** kovası planlanır. Bir örnekte birden fazla kategori varsa `multi-hot` kullanılabilir. Seyrek gösterim yalnız sıfır olmayan konumları saklayarak belleği azaltır; kategorilerin sayısal anlamını değiştirmez.

## Küçük kontrol

**S1:** Üç kanal ve bir OOV kovası varsa 20 siparişin yoğun gösterim boyutu nedir?

**C:** `(20, 4)`. Her satır bir sipariş, her sütun bir kategoridir.

**S2:** Eğitimde `web` ikinci sütundayken tahminde üçüncü sütuna taşınırsa ne olur?

**C:** Model başka bir kategori için öğrendiği ağırlığı kullanır. Vektör boyutunun doğru olması tek başına yeterli değildir.

## Anahtar terimler

`categorical feature` · `vocabulary` · `one-hot` · `multi-hot` · `sparse representation` · `OOV`

---
💻 Ek pekiştirme örneği: [`kodlama_ve_caprazlama.py`](../../kod/05-kategorik-veri/kodlama_ve_caprazlama.py)
