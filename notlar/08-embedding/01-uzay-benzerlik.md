# 8.1 Embedding Uzayı ve Benzerlik

> Kaynaklar: [MLCC — Statik embedding](https://developers.google.com/machine-learning/crash-course/embeddings/embedding-space?hl=tr) · [Benzerlik ölçüleri](https://developers.google.com/machine-learning/clustering/dnn-clustering/supervised-similarity) · [Etkileşimli alıştırmalar](https://developers.google.com/machine-learning/crash-course/embeddings/interactive-exercises?hl=tr)

**Statik embedding**, aynı öğeye her kullanımda aynı vektörü verir. word2vec gibi yöntemlerde benzer bağlamlarda görünen kelimeler benzer temsiller edinebilir. Bu temsil eğitim metninin kapsamını ve yanlılıklarını da taşır.

İki vektör için üç yaygın ölçü:

| Ölçü | Formül | Daha benzer |
|---|---|---|
| Öklid uzaklığı | $\|a-b\|_2$ | Daha küçük |
| Nokta çarpımı | $a^Tb$ | Daha büyük |
| Kosinüs benzerliği | $a^Tb/(\|a\|\|b\|)$ | Daha büyük |

Kosinüs yönü karşılaştırır; nokta çarpımı uzunluktan da etkilenir. Sıfır vektörünün kosinüsü tanımsızdır. Uzunlukları 1'e normalize edilmiş vektörlerde nokta çarpımı kosinüse eşittir; Öklid uzaklığı da aynı komşu sıralamasını verir.

## Ek hesap örneği

$a=[1,0]$, $b=[2,0]$, $c=[0,1]$ olsun. $a$ ile $b$ arasındaki kosinüs 1, nokta çarpımı 2, Öklid uzaklığı 1'dir. $a$ ve $c$ dik olduğundan kosinüsleri 0'dır. “Yakın” kelimesi bu yüzden kullanılan ölçüyle birlikte söylenmelidir.

Projector gibi araçlar yüksek boyutlu uzayı iki veya üç boyutta gösterir. Görselde birbirine yakın duran noktalar asıl uzayda en yakın komşular olmayabilir. Komşu listesini asıl vektörlerden hesaplamak, yalnız resme bakmaktan daha güvenilirdir. Bir kelimenin listede olmaması da onun dilde bulunmadığını değil, kullanılan sözlükte bulunmadığını gösterebilir.

## ✅ Kendimi test

**S1:** Bir vektörü pozitif bir sabitle çarpmak kosinüsü değiştirir mi?

**C:** Hayır; yön değişmez. Nokta çarpımı değişebilir.

**S2:** Şehir isimlerinin komşuları belirli bir bölgeye yığılıyorsa ne araştırılır?

**C:** Eğitim verisinin coğrafi kapsamı, örnek sıklıkları ve görevin tanımı; hemen evrensel bir anlam ilişkisi çıkarılmaz.

## 🔑 Anahtar terimler
`cosine similarity` · `dot product` · `nearest neighbor` · `projection` · `word2vec`

💻 Ek pekiştirme örneği: [benzerlik.py](../../kod/08-embedding/benzerlik.py)
