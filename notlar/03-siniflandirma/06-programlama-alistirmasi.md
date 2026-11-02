# 3.6 Sınıflandırma Programlama Alıştırması

> Kaynak: [MLCC — Classification programming exercise](https://developers.google.com/machine-learning/crash-course/classification/programming-exercise)

Resmî alıştırmada birbirine benzeyen iki pirinç türünü ayıran ikili sınıflandırıcı eğitilir ve ilgili başarı ölçütleri hesaplanır. Notebook bağlantısına kaynak sayfasından ulaşılabilir.

## Tekrar ederken izleyeceğim akış

1. Özellikleri, etiketi ve hangi sınıfın pozitif olduğunu belirle.
2. Eğitim ve değerlendirme ayrımını kontrol et. Dönüşümleri eğitim verisinden öğren.
3. Modelin olasılık çıktısı ile eşik sonrası sınıf kararını ayır.
4. Karışıklık matrisinden precision ve recall hesapla.
5. Eşiği değiştirince FP ve FN sayılarını karşılaştır. Son değerlendirme verisiyle eşik ayarı yapma.

## ✅ Kendimi test

**S:** Pozitif sınıfı değiştirirsem precision aynı kalır mı?

**C:** Genel olarak hayır; TP, FP ve FN tanımları değişir.

**S:** Eşik değişince modeli yeniden eğitmek gerekir mi?

**C:** Hayır; aynı olasılık tahminlerine farklı karar eşiği uygulanabilir.

Bu dosya tekrar özetidir. Kişisel Colab çıktısı paylaşılmadığından eğitim sonucu veya başarı puanı eklenmemiştir.

💻 Mevcut yerel tekrarlar: [metrikler.py](../../kod/03-siniflandirma/metrikler.py) · [roc_auc.py](../../kod/03-siniflandirma/roc_auc.py)
