# 12.2 Demografik Eşitlik ve Fırsat Eşitliği

> Kaynaklar: [MLCC — Evaluating for bias](https://developers.google.com/machine-learning/crash-course/fairness/evaluating-for-bias) · [Demographic parity](https://developers.google.com/machine-learning/crash-course/fairness/demographic-parity) · [Equality of opportunity](https://developers.google.com/machine-learning/crash-course/fairness/equality-of-opportunity)

`A` grup, `Y` gerçek etiket, `Ŷ` model kararı olsun. Her grubun örnek sayısı ve karışıklık matrisi ayrı incelenir. Adalet ölçütünü seçmeden önce olumlu kararın ne olduğu ve yanlış kararların etkisi tanımlanır.

## İki farklı payda

**Demografik eşitlik (demographic parity):** Olumlu tahmin oranları gruplar arasında eşittir.

$$P(\hat Y=1\mid A=a)=P(\hat Y=1\mid A=b)$$

Hesap: `(TP + FP) / N`. Gerçek etiketin olumlu olup olmadığına koşullanmaz; toplam seçilme oranını karşılaştırır.

**Fırsat eşitliği (equality of opportunity):** Gerçekte olumlu etikete sahip örneklerde olumlu karar oranları, yani **recall/TPR**, eşittir.

$$P(\hat Y=1\mid Y=1,A=a)=P(\hat Y=1\mid Y=1,A=b)$$

Hesap: `TP / (TP + FN)`. Gerçek etiketlerin kendisi yanlıysa değerlendirme de bu sorunu devralabilir. Ayrıca bu ölçüt tek başına FPR eşitliğini istemez. **Equalized odds**, TPR ile FPR'yi birlikte karşılaştırır.

## Ek sayısal örnek

| Grup | TP | FP | FN | TN | Olumlu karar | TPR |
|---|---:|---:|---:|---:|---:|---:|
| A | 18 | 2 | 12 | 18 | 20/50 = %40 | 18/30 = %60 |
| B | 9 | 1 | 1 | 14 | 10/25 = %40 | 9/10 = %90 |

Bu oluşturulmuş örnekte demografik eşitlik sağlanır; fırsat eşitliği sağlanmaz. İki ölçüt farklı soruları yanıtlar. Grup sayıları küçükse oranlar oynaktır; ham sayılar ve belirsizlik de raporlanmalıdır. Payda sıfırsa oranı 0 başarı gibi göstermek yerine tanımsız olarak işaretle.

## ✅ Kendimi test

**S1:** İki grubun seçilme oranı aynıysa recall da aynı mıdır?

**C:** Hayır. Tabloda aynı %40 seçilme oranına rağmen recall farklıdır.

**S2:** Fırsat eşitliği değerlendirmesi için yalnız tahminler yeterli mi?

**C:** Hayır. Grup bilgisiyle birlikte gerçek olumlu etiketlerin de bilinmesi gerekir.

## 🔑 Anahtar terimler

`demographic parity` · `equality of opportunity` · `equalized odds` · `TPR` · `FPR`

💻 Ek pekiştirme kodu: [grup_metrikleri.py](../../kod/12-adalet/grup_metrikleri.py)
