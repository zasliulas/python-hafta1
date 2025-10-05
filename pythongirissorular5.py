# ==========================================
# 1️⃣ Soyut Sınıf / Abstract Class Örneği
# ==========================================
from abc import ABC, abstractmethod

# Soyut sınıf
class Animal(ABC):
    @abstractmethod
    def yurume(self):
        pass

    @abstractmethod
    def kosma(self):
        pass

# Çocuk sınıf
class Kus(Animal):
    def __init__(self):
        print("Kuş oluşturuldu")

    def yurume(self):
        print("Kuşlar pek yürümez")

    def kosma(self):
        print("Kuşlar pek koşmaz")

# Nesne oluşturma
# a = Animal()  # Soyut sınıflardan direkt nesne oluşturulamaz
b = Kus()
b.kosma()
b.yurume()

print("-" * 50)

# ==========================================
# 2️⃣ Overriding Örneği
# ==========================================
class Animal2:
    def sesVer(self):
        print("Ses çıkarırlar")

class Kedi(Animal2):
    def sesVer(self):  # Ata sınıf metodu ezildi
        print("Miyav")

a = Animal2()
a.sesVer()

k = Kedi()
k.sesVer()

print("-" * 50)

# ==========================================
# 3️⃣ Polymorphism / Çok Biçimlilik Örneği
# ==========================================
class Hayvanlar:
    def __init__(self, isim):
        self.isim = isim

    def tepki(self):
        raise NotImplementedError("Subclass bunu implemente etmeli")

class Kedi(Hayvanlar):
    def tepki(self):
        return "Miyav!"

class Kopek(Hayvanlar):
    def tepki(self):
        return "Haav! Hav!"

hayvan_listesi = [Kedi('Boncuk'), Kedi('Tekir'), Kopek('Elmas')]

for hyvn in hayvan_listesi:
    print(hyvn.isim + ': ' + hyvn.tepki())

print("-" * 50)

# ==========================================
# 4️⃣ Polymorphism Örneği - Farklı Hayvan Sınıfları
# ==========================================
class Animal3:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal3):
    def talk(self):
        return "Meow!"

class Dog(Animal3):
    def talk(self):
        return "Woof! Woof!"

animals = [Cat('Missy'), Cat('Mr. Mistoffelees'), Dog('Lassie')]

for animal in animals:
    print(animal.name + ': ' + animal.talk())
