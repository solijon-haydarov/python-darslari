# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 21:33:40 2023

@author: Solijon Haydarov

Lists Ro'yhatlar 
"""
mevalar = ['olma', 'gilos', 'shaftoli', 'anor'] #mevalar ro'yhati
narxlar = [1200, 6500, 7800, 9500, 10200, -6.5, 99.9] #sonlar ro'yhati
ismlar = []#bo'sh ro'yhat

#RO'YHAT ichidagi har bir qiymat ro'yhat elementi deyiladi
#ro'yhatning elementini chaqirib olish
print("birinchi meva: ", mevalar[0] )#dasturlashda indexlash ya'ni sanash noldan boshlanadi
print("uchinchi meva: ", mevalar[2])
print("oxirgi meva: ", mevalar[-1])#eng oxirgi elementni chiqarish
print(mevalar[1].upper())#matnga oid har qanday metodlarni qo'llashimiz mumkin ro'yhatga

#ro'yhatga o'zgartirish kiritish
mevalar[0] = 'mandarin'
print(mevalar[0])

# Ro'yhadni .append() metodi yordamida to'ldirish mumkin
mevalar.append('xurmo')#append oxiridan to'ldiradi
print(mevalar)
mevalar.append('olma')
print(mevalar)

#ro'yhatni xoxlagan joyidan qo'shish uchun insert metodidan foydalaniladi
mevalar.insert(3, 'limon')
print(mevalar)

#ro'yhatlarni nomlashda ko'plik qo'shimchasidan foydalangan ma'qul

cars = []
cars.append('toyota')
cars.append('BMW')
cars.append('chevrolet')
cars.append('mersedes')
print(cars)

#ro'yhat ichidan elementni del operatori yordamida o'chirish mumkin
del cars[2]
print(cars)
cars.insert(0, 'Hyundai')
print(cars)

#ro'yhatdagi elementni indeksi aniq bo'lmasa nomi bilan o'chirish mumkin
cars.remove('toyota')
print(cars)
#remove metodi faqatgina eng birinchi uchragan qiymatni o'chirib tashlaydi


#Ro'yhatni ichidan element sug'urib olish

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(1)#ro'yhatdan boshqa ro'yhatga sug'urib olish
print("Men " + mahsulot + " sotib oldim")
print("olinmagan mahsulotlar ", bozorlik)

#pop metotidan foydalanganda hechqanaqa index berilmasa ro'yhat oxiridan sug'irib oladi
mahsulot = bozorlik.pop()
print(mahsulot)




#Uyga Vazifa

#ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ['Ubaydulla', 'Husanjon', 'Bilolbek']

#Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
print("Salom " + ismlar[0] + " bugun fudbolga boramizmi")
print(ismlar[1] + " choyhona qachon?")
print(ismlar[2] + " moshinani narxi nega oshayapti?")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [22, -58.2, 34.0, 67, 1983, 123_456_678_000, 112.4]
print(sonlar)

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
sonlar[0] = sonlar[0]+sonlar[-1]
sonlar[1] = -67.8
sonlar[4] = sonlar[4] + 37
del sonlar[5]
print(sonlar)

#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']


#Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
suhbat qilishni istar edim\n")














  