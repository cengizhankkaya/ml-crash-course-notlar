# 7.1 Aktivasyon Fonksiyonları

> Kaynak: [MLCC — Aktivasyon fonksiyonları](https://developers.google.com/machine-learning/crash-course/neural-networks/activation-functions?hl=tr)

Aktivasyon, nöronun ağırlıklı toplamını dönüştürür: $h=f(w\cdot x+b)$. Gizli katmanlardaki doğrusal olmayan dönüşümler, ağın karmaşık karar sınırları kurabilmesini sağlar.

| Fonksiyon | Formül | Çıktı |
|---|---|---|
| Sigmoid | $1/(1+e^{-z})$ | $(0,1)$ |
| tanh | $\tanh(z)$ | $(-1,1)$ |
| ReLU | $\max(0,z)$ | $[0,\infty)$ |

Sigmoid ve tanh uçlarda doygunlaşır: girdi çok büyüdüğünde küçük değişiklikler çıktıyı az etkiler. Türevler küçülür ve derin ağlarda gradyan akışı zorlaşabilir. ReLU pozitif bölgede doğrusal, negatif bölgede sıfırdır. Hesabı basittir; ancak sürekli negatif kalan bir nöron öğrenmeyi durdurabilir.

Gizli katmanın aktivasyonu ile çıkışın aktivasyonu aynı olmak zorunda değildir. Çıkışı göreve göre seç: sınırsız bir sayısal tahmin için doğrusal çıkış, ikili olasılık için sigmoid, birbirini dışlayan sınıflar için softmax yaygın seçeneklerdir.

## Küçük hesap

$z=[-2,0,3]$ için ReLU çıktısı $[0,0,3]$ olur. Aynı girdilere sigmoid uygulanınca yaklaşık $[0.119,0.5,0.953]$ elde edilir. ReLU'nun çıktısı bir olasılık değildir: 3 değeri geçerlidir.

Bu depodaki örnek ağ, hesapları rahat izlemek için gizli katmanda tanh kullanır. Bu bir genel performans önerisi değildir. Aktivasyon seçimini yalnız eğitim kaybına göre değil, doğrulama performansı ve öğrenmenin kararlılığıyla birlikte değerlendirmek gerekir.

## ✅ Kendimi test

**S1:** ReLU uygulanan bir regresyon çıktısı negatif değer tahmin edebilir mi?

**C:** Hayır. Hedef negatif olabiliyorsa bu çıkış seçimi uygun olmayabilir.

**S2:** ReLU'nun bütün girdileri negatifse çıktıların aynı olması ağırlıkların aynı olduğunu gösterir mi?

**C:** Hayır. Farklı negatif toplamların hepsi sıfıra dönüşür; ara hesapları da incelemek gerekir.

## 🔑 Anahtar terimler
`activation` · `sigmoid` · `tanh` · `ReLU` · `saturation`

💻 Ek pekiştirme örneği: [ileri_geri_yayilim.py](../../kod/07-sinir-aglari/ileri_geri_yayilim.py)
