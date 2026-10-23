# 4.1 Model Veriyi Nasıl Alır? Özellik Vektörleri

> Kaynak: [ML Crash Course — Sayısal veriler: Bir model, özellik vektörlerini kullanarak verileri nasıl alır?](https://developers.google.com/machine-learning/crash-course/numerical-data/feature-vectors?hl=tr)

## Yanlış fikir: Model tablonun satırlarını okur
Veri kümesinde 5 sütun (`a`–`e`) olsun, ama modelin özellikleri yalnızca **`b`** ve **`d`**. Model 3. satırı işlerken **3b** ve **3d** hücrelerini doğrudan mı alır?

**Hayır** (Şekil 1). Model aslında bir **özellik vektörü (feature vector)** alır:

> **Özellik vektörü** = Tek bir örneği temsil eden **kayan nokta (float) değerleri dizisi**.

## Ham değer → dönüştürülmüş değer
| Şekil | Model ne alır? | Gerçekçi mi? |
|---|---|---|
| 1 | Tablodaki hücreler (3b, 3d) | ❌ Böyle çalışmaz |
| 2 | Ham değerlerden oluşan vektör: `[2850, 14]` | 🟡 Gerçeğe yakın ama nadir |
| 3 | **Dönüştürülmüş** değerler: `[0.28, 0, 1, 0]` | ✅ Gerçekçi |

Özellik vektörleri veri kümesinin **ham değerlerini nadiren** kullanır. Değerler genelde modelin **daha iyi öğrenebileceği temsillere** dönüştürülür.

> ❓ Model gerçek (ham) değerlerle eğitilirse daha iyi tahmin yapmaz mı?
> **Şaşırtıcı ama hayır.** Dönüştürülmüş değerlerle genelde daha iyi öğrenir. (Örnek: Taksi alıştırmasında saniye yerine dakika kullanmak bile eğitimi kolaylaştırmıştı.)

### Kodla: Şekil 1 → 2 → 3
| | a | **b** | c | **d** | e (etiket) |
|---|---|---|---|---|---|
| 0 | kırmızı | 1200 | 2021-03-01 | 3 | 0 |
| 1 | mavi | 3400 | 2022-07-15 | 27 | 1 |
| **2** | yeşil | **2850** | 2020-11-30 | **14** | 1 |
| 3 | mavi | 990 | 2023-01-09 | 41 | 0 |
| 4 | kırmızı | 4100 | 2021-12-24 | 8 | 1 |

3. satır (indeks 2) için:
- **b = 2850** → **normalleştirme** (z-puanı) → **0.280**
- **d = 14** → **gruplandırma**: `0–10`, `10–20`, `20–50` kovalarından `10–20` → one-hot **[0, 1, 0]**

**Özellik vektörü:** `[0.280, 0.0, 1.0, 0.0]`

Modelin gördüğü tablo artık şu:

| b_normal | d_0–10 | d_10–20 | d_20–50 |
|---|---|---|---|
| −1.071 | 1 | 0 | 0 |
| 0.730 | 0 | 0 | 1 |
| **0.280** | **0** | **1** | **0** |
| −1.243 | 0 | 0 | 1 |
| 1.303 | 1 | 0 | 0 |

İki özellik (b, d) dört sayılık bir vektöre dönüştü; `a` ve `c` sütunları ise hiç kullanılmadı.

## Özellik mühendisliği (feature engineering)
Ham değerleri özellik vektöründe **eğitilebilir değerler** olarak göstermenin en iyi yolunu bulma süreci. ML'nin **en önemli** parçalarından biri.

En yaygın iki teknik (bu ünitede işlenecek):

| Teknik | Ne yapar? |
|---|---|
| **Normalleştirme (normalization)** | Sayısal değerleri **standart bir aralığa** dönüştürür |
| **Gruplandırma (binning / bucketing)** | Sayısal değerleri **aralık kovalarına** dönüştürür |

> 📝 Burada "normalleştirme" gerçekten *normalization* (özellik ölçekleme). 2. modüldeki "normalleştirme" ise yanlış çeviriydi, orada *regularization* kastediliyordu.

**Ön işleme (preprocessing):** Sayısal olmayan verileri (ör. metinleri) kayan nokta değerlerine dönüştürmek gibi işlemler. Bir sonraki ünite olan *Kategorik verilerle çalışma*'da işlenecek.

📌 **Özellik vektöründeki her değer kayan nokta olmalıdır.** Ama birçok özellik doğal olarak metin ya da sayısal olmayan bir değerdir. Bu yüzden özellik mühendisliğinin büyük kısmı, **sayısal olmayan değerleri sayısal olarak temsil etmektir**.

## 🔑 Anahtar terimler
`feature vector` · `feature engineering` · `normalization` · `binning` · `bucketing` · `preprocessing` · `one-hot encoding`

---
💻 İlgili kod: [`ozellik_vektoru.py`](../../kod/04-sayisal-veri/ozellik_vektoru.py)
