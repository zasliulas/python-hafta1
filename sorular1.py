# ----------------------------------------------------
# 1. Soru: Öğrenci Sınıfı
# ----------------------------------------------------
class Ogrenci:
    def __init__(self, ad, soyad, numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara

    def bilgileri_yazdir(self):
        print(f"Ad: {self.ad}, Soyad: {self.soyad}, Numara: {self.numara}")


# Kullanım
print("1. Soru Çıktısı:")
ogrenci1 = Ogrenci("Aslı", "Ulaş", 123)
ogrenci1.bilgileri_yazdir()
print("-" * 40)


# ----------------------------------------------------
# 2. Soru: Araba Sınıfı
# ----------------------------------------------------
class Araba:
    def __init__(self, marka, model, yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def calistir(self):
        print(f"{self.marka} {self.model} çalıştı!")

# Kullanım
print("2. Soru Çıktısı:")
araba1 = Araba("Toyota", "Corolla", 2020)
araba1.calistir()
print("-" * 40)


# ----------------------------------------------------
# 3. Soru: Kare Sınıfı
# ----------------------------------------------------
class Kare:
    def __init__(self, kenar):
        self.kenar = kenar

    def alan_hesapla(self):
        return self.kenar ** 2

    def kareyi_yazdir(self):
        print(f"Kare kenarı: {self.kenar}, Alan: {self.alan_hesapla()}")

# Kullanım
print("3. Soru Çıktısı:")
kare1 = Kare(5)
kare1.kareyi_yazdir()
print("-" * 40)


# ----------------------------------------------------
# 4. Soru: Hesap Makinesi Sınıfı
# ----------------------------------------------------
class HesapMakinesi:
    def topla(self, sayi1, sayi2, sayi3=None):
        if sayi3 is not None:
            return sayi1 + sayi2 + sayi3
        else:
            return sayi1 + sayi2

# Kullanım
print("4. Soru Çıktısı:")
hesap_makinesi = HesapMakinesi()
print("İki sayının toplamı:", hesap_makinesi.topla(10, 20))
print("Üç sayının toplamı:", hesap_makinesi.topla(10, 20, 30))
print("-" * 40)


# ----------------------------------------------------
# 5. Soru: Merhaba Sınıfı
# ----------------------------------------------------
class Merhaba:
    def merhaba_yazdir(self):
        print("Merhaba Dünya")

# Kullanım
print("5. Soru Çıktısı:")
merhaba = Merhaba()
merhaba.merhaba_yazdir()
print("-" * 40)
