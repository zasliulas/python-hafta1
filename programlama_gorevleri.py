import random
import math


# ==============================================================================
# 1. TEMEL GİRİŞ/ÇIKIŞ VE İŞLEMLER
# ==============================================================================

def gorev_1_metin_gosterme():
    """Kullanıcıdan Alınan Metni Ekranda Gösterme"""
    print("--- Görev 1: Metin Gösterme ---")
    metin = input("Lütfen ekranda görmek istediğiniz metni girin: ")
    print(f"Girdiğiniz metin: {metin}")


def gorev_2_iki_sayi_toplama():
    """Kullanıcının Girdiği İki Sayıyı Toplama"""
    print("--- Görev 2: İki Sayı Toplama ---")
    try:
        s1 = int(input("Birinci sayıyı girin: "))
        s2 = int(input("İkinci sayıyı girin: "))
        toplam = s1 + s2
        print(f"{s1} + {s2} = {toplam}")
    except ValueError:
        print("HATA: Lütfen geçerli tam sayılar girin.")


def gorev_14_toplam_ve_ortalama():
    """Girilen Sayıların Toplamını ve Ortalamasını Bulma"""
    print("--- Görev 14: Toplam ve Ortalama Bulma ---")
    sayilar = []
    print("Sayı girin (Bitirmek için 'q'):")
    while True:
        girdi = input("> ")
        if girdi.lower() == 'q':
            break
        try:
            sayilar.append(float(girdi))
        except ValueError:
            print("Geçersiz giriş. Lütfen sayı veya 'q' girin.")

    if sayilar:
        toplam = sum(sayilar)
        ortalama = toplam / len(sayilar)
        print(f"Toplam {len(sayilar)} sayı girildi.")
        print(f"Sayıların Toplamı: {toplam}")
        print(f"Sayıların Ortalaması: {ortalama:.2f}")
    else:
        print("Hiç sayı girilmedi.")


# ==============================================================================
# 3. TEK/ÇİFT VE KOŞULLU İFADELER
# ==============================================================================

def gorev_3_tek_cift_kontrol():
    """Girilen Sayının Tek veya Çift Sayı Olduğunu Belirleme"""
    print("--- Görev 3: Tek/Çift Kontrolü ---")
    try:
        sayi = int(input("Lütfen bir tam sayı girin: "))
        if sayi % 2 == 0:
            print(f"{sayi} ÇİFT SAYIdır.")
        else:
            print(f"{sayi} TEK SAYIdır.")
    except ValueError:
        print("HATA: Lütfen geçerli bir tam sayı girin.")


def gorev_18_sonsuz_tek_cift():
    """Kullanıcının Sonsuz Sayıda Girdiği Değerlerin Yanına Tek/Çift Yazma"""
    print("--- Görev 18: Sonsuz Tek/Çift Kontrolü (Çıkış için 'q') ---")
    while True:
        girdi = input("Sayı: ")
        if girdi.lower() == 'q':
            break
        try:
            sayi = int(girdi)
            if sayi % 2 == 0:
                print(f"-> {sayi} ÇİFT")
            else:
                print(f"-> {sayi} TEK")
        except ValueError:
            print("HATA: Geçersiz giriş. Lütfen tam sayı veya 'q' girin.")
    print("İşlem sonlandırıldı.")


# ==============================================================================
# 4 & 5. HESAP MAKİNESİ VE HATA ÖNLEME
# ==============================================================================

def gorev_4_ve_5_hesap_makinesi():
    """İki Sayı ile İşlem Yapan Basit Hesap Makinesi (Hata Korumalı)"""
    print("--- Görev 4 & 5: Basit Hesap Makinesi ---")
    try:
        s1 = float(input("Birinci sayı: "))
        islem = input("İşlem seçin (+, -, *, /): ")
        s2 = float(input("İkinci sayı: "))
        sonuc = None

        if islem == '+':
            sonuc = s1 + s2
        elif islem == '-':
            sonuc = s1 - s2
        elif islem == '*':
            sonuc = s1 * s2
        elif islem == '/':
            if s2 == 0:
                print("HATA: Sıfıra bölme yapılamaz.")
                return
            sonuc = s1 / s2
        else:
            print("HATA: Geçersiz işlem sembolü.")
            return

        print(f"Sonuç: {s1} {islem} {s2} = {sonuc}")

    except ValueError:
        print("HATA: Lütfen sayıları doğru formatta girin.")


