# ==========================================
# 1️⃣ Basit Değişken Örnekleri
# ==========================================
a = 5
string = "dogus"

isci_ismi = "ali"
isci_yas = 50
isci_adres = "Üsküdar"
isci_kurum = "dogus"

# Not: Her çalışan için ayrı değişken tanımlamak yerine sınıf kullanılır

# ==========================================
# 2️⃣ Sınıf Yapısı - Temel
# ==========================================
class Calisan:
    # Özellikler; yaş, adres, tc, ad, soyad, vs
    # Metotlar/davranışlar; çalışma, terfi alma, vs
    pass  # İçerik sonradan oluşturulacak

# Nesne türetme
calisan1 = Calisan()
print(calisan1)  # <__main__.Calisan object at ...> şeklinde çıktı verir

# ==========================================
# 3️⃣ Sınıf Öznitelikleri (Attribute/Property)
# ==========================================
class Arac:
    renk = "sarı"
    model = "jeep"
    marka = "kia"

a1 = Arac()
print("Nesne:", a1)
print("Marka:", a1.marka)
print("Model:", a1.model)
print("Renk:", a1.renk)

# Nesne üzerinden öznitelik değiştirme
a1.marka = "BMW"
print("Yeni Marka:", a1.marka)

# ==========================================
# 4️⃣ Sınıf Metotları
# ==========================================
class Kare:
    kenar = 10  # metre

    def alan(self):
        alan = self.kenar * self.kenar
        print("Alan:", alan)

k1 = Kare()
print("Nesne:", k1)
print("Kenar:", k1.kenar)
k1.alan()  # Metodu çağırma

# ==========================================
# 5️⃣ Metot Örneği - İşçi
# ==========================================
class Isci:
    yas = 20
    maas = 1000

    def yasaGoreMaasOranla(self):
        oran = self.yas / self.maas
        print("Yaş/Maaş Oranı:", oran)

isci1 = Isci()
isci1.yasaGoreMaasOranla()

# Class dışı metot örneği
def yasMaasOrani(yas, maas):
    a = yas / maas
    print("Oran:", a)

yasMaasOrani(20, 2000)
