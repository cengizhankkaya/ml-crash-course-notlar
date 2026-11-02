# 6.0 Veri Özellikleri, Kalite ve Etiketler

> Kaynaklar: [MLCC — Veri özellikleri](https://developers.google.com/machine-learning/crash-course/overfitting/data-characteristics?hl=tr) · [Etiketler](https://developers.google.com/machine-learning/crash-course/overfitting/labels?hl=tr)

Veri kümesini yalnız satır sayısıyla değerlendirme. **Tür, miktar, kalite/güvenilirlik ve eksiksizlik** birlikte önemlidir. Sayısal ölçüm, kategori, metin, görüntü ve başka bir modelin çıktısı farklı hazırlık gerektirir.

## Kalite kontrolü

Eksik değer, yinelenmiş kayıt, yanlış özellik, yanlış etiket ve belirli bir zaman dilimindeki bozuk kayıtlar farklı sorunlardır. Örneğin sensörün yalnız bir gün yanlış birimle kayıt tutması, bütün sütunun ortalamasında gizlenebilir.

Eksik kayıtlar silinebilir veya değerleri doldurulabilir (**imputation**). Silmek belirli grupları sistematik olarak dışarıda bırakabilir; doldurmak ise gözlemlenmemiş bir değeri tahmin eder. Ortalama/medyan gibi istatistikler eğitim verisinden öğrenilmeli, aynı dönüşüm diğer bölümlere uygulanmalıdır. Ek bir `deger_eksikti` özelliği, gözlenen ve doldurulan değerleri ayırabilir.

## Hedefi doğru tarif et

| Etiket | Anlamı | Bu nota ait örnek |
|---|---|---|
| Doğrudan | Tahmin etmek istediğimiz olay | Paketin gerçekten gecikmesi |
| Vekil (*proxy*) | Olayla ilişkili dolaylı işaret | Müşterinin gecikme şikâyeti açması |

Şikâyet açılmaması, paketin zamanında geldiğini kanıtlamaz. Vekil hedef çok iyi tahmin edilse bile asıl amaç kaçırılabilir. İnsan etiketlerinde açık yönerge, birden fazla değerlendirme ve uyuşmazlık incelemesi yararlıdır; insan veya model etiketi otomatik olarak güvenilir değildir.

## Ek düşünme alıştırması

Bir kargo tablosunda mesafe, gönderim saati ve teslimat sonucu var. Eksik mesafenin yalnız belirli bir şubede görüldüğünü varsay. Bütün eksik satırları silmeden önce şubenin kalan veride temsil edilip edilmediğini kontrol et. Sonuç etiketini doldurmakla bir giriş özelliğini doldurmanın aynı karar olmadığını da not et.

**S1:** Doğrulama verisinin medyanıyla eğitimdeki eksikleri doldurmak uygun mu?

**C:** Hayır; geliştirme verisine ayrılmış değerlendirme bilgisini taşır.

**S2:** “Şikâyet yok” neden doğrudan memnuniyet etiketi değildir?

**C:** Memnun olmayan kullanıcı şikâyet etmeyebilir; ölçülen davranış hedef kavramdan farklıdır.

## Anahtar terimler

`dataset` · `data quality` · `imputation` · `direct label` · `proxy label` · `duplicate`

---
💻 Ek pekiştirme örneği: [`veri_ayirma.py`](../../kod/06-veri-kumeleri-genelleme-asiri-ogrenme/veri_ayirma.py)
