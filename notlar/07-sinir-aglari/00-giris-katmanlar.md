# 7.0 Sinir Ağları: Düğümler ve Gizli Katmanlar

> Kaynaklar: [MLCC — Sinir ağları](https://developers.google.com/machine-learning/crash-course/neural-networks?hl=tr) · [Düğümler ve gizli katmanlar](https://developers.google.com/machine-learning/crash-course/neural-networks/nodes-hidden-layers?hl=tr)

Bir doğrusal model, özelliklerin ağırlıklı toplamından tahmin üretir. Bazı ilişkilerde tek çizgi veya düzlem yetmez. Sinir ağı, aradaki **gizli katmanlarla** yeni temsiller öğrenir; elle özellik çaprazı tasarlamaya bir alternatif sunar. Her problemde daha iyi sonuç vereceği garanti değildir.

Bir nöron önce $z=\sum_i w_i x_i+b$ hesaplar. Ağırlık ve bias eğitimde öğrenilen **parametrelerdir**. Katman sayısı ve katman genişliği ise seçtiğimiz **hiperparametrelerdir**. Giriş katmanı veriyi taşır, gizli katmanlar dönüştürür, çıkış katmanı görevin gerektirdiği tahmini üretir.

## Boyutları takip et

Satırlarda örneklerin tutulduğu küçük bir ağ düşün:

| Parça | Boyut | Anlam |
|---|---|---|
| $X$ | $(5,2)$ | Beş örnek, iki özellik |
| $W_1$ | $(2,3)$ | Üç gizli nörona bağlantı |
| $b_1$ | $(3,)$ | Her gizli nöron için bias |
| $H$ | $(5,3)$ | Gizli katman çıktısı |
| $W_2$ | $(3,1)$ | Tek çıktıya bağlantı |
| $\hat y$ | $(5,1)$ | Her örnek için tahmin |

Bu ağın parametre sayısı $(2\times3+3)+(3\times1+1)=13$ olur. Örnek sayısı değişince parametre sayısı değişmez; aynı ağırlıklar bütün örneklere uygulanır. Bias vektörü her satıra eklenir.

**Yalnız doğrusal katmanları üst üste koymak yeterli değildir:** $W_2(W_1x+b_1)+b_2$, yine tek bir doğrusal dönüşüm ve bias olarak yazılabilir. Doğrusal olmayan aktivasyonlar bu nedenle gerekir; sonraki not bunları ele alır.

## ✅ Kendimi test

**S1:** Yukarıdaki ağda mini batch 5 yerine 12 örnek içerirse $H$ nasıl değişir?

**C:** $(12,3)$ olur. Ağırlıkların boyutları aynı kalır.

**S2:** Üç gizli nöronu altıya çıkarınca ne değişir?

**C:** Model kapasitesi ve parametre sayısı artar; eğitim maliyeti ve aşırı öğrenme riski de değişebilir. Başarıyı doğrulama verisiyle değerlendirmek gerekir.

## 🔑 Anahtar terimler
`neuron` · `hidden layer` · `parameter` · `hyperparameter` · `forward pass`

💻 Ek pekiştirme örneği: [ileri_geri_yayilim.py](../../kod/07-sinir-aglari/ileri_geri_yayilim.py)
