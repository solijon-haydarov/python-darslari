# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 21:33:40 2023

@author: Solijon Haydarov

Matn bilan ishlash 
"""

# UNICODE bu barcha qurilmalar tomonidan katta jadval yoki alfabet


#String ustida amallar

ism = 'Solijon'
familia = 'Haydarov'

# + operatori yordamida matnlarni bir biriga qo'shishimiz mumkin

print(ism, ' ' + familia)

# f '' string 

ism = 'Ubaydulla'
familiya = 'Jumayev'

print(f'Salom mening ismim {ism} familiyam esa {familiya}')


#Mahsus Belgilar

print("Hello world") #oddiy usulda
print('hello \tworld') #joy tashlaydi 
print("Hello \nworld") #qator tashlaydi


#STRING METODLARI

#metod chaqirish uchun nuqta va metod nomidan foydalanamiz
#Metod qo'llanganda bizni o'zgaruvchini ichidagi asl matn o'zgarmaydi

print("assalomu Aleykum".upper())# metod yozish

ism = 'karim'
familia = 'benzema'
ism_sharif = f'{ism} {familia}'
print(ism_sharif.capitalize())
print(ism_sharif.casefold())
print(ism_sharif.upper())
print(ism_sharif.lower())
print(ism_sharif.title())


#INPUT

#foydalanuvchidan ma'lumot olish uchun input f-yasidan foydalanamiz

ism = input('Ismingizni kiriting: ') #foydalanuvchidan matn kiritishni talab qiladi
#print(ism.capitalize())
print(f"Assalomu Aleykum {ism.title()}")


#Uyga vazifa


#Quyidagi o'zgaruvchilarni yarating:
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"

#Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
#Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati ")

#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
print("Iltimos, quyidagi ma'lumotlarni kiriting:")
kocha = input("Ko'changiz: ")
mahalla = input("Mahallangiz: ")
tuman = input("Tumaningiz: ")
viloyat = input("Viloyatingiz: ")
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati")   
    
# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing
print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + \
      tuman + " tumani,\n" + viloyat + " viloyati")
    
# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)


#manzil ga biz yuqorida o'rgangan metodlarni qo'llab ko'ring.
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())



 
