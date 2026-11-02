# 10.0 Üretim ML Sistemi ve Eğitim Stratejisi

> Kaynaklar: [MLCC — Üretim ML sistemleri](https://developers.google.com/machine-learning/crash-course/production-ml-systems) · [Statik ve dinamik eğitim](https://developers.google.com/machine-learning/crash-course/production-ml-systems/static-vs-dynamic-training)

## Model, sistemin bir parçası

Bir model dosyasını kaydetmek, çalışan bir ürünün bütününü tamamlamaz. Veri toplama ve doğrulama, özellik üretimi, eğitim işleri, model sürümleri, tahmin sunma ve izleme birlikte çalışır. Bu parçalar arasındaki sözleşmeler bozulursa, doğru model de yanlış sonuç üretebilir.

Örnek bir akış:

`ham veri → doğrulama → özellikler → eğitim → değerlendirme → sürümlü model → tahmin servisi → izleme`

İzlemeden gelen bulgular veri hazırlama ve eğitim kararlarına geri döner. Modelin tahminleri sonradan eğitim verisini etkiliyorsa ayrıca geri besleme riski doğar.

## Eğitim ne zaman yenilenir?

| Yaklaşım | İşleyiş | Temel ödünleşim |
|---|---|---|
| Statik / offline eğitim | Bir kez eğitilen sürüm bir süre kullanılır. | Daha basit işletim; değişen dünyada eskime riski. |
| Dinamik / online eğitim | Model sık veya sürekli yeni veriyle güncellenir. | Değişime uyum; daha yoğun test, izleme ve sürüm yönetimi. |

Burada **online eğitim, her istekte ağırlıkların güncellenmesi zorunluluğu** anlamına gelmez; periyodik yeniden eğitim de bu modüldeki dinamik yaklaşımın kapsamındadır. Tahmin sunma yöntemi ise ayrı bir karardır.

## Ek çalışma örneği

Bir çağrı merkezinin talep tahmini yaz verisiyle eğitilsin. Kampanya döneminde başvuruların ilişkisi değişebilir. Modelin dosyası sağlam olsa da tahmin kalitesi düşer. İzleme, hem giriş dağılımını hem gerçek talepler geldikçe hatayı karşılaştırmalıdır. Her saat otomatik yeniden eğitim de kendiliğinden çözüm değildir: bozuk yeni veriyi hızla modele taşıyabilir.

## ✅ Kendimi test

**S1:** Değişmeyen model kullanılıyorsa veri izlemesi kaldırılabilir mi?

**C:** Hayır. Servise gelen veri değişebilir; modelin eskimesi ancak ölçülerek anlaşılır.

**S2:** Yeni modeli her gün eğitmek onu doğrudan yayımlamayı gerektirir mi?

**C:** Hayır. Yeni sürüm değerlendirilir; uygun olmayan sürüm yerine önceki sürüm korunabilir.

## 🔑 Anahtar terimler

`production ML` · `pipeline` · `static training` · `dynamic training` · `model staleness`

Sonraki not: [Çıkarım ve dönüşüm](01-cikarim-ve-donusum.md)
