# 🧠 Google ML Crash Course — Öğrenme Notlarım

[Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course?hl=tr) için Türkçe ders notları, kaynak bağlantıları ve Python örnekleri.

**Kurs durumu: ✅ Tamamlandı — 12/12 modül.** Kursun tamamlandığı 2 Kasım 2026 tarihinde bildirildi; ilerleme kaydı buna göre güncellendi.

Notlar tüm modüllerin ana konularını kapsayan bir tekrar arşividir. İlk dört modüldeki notlar korunarak eksik dersler ve sonraki sekiz modül eklendi. Yeni içerikler resmî kaynaklardan hazırlanmış Türkçe özetler ve ek pekiştirme örnekleridir; video, etkileşimli alıştırma ve modül testlerine kaynak bağlantılarından ulaşılabilir.

> Tamamlanma bilgisi kurs ilerlemesini gösterir. Kişisel Colab çıktıları kaydedilmemiş sonuç tabloları boş bırakılmıştır. Eklenen örnek kodların çalışması, kişisel alıştırma sonuçları veya quiz puanları yerine geçmez.

## 📚 İlerleme

| # | Modül | Durum | Notlar | Kod |
|---|-------|-------|--------|-----|
| 1 | Doğrusal Regresyon | ✅ Tamamlandı | [notlar](notlar/01-dogrusal-regresyon/) | [kod](kod/01-dogrusal-regresyon/) |
| 2 | Mantıksal Regresyon | ✅ Tamamlandı | [notlar](notlar/02-mantiksal-regresyon/) | [kod](kod/02-mantiksal-regresyon/) |
| 3 | Sınıflandırma | ✅ Tamamlandı | [notlar](notlar/03-siniflandirma/) | [kod](kod/03-siniflandirma/) |
| 4 | Sayısal Verilerle Çalışma | ✅ Tamamlandı | [notlar](notlar/04-sayisal-veri/) | [kod](kod/04-sayisal-veri/) |
| 5 | Kategorik Verilerle Çalışma | ✅ Tamamlandı | [notlar](notlar/05-kategorik-veri/) | [kod](kod/05-kategorik-veri/) |
| 6 | Veri Kümeleri, Genelleme ve Aşırı Öğrenme | ✅ Tamamlandı | [notlar](notlar/06-veri-kumeleri-genelleme-asiri-ogrenme/) | [kod](kod/06-veri-kumeleri-genelleme-asiri-ogrenme/) |
| 7 | Sinir Ağları | ✅ Tamamlandı | [notlar](notlar/07-sinir-aglari/) | [kod](kod/07-sinir-aglari/) |
| 8 | Embedding (Yerleştirmeler) | ✅ Tamamlandı | [notlar](notlar/08-embedding/) | [kod](kod/08-embedding/) |
| 9 | Büyük Dil Modellerine Giriş | ✅ Tamamlandı | [notlar](notlar/09-buyuk-dil-modelleri/) | [kod](kod/09-buyuk-dil-modelleri/) |
| 10 | Üretim ML Sistemleri | ✅ Tamamlandı | [notlar](notlar/10-uretim-ml-sistemleri/) | [kod](kod/10-uretim-ml-sistemleri/) |
| 11 | AutoML | ✅ Tamamlandı | [notlar](notlar/11-automl/) | [kod](kod/11-automl/) |
| 12 | ML’de Adalet | ✅ Tamamlandı | [notlar](notlar/12-adalet/) | [kod](kod/12-adalet/) |

## Ders notları

### 1. Doğrusal Regresyon

