# 1.1 Doğrusal Regresyona Giriş

> Kaynak: [ML Crash Course — Doğrusal regresyon](https://developers.google.com/machine-learning/crash-course/linear-regression?hl=tr)

## Nedir?
Doğrusal regresyon, **özellikler (features)** ile **etiket (label)** arasındaki ilişkiyi bir doğru (ya da çok boyutta bir düzlem) ile modelleyen yöntemdir.

- **Özellik (x):** Modele verilen girdi → ör. arabanın ağırlığı
- **Etiket (y):** Tahmin etmek istediğimiz değer → ör. yakıt verimliliği (mil/galon)

## Örnek veri: Ağırlık → Yakıt verimliliği

| Ağırlık (bin pound) | Mil/galon |
|---|---|
| 3.50 | 18 |
| 3.69 | 15 |
| 3.44 | 18 |
| 3.43 | 16 |
| 4.34 | 15 |
| 4.42 | 14 |
| 2.37 | 24 |

Gözlem: Araba ağırlaştıkça yakıt verimliliği **düşüyor** → negatif ilişki.

## Model denklemi

Matematikteki `y = mx + b` → ML gösterimi:

$$y' = b + w_1 x_1$$

| Terim | Anlamı |
|---|---|
| `y'` | Tahmin edilen etiket |
| `b` | **Yanlılık (bias)** — y eksenini kestiği yer (bazen `w₀`) |
| `w₁` | **Ağırlık (weight)** — eğim; özelliğin etkisi |
| `x₁` | **Özellik** — girdi değeri |

📌 `b` ve `w` modelin **parametreleridir**, eğitim sırasında **öğrenilir**. `x` değerleri ise verinin parçasıdır, değişmez.

### Sayısal örnek
Eğitim sonucunda `b = 34`, `w₁ = -4.6` bulunduğunu varsayalım:

$$y' = 34 + (-4.6) \cdot x_1$$

4.000 pound'luk (x₁ = 4) bir araba için: `34 − 4.6 × 4 = 15.6` mil/galon.

## Birden fazla özellik

$$y' = b + w_1x_1 + w_2x_2 + \dots + w_nx_n$$

Yakıt verimliliği için kullanılabilecek ek özellikler: motor hacmi, ivme, silindir sayısı, beygir gücü.
- Motor hacmi ↑ → verimlilik ↓ (negatif ilişki)
- İvme ↑ → verimlilik ↑ (pozitif ilişki)

## ✅ Kendimi test
**S:** Eğitim sırasında denklemin hangi kısımları güncellenir?
**C:** Yalnızca **yanlılık (b)** ve **ağırlıklar (w)**. Özellikler ve tahminler güncellenmez.

## 🔑 Anahtar terimler
`bias` · `feature` · `label` · `linear regression` · `parameter` · `weight`

---
💻 İlgili kod: [`basit_regresyon.py`](../../kod/01-dogrusal-regresyon/basit_regresyon.py)