# ==============================================================================
# 6 & 7. ARALIK VE SAYAC DÖNGÜLERİ
# ==============================================================================

def gorev_6_arttir_azalt():
    """+/- İşaretine Her Basıldığında Sayıyı Arttırma/Azaltma"""
    print("--- Görev 6: Artır/Azalt Sayacı (Çıkış için 'q') ---")
    sayac = 0
    print(f"Başlangıç değeri: {sayac}")
    while True:
        komut = input("Komut ('a': Artır, 'z': Azalt, 'q': Çıkış): ").lower()
        if komut == 'a':
            sayac += 1
            print(f"Yeni Değer: {sayac}")
        elif komut == 'z':
            sayac -= 1
            print(f"Yeni Değer: {sayac}")
        elif komut == 'q':
            break
        else:
            print("Geçersiz komut.")
    print(f"İşlem sonlandırıldı. Son değer: {sayac}")


def gorev_7_aralik_yazdirma():
    """+10 ile -10 Arasındaki Sayıları Ekrana Yazma"""
    print("--- Görev 7: +10 ile -10 Arasındaki Sayılar ---")
    # range(başlangıç, bitiş, adım)
    sayilar = list(range(-10, 11))
    print(" ".join(map(str, sayilar)))


# ==============================================================================
# 8, 15, 22, 26, 28, 29. STRING İŞLEMLERİ
# ==============================================================================

def gorev_8_virgul_ekleme():
    """Metindeki Her Harfin Arasına Virgül Koyma"""
    print("--- Görev 8: Harf Aralarına Virgül Koyma ---")
    metin = input("Lütfen bir metin girin: ")
    virgullu_metin = ', '.join(metin)
    print("Virgüllü Metin:", virgullu_metin)


def gorev_15_harf_donusumu():
    """Büyük Harfleri Küçük Harflere, Küçük Harfleri Büyük Harflere Dönüştürme"""
    print("--- Görev 15: Büyük/Küçük Harf Dönüşümü ---")
    metin = input("Lütfen dönüştürmek istediğiniz metni girin: ")
    donusmus_metin = metin.swapcase()
    print("Dönüşmüş Metin:", donusmus_metin)


def gorev_22_sesli_harf_sayisi():
    """Metindeki Sesli Harf Sayısını Hesaplama"""
    print("--- Görev 22: Sesli Harf Sayısı Hesaplama ---")
    metin = input("Lütfen bir metin girin: ")
    sesli_harfler = 'aeıioöuü'
    sayac = 0
    for harf in metin.lower():
        if harf in sesli_harfler:
            sayac += 1
    print(f"Metindeki Sesli Harf Sayısı: {sayac}")


def gorev_26_en_uzun_kelime():
    """Metindeki En Uzun Kelimeyi Bulma"""
    print("--- Görev 26: En Uzun Kelimeyi Bulma ---")
    metin = input("Lütfen bir metin/cümle girin: ")
    kelimeler = metin.split()
    if not kelimeler:
        print("Metin boş.")
        return

    en_uzun_kelime = max(kelimeler, key=len)
    print(f"En Uzun Kelime: '{en_uzun_kelime}' ({len(en_uzun_kelime)} karakter)")


def gorev_28_kelimeleri_tersten_yazdirma():
    """Cümledeki Her Kelimeyi Tersten Yazdırma"""
    print("--- Görev 28: Kelimeleri Tersten Yazdırma ---")
    cumle = input("Lütfen bir cümle girin: ")
    kelimeler = cumle.split()
    ters_kelimeler = [kelime[::-1] for kelime in kelimeler]
    yeni_cumle = " ".join(ters_kelimeler)
    print("Ters Çevrilmiş Kelimelerle Cümle:", yeni_cumle)


def gorev_29_mors_alfabesi():
    """Metni Mors Alfabesine Çevirme"""
    print("--- Görev 29: Mors Alfabesi Çevirici ---")
    MORS_DICT = {'A': '.-', 'B': '-...', 'E': '.', 'M': '--', 'T': '-', ' ': '/'}  # Kısaltılmış sözlük
    metin = input("Mors'a çevrilecek metni girin (A, B, E, M, T dışındaki karakterler ? olacaktır): ").upper()

    mors_kodu = []
    for karakter in metin:
        mors_kodu.append(MORS_DICT.get(karakter, '?'))

    mors_sonuc = ' '.join(mors_kodu)
    print("Mors Kodu:", mors_sonuc)


# ==============================================================================
# 9 & 24. RASTGELE SAYILAR
# ==============================================================================

