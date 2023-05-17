import os
import requests as req,re,time,pyotp,os,sys
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tdp
try:
	

	import pyotp
except ModuleNotFoundError:
	os.system('pip install pyotp')
import requests as req, re,time,os,random
from bs4 import BeautifulSoup as par
jh=[]
logo=("""
\033[1;32m╔══════════╦═════════════════════════════════╗\033[1;32m
║\033[1;36m╦═╗═╗ ╦╔═╗\033[1;32m║\033[1;36mOWNER: REYAD AND SHIPU \033[1;32m          ║\033[1;32m
║\033[1;36m╠╦╝╔╩╦╝╚═╗\033[1;32m║\033[1;36mFACEBOOK: MD REYAD HOSSAIN SHANTO\033[1;32m║\033[1;32m
║\033[1;36m╩╚═╩ ╚═╚═╝\033[1;32m║\033[1;36mWHATSAPP: +8801989861704\033[1;32m         ║\033[1;32m
╠══════════╩════╦═════════════╦══════════════╣
║\033[1;36mGITHUB:BINOD-XD\033[1;32m║\033[1;36mVERSION:1.0.1\033[1;32m║\033[1;36m 2FACTOR ADD \033[1;32m ║\033[1;32m
╚═══════════════╩═════════════╩══════════════╝
\033[1;91m\033[1;46m\033[1;97m             RXS PAID TOOLS            \033[;0m\033[1;91m\033[1;92m""")
                
            
            
