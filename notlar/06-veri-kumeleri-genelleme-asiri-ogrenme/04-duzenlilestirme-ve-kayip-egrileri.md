# 6.4 L2, Erken Durdurma ve Kayıp Eğrileri

> Kaynaklar: [MLCC — L2 düzenlileştirme](https://developers.google.com/machine-learning/crash-course/overfitting/regularization?hl=tr) · [Kayıp eğrilerini yorumlama](https://developers.google.com/machine-learning/crash-course/overfitting/interpreting-loss-curves?hl=tr)

L2 düzenlileştirme, veri kaybına ağırlıkların kareleri toplamını ekler:

$$J(w)=L_{veri}(w)+\lambda\sum_j w_j^2$$

`λ`, cezanın gücünü belirleyen hiperparametredir. `λ=0` bu cezayı kaldırır; çok büyük değerler modelin gerekli ilişkiyi öğrenmesini engelleyebilir. L2 genel olarak ağırlıkları küçültür; L1'deki gibi seyrek ağırlıklar üretmeyi hedeflemez. Sabit terim çoğu uygulamada bu cezanın dışında bırakılır; kullanılan tanımı kontrol et.

`w=[2,-3]`, `λ=0.1` için ek ceza `0.1×(4+9)=1.3` olur. Modelin veri kaybı `0.4` ise toplam amaç `1.7`dir. **Veri kaybıyla ceza dahil eğitim amacını karıştırma.** Farklı `λ` değerlerini karşılaştırırken doğrulama performansına bak.

## Erken durdurma

Eğitim sürerken doğrulama kaybı iyileşmeyi bırakırsa durdurma düşünülebilir. Pratikte tek gürültülü noktaya tepki vermek yerine sabır aralığı (*patience*) kullanılır ve en iyi doğrulama adımındaki ağırlıklar geri yüklenir. Test verisi durdurma kararını vermez.

## Eğriyi ipucu olarak oku

| Gözlem | Olası açıklama / kontrol |
|---|---|
| Eğitim azalıyor, doğrulama yükseliyor | Aşırı öğrenme; kapasite ve düzenlileştirmeyi incele |
| Kayıp sert dalgalanıyor | Öğrenme oranı, grup bileşimi, bozuk örnekler |
| Ani sıçrama veya sonlu olmayan sonuç | NaN/sonsuz girdiler, taşma, aşırı değerler |
| Tekrarlayan dalga örüntüsü | Sıralı gruplar ve yetersiz karıştırma |
| İki eğri de yüksek ve düz | Eksik öğrenme veya optimizasyon sorunu |

Bir eğri tek başına nedeni kanıtlamaz. Küçük ve güvenilir veriyle denemek, hatanın veri mi eğitim akışı mı olduğunu ayırmaya yardımcı olabilir. Önce karşılaştırılan kayıpların aynı tanım ve ölçeğe sahip olduğunu doğrula.

**S1:** Doğrulama en düşük kaybına 12. dönemde ulaştı; son dönem 20. Hangi ağırlıklar tercih edilir?

**C:** Erken durdurma tasarımında 12. dönemde kaydedilenler.

**S2:** L2 ekleyince eğitim veri kaybı arttı, doğrulama kaybı azaldı. Çelişki mi?

**C:** Hayır. Eğitim örneklerine daha az uyum, yeni veride daha iyi sonuç verebilir.

## Anahtar terimler

`L2 regularization` · `lambda` · `early stopping` · `patience` · `loss curve` · `convergence`

## Resmî tekrar bağlantısı

[Veri kümeleri, genelleme ve aşırı öğrenme: Modül sonu bilgi testi](https://developers.google.com/machine-learning/crash-course/overfitting/test-your-knowledge?hl=tr). Bu nottaki sorular bağımsız pekiştirme içindir; resmî testin cevap anahtarı değildir.

---
💻 Ek pekiştirme örneği: [`asiri_ogrenme_ve_l2.py`](../../kod/06-veri-kumeleri-genelleme-asiri-ogrenme/asiri_ogrenme_ve_l2.py)
