# ==========================================
# 1️⃣ Python Keyword ve Dosya Uzantıları Soruları
# ==========================================

print("Soru 1: Hangi keyword ile sınıf tanımlanır?")
print("Cevap: class")  # B şıkkı

print("Soru 2: Hangisi ile Python kodu yazılamaz?")
print("Cevap: chromepy")  # E şıkkı

print("Soru 3: Nesneye dayalı programlama ile ilgili değildir.")
print("Cevap: Bir sınıftan birden çok nesne türetilemez")  # C şıkkı

print("Soru 4: Python dosya uzantısı hangisidir?")
print("Cevap: .py")  # B şıkkı

print("Soru 5: Hangisi ile fonksiyon oluşturulur?")
print("Cevap: def fonksiyon1():")  # B şıkkı

print("Soru 6: Bir sınıftan yeni ve eşsiz bir örnek (instance) oluşturmak için hangisi gerekli?")
print("Cevap: constructors")  # C şıkkı

print("-" * 50)

# ==========================================
# 2️⃣ Yapıcı / Constructor / Initializer Örneği
# ==========================================
class Hayvan:
    def __init__(self, isim, yas):  # Constructor metot
        self.isim = isim
        self.yas = yas

    def getYas(self):
        return self.yas

    def getAd(self):
        return self.isim


h1 = Hayvan("dog", 2)
print("h1 in yaşı:", h1.getYas())
print("h1 in ismi:", h1.getAd())

h2 = Hayvan("cat", 3)
print("h2 in yaşı:", h2.getYas())
print("h2 in ismi:", h2.getAd())

print("-" * 50)

# ==========================================
# 3️⃣ OOP ile Basit Hesap Makinesi
# ==========================================
class Makine:
    "Hesap makinesi sınıfı"
    def __init__(self, a, b):
        self.deger1 = a
        self.deger2 = b

    def topla(self):
        "Toplama: a + b"
        return self.deger1 + self.deger2

    def carp(self):
        "Çarpma: a * b"
        return self.deger1 * self.deger2

    def cikar(self):
        return self.deger1 - self.deger2

    def bol(self):
        return self.deger1 / self.deger2


x = 5
y = 2
h = Makine(x, y)
tSonuc = h.topla()
cSonuc = h.carp()
print("Toplama sonucu: {}, Çarpma sonucu: {}".format(tSonuc, cSonuc))
print("Çıkarma sonucu:", h.cikar())
print("Bölme sonucu:", h.bol())
