# 11.0 AutoML: Kapsamı, Faydaları ve Sınırları

> Kaynaklar: [MLCC — AutoML](https://developers.google.com/machine-learning/crash-course/automl) · [Benefits and limitations](https://developers.google.com/machine-learning/crash-course/automl/benefits-limitations)

**AutoML**, model geliştirmedeki bazı tekrar eden kararları otomatikleştirir. Özellik dönüştürme/seçme, algoritma seçimi ve hiperparametre araması buna dahildir. Kullanılan araç hangi adımları destekliyorsa otomasyonun kapsamı odur; her ürün bütün süreci üstlenmez.

Örneğin bir sistem birkaç model ailesini ve öğrenme oranını deneyip doğrulama metriğine göre aday seçebilir. Böylece insanın her denemeyi ayrı yazması azalır. Ancak hedefin doğru tanımlanması, etiketlerin güvenilirliği ve verinin kullanım durumunu temsil etmesi hâlâ gerekir.

## Ne sağlar, neyi garanti etmez?

| Fayda | Sınır |
|---|---|
| Daha hızlı başlangıç ve çok sayıda aday denemesi | Arama, hesaplama ve zaman bütçesiyle sınırlıdır. |
| Veride yararlı sinyal olup olmadığını inceleme | Zayıf veri otomatik olarak düzelmez. |
| Özellikleri ve temel performansı karşılaştırma | Seçim süreci veya birleşik model zor anlaşılabilir. |
| Tekrarlanan işlemleri standartlaştırma | Araçta olmayan özel eğitim davranışı eklenemeyebilir. |

Bir AutoML sonucu, aynı veriyle mümkün olan mutlak en iyi model olduğu anlamına gelmez. Arama tekrarlarında farklı sonuçlar görülebilir. Transfer öğrenmesi kullanan özel sistemler daha az etiketli veriyle çalışabilir; veri gereksinimi görev ve araca bağlıdır.

## Ek düşünme örneği

Arşiv kayıtlarının kategorisini tahmin etmek için önce basit bir temel model kurulduğunu düşün. AutoML, ayrılmış doğrulama verisinde daha iyi sonuç veriyor ama tahmini çok yavaş. Model seçimine yalnız başarıyı değil, gecikme ve işletim maliyetini de dahil et. Gerçek bir ölçüm yapılmadan bu ödünleşimde hangi adayın daha iyi olduğu söylenemez.

## ✅ Kendimi test

**S1:** Hedef sütunu yanlış seçilen deneyi AutoML kurtarır mı?

**C:** Hayır. Yanlış soruyu iyi optimize edebilir; problem tanımı kontrol edilmelidir.

**S2:** AutoML sadece yeni başlayanlar için mi?

**C:** Hayır. Deneyimli ekipler de hızlı başlangıç, veri inceleme ve aday araması için kullanabilir.

## 🔑 Anahtar terimler

`AutoML` · `model search` · `feature selection` · `hyperparameter tuning` · `transfer learning`
