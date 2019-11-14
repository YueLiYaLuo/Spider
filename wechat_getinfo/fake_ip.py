from bs4 import BeautifulSoup
import requests
import random
import urllib.request

def get_ip_list():
    url = 'http://www.xicidaili.com/nn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    web_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'lxml')
    ips = soup.find_all('tr')
    ip_list = []
    for i in range(1, len(ips)):
        ip_info = ips[i]
        tds = ip_info.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

if __name__ == '__main__':
    ip_list = get_ip_list()
    proxy = get_random_ip(ip_list)
    print(proxy)
    try:
        httpproxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(httpproxy_handler)
        request = urllib.request.Request("https://www.baidu.com/")
        response = opener.open(request)
        print(response.read())
    except Exception as e:
        print(e)