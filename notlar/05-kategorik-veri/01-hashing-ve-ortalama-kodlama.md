# 5.1 Çok Kategorili Özellikler: Hashing ve Ortalama Kodlama

> Kaynak: [MLCC — Yüksek boyutlu kategorik özellikler ve hashing](https://developers.google.com/machine-learning/crash-course/categorical-data/one-hot-encoding?hl=tr)
>
> Ek teknik kaynak: [scikit-learn — Target Encoder](https://scikit-learn.org/stable/modules/preprocessing.html#target-encoder). Ortalama kodlama kursun ana sayfasında anılır; aşağıdaki ayrıntılar bu ek kaynaktan özetlenmiştir.

## Hashing

Kategori, sabit sayıda kovadan birine gönderilir:

$$j = h(\text{kategori}) \bmod B$$

Böylece büyük sözlüğün yerine `B` boyutlu bir temsil kullanılır. Farklı kategoriler aynı kovaya düşebilir: buna **çakışma** denir. Kova numarası yine bir kimliktir; sürekli büyüklük değildir. Çok sayıda kategori için öğrenilen **embedding** vektörleri de bir seçenektir.

Ek kod örneği tekrar üretilebilir sonuç için sabit bir hash kullanır. `B=3` için dört farklı kelime seçildiğinde en az iki kelime aynı kovayı paylaşmak zorundadır. Bu, güvercin yuvası ilkesinin doğrudan bir örneğidir.

## Ortalama / hedef kodlama

Kategori, o kategorideki etiket ortalamasıyla temsil edilir. Az görülen kategoriyi genel ortalamaya yaklaştırmak için:

$$e_c = \frac{\sum_{i:x_i=c} y_i + m\mu}{n_c+m}$$

Burada `μ` eğitim etiketi ortalaması, `n_c` kategori sayısı, `m` yumuşatma gücüdür. Eğitim satırlarını kodlarken her parçanın istatistikleri diğer eğitim parçalarından hesaplanır (**cross-fitting**). Doğrulama ve test etiketleri hesaplamaya katılmaz. Görülmemiş kategoriye eğitim ortalaması atanabilir.

## Küçük kontrol

**S1:** Bir kategorinin tek örneği ve etiketi 1. Kendi etiketiyle doğrudan kodlanması neden sorun?

**C:** Girdi, tahmin edilmesi gereken cevabı taşır; model tesadüfi ilişkileri ezberleyebilir.

**S2:** `n_c=2`, etiket toplamı 1, `μ=0.25`, `m=2` ise kod nedir?

**C:** `(1 + 2×0.25)/(2+2) = 0.375`.

## Anahtar terimler

`hashing trick` · `collision` · `target encoding` · `smoothing` · `cross-fitting` · `data leakage`

---
💻 Ek pekiştirme örnekleri: [`kodlama_ve_caprazlama.py`](../../kod/05-kategorik-veri/kodlama_ve_caprazlama.py) · [`ortalama_kodlama.py`](../../kod/05-kategorik-veri/ortalama_kodlama.py)