[Resmî modül](https://developers.google.com/machine-learning/crash-course/linear-regression)

- [Doğrusal Regresyona Giriş](notlar/01-dogrusal-regresyon/01-giris.md)
- [Kayıp (Loss)](notlar/01-dogrusal-regresyon/02-kayip.md)
- [Etkileşimli Alıştırma: Parametreler](notlar/01-dogrusal-regresyon/02b-parametre-alistirmasi.md)
- [Gradyan İnişi (Gradient Descent)](notlar/01-dogrusal-regresyon/03-gradyan-inisi.md)
- [Hiperparametreler](notlar/01-dogrusal-regresyon/04-hiperparametreler.md)
- [Gradyan İnişi Alıştırması](notlar/01-dogrusal-regresyon/04b-gradyan-inisi-alistirmasi.md)
- [Programlama Alıştırması: Chicago Taksi Ücreti](notlar/01-dogrusal-regresyon/05-programlama-alistirmasi.md)
- [Modül sonu testi](https://developers.google.com/machine-learning/crash-course/linear-regression/test-your-knowledge)
- [Taksi ücreti notebook’u](kod/01-dogrusal-regresyon/taksi_ucreti.ipynb)

### 2. Mantıksal Regresyon

[Resmî modül](https://developers.google.com/machine-learning/crash-course/logistic-regression)

- [Mantıksal Regresyon: Modüle Giriş](notlar/02-mantiksal-regresyon/00-giris.md)
- [Sigmoid ile Olasılık Hesaplama](notlar/02-mantiksal-regresyon/01-sigmoid.md)
- [Log Kaybı ve Düzenlileştirme](notlar/02-mantiksal-regresyon/02-kayip-duzenlilestirme.md)
- [Modül sonu testi](https://developers.google.com/machine-learning/crash-course/logistic-regression/test-your-knowledge)

### 3. Sınıflandırma

[Resmî modül](https://developers.google.com/machine-learning/crash-course/classification)

- [Sınıflandırma: Modüle Giriş](notlar/03-siniflandirma/00-giris.md)
- [Eşikler ve Karışıklık Matrisi](notlar/03-siniflandirma/01-esik-karisiklik-matrisi.md)
- [Doğruluk, Geri Çağırma, Kesinlik ve İlgili Metrikler](notlar/03-siniflandirma/02-metrikler.md)
- [ROC ve AUC](notlar/03-siniflandirma/03-roc-auc.md)
- [Tahmin Yanlılığı (Prediction Bias)](notlar/03-siniflandirma/04-tahmin-yanliligi.md)
- [Çok Sınıflı Sınıflandırma](notlar/03-siniflandirma/05-cok-sinifli.md)
- [Sınıflandırma Programlama Alıştırması](notlar/03-siniflandirma/06-programlama-alistirmasi.md)
- [Modül sonu testi](https://developers.google.com/machine-learning/crash-course/classification/test-your-knowledge)

### 4. Sayısal Verilerle Çalışma

[Resmî modül](https://developers.google.com/machine-learning/crash-course/numerical-data)

- [Sayısal Verilerle Çalışma: Modüle Giriş](notlar/04-sayisal-veri/00-giris.md)
- [Model Veriyi Nasıl Alır? Özellik Vektörleri](notlar/04-sayisal-veri/01-ozellik-vektorleri.md)
- [Sayısal Veri: İlk Adımlar](notlar/04-sayisal-veri/02-ilk-adimlar.md)
- [Sayısal Veri: Programlama Alıştırmaları](notlar/04-sayisal-veri/03-programlama-alistirmalari.md)
- [Normalleştirme](notlar/04-sayisal-veri/04-normallestirme.md)
- [Gruplama (Binning)](notlar/04-sayisal-veri/05-gruplama.md)
- [Veri Temizleme ve İyi Sayısal Özellikler](notlar/04-sayisal-veri/06-temizleme-iyi-ozellikler.md)
- [Polinom Dönüşümleri](notlar/04-sayisal-veri/07-polinom-donusumleri.md)
- [Modül sonu testi](https://developers.google.com/machine-learning/crash-course/numerical-data/test-your-knowledge)

### 5. Kategorik Verilerle Çalışma

[Resmî modül](https://developers.google.com/machine-learning/crash-course/categorical-data)

- [Kategorik Veri, Sözlük ve One-Hot](notlar/05-kategorik-veri/00-giris-ve-one-hot.md)
- [Çok Kategorili Özellikler: Hashing ve Ortalama Kodlama](notlar/05-kategorik-veri/01-hashing-ve-ortalama-kodlama.md)
- [Kategorik Veride Yaygın Sorunlar](notlar/05-kategorik-veri/02-yaygin-sorunlar.md)
- [Özellik Çaprazlama ve Pekiştirme](notlar/05-kategorik-veri/03-ozellik-caprazlama.md)

### 6. Veri Kümeleri, Genelleme ve Aşırı Öğrenme

[Resmî modül](https://developers.google.com/machine-learning/crash-course/overfitting)

- [Veri Özellikleri, Kalite ve Etiketler](notlar/06-veri-kumeleri-genelleme-asiri-ogrenme/00-veri-kalitesi-ve-etiketler.md)
- [Sınıfları Dengesiz Veri Kümeleri](notlar/06-veri-kumeleri-genelleme-asiri-ogrenme/01-dengesiz-veri.md)
- [Eğitim, Doğrulama, Test ve Veri Dönüşümü](notlar/06-veri-kumeleri-genelleme-asiri-ogrenme/02-veri-ayirma-ve-donusturme.md)
- [Genelleme, Aşırı Öğrenme ve Model Karmaşıklığı](notlar/06-veri-kumeleri-genelleme-asiri-ogrenme/03-genelleme-ve-model-karmasikligi.md)
- [L2, Erken Durdurma ve Kayıp Eğrileri](notlar/06-veri-kumeleri-genelleme-asiri-ogrenme/04-duzenlilestirme-ve-kayip-egrileri.md)

### 7. Sinir Ağları

[Resmî modül](https://developers.google.com/machine-learning/crash-course/neural-networks)

- [Sinir Ağları: Düğümler ve Gizli Katmanlar](notlar/07-sinir-aglari/00-giris-katmanlar.md)
- [Aktivasyon Fonksiyonları](notlar/07-sinir-aglari/01-aktivasyonlar.md)
- [Geri Yayılım ve Eğitim](notlar/07-sinir-aglari/02-geri-yayilim-egitim.md)
- [Çok Sınıflı Çıkış ve Softmax](notlar/07-sinir-aglari/03-cok-sinif-softmax.md)

### 8. Embedding (Yerleştirmeler)

[Resmî modül](https://developers.google.com/machine-learning/crash-course/embeddings)

- [Embedding: Seyrek Kodlamadan Yoğun Temsile](notlar/08-embedding/00-giris-temsil.md)
- [Embedding Uzayı ve Benzerlik](notlar/08-embedding/01-uzay-benzerlik.md)
- [Embedding Öğrenmek ve Bağlamı Katmak](notlar/08-embedding/02-ogrenme-baglamsal.md)

### 9. Büyük Dil Modellerine Giriş

[Resmî modül](https://developers.google.com/machine-learning/crash-course/llm)

- [Dil Modeli, Token ve Bağlam](notlar/09-buyuk-dil-modelleri/00-token-baglam.md)
- [Transformer ve Self-Attention](notlar/09-buyuk-dil-modelleri/01-transformer.md)
- [Fine-Tuning, Damıtma ve Prompt](notlar/09-buyuk-dil-modelleri/02-uyarlama-damitma-prompt.md)

### 10. Üretim ML Sistemleri

[Resmî modül](https://developers.google.com/machine-learning/crash-course/production-ml-systems)

- [Üretim ML Sistemi ve Eğitim Stratejisi](notlar/10-uretim-ml-sistemleri/00-sistem-ve-egitim.md)
- [Çıkarım ve Veri Dönüşümü](notlar/10-uretim-ml-sistemleri/01-cikarim-ve-donusum.md)
- [Dağıtım Testleri ve İzleme](notlar/10-uretim-ml-sistemleri/02-test-ve-izleme.md)
- [Özellik Maliyeti, Veri Kaynağı ve Geri Besleme](notlar/10-uretim-ml-sistemleri/03-sorular-ve-geri-besleme.md)

### 11. AutoML

[Resmî modül](https://developers.google.com/machine-learning/crash-course/automl)

- [AutoML: Kapsamı, Faydaları ve Sınırları](notlar/11-automl/00-kapsam-faydalar-sinirlar.md)
- [AutoML İş Akışı ve Model Seçimi](notlar/11-automl/01-is-akisi-ve-model-secimi.md)

### 12. ML’de Adalet

[Resmî modül](https://developers.google.com/machine-learning/crash-course/fairness)

- [ML'de Adalet ve Yanlılık Türleri](notlar/12-adalet/00-yanlilik-turleri.md)
- [Yanlılığı Tespit Etme ve Azaltma](notlar/12-adalet/01-tespit-ve-azaltma.md)
- [Demografik Eşitlik ve Fırsat Eşitliği](notlar/12-adalet/02-grup-metrikleri.md)
- [Karşıolgusal Adalet ve Modül Tekrarı](notlar/12-adalet/03-karsiolgusal-adalet-ve-tekrar.md)

## 🗂️ Klasör yapısı

```text
notlar/   → 01–12 modülleri için ders özetleri, kaynaklar ve tekrar soruları
kod/      → Modüllerle eşleşen Python örnekleri ve mevcut notebook
```

## ▶️ Kodları çalıştırma

Komutları depo kökünden çalıştır:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Windows PowerShell için etkinleştirme komutu: `.venv\Scripts\Activate.ps1`.

Her örnek bağımsız çalıştırılabilir. Yeni eklenen küçük örnekler NumPy veya Python standart kütüphanesini kullanır; sentetik verileri ve sınırlamaları kendi açıklamalarında belirtilir.

```bash
# Doğrusal Regresyon
python kod/01-dogrusal-regresyon/basit_regresyon.py
python kod/01-dogrusal-regresyon/gradyan_inisi.py
python kod/01-dogrusal-regresyon/grafik.py
python kod/01-dogrusal-regresyon/hiperparametreler.py
python kod/01-dogrusal-regresyon/kayip.py

# Mantıksal Regresyon
python kod/02-mantiksal-regresyon/log_kaybi.py
python kod/02-mantiksal-regresyon/neden_mantiksal.py
python kod/02-mantiksal-regresyon/sigmoid.py

# Sınıflandırma
python kod/03-siniflandirma/cok_sinifli.py
python kod/03-siniflandirma/karisiklik_matrisi.py
python kod/03-siniflandirma/metrikler.py
python kod/03-siniflandirma/olasiliktan_sinifa.py
python kod/03-siniflandirma/roc_auc.py
python kod/03-siniflandirma/tahmin_yanliligi.py

# Sayısal Verilerle Çalışma
python kod/04-sayisal-veri/ilk_adimlar.py
python kod/04-sayisal-veri/normallestirme.py
python kod/04-sayisal-veri/ozellik_vektoru.py
python kod/04-sayisal-veri/sayisal_mi_kategorik_mi.py
python kod/04-sayisal-veri/veri_donusumleri.py

# Kategorik Verilerle Çalışma
python kod/05-kategorik-veri/kodlama_ve_caprazlama.py
python kod/05-kategorik-veri/ortalama_kodlama.py

# Veri Kümeleri, Genelleme ve Aşırı Öğrenme
python kod/06-veri-kumeleri-genelleme-asiri-ogrenme/asiri_ogrenme_ve_l2.py
python kod/06-veri-kumeleri-genelleme-asiri-ogrenme/veri_ayirma.py

# Sinir Ağları
python kod/07-sinir-aglari/ileri_geri_yayilim.py

# Embedding (Yerleştirmeler)
python kod/08-embedding/benzerlik.py

# Büyük Dil Modellerine Giriş
python kod/09-buyuk-dil-modelleri/token_olasiliklari.py

# Üretim ML Sistemleri
python kod/10-uretim-ml-sistemleri/egitim_sunum_farki.py

# AutoML
python kod/11-automl/model_secimi.py

# ML’de Adalet
python kod/12-adalet/grup_metrikleri.py

# Mevcut taksi ücreti notebook’u
jupyter notebook kod/01-dogrusal-regresyon/taksi_ucreti.ipynb
```

[Taksi notebook’unu Colab’da aç](https://colab.research.google.com/github/cengizhankkaya/ml-crash-course-notlar/blob/main/kod/01-dogrusal-regresyon/taksi_ucreti.ipynb).

## Kaynaklar

Modül sırası ve kapsamı [Google MLCC ders listesi](https://developers.google.com/machine-learning/crash-course) üzerinden 2 Kasım 2026 tarihinde kontrol edildi. Ayrıntılı kaynaklar ilgili notların başındadır. Notlardaki ek tekrar soruları resmî quiz cevap anahtarı değildir.
