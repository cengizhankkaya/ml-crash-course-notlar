# 6.1 Sınıfları Dengesiz Veri Kümeleri

> Kaynak: [MLCC — Dengesiz veri kümeleri](https://developers.google.com/machine-learning/crash-course/overfitting/imbalanced-datasets?hl=tr)

Bir sınıf çok azsa yüksek doğruluk yanıltıcı olabilir. Ayrıca küçük eğitim gruplarında nadir sınıftan hiç örnek bulunmayabilir. Modelin sınıfları ayırmayı öğrenmesiyle gerçek dünyadaki görülme oranını öğrenmesi farklı ihtiyaçlardır.

## Azalt ve ağırlıklandır

Kurstaki yöntem, çoğunluk sınıfını **alt örneklemek** ve seçilen çoğunluk örneklerinin kaybını seçim olasılığının tersiyle ağırlıklandırmaktır. Çoğunluğun `1/k` kadarı tutulursa kalan çoğunluk örneklerinin ağırlığı `k` olur. Bu, eğitimde daha dengeli gruplar görürken asıl dağılımın kayıptaki etkisini yaklaşık korumaya çalışır.

Azınlığa daha yüksek hata maliyeti atamak ise başka bir amaç olabilir; aynı işlem değildir. Örnekleme oranı ve hata maliyeti birbirine karıştırılmamalıdır.

## Bu nota ait hesap

Veride 900 negatif, 100 pozitif örnek olsun. Negatiflerin onda birini tutarsak 90 negatif ve 100 pozitif kalır. Negatiflere 10, pozitiflere 1 ağırlık verildiğinde temsil edilen toplam ağırlıklar yeniden 900 ve 100 olur. Bunun, seçilen 90 kaydın silinen bütün örnekleri kusursuz temsil ettiğini garanti etmediğini unutma.

Değerlendirme verisini, hizmet verilecek dağılımı temsil edecek şekilde koru. Kesinlik, geri çağırma ve hataların maliyetini de incele; oran değişirse bu ölçülerin yorumu değişebilir.

## Küçük kontrol

**S1:** 5.000 örneğin 50'si pozitif. Hep negatif diyen modelin doğruluğu ve geri çağırması?

**C:** Doğruluk `%99`, pozitif geri çağırma `0`.

**S2:** Çoğunluk örnekleri `1/4` olasılıkla tutuldu. Dağılımı kayıpta temsil etmek için ağırlıkları ne olmalı?

**C:** Tutulan çoğunluk örnekleri için 4; diğerleri aynı bırakılır.

## Anahtar terimler

`class imbalance` · `majority class` · `minority class` · `downsampling` · `upweighting`

---
💻 Ağırlık hesabını gösteren ek örnek: [`veri_ayirma.py`](../../kod/06-veri-kumeleri-genelleme-asiri-ogrenme/veri_ayirma.py)
