#!/usr/bin/env python

import os

os.system("Terminal=true")
os.system("Type=Application")
os.system("Name[en_US]=ssh")
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet BILGI TOPLAMA")

print(""""

Bilgi Toplama Aracina Hos Geldiniz

        egeorcun
          v1.0

""")
number = input("Programa baslamak icin 1 yaziniz: ")

targetdomain = input("""

Hedef site ise, linkini girin degilse enter'a basin

               ex(www.google.com)           : """) 

os.system("nslookup " + targetdomain)

targetip = input("Hedefin ip adresini girin: ")

if(number == "1"):
    os.system(str('gnome-terminal --tab --title= "ike-scan" -e "bash -c \\"figlet  VPN?; echo dirtysoul; ike-scan ') + str(targetip) + str(';  exec bash\\""'))
    os.system(str('gnome-terminal --tab --title= "firewall_tespit" -e "bash -c \\"figlet Firewall Tespit; echo dirtysoul; wafw00f ') + str(targetdomain) + str(';  exec bash\\""'))
    os.system(str('gnome-terminal --tab --title= "dmitry" -e "bash -c \\"figlet dmitry; echo dirtysoul; dmitry -i ') + str(targetdomain) + str(';  exec bash\\""'))
    os.system(str('gnome-terminal --tab --title= "dirb" -e "bash -c \\"figlet DIRB-1; echo dirtysoul; dirb ') + str("https://") + str(targetdomain) + str(';  exec bash\\""'))
    os.system(str('gnome-terminal --tab --title= "dirb" -e "bash -c \\"figlet DIRB-2; echo dirtysoul; dirb ') + str("http://") + str(targetdomain) + str(';  exec bash\\""'))
    os.system(str('gnome-terminal --tab --title= "nikto" -e "bash -c \\"figlet NIKTO; echo dirtysoul; nikto -h ') + str(targetip) + str(';  exec bash\\""'))
    os.system(str('gnome-terminal --tab --title= "golismero" -e "bash -c \\"figlet Golismero; echo dirtysoul; golismero scan ') + str(targetdomain) + str(';  exec bash\\""'))
    os.system(str('gnome-terminal --tab --title= "nmap" -e "bash -c \\"figlet NMAP; echo dirtysoul; nmap -sV -T4 -O -F --version-light ') + str(targetip or targetdomain) + str(';  exec bash\\""'))
    os.system(str('gnome-terminal --tab --title= "joomscan" -e "bash -c \\"figlet  joomscan; echo dirtysoul; joomscan -u ') + str(targetip) + str(';  exec bash\\""'))
    
    os.system("clear")
    os.system("figlet BILGI TOPLAMA")
    os.system("nslookup " + targetdomain)
1
