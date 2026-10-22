# 🧠 Google ML Crash Course — Öğrenme Notlarım

[Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course?hl=tr) eğitimini takip ederken tuttuğum Türkçe notlar ve denediğim kodlar.

## 📚 İlerleme

| # | Modül | Durum | Notlar | Kod |
|---|-------|-------|--------|-----|
| 1 | Doğrusal Regresyon | 🟡 Devam ediyor | [notlar](notlar/01-dogrusal-regresyon/) | [kod](kod/01-dogrusal-regresyon/) |

### 1. Doğrusal Regresyon
- [x] [Giriş: model, ağırlık, yanlılık](notlar/01-dogrusal-regresyon/01-giris.md)
- [x] [Kayıp (Loss): L1, L2, MAE, MSE, RMSE](notlar/01-dogrusal-regresyon/02-kayip.md)
- [x] [Gradyan inişi: yakınsama, kayıp eğrisi, dışbükey yüzey](notlar/01-dogrusal-regresyon/03-gradyan-inisi.md)
- [ ] Hiperparametreler
- [ ] Programlama alıştırması

## 🗂️ Klasör yapısı

```
notlar/   → Her modül için ders ders Markdown notlar
kod/      → Denemeler ve alıştırma kodları (Python)
```

## ▶️ Kodları çalıştırma

```bash
pip install -r requirements.txt
python kod/01-dogrusal-regresyon/basit_regresyon.py
python kod/01-dogrusal-regresyon/grafik.py
python kod/01-dogrusal-regresyon/kayip.py
python kod/01-dogrusal-regresyon/gradyan_inisi.py
```