def randNewDeviceUA():
	model = random.choice(['Android 9; SM-N960F Build/N960FXXU9ETF5_BNG','Android 9; SM-M405F Build/M405FDDU2BSL2_BNG','Android 9; SM-M305G Build/M305GDDU1ASL5_BNG','Android 9; SM-M305F Build/M305FDDU3CSL2_BNG','Android 9; SM-M205G Build/M205GDXS5CTC2_BNG','Android 9; SM-M205F Build/M205FDDU5CTC9_BNG','Android 9; SM-M105G Build/M105GDXU3BSL3_BNG','Android 9; SM-J730GM Build/J730GMDDU7CSI1_BNG','Android 9; SM-J730G Build/J730GUBSACTD3_BNG','Android 9; SM-J730G Build/J730GUBSACTC3_BNG','Android 9; SM-J701MT Build/J701MTVJU8CTK1_BNG','Android 9; SM-J610F Build/J610FXXU2BSF6_BNG','Android 9; SM-J610F Build/J610FXXS8CTG1_BNG','Android 9; SM-J600GT Build/J600GTUBS9CTG3_BNG','Android 9; SM-J530G Build/J530GUBS7CTG1_BNG','Android 9; SM-J415G Build/J415GUBS5BSL2_BNG','Android 9; SM-J415F Build/J415FXXU6BTF1_BNG','Android 9; SM-J415F Build/J415FXXU6BTD1_BNG','Android 9; SM-J400F Build/J400FXXU6BTD1_BNG','Android 9; SM-J337A Build/J337AUCU9BSG3_BNG','Android 9; SM-J260G Build/J260GDDU4ASI3_BNG','Android 9; SM-J260F Build/J260FXXS9CTK1_BNG','Android 9; SM-G975F Build/G975FXXU9CTJ4_BNG','Android 9; SM-G973F Build/G973FXXU9FUCD_BNG','Android 9; SM-G970F Build/G970FXXS9DUE2_BNG','Android 9; SM-G965W Build/G965WVLS9FUE1_BNG','Android 9; SM-G965U1 Build/G965U1UEU9FUC5_BNG','Android 9; SM-G960U Build/G960USQS10FUA9_BNG','Android 9; SM-G960F Build/G960FXXUCFTK1_BNG','Android 9; SM-G955F Build/G955FXXU5DSFB_BNG','Android 9; SM-G950W Build/G950WVLU7DTA5_BNG','Android 9; SM-G950N Build/G950NKSU4DTF3_BNG','Android 9; SM-G950F Build/G950FXXU5DSFB_BNG','Android 9; SM-G935F Build/G935FXXS8ETC6_BNG','Android 9; SM-G610F Build/G610FDDU1CRJ1_BNG','Android 9; SM-G610F Build/G610FDDS1CTG1_BNG','Android 9; SM-A750GN Build/A750GNDXU3CTF2_BNG','Android 9; SM-A750GN Build/A750GNDXU3BTF1_BNG','Android 9; SM-A205F Build/A205FDDU8BUE3_BNG','Android 8; SM-N960U Build/N960USQS9FUE2_BNG','Android 8; SM-N950U Build/N950USQS9DUE4_BNG','Android 8; SM-N950U Build/N950USQS6DSH4_BNG','Android 8; SM-J730GM Build/J730GMDDU9CUE2_BNG','Android 8; SM-J730F Build/J730FXXU6CSK6_BNG','Android 8; SM-J730F Build/J730FXXS9CTG1_BNG','Android 8; SM-J727T Build/J727TUVS7BSI2_BNG','Android 8; SM-J701M Build/J701MUBU6BRI1_BNG','Android 8; SM-J701F Build/J701FXXU6BRI9_BNG','Android 8; SM-J701F Build/J701FDDU7CSG2_BNG','Android 8; SM-J701F Build/J701FDDU6BRL2_BNG','Android 8; SM-J610F Build/J610FXXU2BSF6_BNG','Android 8; SM-J600FN Build/J600FNXXU7CTG2_BNG','Android 8; SM-J600F Build/J600FXXU6BSK6_BNG','Android 8; SM-J530Y Build/J530YDXU7CTH2_BNG','Android 8; SM-J530F Build/J530FXXU7CSH8_BNG','Android 8; SM-J530F Build/J530FXXU7CSH3_BNG','Android 8; SM-J530F Build/J530FXWU4CSE1_BNG','Android 8; SM-J400F Build/J400FXXU6BTD1_BNG','Android 8; SM-J260F Build/J260FXXS7ATK4_BNG','Android 8; SM-G965U Build/G965USQS9FUE2_BNG','Android 8; SM-G960W Build/G960WVLS9FUE1_BNG','Android 8; SM-G960U Build/G960USQU8FTK4_BNG','Android 8; SM-G955F Build/G955FXXU8DTH7_BNG','Android 8; SM-G950U Build/G950USQS9DUE4_BNG','Android 8; SM-G950F Build/G950FXXSFDUE5_BNG','Android 8; SM-G935F Build/G935FXXU2ERD5_BNG','Android 8; SM-G930V Build/G930VVRS9CUE4_BNG','Android 8; SM-G930F Build/G930FXXU2ERD5_BNG','Android 8; SM-G930F Build/G930FXXS8ETC1_BNG','Android 8; SM-G610F Build/G610FDDU1CRL2_BNG','Android 8; SM-A720F Build/A720FXXU7CRJ1_BNG','Android 8; SM-A520W Build/A520WVLU9CSK1_BNG','Android 8; SM-A520F Build/A520FXXUCCSK2_BNG','Android 7; SM-J730GM Build/J730GMUBSACTC1_BNG','Android 7; SM-J730F Build/J730FXXU3BRI3_BNG','Android 7; SM-J710F Build/J710FXXU5BRC2_BNG','Android 7; SM-J701M Build/J701MUBSACSK1_BNG','Android 7; SM-J701M Build/J701MUBS7CTG3_BNG','Android 7; SM-J701F Build/J701FXXU6BRL3_BNG','Android 7; SM-J701F Build/J701FXXU6BRI9_BNG','Android 7; SM-J701F Build/J701FXXU5ARG1_BNG','Android 7; SM-J330F Build/J330FXXS3BRL1_BNG','Android 7; SM-J320F Build/J320FXXU0AQL1_BNG','Android 7; SM-G955U Build/G955USQU9DUE1_BNG','Android 7; SM-G950W Build/G950WVLU7DTF1_BNG','Android 7; SM-G950F Build/G950FXXU8DTC5_BNG','Android 7; SM-G935F Build/G935FXXU2DRB6_BNG','Android 7; SM-G930T1 Build/G930T1UVU4BQH7_BNG','Android 7; SM-G930T Build/G930TUVSACSG1_BNG','Android 7; SM-G610M Build/G610MUBS4CSJ1_BNG','Android 7; SM-G610F Build/G610FDDU1CRK1_BNG','Android 7; SM-G570F Build/G570FDDU1BQJ1_BNG','Android 7; SM-A720F Build/A720FXXU5CRD6_BNG','Android 7; SM-A710F Build/A710FXXU2CRK1_BNG','Android 7; SM-A710F Build/A710FDXU2CQE5_BNG','Android 7; SM-A520W Build/A520WVLS9CTJ1_BNG','Android 7; SM-A520S Build/A520SKSU2BQK2_BNG','Android 7; SM-A520F Build/A520FXXUDDUD1_BNG','Android 7; SM-A520F Build/A520FXXUCCSL1_BNG','Android 7; SM-A520F Build/A520FXXSBDTJ1_BNG','Android 7; SM-A510F Build/A510FXXS8CSG1_BNG','Android 7; SM-A500F Build/A500FXXU1CQK2_BNG','Android 7; SM-A320F Build/A320FXXU3CRD4_BNG','Android 6; SM-N910H Build/N910HXXU2DPG2_BNG','Android 6; SM-J710GN Build/J710GNDXU5CRL1_BNG','Android 6; SM-J710FN Build/J710FNDDU1BQI5_BNG','Android 6; SM-J710F Build/J710FXXU5CRJ7_BNG','Android 6; SM-J700M Build/J700MUBU2BQH1_BNG','Android 6; SM-J700F Build/J700FXXU4BQL1_BNG','Android 6; SM-J510FN Build/J510FNXXU2AQE2_BNG','Android 6; SM-J500H Build/J500HXXU1AOL1_BNG','Android 6; SM-J500H Build/J500HXXS1BQE1_BNG','Android 6; SM-J500G Build/J500GXXU1BPK3_BNG','Android 6; SM-J500FN Build/J500FNXXU1BPK2_BNG','Android 6; SM-J320F Build/J320FXXU0AQB1_BNG','Android 6; SM-J210F Build/J210FXXU0APH2_BNG','Android 6; SM-G935P Build/G935PVPS8CRK2_BNG','Android 6; SM-G930P Build/G930PVPS4BQE1_BNG','Android 6; SM-G930FD Build/G930FXXU1DQCE_BNG','Android 6; SM-G930F Build/G930FXXU1BPHJ_BNG','Android 6; SM-G928C Build/G928CXXS5CRH1_BNG','Android 6; SM-G920V Build/G920VVRU4CPC2_BNG','Android 6; SM-G900H Build/G900HXXS1CQD1_BNG','Android 6; SM-G900F Build/G900FXXS1CQD4_BNG','Android 6; SM-G570F Build/G570FXXU1BQL2_BNG','Android 6; SM-A310F Build/A310FXXU3CQE6_BNG','Android 11; SM-M515F Build/M515FXXU1BUD1_BNG','Android 11; SM-M425F Build/M425FXXU1BUD2_BNG','Android 11; SM-M325F Build/M325FXXU1AUD1_BNG','Android 11; SM-M315F Build/M315FXXU2BUD8_BNG','Android 11; SM-M215F Build/M215FXXU2ATJ3_BNG','Android 11; SM-M127G Build/M127GDXU3AUF3_BNG','Android 11; SM-M127F Build/M127FXXU3AUF3_BNG','Android 11; SM-M025F Build/M025FXXU2AUF1_BNG','Android 11; SM-J415F Build/J415FXXU6BUF1_BNG','Android 11; SM-J250F Build/J250FXXU6CUD1_BNG','Android 11; SM-G998B Build/G998BXXU3AUF9_BNG','Android 11; SM-G996B Build/G996BXXU3AUF9_BNG','Android 11; SM-G991U Build/G991USQU2AUCP_BNG','Android 11; SM-G991B Build/G991BXXU3AUH3_BNG','Android 11; SM-G991B Build/G991BXXU3AUF9_BNG','Android 11; SM-G988B Build/G988BXXS7DUD2_BNG','Android 11; SM-G985F Build/G985FXXS6DUD1_BNG','Android 11; SM-G980F Build/G980FXXS6DUD1_BNG','Android 11; SM-G975F Build/G975FXXS9FUE4_BNG','Android 11; SM-G973F Build/G973FXXS9FUE4_BNG','Android 11; SM-G780G Build/G780GDXS3AUE1_BNG','Android 11; SM-G770F Build/G770FXXS4EUD3_BNG','Android 11; SM-F916U1 Build/F916U1UEU2DUD4_BNG','Android 11; SM-F711N Build/F711NKOU2ATJ1_BNG','Android 11; SM-F711B Build/F711BXXU1ATK1_BNG','Android 11; SM-A925F Build/A925FXXU5DUD1_BNG','Android 11; SM-A920F Build/A920FXXU3CUG1_BNG','Android 11; SM-A908B Build/A908BXXU3DUF5_BNG','Android 11; SM-A750G Build/A750GNDXU3CTF2_BNG','Android 11; SM-A735F Build/A735FXXU5CUD1_BNG','Android 11; SM-A727B Build/A727BXXU4BUD1_BNG','Android 11; SM-A725M Build/A725MUBU2BUE2_BNG','Android 11; SM-A725F Build/A725FXXU4BUD1_BNG','Android 11; SM-A716B Build/A716BXXU5CUD1_BNG','Android 11; SM-A526U Build/A526USQU1AUE1_BNG','Android 11; SM-A526B Build/A526BXXU1AUE3_BNG','Android 11; SM-A525F Build/A525FXXS2AUF1_BNG','Android 11; SM-A515F/DS Build/A515FXXU4EUD7_BNG','Android 11; SM-A515F Build/A515FXXU5CUF3_BNG','Android 11; SM-A515F Build/A515FXXU4EUD7_BNG','Android 11; SM-A515F Build/A515FXXU4EUD1_BNG','Android 11; SM-A515F Build/A515FXXS4AUF2_BNG','Android 11; SM-A505F Build/A505FDDU7CUG1_BNG','Android 11; SM-A326B Build/A326BXXU2AUF1_BNG','Android 11; SM-A325F Build/A325FXXU2AUD4_BNG','Android 11; SM-A325F Build/A325FXXU1AUD3_BNG','Android 11; SM-A325F Build/A325FXXU1AUD1_BNG','Android 11; SM-A225F Build/A225FXXU1AUD1_BNG','Android 11; SM-A225F Build/A225FXXS2AUF2_BNG','Android 11; SM-A217M Build/A217MUBS5AUF1_BNG','Android 11; SM-A217F Build/A217FXXU5BUD8_BNG','Android 11; SM-A217F Build/A217FXXU5AUF1_BNG','Android 11; SM-A217F Build/A217FXXU3AUF3_BNG','Android 11; SM-A125M Build/A125MUBS2AUD5_BNG','Android 11; SM-A125F Build/A125FXXU1AUD1_BNG','Android 11; SM-A025M Build/A025MUBS2AUF2_BNG','Android 11; SM-A025G Build/A025GUBU2AUF3_BNG','Android 11; SM-A025F Build/A025FXXU2AUF2_BNG','Android 11; SM-A013F Build/A013FXXS4BUA1_BNG','Android 10; SM-M515F Build/M515FXXS3BTF1_BNG','Android 10; SM-M407F Build/M407FXXS3BTF2_BNG','Android 10; SM-M405F Build/M405FDDS2BUB2_BNG','Android 10; SM-M317F Build/M317FXXU2BTK1_BNG','Android 10; SM-M317F Build/M317FXXS2BUA2_BNG','Android 10; SM-M315F Build/M315FXXU2BTK3_BNG','Android 10; SM-M315F Build/M315FXXS2BUA6_BNG','Android 10; SM-M315F Build/M315FXXS2ATJ2_BNG','Android 10; SM-M307F Build/M307FXXU4CUA1_BNG','Android 10; SM-M215F Build/M215FXXU2ATJ3_BNG','Android 10; SM-M205F Build/M205FDDU9CUH6_BNG','Android 10; SM-M105F Build/M105FDDU7BUA2_BNG','Android 10; SM-M015G Build/M015GUBU2BTK1_BNG','Android 10; SM-J730GM Build/J730GMDDU9CUE2_BNG','Android 10; SM-J600G Build/J600GDXS9CUE1_BNG','Android 10; SM-J400F Build/J400FXXU6BTD1_BNG','Android 10; SM-G965F Build/G965FXXU9ETF5_BNG','Android 10; SM-G960F Build/G960FXXU9ETF5_BNG','Android 10; SM-G780F Build/G780FXXS3BUE3_BNG','Android 10; SM-G715U Build/G715USQU5BUE3_BNG','Android 10; SM-G715FN Build/G715FNXXU5BUA1_BNG','Android 10; SM-G715FN Build/G715FNXXS4ATJ1_BNG','Android 10; SM-G7102 Build/G7102DDUANE1_BNG','Android 10; SM-G615F Build/G615FXXS2BTD2_BNG','Android 10; SM-G532F Build/G532FXWU1ASA5_BNG','Android 10; SM-A805F Build/A805FXXU5DUD1_BNG','Android 10; SM-A750GN Build/A750GNDXU3CTF2_BNG','Android 10; SM-A735F Build/A735FXXU5CUD1_BNG','Android 10; SM-A727B Build/A727BXXU4BUD1_BNG','Android 10; SM-A725F Build/A725FXXU4BUD1_BNG','Android 10; SM-A716B Build/A716BXXU5CUD1_BNG','Android 10; SM-A716B Build/A716BXXU2BUE1_BNG','Android 10; SM-A715F Build/A715FXXU5CUD1_BNG','Android 10; SM-A707F Build/A707FXXU2DUC6_BNG','Android 10; SM-A705GM Build/A705GMDDU7CTH1_BNG','Android 10; SM-A516B Build/A516BXXU4BUD1_BNG','Android 10; SM-A515F Build/A515FXXU5EUD7_BNG','Android 10; SM-A515F Build/A515FXXU5CUF3_BNG','Android 10; SM-A505G Build/A505GUBS6BUD1_BNG','Android 10; SM-A405FM Build/A405FMPUU3CTK3_BNG','Android 10; SM-A315G Build/A315GUBS2BUD3_BNG','Android 10; SM-A315G Build/A315GUBS2BTK4_BNG','Android 10; SM-A315G Build/A315GDXU2BUC1_BNG','Android 10; SM-A307G Build/A307GUBS3BUE1_BNG','Android 10; SM-A307FN Build/A307FNXXU2CUF2_BNG','Android 10; SM-A307FN Build/A307FNXXU2BTK1_BNG','Android 10; SM-A225F Build/A225FXXU1AUB1_BNG','Android 10; SM-A217M Build/A217MUBS5ATK1_BNG','Android 10; SM-A217F Build/A217FXXU5BUE1_BNG','Android 10; SM-A217F Build/A217FXXU5AUF1_BNG','Android 10; SM-A215U Build/A215UUES3BUC3_BNG','Android 10; SM-A207F Build/A207FXXU2BUC4_BNG','Android 10; SM-A207F Build/A207FXXU2BTD7_BNG','Android 10; SM-A205U Build/A205USQS7BTK1_BNG','Android 10; SM-A205F Build/A205FXXUACUF3_BNG','Android 10; SM-A205F Build/A205FDDU8BUE3_BNG','Android 10; SM-A115M Build/A115MUBU2BTK2_BNG','Android 10; SM-A115F Build/A115FXXS1BTF2_BNG','Android 10; SM-A115A Build/A115AUCS2BTF2_BNG','Android 10; SM-A107F Build/A107FXXU8BUC1_BNG','Android 10; SM-A107F Build/A107FXXU7BTF1_BNG','Android 10; SM-A107F Build/A107FXXU5BUA5_BNG','Android 10; SM-A105M Build/A105MUBS7BTH1_BNG','Android 10; SM-A105G Build/A105GDXU7BTF1_BNG','Android 10; SM-A105F Build/A105FDDU6DUC1_BNG','Android 10; SM-A015M Build/A015MUBU4BUA2_BNG'])
	aa='Mozilla/5.0 (Linux; '
	model_parts = model.split(" ")
	android_version = model_parts[0]
	os_version = model_parts[1] 
	model2 = model_parts[2]
	make= (f"{android_version} {os_version} {model2}")
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	l='Mobile Safari/537.36'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	ua=(f"{aa} {make}) {g}{h}.{i}.{j}.{k} {l}")
	return ua