def gorev_9_rastgele_sayi_uretimi():
    """1 ile 100 Arasında Rastgele 10 Tam Sayı Üretip Dizi İçine Ekleme"""
    print("--- Görev 9: Rastgele 10 Sayı Üretme ---")
    rastgele_sayilar = [random.randint(1, 100) for _ in range(10)]
    print("Üretilen Rastgele Sayılar:", rastgele_sayilar)


def gorev_24_tekrarsiz_rastgele_sayi():
    """Tekrarsız Rastgele Sayı Üretme"""
    print("--- Görev 24: Tekrarsız Rastgele Sayı Üretme (1-49 arası 6 adet) ---")
    try:
        # random.sample, belirtilen aralıktan tekrarsız k adet eleman çeker
        tekrarsiz_sayilar = random.sample(range(1, 50), 6)
        tekrarsiz_sayilar.sort()
        print("Tekrarsız Sayılar:", tekrarsiz_sayilar)
    except ValueError:
        print("HATA: Aralıktan daha fazla sayı istediniz.")


# ==============================================================================
# 10, 19, 23, 30. DÖNGÜ VE LİSTE İŞLEMLERİ
# ==============================================================================

def gorev_10_bese_bolunenler():
    """-100 ile +100 Arasındaki 5’e Tam Bölünen Sayıları Yan Yana Gösterme"""
    print("--- Görev 10: -100 ile +100 Arası 5'e Bölünenler ---")
    sayilar = list(range(-100, 101, 5))
    print(" ".join(map(str, sayilar)))


def gorev_19_onbire_bolunenler():
    """1 ile 300 Arasındaki Sayılardan 11 Sayısına Bölünenleri Bulma"""
    print("--- Görev 19: 1 ile 300 Arası 11'e Bölünenler ---")
    bolunenler = [sayi for sayi in range(1, 301) if sayi % 11 == 0]
    print("11'e bölünen sayılar:", bolunenler)


def gorev_23_kendisi_kadar_yazdirma():
    """Her Sayıyı Kendisi Kadar Yan Yana Yazdırma"""
    print("--- Görev 23: Sayıyı Kendisi Kadar Yazdırma ---")
    try:
        N = int(input("Lütfen bir limit girin (Örn: 5): "))
        for i in range(1, N + 1):
            print(str(i) * i)
    except ValueError:
        print("HATA: Lütfen geçerli bir tam sayı girin.")


def gorev_30_kumulatif_toplam():
    """Kümülatif Toplam Hesaplama"""
    print("--- Görev 30: Kümülatif Toplam Hesaplama ---")
    veri_listesi = [4, 6, 2, 8, 1, 5]
    kumulatif_toplam = []
    gecici_toplam = 0
    for sayi in veri_listesi:
        gecici_toplam += sayi
        kumulatif_toplam.append(gecici_toplam)
    print("Veri Listesi:", veri_listesi)
    print("Kümülatif Toplam Listesi:", kumulatif_toplam)


# ==============================================================================
# 11, 16, 17, 20, 21, 27. MATEMATİKSEL & KARAR PROBLEMLERİ
# ==============================================================================

def gorev_11_sayi_siralama():
    """Üç Adet Sayıyı Karşılaştırıp Sıralama"""
    print("--- Görev 11: Üç Sayıyı Sıralama ---")
    try:
        s1 = float(input("Birinci sayı: "))
        s2 = float(input("İkinci sayı: "))
        s3 = float(input("Üçüncü sayı: "))
        sayilar = sorted([s1, s2, s3])
        print("Sıralanmış Sayılar (Küçükten Büyüğe):", sayilar)
    except ValueError:
        print("HATA: Lütfen geçerli sayılar girin.")


def gorev_12_faktoriyel():
    """Faktöriyel Hesaplama ve Açılımını Yazdırma"""
    print("--- Görev 12: Faktöriyel Hesaplama ---")
    try:
        sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin (n>=0): "))
        if sayi < 0:
            print("Faktöriyel negatif sayılar için tanımlı değildir.")
            return

        faktoriyel = 1
        acilim = ""
        for i in range(sayi, 0, -1):
            faktoriyel *= i
            acilim += str(i) + (" x " if i > 1 else "")

        print(f"{sayi}! Açılımı: {acilim}")
        print(f"{sayi}! Sonucu: {faktoriyel}")
    except ValueError:
        print("HATA: Lütfen geçerli bir tam sayı girin.")


