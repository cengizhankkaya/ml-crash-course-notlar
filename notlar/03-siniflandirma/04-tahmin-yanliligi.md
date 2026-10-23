# 3.4 Tahmin Yanlılığı (Prediction Bias)

> Kaynak: [ML Crash Course — Sınıflandırma: Tahmin yanlılığı](https://developers.google.com/machine-learning/crash-course/classification/prediction-bias?hl=tr)

## Nedir?
Model ya da eğitim verisindeki sorunları **erken** fark etmeyi sağlayan **hızlı bir kontrol**.

$$\text{tahmin yanlılığı} = \text{ortalama(tahminler)} - \text{ortalama(gerçek etiketler)}$$

**Örnek:** E-postaların **%5**'i spam olan bir veriyle eğitilen model:
- Gerçek etiketlerin ortalaması = **0.05**
- Modelin tahminlerinin ortalaması da **≈ 0.05** olmalı → yanlılık **≈ 0** ✅
- Model ortalamada **%50** spam diyorsa → bir yerde sorun var ❌. Sorun eğitim verisinde, modelin uygulandığı yeni veride ya da modelin kendisinde olabilir.

> ⚠️ Yanlılığın sıfır olması modelin **iyi** olduğu anlamına gelmez; modelde başka sorunlar olabilir (aşağıdaki deneyde 4. senaryo).

> 📝 Türkçe sayfada aynı kavram için hem "tahmin **yanlılığı**" hem "tahmin **önyargısı**" kullanılıyor. İkisi de *prediction bias*. "Kesin referans" ise *ground truth*, yani gerçek etiket.
> Bu *bias*, modelin **yanlılık parametresi b** (doğrusal denklemdeki y-kesişimi) ile aynı şey değil.

## Olası nedenler
1. **Verideki önyargı veya gürültü**, eğitim kümesinde önyargılı örnekleme dahil
2. **Çok güçlü düzenlileştirme**: Model aşırı basitleşir, gereken karmaşıklığı kaybeder
3. **Eğitim ardışık düzeninde (pipeline) hatalar**
4. **Yetersiz özellik kümesi**: Verilen özellikler görev için yeterli değil

## Deney: dört senaryo
Gerçek dünyada e-postaların %5'i spam. Mantıksal regresyon modelini farklı koşullarda eğitip aynı test verisinde ölçtüm:

| Senaryo | Ort. tahmin | Ort. etiket | **Yanlılık** | AUC |
|---|---|---|---|---|
| 1) Normal eğitim | 0.051 | 0.049 | **+0.002** ✅ | 0.957 |
| 2) Çok güçlü düzenlileştirme (λ = 1) | 0.451 | 0.049 | **+0.402** ❌ | 0.957 |
| 3) Önyargılı örnekleme (eğitimde %50 spam) | 0.185 | 0.049 | **+0.137** ❌ | 0.957 |
| 4) Bilgi taşımayan özellikler | 0.050 | 0.049 | **+0.001** 🤔 | **0.498** |

### Çıkarımlar
- **2 ve 3:** Yanlılık büyük, ama AUC **değişmedi** (0.957). Model örnekleri hâlâ **doğru sıralıyor**, fakat verdiği **olasılıklar** gerçeği yansıtmıyor (kalibrasyon bozuk). Yani AUC ve tahmin yanlılığı **farklı şeyleri** ölçüyor; ikisine birlikte bakmak gerekiyor.
- **3:** Eğitimde %50 spam görmüş model, %5 spam'li gerçek dünyada spam'i olduğundan çok daha sık tahmin ediyor. Önyargılı örneklemenin tipik sonucu.
- **4:** Özellikler hiçbir bilgi taşımıyor. Model sadece **ortalamayı (%5) tutturmayı** öğreniyor: yanlılık ≈ 0, ama AUC ≈ 0.5, yani yazı-tura kadar işe yaramaz. Yetersiz özellik her zaman genel yanlılık olarak görünmüyor; bu yüzden yanlılık **tek başına yeterli bir kontrol değil**.

## 🔑 Anahtar terimler
`prediction bias` · `prediction` · `ground truth` · `regularization` · `sampling bias` · `calibration`

---
💻 İlgili kod: [`tahmin_yanliligi.py`](../../kod/03-siniflandirma/tahmin_yanliligi.py)
