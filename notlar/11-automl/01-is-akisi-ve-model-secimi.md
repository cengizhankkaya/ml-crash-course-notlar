# 11.1 AutoML İş Akışı ve Model Seçimi

> Kaynak: [MLCC — AutoML: Getting started](https://developers.google.com/machine-learning/crash-course/automl/getting-started)

## Araçtan önce kararlar

No-code araçlarda deneyler arayüzle, API/CLI araçlarında programatik olarak tanımlanır. Her ikisinde de iş akışı problem, veri, deney ayarları ve değerlendirmeyle başlar.

1. **Problemi tanımla:** Hangi çıktı tahmin edilecek ve ne zaman kullanılacak?
2. **Veriyi hazırla:** Etiketleri, eksikleri, biçimi ve kaynakların uyumunu incele.
3. **Türleri kontrol et:** Sayı olarak saklanan kategori kimliklerinin anlamını doğrula.
4. **Deneyi yapılandır:** Hedef, özellikler, model adayları ve seçim metriğini belirle.
5. **Sonuçları incele:** Metrikleri, özellik katkılarını ve sunulan mimari bilgilerini değerlendir.
6. **Gerekiyorsa yenile:** Veri kalitesi veya kullanım koşulu değiştiğinde tekrar değerlendir.

Aracın otomatik tür tahmini bir öneridir. Örneğin ürün kodu `1001` ile `1002` arasındaki fark bir büyüklük ilişkisi taşımıyorsa bu sütunu sürekli sayısal özellik gibi kullanmak yanıltıcı olabilir.

## Ek pekiştirme: küçük bir model araması

[model_secimi.py](../../kod/11-automl/model_secimi.py), oluşturulmuş sayısal veride birkaç polinom derecesini karşılaştırır. Tam bir AutoML ürünü değildir; yalnız **aday oluştur → eğit → doğrulamada seç → ayrılmış testte raporla** düzenini gösterir.

Model ağırlıkları eğitim bölümünde öğrenilir. Derece, doğrulama hatasıyla seçilir. Test bölümü, seçim tamamlandıktan sonra seçilen modelin son değerlendirmesinde kullanılır. Bu örnekte derece yükseldikçe eğitim hatası düşebilir; doğrulama hatasının da düşmesi garanti değildir.

Birçok adayı aynı doğrulama kümesine göre seçmek, zamanla o kümeye de uyum riskini artırır. Küçük kodun amacı bu riski çözmek değil, veri rollerini görünür kılmaktır. Resmî kursun bulut üzerinde yürütülmüş bir deneyinin çıktısı değildir.

## ✅ Kendimi test

**S1:** En düşük test hatalı adayı seçip aynı test hatasını son başarı diye sunmak uygun mu?

**C:** Hayır. Test kümesi seçime karışır; bağımsız son değerlendirme özelliğini kaybeder.

**S2:** Araç sütunu sayısal tanıdıysa bunu kabul etmek zorunda mıyız?

**C:** Hayır. Depolama türü ile özelliğin anlamsal türü farklı olabilir.

## 🔑 Anahtar terimler

`no-code` · `API` · `semantic type` · `validation` · `model selection`
