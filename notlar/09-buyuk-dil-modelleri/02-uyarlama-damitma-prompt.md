# 9.2 Fine-Tuning, Damıtma ve Prompt

> Kaynak: [MLCC — Fine-tuning, distillation ve prompt engineering](https://developers.google.com/machine-learning/crash-course/llm/tuning?hl=tr)

Önceden eğitilmiş modelden belirli bir görevde yararlanmanın birkaç yolu vardır:

| Yöntem | Ne değişir? | Amaç |
|---|---|---|
| Prompt düzenleme | Girdi talimatı ve örnekler | Mevcut yeteneği yönlendirmek |
| Fine-tuning | Eğitilebilir parametreler | Göreve uygun davranış öğrenmek |
| Damıtma | Öğretmenden öğrenen öğrenci model | Daha düşük maliyetli model elde etmek |

**Zero-shot** örneksiz, **one-shot** bir örnekli, **few-shot** birkaç örnekli yönlendirmedir. Prompt'a örnek koymak tek başına model ağırlıklarını güncellemez. Fine-tuning ise görev verisinden gradyanla öğrenir; standart biçiminde temel mimarinin parametre sayısını azaltmaz. Parametre verimli yöntemler yalnız sınırlı bir parametre kümesini eğitebilir.

Damıtmada öğretmenin etiketleri veya olasılıkları öğrenciye eğitim sinyali sağlar. Daha küçük öğrenci daha ucuz çalışabilir; kalite ve hız birlikte ölçülmelidir. Öğretmenin hataları ve yanlılıkları da aktarılabilir.

**Çevrimdışı çıkarım**, sonuçları önceden hesaplayıp saklamaktır. Gerçek zamanlı cevap gerektirmeyen işler için yararlıdır; modelin internetsiz çalışması anlamına gelmez.

## Ek uygulama düşüncesi

Destek mesajlarını `fatura`, `teslimat`, `diğer` diye ayıran bir sistem düşün. Önce açık talimat ve birkaç örnekle bir başlangıç sonucu ölç. Sonra uyarlama gerekiyorsa eğitim örneklerini ayrı tut ve bütün seçenekleri aynı ayrılmış değerlendirme kümesinde karşılaştır. Seçim ölçütlerine gecikme ve yanlış sınıflandırma maliyetini de ekle.

## ✅ Kendimi test

**S1:** Prompt'a on örnek eklemek fine-tuning midir?

**C:** Hayır; ağırlık güncellemesi yapılmıyorsa few-shot prompting'dir.

**S2:** Daha küçük öğrenci modeli her görevde öğretmenden daha kötü olmak zorunda mı?

**C:** Böyle bir mutlak kural yoktur. Hedef görev ve değerlendirme verisi üzerinde ölçüm gerekir.

## 🔑 Anahtar terimler
`fine-tuning` · `distillation` · `teacher/student` · `few-shot` · `offline inference`

## Resmî tekrar

[Modül sonu bilgi testi](https://developers.google.com/machine-learning/crash-course/llm/test-your-knowledge?hl=tr). Buradaki kendimi test soruları ek pekiştirme içindir; resmî sınavın cevap anahtarı değildir.
