# 1.5 Programlama Alıştırması: Chicago Taksi Ücreti

> Kaynak: [ML Crash Course — Programlama alıştırması](https://developers.google.com/machine-learning/crash-course/linear-regression/programming-exercise?hl=tr) · [Kursun Colab'ı](https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/linear_regression_taxi.ipynb) · ⏱️ ~20 dk

📓 **Benim notebook'um:** [`taksi_ucreti.ipynb`](../../kod/01-dogrusal-regresyon/taksi_ucreti.ipynb) · [![Colab'da aç](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/cengizhankkaya/ml-crash-course-notlar/blob/main/kod/01-dogrusal-regresyon/taksi_ucreti.ipynb)

> ⚠️ **Colab'da tarayıcı çevirisini kapat!** Çeviri açıkken kod da Türkçeye çevriliyor: `pip install` → `pip yükleme`, `pandas` → `pandalar`, `tensorflow` → `tensor akışı`, `learning_rate=0.001` → `öğrenme_oranı = 0,001`. Hücreler bu yüzden hata verir. Metni Türkçe okumak istersen çeviriyi yalnızca okurken aç, kodu çalıştırmadan önce kapat.

## Amaç
Gerçek bir veri kümesiyle (Chicago'da Mayıs 2022'den iki günlük taksi yolculukları) **taksi ücretini (FARE)** tahmin eden doğrusal regresyon modeli eğitmek.

### Öğrenme hedefleri
- `.csv` dosyasını **pandas DataFrame**'e okumak
- Veriyi görselleştirme kütüphaneleriyle **keşfetmek**
- Farklı **özelliklerle** model denemek
- **Hiperparametreleri** ayarlamak
- Eğitimleri **RMSE** ve **kayıp eğrileriyle** karşılaştırmak

## Kullanılan araçlar
| Araç | Ne işe yarıyor? |
|---|---|
| **Colab** | Google'ın tarayıcıda çalışan Jupyter Notebook'u |
| **pandas** | Tablo verisi (DataFrame): satır = örnek, sütun = özellik |
| **matplotlib** | Grafikler |
| **Keras** | Kursta modeli kurmak için kullanılıyor (optimizer: RMSprop) |

> 💡 Benim notebook'umda Keras yerine modeli **NumPy ile sıfırdan** yazdım: mini grup SGD ve RMSprop. Böylece önceki derslerdeki gradyan inişi ve hiperparametreler kodda açıkça görünüyor.

---

## Bölüm 2 — Veriyi tanıma

### `describe()` ve NaN
`df.describe()` sayısal sütunların istatistiklerini (ortalama, min, max…) verir.
`COMPANY` ve `PAYMENT_TYPE` **kategorik** (metin) özellikler olduğu için onların ortalaması/max'ı **NaN** görünür. Bu bir eksik veri ya da hata değil, sadece anlamsız olduğu için hesaplanmıyor.

Colab'daki sorular: en yüksek ücret, ortalama mesafe, şirket sayısı, en sık ödeme türü ve eksik veri olup olmadığı. Notebook'ta hepsini **kodla** cevaplayan bir hücre var.

### Korelasyon matrisi
| Değer | Anlamı |
|---|---|
| **1.0** | Mükemmel pozitif: biri artınca diğeri de artar |
| **−1.0** | Mükemmel negatif: biri artınca diğeri azalır |
| **0.0** | Doğrusal ilişki yok |

📌 Korelasyonun **mutlak değeri** ne kadar büyükse, özellik etiketi tahmin etmede o kadar güçlüdür.
Beklenen: Ücretle en güçlü ilişkili özellik **mesafe (TRIP_MILES)**, ardından **süre** geliyor. **Bahşiş oranı (TIP_RATE)** ise ücretle neredeyse ilişkisiz.

### Çift grafiği (pair plot)
Her özelliğin diğer tüm özelliklerle ilişkisini tek bir grafik ızgarasında gösterir.

---

## Bölüm 3 — Model eğitme

### RMSE neden?
RMSE'nin birimi **etiketin birimiyle aynıdır**, yani **dolar**. "RMSE = 3" demek, tahminlerin gerçek ücretten ortalama yaklaşık **3 $** saptığı anlamına gelir. Bu yüzden MSE'ye göre çok daha kolay yorumlanır (bkz. [1.2 Kayıp](02-kayip.md)).

### Deney 1 — tek özellik
```python
learning_rate = 0.001
epochs        = 20
batch_size    = 50
features      = ["TRIP_MILES"]
```
Sorular: Kaç dönemde yakınsadı? Model veriye ne kadar iyi uyuyor?

### Hiperparametre deneyleri
Her seferinde **yalnızca bir** hiperparametre değiştirilir; aynı anda birkaçını değiştirirsen sonucu hangisinin etkilediğini anlayamazsın.

| Deney | Değişiklik | Beklenen (bkz. [1.4 Hiperparametreler](04-hiperparametreler.md)) |
|---|---|---|
| A | Öğrenme oranı **1.0** | Adımlar çok büyük: kayıp eğrisi zıplar, düzgün yakınsamaz |
| B | Öğrenme oranı **0.0001** | Adımlar çok küçük: 20 dönem yetmez, RMSE yüksek kalır |
| C | Grup boyutu **500** | Dönem başına 10 kat daha az güncelleme: aynı 20 dönemde daha yavaş yakınsar |

### Deney 3 — iki özellik
`TRIP_MILES` + `TRIP_MINUTES`. Dakika veride yok, saniyeden türetiliyor:
```python
training_df["TRIP_MINUTES"] = training_df["TRIP_SECONDS"] / 60
```
Bu, **özellik mühendisliğinin (feature engineering)** ilk örneği: var olan veriden yeni bir özellik üretmek.

- İki özellikli modelde tahmin bir **doğru** değil, bir **düzlemdir**: x = mil, y = dakika, z = ücret (3B grafik).
- **Saniye mi, dakika mı?** Teoride aynı bilgi; ağırlık sadece 60 kat değişmeli. Pratikte ise ölçek önemli: saniyeler binlerle ifade edildiği için aynı öğrenme oranıyla gradyanlar çok büyük olur ve model daha zor eğitilir. Bu konu ileride **normalleştirme (normalization)** dersinde işlenecek.

---

## Bölüm 4 — Tahmin
Eğitilmiş modelle örnek yolculukların ücreti tahmin edilip gerçek değerle karşılaştırılıyor.

> ⚠️ Bu alıştırmada tahmin için **eğitim verisinin kendisi** kullanılıyor. Doğrusu, modeli **hiç görmediği** verilerle test etmek. Bu da ileriki derslerde işlenecek (eğitim/test ayrımı).

---

## 📝 Sonuçlarım
*Colab'da çalıştırınca doldur:*

| Deney | Özellik(ler) | lr | Grup | Son RMSE ($) | Gözlem |
|---|---|---|---|---|---|
| 1 | TRIP_MILES | 0.001 | 50 | | |
| A | TRIP_MILES | 1.0 | 50 | | |
| B | TRIP_MILES | 0.0001 | 50 | | |
| C | TRIP_MILES | 0.001 | 500 | | |
| 3 | MILES + MINUTES | 0.001 | 50 | | |

## 🔑 Anahtar terimler
`DataFrame` · `describe` · `NaN` · `categorical feature` · `correlation matrix` · `pair plot` · `RMSE` · `feature engineering` · `hyperparameter tuning`
