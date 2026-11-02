# 9.1 Transformer ve Self-Attention

> Kaynak: [MLCC — Büyük dil modeli nedir?](https://developers.google.com/machine-learning/crash-course/llm/transformers?hl=tr)

Transformer, token temsillerini bağlam içindeki ilişkilerle dönüştürür. **Self-attention**, aynı dizideki tokenlardan gelen bilgiyi ağırlıklandırarak birleştirir. Farklı attention başlıkları farklı ilişki örüntüleri öğrenebilir; çok sayıda katman bu dönüşümleri tekrarlar.

| Mimari | Temel rol |
|---|---|
| Encoder | Girdi dizisini temsillere dönüştürmek |
| Decoder | Önceki tokenlardan devam üretmek |
| Encoder–decoder | Girdi temsilini kullanarak çıktı dizisi üretmek |

Encoder tipi çift yönlü bağlamdan yararlanabilir. Otoregresif decoder'da **causal mask**, bir konumun gelecekteki tokenları görmesini engeller. Eğitimde birçok konumun hesabı paralel yapılabilse de üretimde bir sonraki token önceki seçime bağlıdır.

## Ön eğitim

Eğitim hedefi mimariye göre değişebilir: gizlenen tokenları tahmin etmek veya önceki tokenlardan sonrakini tahmin etmek. Hedefler metnin kendisinden üretildiğinden bu yaklaşım **öz gözetimli öğrenme** olarak adlandırılır. Kayıp üzerinden geri yayılım parametreleri günceller; sonradan talimat izleme eğitimi de uygulanabilir.

## Üç önemli sınırlama

- **Yanlış üretim:** Akıcı ve kendinden emin ifade doğruluğu garanti etmez.
- **Kaynak maliyeti:** Eğitim ve çıkarım hesaplama, bellek ve enerji gerektirir.
- **Yanlılık:** Veri ve tasarım seçimleri çıktılardaki örüntüleri etkileyebilir.

## Ek düşünce deneyi

“Ece kitabı Deniz'e verdi çünkü o okumak istiyordu.” cümlesinde “o” için iki aday vardır. Attention ağırlıkları ilişkili tokenların bilgisini taşımaya yardımcı olabilir; tek bir ağırlık grafiği modelin gerekçesini kesin olarak açıklamaz.

Üç konumlu bir causal görünürlük tablosu çiz: birinci konum yalnız kendini, ikinci ilk ikisini, üçüncü ilk üçünü görebilsin. Geleceği gizlemek, gerçek metin üretiminde henüz bilinmeyen cevabın eğitim hesabına sızmasını önler.

## ✅ Kendimi test

**S1:** Her Transformer hem encoder hem decoder içerir mi?

**C:** Hayır; yalnız encoder veya yalnız decoder kullanan mimariler de vardır.

**S2:** Model çok akıcı bir tarih açıklaması ürettiyse doğrulama gereksiz midir?

**C:** Hayır. Dil olasılığı ile olgusal doğruluk aynı ölçüt değildir.

## 🔑 Anahtar terimler
`Transformer` · `encoder` · `decoder` · `self-attention` · `causal mask` · `hallucination`
