#!/bin/py

#module
import os,sys,time,requests
from time import sleep

#tampilan
os.system("clear")
os.system("figlet kalkulator")
tampilan ="""
===========================================================
=       (+)Author     : Reza Alfauzan                     =
=       (+)Github     : https://github.com/GRCR4K3R       =
=       (+)Youtube    : Reja Gaming                       =
=       (+)Pesan      : Jangan Recode Mas:)               =
=       (+)Pesan      : Gua Masih Noob:'(                 =
=              (+)===  Welcome To Termux ===(+)           =
===========================================================
(+)=====================================================(+)
(+)==================== Jangan Recode Mas ==============(+)
(+)=====================================================(+)"""
sleep(0.1)
print(tampilan)
print("")
print("1)Pertambahan")
print("2)Pengurangan")
print("3)Perkalian")
print("4)Pembagian")
print("_______________________")
pilih =input("Pilih Salah Satu :")

#Data Pertambahan
if pilih =="1":
        angka1 =int(input("Angka Pertama :"))
        angka2 =int(input("Angka Kedua :"))
        print(angka1 + angka2)
#Data Pengurangan
if pilih =="2":
        angka1 =int(input("Angka Pertama :"))
        angka2 =int(input("Angka Kedua : "))
        print(angka1 - angka2)
#Data Perkalian
if pilih =="3":
        angka1 =int(input("Angka Pertama :"))
        angka2 =int(input("Angka Kedua :"))
        print(angka1 * angka2)
#Data Pembagian
if pilih =="4":
        angka1 =int(input("Angka Pertama :"))
        angka2 =int(input("Angka Kedua :"))
        print(angka1 / angka2)
