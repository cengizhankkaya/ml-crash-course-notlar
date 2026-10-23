# 🧠 Google ML Crash Course — Öğrenme Notlarım

[Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course?hl=tr) eğitimini takip ederken tuttuğum Türkçe notlar ve denediğim kodlar.

## 📚 İlerleme

| # | Modül | Durum | Notlar | Kod |
|---|-------|-------|--------|-----|
| 1 | Doğrusal Regresyon | 🟡 Devam ediyor | [notlar](notlar/01-dogrusal-regresyon/) | [kod](kod/01-dogrusal-regresyon/) |
| 2 | Mantıksal Regresyon | 🟡 Devam ediyor | [notlar](notlar/02-mantiksal-regresyon/) | [kod](kod/02-mantiksal-regresyon/) |
| 3 | Sınıflandırma | 🟡 Devam ediyor | [notlar](notlar/03-siniflandirma/) | [kod](kod/03-siniflandirma/) |
| 4 | Sayısal Verilerle Çalışma | 🟡 Devam ediyor | [notlar](notlar/04-sayisal-veri/) | [kod](kod/04-sayisal-veri/) |

### 1. Doğrusal Regresyon
- [x] [Giriş: model, ağırlık, yanlılık](notlar/01-dogrusal-regresyon/01-giris.md)
- [x] [Kayıp (Loss): L1, L2, MAE, MSE, RMSE](notlar/01-dogrusal-regresyon/02-kayip.md)
- [x] [Etkileşimli alıştırma: Parametreler](notlar/01-dogrusal-regresyon/02b-parametre-alistirmasi.md)
- [x] [Gradyan inişi: yakınsama, kayıp eğrisi, dışbükey yüzey](notlar/01-dogrusal-regresyon/03-gradyan-inisi.md)
- [x] [Hiperparametreler: öğrenme oranı, grup boyutu, dönem](notlar/01-dogrusal-regresyon/04-hiperparametreler.md)
- [ ] Etkileşimli alıştırma: Eğim azalma
- [x] [Programlama alıştırması: Chicago taksi ücreti](notlar/01-dogrusal-regresyon/05-programlama-alistirmasi.md) · [notebook](kod/01-dogrusal-regresyon/taksi_ucreti.ipynb)
- [ ] Bilginizi test edin (modül sonu testi)

### 2. Mantıksal Regresyon
- [x] [Modüle giriş: neden mantıksal regresyon?](notlar/02-mantiksal-regresyon/00-giris.md)
- [x] [Olasılık hesaplama: sigmoid fonksiyonu, log-odds](notlar/02-mantiksal-regresyon/01-sigmoid.md)
- [x] [Log kaybı ve düzenlileştirme: L2, erken durdurma](notlar/02-mantiksal-regresyon/02-kayip-duzenlilestirme.md)
- [ ] Bilginizi test edin

### 3. Sınıflandırma
- [x] [Modüle giriş: olasılıktan sınıfa, eşik](notlar/03-siniflandirma/00-giris.md)
- [x] [Eşikler ve karışıklık matrisi: TP, FP, FN, TN](notlar/03-siniflandirma/01-esik-karisiklik-matrisi.md)
- [x] [Doğruluk, geri çağırma, kesinlik, FPR, F1](notlar/03-siniflandirma/02-metrikler.md)
- [x] [ROC ve AUC: eşikten bağımsız değerlendirme](notlar/03-siniflandirma/03-roc-auc.md)
- [x] [Tahmin yanlılığı](notlar/03-siniflandirma/04-tahmin-yanliligi.md)
- [x] [Çok sınıflı sınıflandırma: biri diğerlerine karşı, aşamalı](notlar/03-siniflandirma/05-cok-sinifli.md)
- [ ] Programlama alıştırması
- [ ] Bilginizi test edin

### 4. Sayısal Verilerle Çalışma
- [x] [Modüle giriş: sayısal veri nedir?](notlar/04-sayisal-veri/00-giris.md)
- [x] [Özellik vektörleri ve özellik mühendisliği](notlar/04-sayisal-veri/01-ozellik-vektorleri.md)
- [x] [İlk adımlar: görselleştirme, istatistik, aykırı değerler](notlar/04-sayisal-veri/02-ilk-adimlar.md)

## 🗂️ Klasör yapısı

```
notlar/   → Her modül için ders ders Markdown notlar
kod/      → Denemeler, alıştırma kodları ve notebook'lar (Python)
```

## ▶️ Kodları çalıştırma

```bash
pip install -r requirements.txt
python kod/01-dogrusal-regresyon/basit_regresyon.py
python kod/01-dogrusal-regresyon/grafik.py
python kod/01-dogrusal-regresyon/kayip.py
python kod/01-dogrusal-regresyon/gradyan_inisi.py
python kod/01-dogrusal-regresyon/hiperparametreler.py
python kod/02-mantiksal-regresyon/neden_mantiksal.py
python kod/02-mantiksal-regresyon/sigmoid.py
python kod/02-mantiksal-regresyon/log_kaybi.py
python kod/03-siniflandirma/olasiliktan_sinifa.py
python kod/03-siniflandirma/karisiklik_matrisi.py
python kod/03-siniflandirma/metrikler.py
python kod/03-siniflandirma/roc_auc.py
python kod/03-siniflandirma/tahmin_yanliligi.py
python kod/03-siniflandirma/cok_sinifli.py
python kod/04-sayisal-veri/sayisal_mi_kategorik_mi.py
python kod/04-sayisal-veri/ozellik_vektoru.py
python kod/04-sayisal-veri/ilk_adimlar.py

# Taksi ücreti notebook'u
jupyter notebook kod/01-dogrusal-regresyon/taksi_ucreti.ipynb
```

> Notebook'u kurulum yapmadan çalıştırmak için [Colab'da aç](https://colab.research.google.com/github/cengizhankkaya/ml-crash-course-notlar/blob/main/kod/01-dogrusal-regresyon/taksi_ucreti.ipynb).