def gorev_16_maas_zam_hesaplama():
    """Personel Maaşından Yüzdesel Zam Hesaplama"""
    print("--- Görev 16: Maaş Zam Hesaplama ---")
    try:
        maas = float(input("Mevcut maaşı girin: "))
        zam_orani = float(input("Uygulanacak zam oranını (%) girin: "))
        zam_miktari = maas * (zam_orani / 100)
        yeni_maas = maas + zam_miktari
        print(f"Zam Miktarı: {zam_miktari:,.2f} TL")
        print(f"Yeni Maaş: {yeni_maas:,.2f} TL")
    except ValueError:
        print("HATA: Lütfen geçerli sayısal değerler girin.")


def gorev_17_basamak_toplami():
    """Sayı Değerlerinin Toplamını Hesaplama (Basamak Toplamı)"""
    print("--- Görev 17: Basamak Toplamı ---")
    sayi = input("Basamaklarının toplamını istediğiniz sayıyı girin: ")
    toplam = sum(int(b) for b in sayi if b.isdigit())
    print(f"{sayi} sayısının basamak toplamı: {toplam}")


def gorev_20_final_notu_hesaplama():
    """Mutlak Sistemde Sınıfı Geçmek İçin Gereken Final Notunu Hesaplama"""
    print("--- Görev 20: Gerekli Final Notu Hesaplama (Vize %40, Final %60) ---")
    try:
        vize = float(input("Vize notunuzu girin: "))
        gecme = float(input("Gerekli geçme notunu girin: "))

        gerekli_final = (gecme - (vize * 0.4)) / 0.6

        if gerekli_final <= 0:
            print("Tebrikler! Vize notunuzla zaten geçme barajını yakaladınız.")
        elif gerekli_final > 100:
            print(f"Gerekli Final Notu: {gerekli_final:.2f}. Maalesef geçmeniz mümkün görünmüyor.")
        else:
            print(f"Sınıfı geçmek için Final'den almanız gereken minimum not: {gerekli_final:.2f}")
    except ValueError:
        print("HATA: Lütfen geçerli sayısal notlar girin.")


def gorev_21_ucgen_alani():
    """Üç Kenarı Girilen Üçgenin Alanını Hesaplama (Heron Formülü)"""
    print("--- Görev 21: Üçgen Alanı Hesaplama ---")
    try:
        a = float(input("1. Kenar: "))
        b = float(input("2. Kenar: "))
        c = float(input("3. Kenar: "))

        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            print("HATA: Girilen kenarlarla üçgen oluşturulamaz.")
            return

        s = (a + b + c) / 2  # Yarı çevre
        alan = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"Üçgenin Alanı: {alan:.2f}")

    except ValueError:
        print("HATA: Lütfen geçerli kenar uzunlukları girin.")


def gorev_27_harf_notu():
    """Girilen Bir Notun Harf Karşılığını Bulma"""
    print("--- Görev 27: Harf Notu Karşılığı ---")
    try:
        notu = float(input("Sayısal notunuzu girin (0-100): "))
        if 90 <= notu <= 100:
            harf = "AA"
        elif 80 <= notu < 90:
            harf = "BA"
        elif 70 <= notu < 80:
            harf = "BB"
        elif 60 <= notu < 70:
            harf = "CB"
        elif 50 <= notu < 60:
            harf = "CC"
        elif 0 <= notu < 50:
            harf = "FF"
        else:
            harf = "Geçersiz Not"

        print(f"Notunuz ({notu}) karşılığı: {harf}")
    except ValueError:
        print("HATA: Lütfen geçerli bir sayısal not girin.")


# ==============================================================================
# 25. ASAL VE MATEMATİK
# ==============================================================================

def gorev_25_asal_carpanlar():
    """Asal Çarpanlarını Bulma"""
    print("--- Görev 25: Asal Çarpanları Bulma ---")
    try:
        sayi = int(input("Asal çarpanlarını bulmak istediğiniz sayıyı girin (N > 1): "))
        if sayi <= 1:
            print("HATA: Lütfen 1'den büyük bir tam sayı girin.")
            return

        gecici_sayi = sayi
        asal_carpanlar = []
        bolen = 2

        while bolen * bolen <= gecici_sayi:
            if gecici_sayi % bolen == 0:
                asal_carpanlar.append(bolen)
                gecici_sayi //= bolen
            else:
                bolen += 1

        if gecici_sayi > 1:
            asal_carpanlar.append(gecici_sayi)

        print(f"{sayi} sayısının asal çarpanları: {asal_carpanlar}")

    except ValueError:
        print("HATA: Lütfen geçerli bir tam sayı girin.")


