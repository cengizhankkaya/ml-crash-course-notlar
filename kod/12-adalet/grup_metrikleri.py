"""Ek pekiştirme: oluşturulmuş iki grubun metriklerini karşılaştır.

Gerçek kişi verisi, eğitilmiş model veya kapsamlı adalet denetimi değildir.
Çalıştır: python kod/12-adalet/grup_metrikleri.py
"""


def oran(pay, payda):
    return pay / payda if payda else None


def metrikler(tp, fp, fn, tn):
    sayilar = (tp, fp, fn, tn)
    if any(not isinstance(x, int) or x < 0 for x in sayilar):
        raise ValueError("Karışıklık matrisi sayıları negatif olmayan tamsayı olmalı.")
    n = sum(sayilar)
    return {
        "n": n,
        "olumlu_oran": oran(tp + fp, n),
        "tpr": oran(tp, tp + fn),
        "fpr": oran(fp, fp + tn),
        "dogruluk": oran(tp + tn, n),
    }


def yuzde(deger):
    return "tanımsız" if deger is None else f"%{100 * deger:.1f}"


def main():
    gruplar = {"A": (18, 2, 12, 18), "B": (9, 1, 1, 14)}
    print("Grup | n | olumlu karar | TPR | FPR | doğruluk")
    for ad, sayilar in gruplar.items():
        m = metrikler(*sayilar)
        print(f"{ad} | {m['n']} | {yuzde(m['olumlu_oran'])} | "
              f"{yuzde(m['tpr'])} | {yuzde(m['fpr'])} | {yuzde(m['dogruluk'])}")
    print("Olumlu karar oranları aynı, fakat TPR farklı.")
    print("Bu örnek demografik eşitliği sağlar; fırsat eşitliğini sağlamaz.")
    print("Gerçek pozitif yoksa TPR:", yuzde(metrikler(0, 1, 0, 9)["tpr"]))


if __name__ == "__main__":
    main()
