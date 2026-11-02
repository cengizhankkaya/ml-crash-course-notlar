# 10.3 Özellik Maliyeti, Veri Kaynağı ve Geri Besleme

> Kaynak: [MLCC — Üretim sistemlerinde sorulacak sorular](https://developers.google.com/machine-learning/crash-course/production-ml-systems/questions)

## Üç temel soru

**Her özellik yararlı mı?** Ek bir veri kaynağı küçük kalite kazancı sağlayabilir; fakat toplama, bakım ve hata maliyeti getirir. Özellik çıkarıldığında ne değiştiğini ölçmek, faydasını değerlendirmeye yardım eder. Sırf mevcut olduğu için her sütunu kullanmak gerekli değildir.

**Kaynak güvenilir mi?** Üst sistemin formatı veya hesaplama yöntemi değişebilir. Kaynağın sürümü, veri gecikmesi ve kesinti davranışı bilinmelidir. Uygun olduğunda sürümlü veri kopyaları, değişiklikleri kontrollü kabul etmeyi sağlar.

**Model kendi gelecekteki verisini etkiliyor mu?** Önerilen bir öğe daha çok görünürlük ve etkileşim alır. Sonraki eğitim bunu doğal talep gibi yorumlarsa öneri kendini pekiştirebilir. Bir modelin kararları başka modelin girdisini de etkileyebilir.

## Ek düşünme alıştırması

Şirket içi belge araması hep en çok açılan belgeyi üstte göstersin. Üstteki belge daha çok açılır; yeni ve yararlı belgeler görünürlük bulamaz. Tıklama sayısının yalnız içeriğin faydasını ölçmediğini fark etmek gerekir: sıralama konumu da veriyi üretmiştir.

Bu örnek için şu notları doldur:

| Soru | İncelenecek kanıt |
|---|---|
| Yeni belge neden az açıldı? | Gösterim sayısı ve sıralama konumu |
| Kaynak gecikti mi? | Son indeksleme ve veri güncelleme zamanı |
| Yeni özellik gerekli mi? | Aynı ayrılmış değerlendirmede özellikli/özelliksiz sonuç |

Tablo, kursa ek düşünme alıştırmasıdır; yürütülmüş bir ürün deneyi değildir. Kontrollü karşılaştırma yapmadan tıklamadaki artışı doğrudan içerik kalitesine bağlama.

## ✅ Kendimi test

**S1:** Bir özellik başarıyı az artırıyor, ama sık bozulan bir servisten geliyor. Kararda ne eksik?

**C:** Kazancın gecikme, bakım ve hata maliyetleriyle karşılaştırılması.

**S2:** Modelin gösterdiği sonuçlar sonraki eğitimi etkiliyorsa ne araştırılır?

**C:** Geri besleme döngüsü ve modelin görünürlük etkisinin veriyle karışması.

## 🔑 Anahtar terimler

`feature cost` · `data dependency` · `feedback loop` · `versioning`

## Resmî tekrar

[Üretim ML sistemleri modül testi](https://developers.google.com/machine-learning/crash-course/production-ml-systems/test-your-knowledge), eğitim/çıkarım seçimlerini ve üretim sorunlarını tekrar etmek için kullanılabilir. Buradaki sorular ek çalışma sorularıdır; resmî testin cevap anahtarı değildir.
