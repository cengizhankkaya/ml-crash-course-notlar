# 8.2 Embedding Öğrenmek ve Bağlamı Katmak

> Kaynak: [MLCC — Embedding elde etme](https://developers.google.com/machine-learning/crash-course/embeddings/obtaining-embeddings?hl=tr)

Temsil elde etmek için boyut indirgeme yöntemleri, önceden eğitilmiş temsiller veya görevle birlikte eğitilen bir embedding katmanı kullanılabilir. PCA gibi yöntemler verinin yapısını daha az boyutta korumaya çalışır. Sinir ağına eklenen embedding katmanı ise son görevdeki kayıp üzerinden güncellenebilir.

Embedding boyutu bir tasarım seçimidir. Çok küçük boyut önemli ilişkileri kaybedebilir; gereksiz büyük boyut maliyeti ve aşırı öğrenme riskini artırabilir. Önceden eğitilmiş bir temsil kullanırken dil, alan ve görev uyumunu değerlendirmek gerekir.

## Statik ve bağlamsal farkı

“Yüz” kelimesi “yüz metre” ve “gülen yüz” ifadelerinde aynı anlamda değildir. Statik bir kelime tablosu aynı kelimeye tek satır ayırır. **Bağlamsal embedding**, çevredeki tokenların bilgisini de kullanarak farklı temsiller üretebilir.

Transformer'da token kimliği ve konum bilgisi girişe katkı verir; self-attention katmanları tokenlar arasında bilgi birleştirir. Yalnız bir konum vektörü eklemek, kelimenin bütün bağlam anlamını çözmüş olmak değildir. Aynı kelimenin farklı cümlelerde farklı temsil almasını sağlayan hesaplamaları takip etmek gerekir.

## Ek pekiştirme önerisi

Üç cümlede aynı kelimeyi kullan ve her cümlede beklediğin anlamı yaz. Sonra şu iki bilgiyi ayır: sözlükteki token kimliği ve model katmanının ürettiği bağlamsal vektör. Birinci bilgi aynı kalabilirken ikincisi değişebilir. Tokenizer'ın kelimeyi birden fazla parçaya ayırabileceğini de hesaba kat.

Bu klasördeki `benzerlik.py`, **elle belirlenmiş** vektörler kullanır. Embedding eğitmez ve Türkçe anlam çözmez; yalnız tablo erişimini ve benzerlik hesabını gösterir.

## ✅ Kendimi test

**S1:** Hazır embedding tablosunu dondurursak görev eğitiminde tablo güncellenir mi?

**C:** Hayır; diğer eğitilebilir katmanlar değişebilir.

**S2:** Her tokenın başlangıç vektörü statikse modelin bütün katman çıktıları da statik midir?

**C:** Hayır. Bağlamla bilgi birleştiren katmanlar sonraki temsilleri değiştirebilir.

## 🔑 Anahtar terimler
`embedding layer` · `PCA` · `contextual embedding` · `positional encoding` · `self-attention`

💻 Ek pekiştirme örneği: [benzerlik.py](../../kod/08-embedding/benzerlik.py)

## Resmî tekrar

[Modül sonu bilgi testi](https://developers.google.com/machine-learning/crash-course/embeddings/test-your-knowledge?hl=tr). Buradaki kendimi test soruları ek pekiştirme içindir; resmî sınavın cevap anahtarı değildir.
