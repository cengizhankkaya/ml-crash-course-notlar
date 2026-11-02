# 8.0 Embedding: Seyrek Kodlamadan Yoğun Temsile

> Kaynaklar: [MLCC — Embedding](https://developers.google.com/machine-learning/crash-course/embeddings?hl=tr) · [Embedding uzayı ve statik embedding](https://developers.google.com/machine-learning/crash-course/embeddings/embedding-space?hl=tr)

One-hot kodlamada her kategori ayrı bir koordinattır. Kodlama kategori kimliğini korur, fakat iki farklı kategorinin ne kadar benzediğini tek başına anlatmaz. Sözlük büyüdükçe vektör de uzar.

**Embedding**, bir öğeyi daha düşük boyutlu, yoğun bir vektörle temsil eder. Benzerliğin anlamı göreve ve eğitim verisine bağlıdır; aynı ürünler renk tahmininde yakın, kullanım amacı tahmininde uzak olabilir. Öğrenilen koordinatların her birine insan tarafından anlaşılır bir isim vermek genellikle mümkün değildir.

## Boyut ve hesap örneği

10.000 kategori, embedding boyutu 16 olsun. Tablo $E\in\mathbb R^{10000\times16}$ biçimindedir ve 160.000 parametre içerir. Kategori 7 için `E[7]` satırı seçilir; tek örneğin çıktısı 16 sayıdır.

One-hot vektörle tablo çarpımı ve satır seçimi aynı sonucu verir:

$$e_7^T E=E[7]$$

Bu nedenle uygulamada büyük bir one-hot vektörünü gerçekten oluşturmadan indeksle erişilebilir. Embedding tablosunun tamamı yine bellekte bulunur; yalnız çıktı vektörünün küçük olması bütün modelin küçük olduğu anlamına gelmez.

**Encoding** başlangıçtaki sayısal eşlemedir; **öğrenilmiş embedding** ise görev kaybından gelen güncellemelerle şekillenebilir. Rastgele sayılarla başlatılmış tablo henüz yararlı anlamsal benzerlik öğrenmiş değildir.

## ✅ Kendimi test

**S1:** 8 kategori ve 3 boyutlu embedding tablosunda kaç sayı vardır?

**C:** 24. Dört kategori indeksinden oluşan bir batch'in çıktısı $(4,3)$ olur.

**S2:** İki embedding birbirine yakınsa öğeler her açıdan aynı mıdır?

**C:** Hayır. Yakınlık yalnız kullanılan temsil ve benzerlik ölçüsü açısından bir ilişkidir; göreve göre yorumlanmalıdır.

## 🔑 Anahtar terimler
`embedding` · `dense vector` · `sparse vector` · `lookup table` · `encoding`

💻 Ek pekiştirme örneği: [benzerlik.py](../../kod/08-embedding/benzerlik.py)
