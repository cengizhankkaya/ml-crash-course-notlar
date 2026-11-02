# 7.3 Çok Sınıflı Çıkış ve Softmax

> Kaynaklar: [MLCC — Çok sınıflı sınıflandırma](https://developers.google.com/machine-learning/crash-course/neural-networks/multi-class?hl=tr) · [scikit-learn — Çok sınıflı yöntemler](https://scikit-learn.org/stable/modules/multiclass.html)

**One-vs-rest / one-vs-all**, her sınıf için ayrı bir ikili karar üretir. Sinir ağında ortak gizli katmanların üzerine sınıf başına sigmoid çıkışı konabilir. Bu olasılıkların toplamı 1 olmak zorunda değildir.

Bir örnek tam olarak bir sınıfa aitse **softmax**, $K$ adet logit'i tek bir olasılık dağılımına dönüştürür:

$$p_j=\frac{e^{z_j}}{\sum_{k=1}^{K}e^{z_k}}$$

Olasılıklar toplamı 1'dir. Örneğin $z=[2,1,0]$ için yaklaşık $p=[0.665,0.245,0.090]$ elde edilir. En büyük olasılık ilk sınıftadır. Eğitimde tek etiketli çapraz entropi $L=-\log p_{\text{doğru sınıf}}$ kullanılarak doğru sınıfa daha yüksek olasılık verilmesi teşvik edilir.

**Sayısal kararlılık:** Üstel almadan önce bütün logit'lerden en büyüğünü çıkar. $\mathrm{softmax}(z)=\mathrm{softmax}(z-\max(z))$; oranlar değişmez, taşma riski azalır.

## Hangi çıktı?

- Tek meyve türü seçilecekse: softmax.
- Fotoğrafta aynı anda kedi ve köpek bulunabiliyorsa: sınıf başına sigmoid; bu **çok etiketli** problemdir.
- Çok büyük sınıf sözlüğünde tam softmax pahalı olabilir. Eğitim sırasında aday örnekleme, bütün negatifleri hesaplamak yerine bir alt kümeyle çalışmayı mümkün kılar.

> **Terim notu:** MLCC bu sayfada softmax için “one-vs-one” ifadesini kullanır. Yaygın literatürde one-vs-one, her sınıf çifti için ayrı sınıflandırıcı kurmaktır; $K(K-1)/2$ model kullanır. Bu notta karışıklığı önlemek için ortak olasılık çıkışına doğrudan **softmax** deniyor.

## ✅ Kendimi test

**S1:** Üç softmax logit'i aynıysa olasılıklar nedir?

**C:** Her biri $1/3$.

**S2:** Dört sınıflı standart one-vs-one kaç ikili sınıflandırıcı kurar?

**C:** $4\times3/2=6$. Bu, dört logit'e tek softmax uygulamaktan farklıdır.

## 🔑 Anahtar terimler
`logit` · `softmax` · `cross entropy` · `multiclass` · `multilabel` · `candidate sampling`

💻 Softmax hesabı için ek örnek: [token_olasiliklari.py](../../kod/09-buyuk-dil-modelleri/token_olasiliklari.py)

## Resmî tekrar

[Modül sonu bilgi testi](https://developers.google.com/machine-learning/crash-course/neural-networks/test-your-knowledge?hl=tr). Buradaki kendimi test soruları ek pekiştirme içindir; resmî sınavın cevap anahtarı değildir.
