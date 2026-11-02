# 12.0 ML'de Adalet ve Yanlılık Türleri

> Kaynaklar: [MLCC — Fairness](https://developers.google.com/machine-learning/crash-course/fairness) · [Types of bias](https://developers.google.com/machine-learning/crash-course/fairness/types-of-bias)

Modelin sayısal işlem yapması, sonuçlarının kendiliğinden nesnel veya adil olduğu anlamına gelmez. Toplama, etiketleme, özellik seçme ve kullanım kararları insan etkisi taşır. Genel kaybın düşük olması, her grubun benzer hizmet aldığı sonucunu vermez.

Buradaki **bias**, model denklemindeki sabit terim `b` değildir; veri ve kararların bazı gruplar açısından sistematik olarak çarpılmasıdır.

## Türleri ayır

| Tür | Kısa açıklama |
|---|---|
| Raporlama yanlılığı | Kayda geçen olayların sıklığı gerçek sıklığı yansıtmaz. |
| Tarihsel yanlılık | Eski eşitsizlikler veride ve etiketlerde taşınır. |
| Otomasyon yanlılığı | Otomatik çıktıya, kanıtından bağımsız fazla güvenilir. |
| Seçim yanlılığı | Örnekler hedef topluluğu temsil etmez. |
| Grup atfetme | Birkaç bireyin özellikleri tüm gruba genellenir. |
| Örtük yanlılık | Kişisel deneyimin evrensel olduğu varsayılır. |
| Doğrulama yanlılığı | Veriler önceki inancı doğrulayacak biçimde yorumlanır. |
| Deneyci yanlılığı | Beklenen sonucu bulana kadar deney tekrarlanır. |

Seçim yanlılığında **kapsama** (bazı gruplara hiç ulaşmama), **yanıt vermeme** (katılım farkları) ve **örnekleme** (uygunsuz seçim yöntemi) ayrımını yap. Grup atfetmede kendi grubunu kayırma ve dış grubu tek tip görme farklı biçimlerdir.

## Ek düşünme örneği

Bir destek sistemi yalnız en öfkeli müşterilerin yazdığı yorumlarla eğitilsin. Sessiz kullanıcıların sorunları daha az görünür. Daha çok yorum toplamak, aynı katılım mekanizması devam ediyorsa temsil sorununu otomatik çözmez. Ayrıca değerlendiren kişi yalnız kendi yaşadığı sorunu önemli sayarsa etiketleme de etkilenir. Aynı projede birden fazla yanlılık bulunabilir; tek bir etiket koymak araştırmayı tamamlamaz.

## ✅ Kendimi test

**S1:** Yalnız mobil uygulama kullanıcılarına anket yapmak kimi dışarıda bırakabilir?

**C:** Uygulamaya erişemeyen veya başka kanalı kullanan hedef kullanıcıları; bu bir kapsama sorunudur.

**S2:** “Makine önerdiğine göre doğrudur” hangi sorunu anlatır?

**C:** Otomasyon yanlılığı; sonuç ayrıca kanıt ve hatalarla değerlendirilmelidir.

## 🔑 Anahtar terimler

`fairness` · `reporting bias` · `historical bias` · `selection bias` · `automation bias`
