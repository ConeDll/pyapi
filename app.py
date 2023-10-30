import base64
from colorama import Fore
import colorama
import os
import pyperclip
import requests
from tqdm import tqdm
import time

import os
import subprocess
colorama.init()

def print_slow(str):
    for letter in str:
        print(letter)
        time.sleep(.1)



version_link = 'https://raw.githubusercontent.com/ConeDll/pyapi/main/app.py'
r = requests.get(version_link)
response_version = r.content.decode()
with open('alfabe.py','r') as g:
    veri = g.read()
if float(veri) < float(response_version):
    with open('alfabe.py','w') as f:
        f.write(str(response_version))
        f.close()

    for i in tqdm (range (101), 
               desc='Güncelleniyor', 
               ascii=False, ncols=75):
        time.sleep(0.01)
    print_slow(Fore.GREEN+'Güncelleme Tamamlandı')
    print_slow(Fore.GREEN+'Sistem Yeniden Başlatılıyor...')
    os.systyem('python alfabe.py')
    os.system(exit)
alfabe = {
    'a': '3K',
    'b': '1Mü',
    'c': 'ZKş',
    'ç': '=Kö',
    'd': 'MM-ç',
    'e': '8ıl',
    'f': '10xg',
    'g': 'mxaf',
    'ğ': '#Lh',
    'h': 'ZjA',
    'ı': 'l@yl',
    'i': 'ay@b',
    'j': 'gnl@',
    'k': 'zn',
    'l': '4k',
    'm': 'z/r',
    'n': '--aq',
    'o': 'xcazo',
    'ö': 'rt',
    'p': 'hll',
    'r': '1vz',
    's': 'xcw',
    'ş': 'kxk',
    't': 'y3QX',
    'u': 'zA==',
    'ü': 'mtaa',
    'v': 'hj8ü',
    'y': 'Ssc',
    'z': 'ekkk',
    '0': 'kma+',
    '1': 'UK--',
    '2': 'XC==',
    '3': 'zxa!',
    '4': 'xs+f-*',
    '5': 'e4mk',
    '6': '19M',
    '7': 'z-1d',
    '8': 'hmloo',
    '9': 'pcv',
    '-': 'w@M_',
    '+': 'DDLL-_',
    '/': ':&',
    '*': 'zxGk8',
    '.': 'UM0k',
    ',': 'zÇş',
    '@': 'zscaS',
    '#': 'eteta',
    '"': 'dsaasd',
    '|': '452',
    '!': 'ccc',
    '<': 'KK)m',
    '>': 'Zxd',
    '=': 'ASD00',
    '(': '3M1500S',
    ')': 'gvt',
    '{': 'NMUER',
    '}': 'zdf',
    '[': 'kmma',
    ']': 'no12',
}

def sifrele(mesaj, alfabe):
    sifreli_mesaj = ''
    for harf in mesaj:
        if harf in alfabe:
            sifreli_mesaj += alfabe[harf]
        else:
            sifreli_mesaj += harf
    return sifreli_mesaj

def coz(mesaj, alfabe):
    orijinal_mesaj = ''
    i = 0
    while i < len(mesaj):
        found = False
        for harf, kod in alfabe.items():
            if mesaj[i:i + len(kod)] == kod:
                orijinal_mesaj += harf
                i += len(kod)
                found = True
                break
        if not found:
            orijinal_mesaj += mesaj[i]
            i += 1
    return orijinal_mesaj

while True:
    secim = input(f"{Fore.YELLOW}Ne yapmak istersiniz?{Fore.WHITE}\n\n\n\n 1- Metni kodla\n2 - Metni çöz\n3 - Temizle\n4 - Çıkış\nSeçiminiz: ")

    if secim == '1':
        mesaj = input("Metni girin: ")
        sifreli_metin = sifrele(mesaj, alfabe)
        print("Şifrelenmiş Metin:", Fore.LIGHTCYAN_EX + sifreli_metin + Fore.WHITE)
        pyperclip.copy(sifreli_metin)
    elif secim == '2':
        mesaj = input("Şifrelenmiş metni girin: ")
        orijinal_metin = coz(mesaj, alfabe)
        print("Orijinal Metin:"+ Fore.LIGHTCYAN_EX + orijinal_metin+ Fore.WHITE)
    elif secim == '3':
        os.system('cls' if os.name == 'nt' else 'clear')
    elif secim == '4':
        exit()
    else:
        print("Geçersiz seçenek!")

         
