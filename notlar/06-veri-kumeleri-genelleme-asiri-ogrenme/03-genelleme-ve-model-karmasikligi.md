# 6.3 Genelleme, Aşırı Öğrenme ve Model Karmaşıklığı

> Kaynaklar: [MLCC — Genelleme dersi](https://developers.google.com/machine-learning/crash-course/overfitting/generalization?hl=tr) · [Aşırı öğrenme](https://developers.google.com/machine-learning/crash-course/overfitting/overfitting?hl=tr) · [Model karmaşıklığı](https://developers.google.com/machine-learning/crash-course/overfitting/model-complexity?hl=tr)

**Genelleme**, modelin eğitim sırasında görmediği ilgili örneklerde de işe yaramasıdır. Eğitim hatası başarı hakkında tek başına yeterli bilgi vermez.

| Durum | Tipik belirti | İncelenecek yön |
|---|---|---|
| Eksik öğrenme (*underfitting*) | Eğitimde bile zayıf sonuç | Temsil, kapasite, eğitim ayarları |
| Aşırı öğrenme (*overfitting*) | Eğitim iyi, yeni veri belirgin kötü | Kapasite, veri kalitesi, düzenlileştirme |
| İyi genelleme | Ayrılmış ilgili veride de iyi sonuç | Kullanım sırasında izlemeyi sürdür |

Küçük, gürültülü veya hedef kullanımı temsil etmeyen eğitim verisi sorun yaratabilir. Fazla esnek model örneklerin tesadüfi ayrıntılarına uyabilir. Ancak “büyük model her zaman kötüdür” sonucu çıkarılmaz; gereken kapasite problem ve veri miktarına bağlıdır.

## Karmaşıklığı sınırlama

Basit bir başlangıç modeli, yeni özellik veya katmanın katkısını ölçmek için karşılaştırma sağlar. Amaç yalnız eğitim kaybını azaltmak değil, uygun bir temsil ve karmaşıklık düzeyi seçmektir. Düzenlileştirme, bu seçimde ağırlık büyüklükleri gibi ölçülere ceza ekleyebilir.

**İstatistiksel yanlılık (*bias*)**, modelin sistematik basitleştirme hatasıdır; denklemdeki sabit `b` parametresiyle aynı kavram değildir. **Varyans**, öğrenilen modelin farklı eğitim örneklemlerine duyarlılığıdır. Çok kısıtlı temsil yanlılığı, aşırı esnek temsil varyansı artırabilir.

## Genellemenin sınırı

Bağımsız ve aynı dağılımdan gelen örnekler, geliştirme değerlendirmesini yorumlamayı kolaylaştırır. Zamanla veri dağılımı değişirse eski test başarısı yeni kullanım için garanti değildir. Kayıp farkı görüldüğünde veri bölümlerinin özelliklerini de karşılaştır.

**S1:** Eğitim MSE'si 0.001, doğrulama MSE'si 8.0. Eğitim sonucuyla modeli seçer misin?

**C:** Hayır. Aşırı öğrenme, veri kayması veya veri hazırlama hatası araştırılmalı.

**S2:** Eğitim ve doğrulama kayıpları birbirine yakın ama çok yüksek. Bu iyi model mi?

**C:** Hayır; aradaki farkın küçük olması, mutlak hatanın kabul edilebilir olduğu anlamına gelmez.

## Anahtar terimler

`generalization` · `overfitting` · `underfitting` · `model complexity` · `bias` · `variance`

---
💻 Ek pekiştirme örneği: [`asiri_ogrenme_ve_l2.py`](../../kod/06-veri-kumeleri-genelleme-asiri-ogrenme/asiri_ogrenme_ve_l2.py)
