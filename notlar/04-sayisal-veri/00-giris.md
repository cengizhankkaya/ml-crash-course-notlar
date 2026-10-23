# 4.0 Sayısal Verilerle Çalışma: Modüle Giriş

> Kaynak: [ML Crash Course — Sayısal verilerle çalışma](https://developers.google.com/machine-learning/crash-course/numerical-data?hl=tr) · ⏱️ Modül: ~85 dk

## Bu modülde ne öğreneceğim?
- **Özellik vektörlerini** anlamayı
- Veri kümesindeki olası özellikleri **görsel ve matematiksel** olarak keşfetmeyi
- **Aykırı değerleri** bulmayı
- Sayısal verileri **normalleştirmenin** dört farklı tekniğini
- **Gruplandırmayı (binning)** ve sayısal verileri gruplandırma stratejilerini
- **İyi sürekli sayısal özelliklerin** niteliklerini

Ön koşul: Makine öğrenimine giriş

## Neden veriye üç ünite?
ML uygulayıcıları zamanlarının çoğunu **model kurmaya değil**, veriyi **değerlendirmeye, temizlemeye ve dönüştürmeye** harcar. Bu yüzden kursta veriye üç ünite ayrılmış:

1. **Sayısal verilerle çalışma** ← bu ünite
2. Kategorik verilerle çalışma
3. Veri kümeleri, genelleme ve aşırı uyum

## Sayısal veri nedir?
**Sayı gibi davranan** tam sayı ya da ondalıklı değerler: **toplanabilir, sayılabilir, sıralanabilir**, oranları anlamlıdır.

| Sayısal ✅ | Neden? |
|---|---|
| Sıcaklık | Ortalaması, farkı anlamlı |
| Ağırlık | 2 kg, 1 kg'ın iki katı |
| Bir koruma alanında kışlayan geyik sayısı | 240 geyik, 120 geyiğin gerçekten iki katı |

### Sayı gibi görünen her şey sayısal değildir
**ABD posta kodları** 5 ya da 9 haneli sayılardır, ama **sayı gibi davranmaz**:
- **40004** (Nelson County, Kentucky), **20002**'nin (Washington, D.C.) **iki katı değildir**.
- Bu numaralar **coğrafi bölgeleri** temsil eder, yani **kategorik veridir**.

Kodla gösterdim:

| İşlem | Sonuç | Anlamlı mı? |
|---|---|---|
| 240 geyik / 120 geyik | 2 kat | ✅ Gerçekten 2 kat fazla geyik |
| 40004 / 20002 | 2 | ❌ Bir bölge diğerinin "2 katı" olamaz |
| Ortalama posta kodu | 23336 | ❌ Hiçbir yere karşılık gelmiyor |

> 💡 Kural: **Sayılar üzerinde yaptığın matematiğin gerçek dünyada bir anlamı varsa** veri sayısaldır. Yoksa (posta kodu, telefon numarası, ürün kodu…) kategoriktir, sadece sayıyla **etiketlenmiştir**.

## 🔑 Anahtar terimler
`numerical data` · `categorical data` · `feature vector` · `normalization` · `binning` · `outlier`

---
💻 İlgili kod: [`sayisal_mi_kategorik_mi.py`](../../kod/04-sayisal-veri/sayisal_mi_kategorik_mi.py)
