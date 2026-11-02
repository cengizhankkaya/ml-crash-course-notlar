# 7.2 Geri Yayılım ve Eğitim

> Kaynaklar: [MLCC — Geri yayılım](https://developers.google.com/machine-learning/crash-course/neural-networks/backpropagation?hl=tr) · [Etkileşimli alıştırmalar](https://developers.google.com/machine-learning/crash-course/neural-networks/interactive-exercises?hl=tr)

Eğitimde dört ayrı iş vardır:

1. **İleri geçiş:** Mevcut parametrelerle tahmin hesaplanır.
2. **Kayıp:** Tahmin ile hedef arasındaki fark ölçülür.
3. **Geri yayılım:** Zincir kuralıyla kaybın her parametreye türevi hesaplanır.
4. **Güncelleme:** Optimizer parametreleri değiştirir; basit gradyan inişinde $w\leftarrow w-\eta\,\partial L/\partial w$.

Geri yayılım gradyanı hesaplar; optimizer bu gradyanla nasıl adım atılacağını belirler. Çıkarımda genellikle yalnız ileri geçiş yapılır.

## Eğitim neden bozulabilir?

| Belirti | Olası neden | İncelenecek nokta |
|---|---|---|
| İlk katmanlar çok yavaş öğreniyor | Kaybolan gradyan | Aktivasyonlar ve gradyan büyüklükleri |
| Kayıp sıçrıyor veya sonlu değil | Patlayan gradyan | Öğrenme oranı, ölçekler, başlangıç |
| ReLU nöronu hep sıfır | Ölü ReLU | Negatif ön aktivasyonlar, öğrenme oranı |
| Eğitim iyi, doğrulama kötü | Aşırı öğrenme | Kapasite, veri, düzenlileştirme |

**Dropout**, eğitim sırasında bazı aktivasyonları rastgele devre dışı bırakan bir düzenlileştirmedir. Oranı arttırmak daha güçlü düzenlileştirme yapar; aşırısı öğrenmeyi engeller. Değerlendirme sırasında standart dropout kapatılır; eğitimde kullanılan ölçekleme buna göre düzenlenir.

## Ek pekiştirme deneyi

Aşağıdaki NumPy örneği, XOR tablosunda tanh ağı eğitir. Türevlerden birini sonlu farkla kontrol eder: bir ağırlığı çok az artırıp azaltarak kayıptaki değişimi ölçer. Bu, zincir kuralı uygulamasını denetler; bütün model doğruluğunun kanıtı değildir.

Dört satırı öğrenmek **genelleme başarısı** olarak raporlanmaz. Amaç eğitim döngüsünü görünür kılmaktır. Öğrenme oranını değiştirirken diğer ayarları sabit tut; başlangıç ve son kaybı karşılaştır.

## ✅ Kendimi test

**S1:** Gradyan hesaplamak ağırlıkları kendiliğinden değiştirir mi?

**C:** Hayır; ayrıca güncelleme adımı gerekir.

**S2:** Eğitim kaybı azalırken doğrulama kaybı artıyorsa daha çok epoch her zaman iyi midir?

**C:** Hayır. Aşırı öğrenme başlamış olabilir; erken durdurma veya düzenlileştirme değerlendirilebilir.

## 🔑 Anahtar terimler
`backpropagation` · `chain rule` · `optimizer` · `dropout` · `vanishing gradient`

💻 Ek pekiştirme örneği: [ileri_geri_yayilim.py](../../kod/07-sinir-aglari/ileri_geri_yayilim.py)