usa=[]
for i in range(10):
    usa.append(randNewDeviceUA())
            
def RXS():
	os.system('clear')
	print (logo)
	print('\x1b[92m══════════════════════════════════════════════\033[1;37m')
	print("[\033[1;36mA\033[1;37m] LOGIN WITH COOKIE ")
	print("[\033[1;36mB\033[1;37m] LOGIN WITH ID PASS ")
	print("[\033[1;32mX\033[1;37m] CONTRACT ADMIN")
	print('[\033[1;31mE\033[1;37m] EXIT')
	print("\x1b[92m══════════════════════════════════════════════\x1b[97m")
tahosin = input('\x1b[92mChoose option: \x1b[97m')
print('\x1b[92m══════════════════════════════════════════════\x1b[97m')
if tahosin =='X':
	admin()
elif tahosin =='E':
	exit()
if tahosin =='A':
	cookie(coki_check,ses)
if tahosin =='B':
	clear()
	os.system('clear')
	print (logo)
	ses = req.Session()
	id = input (' Enter number/uid: ')
	pas=input (' Enter Password: ')
	crack(id,pas)
	exit()
          
def crack(id,pas):
	ua = random.choice(usa)
	ua2 = random.choice(usa)
	ses = req.Session()
	for pw in range(1):
		try:
			ses.headers.update({"Host":'mbasic.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+id+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":id,"flow":"login_no_pin","pass":pas,"next":"https://mbasic.facebook.com/login/save-device/'"}
			ses.headers.update({"Host":'mbasic.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":'https://mbasic.facebook.com/login/device-based/password/?uid='+id+'&flow=login_no_pin&refsrc=deprecated&locale=id_ID&_rdr',"accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict().keys():
				coki=ses.cookies.get_dict()
				#print (cokii)
				coki_check(ses,coki,pas)
			elif "checkpoint" in po.cookies.get_dict().keys():
				print (f' [S-CP] '+id+'|'+pas)
				break
			else:
				#print (idf,pw)
				continue
		except req.exceptions.ConnectionError:
			time.sleep(10)
def coki_check(ses,coki,pas):
	#cok="datr=-ddYZGxLxov7m3bPsclmSokk;sb=-ddYZJe4uMMzlwrO0RiY-4_2;c_user=100077473742575;xs=39%3A6c1smGNy1uL_1w%3A2%3A1683544057%3A-1%3A5228;fr=0XwzusaH6yqL6mUXg.AWVVTZZFuzfizc3tIacYh5-1ybs.BkWNf5.Ua.AAA.0.0.BkWNf5.AWXfopNJmoE"
	#cookies = {'cookie':cok}
	resss = req.get("https://mbasic.facebook.com/profile.php", cookies=coki).text
	#open("113.html","w").write(resss)
	if "mbasic_logout_button" in resss:
		nama = re.findall('\<title\>(.*?)<\/title\>',str(resss))[0]
		print(nama)
		main(ses,coki,pas,nama)
	else:
		exit(" × Cookies invalid")

def main(ses,coki,pas,nama):
	os.system('clear')
	print (logo)
	print(f'\nWelcome {nama}\n')
	try:
		r = par(ses.get("https://mbasic.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=coki).text, 'html.parser')
	except req.exceptions.TooManyRedirects:
		r = par(req.get("https://mbasic.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=coki).text, 'html.parser')
	try:
		uaa = r.find("a",string="Use Authentication App").get("href")
	except:
		exit(" ! Your account already 2fa enabled×")
	print ('\nLink:  '+uaa)
	try:
		__r = ses.get(uaa,cookies=coki).text
	except req.exceptions.TooManyRedirects:
		__r = req.get(uaa,cookies=coki).text
	co = par(__r, 'html.parser')
	try:
		kode = re.findall('\<div\ class\=\".*?\"\>Or enter this code into your authentication app<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>\<\/div\>',str(co))[0]
		cod(kode,co,ses,coki)
	except:
		if "For your security, please re-enter your password to continue." in __r:
			#print(" \n* For your security, please re-enter your password to continue.")
			print ('Your Password Is '+pas)
			lanjut = co.find('form',{'method':'post'})
			memek = {}
			lst = ["fb_dtsg","jazoest","save"]
			for x in lanjut:
				if x.get("name") in lst:
					memek.update({x.get("name"):x.get("value")})
			memek.update({"pass":pas})
			response = ses.post(lanjut.get("action"),cookies=coki,data=memek).text
			if "The password you entered is not correct." in response:
				exit(" ! The password you entered is not correct.")
			else:
				try:
					kode = re.findall('\<div\ class\=\".*?\"\>Or enter this code into your authentication app<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>\<\/div\>',str(response))[0]
					cod(kode,co,ses,coki)
				except IndexError:
					exit(" × Facebook Exposed Checkpoint")
				
		else:
			exit("  your account in checkpoint")
			
def cod(kode,co,ses,coki):
	key= kode.replace(" ","")
	print ('\nKey= '+key)
	kt=pyotp.TOTP(key)
	current_code=kt.now()
	print (f'\nYOUR AUTHENTICATION TOTP is : {current_code} ')
	ad(co,current_code,ses,coki)
def ad(co,current_code,ses,coki):
	#s = input('do you want to continue')
	data = {}
	masuk = current_code
	lst = ["fb_dtsg","jazoest","code_handler_type","confirmButton"]
	lanjut = co.find('form',{'method':'post'})
	for x in lanjut:
		if x.get('name') in lst:
			data.update({x.get('name'):x.get('value')})	
	data.update({'confirmButton':'Continue'})
	res = par(ses.post('https://mbasic.facebook.com'+str(lanjut.get("action")),cookies=coki,data=data).text, 'html.parser')
	data.clear()
	lanjut = res.find("form",{"id":"input_form"})
	lst = ["fb_dtsg","jazoest"]
	for x in lanjut:
		if x.get("name") in lst:
			data.update({x.get("name"):x.get("value")})
	data.update({"code":masuk,"submit_code_button":"Continue"})
	response = ses.post('https://mbasic.facebook.com'+str(lanjut.get("action")),cookies=coki,data=data).text
	if "checkpoint" in response:
		#open('/sdcard/2faa.html', 'a').write(str(response))
		exit(" account in checkpoint")
	elif "Two-factor authentication is on" in response:
		print(" 2FA ENABLE SUCCESSFUL ")
		print(" Your Recovery Code: ")
		open('/sdcard/2faa.html', 'a').write(str(response))
		get_code(ses,coki)
	else:
		print(" ! Text:",response)
		exit(" × There is something wrong in the script, try to report it to the Developer. Copy the text above! Send to wa 083172566909. ")

def get_code(ses,coki):
	
	#ses.headers.update(waifu_wangy)
	__res = ses.get("https://mbasic.facebook.com/security/2fac/factors/recovery-code/",cookies=coki).text
	
	kontol = par(__res, 'html.parser')
	if "Use recovery codes to log in if you lose your phone or can’t receive a verification code via text message or an authentication app." in __res:
		data = {}
		lst = ["fb_dtsg","jazoest","reset"]
		for x in kontol.find('form',{'method':'post'}):
			if x.get('name') in lst:
				data.update({x.get('name'):x.get('value')})
		data.update({"":"Get codes"})
		kontol = par(ses.post("https://mbasic.facebook.com/security/2fac/factors/recovery-code/",cookies=coki,data=data).text, 'html.parser')
		num = 0
		for x in kontol.find_all('span'):
			if(re.findall('\d+\s\d+',str(x))):
				num+=1
				if(num==1):
					print(f" {[num]} {x.text}")
				else:
					print(f" {[num]} {x.text}")
	else:
		num = 0
		for x in kontol.find_all('span'):
			if(re.findall('\d+\s\d+',str(x))):
				num+=1
				if(num==1):
					print(f" {[num]} {x.text}")
				else:
					print(f" {[num]} {x.text}")
					
def admin():
	os.system('clear')
	print(logo)
	print('\x1b[92m══════════════════════════════════════════════\x1b[97m')
	print(' \033[1;96m[\033[1;32m1\033[1;96m] \033[1;93mCONTACT WHATSAPP ')
	print(' \033[1;96m[\033[1;32m2\033[1;96m] CONTACT FACEBOOK ')
	print(' \033[1;96m[\033[1;32m3\033[1;96m] \033[1;94mJOIN MESSENGER GROUP')
	print(' \033[1;96m[\033[1;32m4\033[1;96m] \033[1;95mJOIN FACEBOOK GROUP')
	print(' [\033[1;32m0\033[1;37m] BACK TO MAIN MENU')
	print("\x1b[92m══════════════════════════════════════════════\x1b[97m")
	bal = input('\x1b[92mChoose option: \x1b[97m')
	if bal =='1':
		os.system('xdg-open https://wa.me/+8801989861704');time.sleep(1)
		admin()
	if bal =='2':
		os.system('xdg-open https://www.facebook.com/reyadbross');time.sleep(1)
		admin()
	if bal =='3':
		os.system('xdg-open https://m.me/j/AbZltMIVrGlcZi6j/');time.sleep(1)
		admin()
	if bal =='4':
		os.system('xdg-open https://facebook.com/groups/450474632802314/');time.sleep(1)
		admin()
	if bal =='0':
		RXS()

def coki_check(ses):
	os.system('clear')
	print (logo)
	print('\x1b[92m══════════════════════════════════════════════\x1b[97m')
	pas = 'mojidul@@@@'
	cokii = input(" + Enter cookies: ")
	print('\x1b[92m══════════════════════════════════════════════\x1b[97m')
	resss = req.get("https://mbasic.facebook.com/profile.php",cookies={"cookie":cokii}).text
	if "mbasic_logout_button" in resss:
		nama = re.findall('\<title\>(.*?)<\/title\>',str(resss))[0]
		
		coki= {"cookie":cokii}
		main(ses,coki,pas,nama)
	else:
		exit(" × Cookies invalid")

headers = {
	"Host":"mbasic.facebook.com",
	"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	'accept-language': 'en-US,en;q=0.9',
	"origin":"https://www.facebook.com",
	"referer":"https://www.facebook.com",
	'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
	"upgrade-insecure-requests":"1",
	'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
}


ses = req.Session()
ses.headers.update(headers)
def main(ses,coki,pas,nama):
	os.system('clear')
	print (logo)
	print('\x1b[92m══════════════════════════════════════════════\x1b[97m')
	print(f'\nWelcome {nama}\n')
	print('\x1b[92m══════════════════════════════════════════════\x1b[97m')
	try:
		r = par(ses.get("https://mbasic.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=coki).text, 'html.parser')
	except req.exceptions.TooManyRedirects:
		r = par(req.get("https://mbasic.facebook.com/security/2fac/setup/intro/metadata/?source=1",cookies=coki).text, 'html.parser')
	try:
		uaa = r.find("a",string="Use authentication app").get("href")
	except:
		exit(" ! Your account already 2fa enabled×")
	print ('\nLink:  '+uaa)
	try:
		__r = ses.get(uaa,cookies=coki).text
	except req.exceptions.TooManyRedirects:
		__r = req.get(uaa,cookies=coki).text
	co = par(__r, 'html.parser')
	try:
		kode = re.findall('\<div\ class\=\".*?\"\>Or enter this code into your authentication app<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>\<\/div\>',str(co))[0]
		cod(kode,co,ses,coki)
	except:
		if "For your security, please re-enter your password to continue." in __r:
			#print(" \n* For your security, please re-enter your password to continue.")
			print ('Your Password Is '+pas)
			lanjut = co.find('form',{'method':'post'})
			memek = {}
			lst = ["fb_dtsg","jazoest","save"]
			for x in lanjut:
				if x.get("name") in lst:
					memek.update({x.get("name"):x.get("value")})
			memek.update({"pass":pas})
			response = ses.post(lanjut.get("action"),cookies=coki,data=memek).text
			if "The password you entered is not correct." in response:
				exit(" ! The password you entered is not correct.")
			else:
				try:
					kode = re.findall('\<div\ class\=\".*?\"\>Or enter this code into your authentication app<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>\<\/div\>',str(response))[0]
					cod(kode,co,ses,coki)
				except IndexError:
					exit(" × Facebook Exposed Checkpoint")
				
		else:
			exit(" × your account in checkpoint")
			
def cod(kode,co,ses,coki):
	key= kode.replace(" ","")
	print ('\nKey= '+key)
	kt=pyotp.TOTP(key)
	current_code=kt.now()
	print (f'\nYOUR AUTHENTICATION KEY IS : {current_code} ')
	print('\x1b[92m══════════════════════════════════════════════\x1b[97m')
	ad(co,current_code,ses,coki)
def ad(co,current_code,ses,coki):
	#s = input('do you want to continue')
	data = {}
	masuk = current_code
	lst = ["fb_dtsg","jazoest","code_handler_type","confirmButton"]
	lanjut = co.find('form',{'method':'post'})
	for x in lanjut:
		if x.get('name') in lst:
			data.update({x.get('name'):x.get('value')})	
	data.update({'confirmButton':'Continue'})
	res = par(ses.post('https://mbasic.facebook.com'+str(lanjut.get("action")),cookies=coki,data=data).text, 'html.parser')
	data.clear()
	lanjut = res.find("form",{"id":"input_form"})
	lst = ["fb_dtsg","jazoest"]
	for x in lanjut:
		if x.get("name") in lst:
			data.update({x.get("name"):x.get("value")})
	data.update({"code":masuk,"submit_code_button":"Continue"})
	response = ses.post('https://mbasic.facebook.com'+str(lanjut.get("action")),cookies=coki,data=data).text
	if "checkpoint" in response:
		#open('/sdcard/2faa.html', 'a').write(str(response))
		exit(" account in checkpoint")
	elif "Two-factor authentication is on" in response:
		print(" 2FA ENABLE SUCCESSFUL ")
		print(" Your Recovery Code: ")
		#open('/sdcard/2faa.html', 'a').write(str(response))
		get_code(ses,coki)
	else:
		print(" ! Text:",response)
		exit(" × There is something wrong in the script, try to report it to the Developer. Copy the text above! Send to wa 083172566909. ")

def get_code(ses,coki):
	waifu_wangy = {
		"Host":"mbasic.facebook.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		'accept-language': 'en-US,en;q=0.9',
		"content-type":"application/x-www-form-urlencoded",
		"origin":"https://www.facebook.com",
		"referer":"https://www.facebook.com",
		"upgrade-insecure-requests":"1",
		'user-agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5',
	}
	ses.headers.update(waifu_wangy)
	__res = ses.get("https://mbasic.facebook.com/security/2fac/factors/recovery-code/",cookies=coki).text
	kontol = par(__res, 'html.parser')
	if "Use recovery codes to log in if you lose your phone or can’t receive a verification code via text message or an authentication app." in __res:
		data = {}
		lst = ["fb_dtsg","jazoest","reset"]
		for x in kontol.find('form',{'method':'post'}):
			if x.get('name') in lst:
				data.update({x.get('name'):x.get('value')})
		data.update({"":"Get codes"})
		kontol = par(ses.post("https://mbasic.facebook.com/security/2fac/factors/recovery-code/",cookies=coki,data=data).text, 'html.parser')
		num = 0
		for x in kontol.find_all('span'):
			if(re.findall('\d+\s\d+',str(x))):
				num+=1
				if(num==1):
					print(f" \_> {x.text}")
				else:
					print(f" |_> {x.text}")
	else:
		num = 0
		for x in kontol.find_all('span'):
			if(re.findall('\d+\s\d+',str(x))):
				num+=1
				if(num==1):
					print(f" \_> {x.text}")
				else:
					print(f" |_> {x.text}")
coki_check(ses)

RXS()
