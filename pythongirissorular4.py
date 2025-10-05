# ==========================================
# 1️⃣ Encapsulation Örneği - Public Değişken Sorunu
# ==========================================
class Banka:
    def __init__(self, isim, para, adres):
        self.isim = isim   # public
        self.para = para   # public
        self.adres = adres

# Nesneler
hesap1 = Banka("Sinan", 1000, "İstanbul")
hesap2 = Banka("Ayşe", 5000, "Erzurum")

print("Hesap1 parası:", hesap1.para)
# Hesap2, Hesap1 parasını alıyor
hesap2.para = hesap2.para + hesap1.para
hesap1.para = 0  # Burada kullanıcı direkt erişip değiştirebilir
print("Hesap1 parası sıfırlandı:", hesap1.para)
print("Hesap2 parası arttı:", hesap2.para)

# ==========================================
# 2️⃣ Encapsulation Örneği - Private Attribute
# ==========================================
class Banka2:
    def __init__(self, isim, para, adres):
        self.__isim = isim   # private
        self.__para = para   # private
        self.__adres = adres # private

    # getter
    def getPara(self):
        return self.__para

    # setter
    def setPara(self, miktar):
        self.__para = miktar

    # işlem metodu
    def islemSayisi(self):
        self.__para -= 10

# Nesneler
hes1 = Banka2("Sinan", 1000, "İstanbul")
hes2 = Banka2("Ayşe", 5000, "Erzurum")

print("1. hesaptaki para:", hes1.getPara())
hes1.setPara(100)
print("Set işlemi sonrası 1. hesaptaki para değişimi:", hes1.getPara())

hes1.islemSayisi()
print("İşlem ücreti sonrası 1. hesaptaki para:", hes1.getPara())

# ==========================================
# 3️⃣ Miras Alma Örneği (Inheritance)
# ==========================================

# Ata sınıf / Parent
class Animal:
    def __init__(self):
        print("Hayvan sınıfının yapıcı metodu çalıştı")

    def sesCikar(self):
        print("hav, miyav, vak...")

    def hareket(self):
        print("Zıplar, koşar, yürür...")

# Çocuk sınıf / Child
class Kedi(Animal):
    def __init__(self):
        super().__init__()  # Ata sınıfın __init__ metodunu çağırır
        print("Kedi sınıfı oluşturuldu")

    # Metot overriding
    def sesCikar(self):
        print("Miyav")

    # Kediye özel metot
    def dokuzCan(self):
        print("Bu sevimli hayvanlar hep dört ayak üstüne düşer")

k1 = Kedi()
k1.sesCikar()   # Override edilmiş metot
k1.hareket()    # Ata sınıf metodu
k1.dokuzCan()   # Kediye özel metot

# Başka bir çocuk sınıf
class Kus(Animal):
    def __init__(self):
        print("Kuş sınıfı oluşturuldu")

    def ucma(self):
        print("Kanatları vardır, uçarlar")

kus1 = Kus()
kus1.ucma()
kus1.hareket()
