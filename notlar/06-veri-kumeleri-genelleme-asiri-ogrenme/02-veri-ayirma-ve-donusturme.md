# 6.2 Eğitim, Doğrulama, Test ve Veri Dönüşümü

> Kaynaklar: [MLCC — Veri kümesini ayırma](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets?hl=tr) · [Veri dönüştürme](https://developers.google.com/machine-learning/crash-course/overfitting/transforming-data?hl=tr)

| Bölüm | Görevi | Kullanım örneği |
|---|---|---|
| Eğitim (*train*) | Model parametrelerini öğrenmek | Ağırlıkları güncellemek |
| Doğrulama (*validation*) | Geliştirme kararlarını vermek | Öğrenme oranı veya model boyutu seçmek |
| Test | Seçim bittikten sonra değerlendirmek | Son modelin performansını raporlamak |

Test sonucuna tekrar tekrar bakıp ayar yapmak, testi dolaylı olarak geliştirme sürecine dahil eder. Doğrulama verisi de çok fazla karar için kullanıldığında aşırı uyuma açık hale gelir. Bölüm yüzdeleri evrensel değildir; temsil gücü, örnek bağımsızlığı ve yeterli örnek sayısı önemlidir.

## Aynı dönüşümü koru

Eğitimde öğrendiğin sözlük, medyan, ortalama ve standart sapmayı sakla. Doğrulama, test ve tahmin girdilerine bunları uygula. Her veri bölümünü kendi ortalamasıyla ölçeklemek modelin gördüğü anlamı değiştirir. Hem eğitim hem testte bulunan aynı kaydın kopyaları da değerlendirmeyi gereğinden iyi gösterebilir.

Çok büyük veriden alt küme seçerken hedef kullanımın temsilini koru. Ham kişisel tanımlayıcıları düşünmeden girdiye ekleme; veri hazırlığı, hangi bilginin gerçekten gerekli olduğuna karar vermeyi de içerir.

## Bu not için uygulama kuralı

Rastgele bölme her durumda uygun değildir. Aynı kişinin çok sayıda kaydı varsa grupları ayırmak; geleceği tahmin ediyorsan geçmişten geleceğe bir ayrım kullanmak, soruya daha uygun bir değerlendirme tasarımı olabilir. Bölümün hangi gerçek kullanım senaryosunu taklit ettiğini önce yaz.

Ek kodda bağımsız yapay satırlar ayrılır; eksik değer doldurma ve ölçekleme yalnız eğitim bölümünden öğrenilir. Bu küçük örneğin rastgele bölme tercihi, bütün projeler için reçete değildir.

**S1:** Doğrulama ortalamasının ölçeklemeden sonra tam sıfır çıkması şart mı?

**C:** Hayır. Eğitim ortalamasıyla dönüştürülür; kendi ortalaması sıfır olmak zorunda değildir.

**S2:** Aynı belgenin kopyaları hem eğitim hem testteyse sorun nedir?

**C:** Yeni belgeyi genelleme yerine önceden görülmüş içeriği hatırlama ölçülebilir.

## Anahtar terimler

`train` · `validation` · `test` · `data leakage` · `preprocessing` · `sampling`

---
💻 Ek pekiştirme örneği: [`veri_ayirma.py`](../../kod/06-veri-kumeleri-genelleme-asiri-ogrenme/veri_ayirma.py)
