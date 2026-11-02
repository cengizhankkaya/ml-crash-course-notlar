# 1.4b Gradyan İnişi Alıştırması

> Kaynak: [MLCC — Gradient descent exercise](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent-exercise)

Bu etkileşimli ders, öğrenme oranının ağırlık ve bias güncellemelerine etkisini gösterir.

## Hatırlanacak ilişki

$$w_{yeni}=w_{eski}-\eta\frac{\partial L}{\partial w}$$

- Çok küçük `η`: Küçük adımlar; yakınsama yavaş olabilir.
- Uygun `η`: Kayıp düşüp kararlı bir bölgeye ulaşabilir.
- Çok büyük `η`: Minimumun üzerinden atlama, salınım veya ıraksama görülebilir.

Karşılaştırırken başlangıç değerlerini ve veriyi aynı tut. Tek bir kayıp değerine değil, adımlar boyunca değişime bak. Yakınsama süresi veri, ölçek, öğrenme oranı ve uygulamaya bağlıdır.

**Kendimi test:** Kayıp düşüyor ama çok yavaşsa ilk inceleyeceğim şey nedir?

**Cevap:** Öğrenme oranı ve özellik ölçekleri. Oranı artırmanın sonucu ayrıca gözlenmelidir.

Bu özet kişisel etkileşim kaydını veya ölçülmüş yakınsama süresini içermez.

💻 Mevcut yerel tekrar: [gradyan_inisi.py](../../kod/01-dogrusal-regresyon/gradyan_inisi.py)
