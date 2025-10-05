# ----------------------------------------------------
# İnsan - Hoca - Sekreter - Öğrenci Sınıfı Örneği
# ----------------------------------------------------

# Üst sınıf
class Insan:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

    def konus(self):
        print(f"{self.ad}: Merhaba, ben bir insanım.")


# Alt sınıf: Hoca
class Hoca(Insan):
    def __init__(self, ad, yas, sicil_no):
        super().__init__(ad, yas)
        self.sicil_no = sicil_no

    def konus(self):
        print(f"{self.ad}: Merhaba, ben bir hocayım. Derse hoş geldiniz!")

    def ders_ver(self):
        print(f"{self.ad} ({self.sicil_no}) şu anda ders veriyor.")


# Alt sınıf: Sekreter
class Sekreter(Insan):
    def __init__(self, ad, yas, departman):
        super().__init__(ad, yas)
        self.departman = departman

    def konus(self):
        print(f"{self.ad}: Merhaba, ben {self.departman} departmanında sekreterim.")

    def randevu_ayarla(self):
        print(f"{self.ad}: Yeni bir randevu başarıyla ayarlandı.")


# Alt sınıf: Öğrenci
class Ogrenci(Insan):
    def __init__(self, ad, yas, ogr_no):
        super().__init__(ad, yas)
        self.ogr_no = ogr_no

    def konus(self):
        print(f"{self.ad}: Merhaba, ben bir öğrenciyim!")

    def ders_calıs(self):
        print(f"{self.ad} ({self.ogr_no}) şu anda ders çalışıyor.")


# ----------------------------------------------------
# Kullanım
# ----------------------------------------------------
print("=== İnsan, Hoca, Sekreter, Öğrenci Örneği ===")

insan = Insan("Ahmet", 40)
insan.konus()
print("-" * 40)

hoca = Hoca("Ayşe Hoca", 45, "H123")
hoca.konus()
hoca.ders_ver()
print("-" * 40)

sekreter = Sekreter("Meltem", 30, "Mühendislik Fakültesi")
sekreter.konus()
sekreter.randevu_ayarla()
print("-" * 40)

ogrenci = Ogrenci("Aslı", 20, "2021001")
ogrenci.konus()
ogrenci.ders_calıs()
print("-" * 40)
