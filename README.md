# 🧠 Google ML Crash Course — Öğrenme Notlarım

[Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course?hl=tr) eğitimini takip ederken tuttuğum Türkçe notlar ve denediğim kodlar.

## 📚 İlerleme

| # | Modül | Durum | Notlar | Kod |
|---|-------|-------|--------|-----|
| 1 | Doğrusal Regresyon | 🟡 Devam ediyor | [notlar](notlar/01-dogrusal-regresyon/) | [kod](kod/01-dogrusal-regresyon/) |
| 2 | Mantıksal Regresyon | 🟡 Devam ediyor | [notlar](notlar/02-mantiksal-regresyon/) | [kod](kod/02-mantiksal-regresyon/) |

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
- [ ] Olasılık hesaplama: sigmoid fonksiyonu
- [ ] Kayıp ve düzenlileştirme (log kaybı)
- [ ] Bilginizi test edin

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

# Taksi ücreti notebook'u
jupyter notebook kod/01-dogrusal-regresyon/taksi_ucreti.ipynb
```

> Notebook'u kurulum yapmadan çalıştırmak için [Colab'da aç](https://colab.research.google.com/github/cengizhankkaya/ml-crash-course-notlar/blob/main/kod/01-dogrusal-regresyon/taksi_ucreti.ipynb).
