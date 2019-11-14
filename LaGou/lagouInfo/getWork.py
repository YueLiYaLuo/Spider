import requests
import datetime
import re
import time
import random
import sys

try:
    from urllib import parse as parse

except:
    import urllib as parse

    sys.reload()
    sys.setdefaultencoding('utf-8')


def init_cookies():
    """
    return the cookies after your first visit
    """
    headers = {
        'Upgrade-Insecure-Requests': '1',
        'Host': 'm.lagou.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'DNT': '1',
        'Cache-Control': 'max-age=0',
        'Referrer Policy': 'no-referrer-when-downgrade',
    }
    url = 'https://m.lagou.com/search.html'
    response = requests.get(url, headers=headers, timeout=10)

    return response.cookies


def crawl_jobs(positionName, addn):
    """
    crawl the job info from lagou H5 web pages
    """
    JOB_DATA = list()

    # init cookies
    cookie = init_cookies()
    # cookie = dict(
    #     cookies_are='')

    for i in range(addn, addn + 10):
        # 请求的json数据
        request_url = 'https://m.lagou.com/search.json?positionName=' + parse.quote(
            positionName) + '&pageNo=' + str(i) + '&pageSize=15'
        # 伪装浏览器访问的头文件
        headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Host': 'm.lagou.com',
            'DNT': '1',
            'Referer': 'https://m.lagou.com/search.html',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Referrer Policy': 'no-referrer-when-downgrade',
        }
        # 发送请求
        response = requests.get(request_url, headers=headers, cookies=cookie)
        # 状态码为200表示伪装请求访问成功
        if response.status_code == 200:
            try:
                # 请求返回得到的json所有数据都放在items中
                items = response.json()['content']['data']['page']['result']
                if len(items) > 0:
                    for each_item in items:
                        #将网页上的“今天/昨天”改成具体日期
                        if "今天" in each_item['createTime']:
                            each_item['createTime'] = re.sub("今天.*", str(datetime.date.today()),
                                                             each_item['createTime'])
                        elif "昨天" in each_item['createTime']:
                            today = datetime.date.today()
                            oneday = datetime.timedelta(days=1)
                            yesterday = today - oneday
                            each_item['createTime'] = re.sub("昨天.*", str(yesterday), each_item['createTime'])
                        #将每一条数据都添加到JOB_DATA中
                        JOB_DATA.append(
                            [str(each_item['positionId']), str(each_item['companyId']), each_item['positionName'],
                             each_item['city'],
                             each_item['createTime'], each_item['salary'],
                             each_item['companyName'], each_item['companyFullName']])
                        print(each_item)
                    print('crawling page %d done...' % i)
                    time.sleep(random.randint(3, 6))
                else:
                    break
            except Exception as exp:
                print('Invalid request is found by Lagou...')
        elif response.status_code == 403:
            print('request is forbidden by the server...')
        else:
            print(response.status_code)

    return JOB_DATA


if __name__ == "__main__":
    write_file = open("info.txt", "r+")

    addn = 200
    while addn < 400:
        datas = crawl_jobs("java", addn)
        for data in datas:
            write_file.write("\t".join(data) + "\n")
        addn = addn + 10
        print(addn)
    write_file.close()