# 1.2b Etkileşimli Alıştırma: Parametreler

> Kaynak: [ML Crash Course — Doğrusal regresyon: Parametre alıştırması](https://developers.google.com/machine-learning/crash-course/linear-regression/parameters-exercise?hl=tr) · ⏱️ ~5 dk

## Görev
Grafikte yakıt verimliliği veri kümesinden **20 örnek** var:
- **x ekseni (özellik):** Araba ağırlığı (bin pound)
- **y ekseni (etiket):** Mil/galon

**Ağırlık (w)** ve **Önyargı / yanlılık (b)** kaydırıcılarını elle ayarlayarak **MSE kaybını en aza indiren** doğrusal modeli bulmak.

### Sorular
1. Elde edebileceğin en düşük MSE nedir?
2. Bu kaybı hangi ağırlık ve önyargı değerleri verdi?

## Kurstaki çözüm
| | Değer |
|---|---|
| En düşük **MSE** | **3.37** |
| **Ağırlık (w)** | **−0.12** |
| **Önyargı (b)** | **16.96** |

$$y' = 16.96 - 0.12 \cdot x$$

> 📝 Bu değerler, [1.1 Giriş](01-giris.md)'teki 7 noktalı örneğin modelinden (`y' = 34 − 4.6x`) çok farklı. Çünkü bu alıştırma **başka 20 örnek** kullanıyor; en iyi w ve b her zaman **o veri kümesine özgüdür**.

## Benim denemem
| Deneme | Ağırlık | Önyargı | MSE |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| En iyim | | | |

## Bu alıştırmadan çıkan dersler
- Kaydırıcıları elle oynatmak aslında **gradyan inişinin yaptığı işi elle yapmak**: Bir parametreyi değiştir, kayba bak, kayıp azalıyorsa o yönde devam et.
- **Ağırlık** doğrunun **eğimini**, **önyargı** ise doğrunun **yukarı-aşağı konumunu** değiştirir.
- İki parametreyi aynı anda ayarlamak zor: biri değişince diğerinin en iyi değeri de değişir. Parametre sayısı arttıkça elle bulmak imkânsızlaşır, bu yüzden otomatik bir yönteme ihtiyaç var → [1.3 Gradyan inişi](03-gradyan-inisi.md).
- En düşük MSE **0 değil** (3.37). Noktalar tam bir doğru üzerinde olmadığı için hiçbir doğru hepsinden geçemez.

## 🔑 Anahtar terimler
`weight` · `bias` · `MSE` · `parameter`