# ==============================================================================
# 13. İLK VE SON KELİME
# ==============================================================================

def gorev_13_ilk_son_kelime():
    """Metindeki İlk Kelime ile Son Kelimeyi Bulma"""
    print("--- Görev 13: İlk ve Son Kelimeyi Bulma ---")
    metin = input("Lütfen bir cümle girin: ")
    kelimeler = metin.split()

    if not kelimeler:
        print("Metin boş.")
        return

    print(f"İlk kelime: {kelimeler[0]}")
    print(f"Son kelime: {kelimeler[-1]}")


# ==============================================================================
# ANA MENÜ
# ==============================================================================

def main_menu():
    """Kullanıcının görev seçimi yapmasını sağlayan ana menü."""
    gorevler = {
        '1': gorev_1_metin_gosterme, '2': gorev_2_iki_sayi_toplama,
        '3': gorev_3_tek_cift_kontrol, '4': gorev_4_ve_5_hesap_makinesi,
        '6': gorev_6_arttir_azalt, '7': gorev_7_aralik_yazdirma,
        '8': gorev_8_virgul_ekleme, '9': gorev_9_rastgele_sayi_uretimi,
        '10': gorev_10_bese_bolunenler, '11': gorev_11_sayi_siralama,
        '12': gorev_12_faktoriyel, '13': gorev_13_ilk_son_kelime,
        '14': gorev_14_toplam_ve_ortalama, '15': gorev_15_harf_donusumu,
        '16': gorev_16_maas_zam_hesaplama, '17': gorev_17_basamak_toplami,
        '18': gorev_18_sonsuz_tek_cift, '19': gorev_19_onbire_bolunenler,
        '20': gorev_20_final_notu_hesaplama, '21': gorev_21_ucgen_alani,
        '22': gorev_22_sesli_harf_sayisi, '23': gorev_23_kendisi_kadar_yazdirma,
        '24': gorev_24_tekrarsiz_rastgele_sayi, '25': gorev_25_asal_carpanlar,
        '26': gorev_26_en_uzun_kelime, '27': gorev_27_harf_notu,
        '28': gorev_28_kelimeleri_tersten_yazdirma, '29': gorev_29_mors_alfabesi,
        '30': gorev_30_kumulatif_toplam,
    }

    while True:
        print("\n" + "=" * 50)
        print("PYTHON TEMEL PROGRAMLAMA GÖREVLERİ MENÜSÜ")
        print("=" * 50)
        print(" 1. Metin Gösterme             11. Sayı Sıralama")
        print(" 2. İki Sayı Toplama           12. Faktöriyel Hesaplama")
        print(" 3. Tek/Çift Kontrolü          13. İlk/Son Kelime Bulma")
        print(" 4. Basit Hesap Makinesi       14. Toplam/Ortalama Bulma")
        print(" 6. Artır/Azalt Sayacı         15. Harf Dönüşümü")
        print(" 7. -10/+10 Sayıları Yazdırma  16. Maaş Zam Hesaplama")
        print(" 8. Harf Araya Virgül Koyma    17. Basamak Toplamı")
        print(" 9. Rastgele 10 Sayı Üretme    18. Sonsuz Tek/Çift Kontrolü")
        print("10. 5'e Bölünenleri Yazdırma   19. 11'e Bölünenleri Bulma")
        print("20. Final Notu Hesaplama       21. Üçgen Alanı Hesaplama")
        print("22. Sesli Harf Sayısı          23. Kendisi Kadar Yazdırma")
        print("24. Tekrarsız Rastgele Sayı    25. Asal Çarpanları Bulma")
        print("26. En Uzun Kelimeyi Bulma     27. Harf Notu Karşılığı")
        print("28. Kelimeleri Tersten Yazdırma 29. Mors Alfabesi Çevirici")
        print("30. Kümülatif Toplam Hesaplama")
        print("---")
        secim = input("Lütfen çalıştırmak istediğiniz görevin numarasını girin (Çıkış için 'q'): ")

        if secim.lower() == 'q':
            print("Program sonlandırılıyor. Güle güle!")
            break

        if secim in gorevler:
            print("\n" + "-" * 50)
            gorevler[secim]()
            input("\nDevam etmek için Enter'a basın...")
        else:
            print("Geçersiz seçim. Lütfen listeden bir numara girin.")


if __name__ == "__main__":
    main_menu()