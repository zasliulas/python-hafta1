# ==========================================
# 1️⃣ Print Fonksiyonu ve Built-in Fonksiyonlar
# ==========================================
print("sinan")
print("sinan", "başarlan", "T", "B", "M", sep='.')

# ==========================================
# 2️⃣ Değişkenler ve Veri Tipleri
# ==========================================
a = "ali"
b = 5

print(type(a))  # <class 'str'>
print(type(b))  # <class 'int'>

# Tek satırlık yorum: #
# Çoklu yorum için üçlü tırnak kullanılabilir:
"""
Bu birden fazla satırlı yorumdur.
"""

# Veri tipleri örnekleri
a = 5           # int (tam sayı)
b = "sinan"     # str (string)
c = 3.5         # float (ondalık)
d = 'k'         # karakter

# ==========================================
# 3️⃣ Veri Yapıları (list, tuple, dict, set)
# ==========================================

# Liste (mutable)
liste1 = [1, 3, 3, 5, 4, 5, 4, "ali", "canan"]
print(liste1[0])        # ilk eleman
print(len(liste1))      # eleman sayısı
print(dir(liste1))      # liste üzerinde kullanılabilecek metotlar

liste2 = [1, 3, 3, 5, 4, 5, 4]
liste2.sort()           # sıralama
print(liste2)
liste2[0] = 100000      # değiştirilebilir
print(liste2)

liste2.pop()            # son elemanı sil
liste2.append(25)       # sona eleman ekle
liste2.insert(7, "25")  # 7. indise eleman ekle
print(liste2)

# Tuple (immutable)
demet = ("ali", "ayşe")
print(demet)
print(len(demet))
print(demet[0])
print(dir(demet))
print(demet.count("ali"))
print(demet.index("ali"))

# ==========================================
# 4️⃣ Fonksiyon Tanımlama ve Kullanma
# ==========================================

def selam():
    print("selam")

selam()  # parametresiz fonksiyon

def selamGotur(isim):
    print("Selam", isim)

selamGotur("sinan")  # parametreli, değer döndürmeyen

def topla(a, b):
    c = a + b
    return c

print("Toplam:", topla(3, 5))

def kareal(a):
    return a * a

sonuc = kareal(4)
print("İstenilen değerin karesi:", sonuc)

# ==========================================
# 5️⃣ Kullanıcıdan Girdi Alma ve İşlem Yapma
# ==========================================
# Not: input() kullanımı için PyCharm terminalinden veri girilir.

# a = int(input("1. sayıyı giriniz: "))
# b = int(input("2. sayıyı giriniz: "))

def cikar(x, y):
    return x - y

print("5 - 3 =", cikar(5, 3))

# ==========================================
# 6️⃣ Lambda (Kısa Fonksiyon Tanımlama)
# ==========================================

kare = lambda x: x * x
print("Lambda kare:", kare(6))

toplama = lambda x, y: x + y
print("Lambda toplama:", toplama(5, 5))

# ==========================================
# 7️⃣ Modül Kullanımı (math, random, time)
# ==========================================

import math
print("Karekök (sqrt):", math.sqrt(16))
print("Üs alma (pow):", math.pow(2, 3))
print("Sinüs 60:", math.sin(math.radians(60)))

import random
rastgele = random.randint(1, 100)
print("Rastgele sayı:", rastgele)

import time
print("Bekleniyor...")
time.sleep(1)
print("Devam!")

# ==========================================
# 8️⃣ Mini Uygulama: Tahmin Oyunu
# ==========================================

import random
import time

rastgele = random.randint(1, 100)
hak = 5

print("=== Tahmin Oyunu ===")
while True:
    tahmin = int(input("1-100 arasında tahmin yap: "))
    print("Kontrol ediliyor...")
    time.sleep(1)

    if tahmin == rastgele:
        print("Tebrikler! Doğru tahmin:", tahmin)
        break
    elif tahmin < rastgele:
        hak -= 1
        print("Daha büyük bir sayı girin.")
    elif tahmin > rastgele:
        hak -= 1
        print("Daha küçük bir sayı girin.")
    else:
        print("Lütfen 1-100 arasında bir sayı girin.")

    if hak == 0:
        print("Tahmin hakkınız bitti! Doğru sayı:", rastgele)
        break
