from bs4 import BeautifulSoup
import requests
import random

def get_ip_list(url, headers):
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
    file = open('proxy_list.text', 'a')  # 将获取到的ip存放在proxy_list.text文件中
    for i in range(0, len(proxy_list)):
        temp={'http': proxy_list[i]}
        file.write(str(temp)+'\n')
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }
    for i in range(1,10):
        url = 'http://www.xicidaili.com/nn/'+str(i)
        ip_list = get_ip_list(url, headers=headers)
        proxies = get_random_ip(ip_list)
        print(proxies)