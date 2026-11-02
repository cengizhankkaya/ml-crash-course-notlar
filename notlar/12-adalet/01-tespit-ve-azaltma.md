# 12.1 Yanlılığı Tespit Etme ve Azaltma

> Kaynaklar: [MLCC — Identifying bias](https://developers.google.com/machine-learning/crash-course/fairness/identifying-bias) · [Mitigating bias](https://developers.google.com/machine-learning/crash-course/fairness/mitigating-bias)

## Veride nerelere bakılır?

Eksik değerlerin yalnız toplam oranını sayma; hangi gruplarda yoğunlaştığını incele. Beklenmedik değerler birim, toplama veya etiketleme sorunu gösterebilir. Bir grubun az temsil edilmesi, o gruba ait hataların toplam metrikte kaybolmasına neden olabilir.

Bir özelliğin adı hassas görünmese bile başka bir özelliğe **vekil (proxy)** olabilir. Konum, dil veya kullanılan cihaz, farklı kullanıcı gruplarıyla ilişkili olabilir. Hassas sütunu silmek bütün ilişkiyi ortadan kaldırmaz.

## Müdahale yolları

**Veriyi iyileştirme:** Eksik temsil edilen koşulları kapsayan, daha doğru etiketli örnekler toplamak. Aynı bozuk örüntüden daha çok veri eklemek yeterli olmayabilir. Yeni verinin hangi sorunu giderdiği açık olmalıdır.

**Eğitim hedefini düzenleme:** Kayıp işlevine, seçilen adalet amacını destekleyen ceza terimleri eklenebilir. Kursun iki örneği:

- **MinDiff:** Belirlenen veri dilimleri arasında tahmin dağılımı farklarını azaltan ceza.
- **Counterfactual Logit Pairing (CLP):** İlgili özellikleri aynı, hassas niteliği farklı eşlenmiş örneklerin skor farkını cezalandırma.

Veri iyileştirme ve eğitim müdahalesi birlikte kullanılabilir. Bir yöntemin adı, tüm gruplarda ve bütün adalet tanımlarında garanti vermez; sonuç tekrar ölçülür.

## Ek çalışma örneği

Sesli komut veri kümesinde A koşulunda 900, B koşulunda 100 kayıt olsun. Gürültü etiketi B kayıtlarının çoğunda eksikse, toplam eksiklik oranı sorunun yerini gizleyebilir. Önce grup bazında eksikliği ve kayıt kalitesini karşılaştır. B grubuna ait aynı 100 kaydı çoğaltmak yeni ses çeşitliliği sağlamaz; hangi çeşitliliğin eksik olduğunu belirlemek gerekir.

## ✅ Kendimi test

**S1:** Hassas grup sütununu kaldırmak adaleti garanti eder mi?

**C:** Hayır. Diğer özellikler vekil olabilir; ayrıca grup bazında denetim hâlâ gereklidir.

**S2:** MinDiff ile CLP aynı şeyi mi karşılaştırır?

**C:** Hayır. İlki dilim dağılımlarına, ikincisi eşlenmiş bireysel örneklerin skorlarına odaklanır.

## 🔑 Anahtar terimler

`missingness` · `data skew` · `proxy` · `MinDiff` · `Counterfactual Logit Pairing`
