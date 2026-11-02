# 12.3 Karşıolgusal Adalet ve Modül Tekrarı

> Kaynak: [MLCC — Counterfactual fairness](https://developers.google.com/machine-learning/crash-course/fairness/counterfactual-fairness)

## Bireysel karşılaştırma

Kursun giriş düzeyindeki karşıolgusal adalet yaklaşımı, ilgili özellikleri aynı olup hassas grup niteliği farklı olan örneklerin aynı kararı almasını inceler. Böyle bir karşılaştırma, toplam grup oranlarının gizlediği bireysel farkları görünür kılabilir.

Grup bilgisi yalnız bazı örneklerde varsa uygun eşler üzerinde inceleme yapılabilir. Ancak birkaç eşte tutarlılık, bütün kullanıcılar için adalet kanıtı değildir. Grupların toplam durumunu ve karşılaştırılan kişilerin gerçekten eşdeğer olup olmadığını da araştırmak gerekir. Gerçek karşıolgusal analizde nedensel varsayımlar önemlidir; bir sütunu mekanik olarak değiştirmek tek başına kapsamlı adalet denetimi sayılmaz.

## Ek düşünme örneği

Bir eğitim içeriği önericisinde benzer geçmiş etkinliğe ve aynı öğrenme hedefine sahip iki örnek düşün. Yalnız denetlenmek istenen grup niteliği değişince öneri puanı büyük ölçüde değişiyorsa bunu inceleme adayı olarak kaydet. Farkın neye dayandığını anlamadan, tek eşten bütün model hakkında sonuç çıkarma.

Grup oranlarının eşit olması bu tür eşlerin eşit muamele gördüğünü garanti etmez. Tersi de geçerlidir: seçilmiş birkaç eşin aynı kararı alması, sistemik temsil ve hata farklarını çözmüş olmayabilir. Ölçütler kullanım bağlamına göre seçilir; tüm adalet tanımları her durumda aynı anda sağlanamaz.

## Tekrar akışı

1. Veri nereden geldi; hangi koşullar az temsil ediliyor?
2. Eksiklikler ve etiket kalitesi gruplar arasında değişiyor mu?
3. Hangi karar ve hata türü değerlendiriliyor?
4. Toplam metrikler, grup metrikleri ve uygun eş karşılaştırmaları ne gösteriyor?
5. Müdahale sonrası aynı ayrılmış değerlendirmede ne değişti?

Bu depodaki sayısal örnekler ek pekiştirmedir; resmî programlama alıştırmasının çalıştırılmış çıktısı olarak sunulmaz.

- [Resmî programlama alıştırması](https://developers.google.com/machine-learning/crash-course/fairness/programming-exercise): Veri kümesini adalet açısından denetleme ve yanlılığı azaltma yöntemlerini inceleme; sayfa Colab'a yönlendirir.
- [Resmî modül testi](https://developers.google.com/machine-learning/crash-course/fairness/test-your-knowledge): Kavramların tekrarını yapma.

## ✅ Kendimi test

**S1:** Üç eşte aynı karar çıktıysa modelin tamamı adil midir?

**C:** Bu sonuç yalnız incelenen eşler hakkında kanıttır; daha geniş değerlendirme gerekir.

**S2:** Her proje için tek bir en iyi adalet metriği var mı?

**C:** Hayır. Amaç, etiketin anlamı, hata etkileri ve veri kapsamı seçimi belirler.

## 🔑 Anahtar terimler

`counterfactual fairness` · `paired examples` · `sensitive attribute` · `fairness trade-off`
