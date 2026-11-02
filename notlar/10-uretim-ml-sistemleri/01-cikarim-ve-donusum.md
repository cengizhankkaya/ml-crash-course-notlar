# 10.1 Çıkarım ve Veri Dönüşümü

> Kaynaklar: [MLCC — Statik/dinamik çıkarım](https://developers.google.com/machine-learning/crash-course/production-ml-systems/static-vs-dynamic-inference) · [Veriyi ne zaman dönüştürmeli?](https://developers.google.com/machine-learning/crash-course/production-ml-systems/transforming-data)

**Çıkarım (inference)**, eğitilmiş ağırlıklarla yeni bir örnek için tahmin üretmektir. Eğitimde ağırlıklar öğrenilir; çıkarımda genellikle sabittir.

## Önceden hesaplamak mı, istekte hesaplamak mı?

| | Statik / batch çıkarım | Dinamik / online çıkarım |
|---|---|---|
| Ne zaman? | Tahminler önceden hesaplanır ve saklanır. | İstek geldiğinde hesaplanır. |
| Güçlü yanı | Hazır tahmine hızlı erişim; yayımdan önce kontrol. | Yeni ve nadir girdilere cevap; güncel bağlam kullanımı. |
| Bedeli | Saklama, yenileme gecikmesi, kapsanmayan girdiler. | İstek gecikmesi, hesaplama kapasitesi, yoğun izleme. |

Örneğin gecelik sabit ürün listesi için puanlar önceden hazırlanabilir. Kullanıcının o anda yazdığı serbest metnin tüm olası biçimlerini önceden hesaplamak ise uygulanabilir değildir. Eğitim sıklığı ile çıkarım biçimini ayrı seç: haftalık eğitilen bir model isteklere gerçek zamanlı cevap verebilir.

## Dönüşüm aynı kalmalı

Özellikler eğitimden önce hesaplanıp saklanabilir veya model akışında dönüştürülebilir. İlk yaklaşım tekrarlanan işi azaltır; ikincisi dönüşümün eğitimde ve sunumda ortak tutulmasını kolaylaştırır. Pahalı dönüşümler servis gecikmesini artırabilir.

**Training-serving skew**, eğitim ile sunumun veri veya dönüşüm bakımından ayrışmasıdır. Z-puanı için eğitimde öğrenilen `μ` ve `σ` saklanıp sunumda tekrar kullanılır. Her gelen istekte yeni ortalama hesaplamak aynı sayıların farklı anlamlara gelmesine neden olur. Kategori sırası, birimler, eksik değer kuralları da aynı olmalıdır.

## Ek çalışma örneği

Eğitim ortalaması 100, standart sapması 20 ise 120 değeri `z=1` olur. Sunumda yanlışlıkla ortalama 80 kullanılırsa `z=2` çıkar. Aynı ham kayıt farklı tahmine dönüşebilir. Aşağıdaki küçük kod bunu gösterir; gerçek bir servis kurulumu değildir.

## ✅ Kendimi test

**S1:** Statik çıkarımın güncel veriye tepki vermesi neden gecikebilir?

**C:** Saklanmış tahminlerin yeniden hesaplanması ve yayımlanması gerekir.

**S2:** Bir isteği kendi ortalamasıyla ölçeklemek doğru mu?

**C:** Eğitimdeki dönüşümün anlamını bozabilir; eğitimden saklanan istatistikler kullanılmalıdır.

## 🔑 Anahtar terimler

`inference` · `batch inference` · `online inference` · `training-serving skew`

💻 Ek pekiştirme kodu: [egitim_sunum_farki.py](../../kod/10-uretim-ml-sistemleri/egitim_sunum_farki.py)
