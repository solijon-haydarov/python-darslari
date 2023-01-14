# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 21:33:40 2023

@author: Solijon Haydarov

Sonlar bilan ishlash 
"""
# int - integer butun sonlar
# float - o'nlik son, sonning butun va o'nlik qismi nuqta bilan ajratiladi bu butun jahonda shunaqa
# type o'zgaruvchilarni turini ko'rsatadi
# a = 5
# b = 1.2
# print(type(a))
# print(type(b))

#katta sonlarni pythonda bo'lib bo'li yozish mumkin

# katta_son = 7_654_321_000
# print(katta_son)

#O'zgaruvchilarga biradan qiyma berish mumkin

# x, y, z = 10, 5.5, -56


#float va integer son qo'shilganda doimo float turiga aylanadi

# c = a*b
# print(c)

#CONSTAT qiymatlar ya'ni o'zgaramas qiymatlar

#kostatnt qiymat yaratish uchun o'zgaruvchini ismi katta harflarda yozilishi kerak

radius = 20
PI = 3.14
diametr = 2*radius
print("Aylana uzunligi=", PI*diametr)


ism = "Solijon"
yosh = 30
xabar = ism + " " + str(yosh) + ' yoshda'
print(xabar)

# #Foydalanuvchining yoshini hisoblovchi dastur

t_yil = int(input("Tug'ilgan yilingizni kiriting  "))
yosh = 2023 - t_yil
print("Siz ", yosh, " yoshda ekansiz" )



#Uyga Vazifa
#Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
number = int(input("Son kiriting  "))
kvadrat = number**2
kub = number**3
#print(f"Siz kiritgan sonning kvadrati {kvadrat} ga teng \nkubi esa {kub}")


#Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
age = int(input("Yoshingiz nechada? "))
t_yili = 2023-age
print(f"Siz {t_yili} da tug'ilgansiz")


#Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
a = float(input("Birinchi sonni kiriting  "))
b = float(input("Ikkinchi sonni kiriting  "))
print(f"{a}+{b}=", a+b)
print(f"{a}-{b}=", a-b)
print(f"{a}x{b}=", a*b)
print(f"{a}/{b}=", a/b)















