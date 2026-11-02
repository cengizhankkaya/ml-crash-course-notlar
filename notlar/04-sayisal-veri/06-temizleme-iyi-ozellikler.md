# 4.6 Veri Temizleme ve İyi Sayısal Özellikler

> Kaynaklar: [MLCC — Scrubbing](https://developers.google.com/machine-learning/crash-course/numerical-data/scrubbing) · [Qualities of good numerical features](https://developers.google.com/machine-learning/crash-course/numerical-data/qualities-of-good-numerical-features)

Veri temizleme, eksik değerleri, yinelenen kayıtları, geçersiz aralıkları ve hatalı etiketleri belirleyip uygun işlem yapmaktır. Türkçe kaynakta görülen “ileri geri oynatma” başlığı burada **veri temizleme** anlamına gelir.

| Sorun | Kontrol | Olası işlem |
|---|---|---|
| Eksik ölçüm | Eksiklik sayısı ve veri kaynağı | Gerekçeli doldurma veya kaydı ayırma |
| Aynı olayın kopyası | Olay kimliği ve zaman | Gerçek kopyayı kaldırma |
| İmkânsız değer | Birim ve geçerli aralık | Kaynaktan düzeltme veya çıkarma |
| Tutarsız etiket | Etiketleme ölçütleri | Yeniden inceleme |

Gerçek fakat nadir bir gözlem otomatik olarak hata değildir. Tekrarlanan bir değer de tek başına yinelenmiş kayıt anlamına gelmez.

## Anlaşılır özellikler

`sure` yerine `sure_saniye` gibi açık adlar kullan. Eksik süreyi `-999` gibi gerçek sayıymış gibi sunma. Ayrı bir `sure_eksik` göstergesi ve uygun doldurma değeri kullanabilirsin. Medyan gibi doldurma istatistikleri yalnız eğitim verisinden hesaplanır.

Örneğin eğitim değerleri `[2, 4, 6, eksik]` ise medyan `4` olur. Eksik satır `[sure=4, sure_eksik=1]` ile, gerçekten 4 ölçülen satır `[4, 0]` ile gösterilir. Üretimde de aynı dönüşüm uygulanır.

## ✅ Kendimi test

**S:** Çok yüksek bir ölçümü hemen silmeli miyim?

**C:** Önce hata mı, geçerli uç değer mi olduğunu araştırmalıyım.

**S:** Eksikliği 0 ile doldurmak yeterli mi?

**C:** Gerçek sıfırla eksik ölçüm karışabilir; ayrı gösterge yararlı olabilir.

## 🔑 Anahtar terimler

`data cleaning` · `scrubbing` · `imputation` · `missing indicator` · `duplicate`

💻 Ek tekrar örneği: [veri_donusumleri.py](../../kod/04-sayisal-veri/veri_donusumleri.py)
