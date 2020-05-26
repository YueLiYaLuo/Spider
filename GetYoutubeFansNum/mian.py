import urllib
import requests
import ssl


def get_RiverReport():
    import requests
    # proxy = {
    #     'https': 'https://61.240.192.54:18348',
    #     'http':'http://61.240.192.54:18348'
    # }

    # 用百度检测ip代理是否成功
    # url = 'https://www.baidu.com'
    # url ='https://m.youtube.com/channel/UCLrPZk6Bej-1CL7bYX2Bj_w'
    url = 'https://en.wikipedia.org'
    # 请求头
    headers = {
        'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36r)'
    }
    # 发送get请求
    response = requests.get(url=url, headers=headers)
    print(response)


def verify_one_proxy(proxy):


    protocol = 'https' if 'https' in proxy else 'http'
    proxies = {protocol: proxy}
    try:
        if requests.get('https://en.wikipedia.org', proxies=proxies,
                        timeout=2).status_code == 200:
            print('success %s' % proxy)
    except:
        print('fail %s' % proxy)


if __name__ == "__main__":
    proxies = 'http://140.227.229.208:3128'
    verify_one_proxy(proxies)
