# ==========================================
# 1️⃣ Encapsulation Tanımı Örneği
# ==========================================
print("1. Soru: Encapsulation tanımı")
print(
    "C şıkkı doğru: Bir nesnenin metot ve verilerini diğer nesnelerden saklayarak erişime engelleyerek yanlış kullanımı engellemektir.\n")

# ==========================================
# 2️⃣ Miras Alma Örneği
# ==========================================
print("2. Soru: Miras alma örneği")


class A:
    def __init__(self, a):
        print("A sınıfı oluşturuldu")

    def ilk(self):
        print("İlk isimli metot")


class B(A):
    def __init__(self, j=10):
        self.j = j


# Nesneler
b = B()
print("B sınıfı A sınıfından miras alır, ama tüm A özelliklerini __init__ ile almaz.")
# Not: A.__init__ çağrılmadığı için 'A sınıfı oluşturuldu' yazısı çıkmaz.

print("-" * 50)

# ==========================================
# 3️⃣ Soyut Sınıf Tanımı Örneği
# ==========================================
print("3. Soru: Soyut sınıf tanımı")
print("B şıkkı doğru: OOP de nesnesi olmayan sınıflara verilen isim.\n")

# ==========================================
# 4️⃣ Overriding Örneği
# ==========================================
print("4. Soru: Kod çıktıları")


class Animal:
    def sesVer(self):
        print("ses çıkarırlar")


class Kedi(Animal):
    def sesVer(self):  # Ata sınıfı ezdi (overriding)
        print("miyav")


# Nesneler ve çıktı
a = Animal()
print("a.sesVer() çıktısı:")
a.sesVer()  # → "ses çıkarırlar"

k = Kedi()
print("k.sesVer() çıktısı:")
k.sesVer()  # → "miyav"
