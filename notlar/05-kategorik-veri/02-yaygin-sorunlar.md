# 5.2 Kategorik Veride Yaygın Sorunlar

> Kaynak: [MLCC — Kategorik veride yaygın sorunlar](https://developers.google.com/machine-learning/crash-course/categorical-data/issues?hl=tr)

Bir kategorinin adı kadar, **onu kimin ve hangi kuralla atadığı** da önemlidir. İnsanların atadığı etiketlere bazen *gold*, modellerin atadıklarına *silver* denir. Bu adlar doğruluk garantisi değildir. İnsanlar hata yapabilir; otomatik etiketleme de önceki modelin hatalarını yeni eğitim verisine taşıyabilir.

## Etiketleme kalitesini incele

- Aynı örneği birden fazla değerlendiriciye ver; uyuşmazlığın hangi örneklerde toplandığını incele.
- Etiket tanımlarını ve sınırda kalan örnekleri açıklığa kavuştur.
- Otomatik etiketlerde yalnız toplam doğruluğa değil, düzenli hata örüntülerine de bak.
- Çok sayıda kategori, temsil boyutunu ve öğrenme maliyetini artırır.

**Değerlendiriciler arası uyum**, insanların aynı örnek için ne kadar benzer karar verdiğini ölçer. Yüksek uyum tek başına doğruluğu kanıtlamaz: herkes aynı eksik talimatı takip ediyor olabilir.

## Bu not için örnek

Destek mesajlarını `hata`, `istek`, `diğer` diye ayırdığımızı düşün. “Arama sonuçlarını dışa aktaramıyorum” mesajı bir değerlendiriciye göre hata, diğerine göre eksik özellik olabilir. Çözüm, rastgele birini doğru kabul etmek yerine mevcut davranışı ve etiketleme kuralını birlikte incelemektir. Gerekirse “mevcut özellik çalışmıyor” ile “yeni özellik isteniyor” ayrımı yazılır.

## Küçük kontrol

**S1:** İki değerlendirici 50 mesajın 40'ında anlaşıyor. Ham uyum nedir?

**C:** `40/50 = %80`. Şansla oluşan uyumu hesaba katan ölçüler bundan farklıdır.

**S2:** Bir model binlerce örneği hızla etiketledi. Bunlar denetlenmeden doğru kabul edilebilir mi?

**C:** Hayır. Özellikle belirli kelimelerde, gruplarda veya sınırlarda sistematik hata bulunabilir.

## Anahtar terimler

`human rater` · `gold labels` · `silver labels` · `inter-rater agreement` · `high dimensionality`

---
💻 Kategori temsillerini incelemek için ek örnek: [`kodlama_ve_caprazlama.py`](../../kod/05-kategorik-veri/kodlama_ve_caprazlama.py)
