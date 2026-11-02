# 9.0 Dil Modeli, Token ve Bağlam

> Kaynak: [MLCC — Büyük dil modellerine giriş](https://developers.google.com/machine-learning/crash-course/llm?hl=tr)

Dil modeli, bir tokenın veya token dizisinin olasılığını tahmin eder. **Token** her zaman kelime değildir; karakter, kelime parçası veya başka bir metin birimi olabilir. Türkçe bir cümlenin token sayısını yalnız kelimeleri sayarak kesin belirleyemeyiz.

**Bağlam**, tahminde kullanılan çevre bilgisidir. “Çay” kelimesinin içecek mi akarsu mu olduğunu anlamak için komşu sözcükler yardımcı olur. Üretici bir modelde sonraki token, o ana kadarki diziden tahmin edilebilir:

$$P(t_1,\ldots,t_n)=\prod_{i=1}^{n}P(t_i\mid t_1,\ldots,t_{i-1})$$

N-gram modelleri sınırlı uzunluktaki dizilerin istatistiklerinden yararlanır. Daha büyük N daha geniş bağlam sağlar, ancak olası diziler arttıkça örnekler seyrekleşir. RNN'ler geçmişten bilgi taşıyan bir durum kullanır; uzun bağımlılıkların öğrenilmesi yine zor olabilir.

## Eğitim ile üretim

Eğitimde gerçek metinlerden hedefler türetilebilir. Üretimde seçilen token diziye eklenir ve yeni tahminin bağlamına katılır. En yüksek olasılıklı tokenı seçmek ile dağılımdan örneklemek farklı işlemlerdir.

Ek bir oyuncak örnekte “Bugün hava” sonrası yalnız üç aday düşündüğümüzü varsayalım: `güzel`, `serin`, `kapalı`. Olasılıkların toplamı 1 olsa bile gerçek bir dil modelinin sözlüğü bunlarla sınırlı değildir. Bu kısıtlı örnek, yalnız seçim mantığını anlatır.

## ✅ Kendimi test

**S1:** Tokenizer “kitaplar”ı iki parçaya ayırırsa model iki kelime mi görmüş olur?

**C:** Hayır; iki token görür. Kelime ve token farklı birimlerdir.

**S2:** N-gram uzunluğunu artırmak neden kesin başarı artışı sağlamaz?

**C:** Uzun bağlamların eğitim verisinde yeterince tekrarlanmaması tahminleri zayıflatabilir.

## 🔑 Anahtar terimler
`token` · `tokenizer` · `context` · `N-gram` · `RNN` · `sampling`

💻 Ek pekiştirme örneği: [token_olasiliklari.py](../../kod/09-buyuk-dil-modelleri/token_olasiliklari.py)
