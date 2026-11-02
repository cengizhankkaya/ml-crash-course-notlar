# 10.2 Dağıtım Testleri ve İzleme

> Kaynaklar: [MLCC — Deployment testing](https://developers.google.com/machine-learning/crash-course/production-ml-systems/deployment-testing) · [Monitoring pipelines](https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring)

## Test katmanları

Veri şeması; tür, aralık, kategori sözlüğü ve eksiklik oranlarını denetler. Dönüştürülmüş özellikler ayrıca kontrol edilir. Örneğin tek kategorili one-hot vektöründeki birlerin toplamı 1 olmalıdır; bu kural multi-hot için geçerli değildir.

Model sürümü, önceki sürüm ve sabit bir asgari kalite ölçütüyle karşılaştırılır. Yalnız önceki sürüme bakmak, küçük ama sürekli bozulmaları kaçırabilir. Uçtan uca testler veri hazırlamadan tahmine kadar parçaların birlikte çalıştığını; sunum ortamındaki denemeler de bağımlılık uyumunu denetler.

Tohum, veri bölümü, kod, bağımlılık ve model sürümü kayıtları karşılaştırmayı kolaylaştırır. Tohum belirlemek tek başına tüm donanım işlemlerini deterministik yapmaz. Sabit anahtarla hash kullanıldığında veri bölme tekrar üretilebilir; aynı varlığa ait kayıtların ayrılmaması gerekiyorsa anahtar buna göre seçilir.

## Canlı sistemde ne ölçülür?

- **Veri:** Tür/dağılım değişimi, bilinmeyen kategoriler, eksik değerler, eğitim-sunum farkı.
- **Model:** Etiket sızıntısı, sürümün yaşı, `NaN`/`Inf`, toplam ve alt grup kalitesi.
- **Sistem:** Bellek, eğitim hızı, istek sayısı, gecikme yüzdelikleri ve hatalar.
- **Kullanım sonucu:** Model metriği yanında ürünün gerçek hedefi.

Gerçek etiket hemen gelmeyebilir. Örnekleri sonradan etiketlemek, kullanıcı geri bildirimini incelemek ve yeni sürümü sınırlı trafikle değerlendirmek kaliteyi anlamaya yardımcı olur. Tahmin anında bilinmeyen bir bilgiyi eğitim özelliği yapmak, test skoru yüksek olsa da canlı kullanımda başarısızlık yaratabilir.

## Ek çalışma örneği

Bir kargo modeli dakika beklerken servis saniye göndersin. Tür kontrolü geçer: ikisi de sayıdır. Birim sözleşmesi ve bilinen örnek üzerindeki dönüşüm testi hatayı yakalar. Ortalama yanıt süresi iyi görünürken az sayıda istek çok yavaş kalabilir; bu yüzden p95 gibi yüzdelikler de incelenir.

## ✅ Kendimi test

**S1:** Yeni sürüm öncekinden yalnız biraz kötü: otomatik kabul edilir mi?

**C:** Hayır; sabit kabul eşiği ve birikimli bozulma da değerlendirilir.

**S2:** Canlı verinin ortalaması değişti: model kesin bozulmuş mudur?

**C:** Hayır. Değişim araştırma sinyalidir; etiketli kalite ve kullanım sonuçlarıyla doğrulanır.

## 🔑 Anahtar terimler

`data schema` · `integration test` · `label leakage` · `monitoring` · `data slice`
