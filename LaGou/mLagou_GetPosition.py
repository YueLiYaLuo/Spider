'''
更新与2019/3/10
因为拉勾网的爬虫访问机制更改，所以获取数据重新写了代码
通过“m.lagou.com”获取数据
但是访问过多还是会被封ip输入验证码
设置延时访问与更新cookie来模拟人手动操作访问越过机器识别
'''
import json
import requests
import time

def get_PositionInfo():
    header = {
        'Accept': 'application/json, text/javascript, */*;q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Cookie':
            '_ga=GA1.2.1828083553.1545226955; user_trace_token=20181219214233-f04f8b9d-0393-11e9-94bc-5254005c3644; LGUID=20181219214233-f04f8f05-0393-11e9-94bc-5254005c3644; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22169488304a0ac-079ccc2efeb972-b79183d-921600-169488304a16aa%22%2C%22%24device_id%22%3A%22169488304a0ac-079ccc2efeb972-b79183d-921600-169488304a16aa%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAAAFDABFG94FF715BDD0FEB69678FA68CFE8CECB6; _gid=GA1.2.1495837627.1552184197; _ga=GA1.3.1828083553.1545226955; OUTFOX_SEARCH_USER_ID_NCOO=1297070174.901033; ab_test_random_num=0; _putrc=9A45885192341F1E123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B77825; ___rl__test__cookies=1552196047926; LGSID=20190310180659-3e9938ba-431c-11e9-90b4-5254005c3644; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.a00000apJPO0FYNyJ3PQIjv_F-UlLeC0UHdPKyy2fId9tRevUJpmYB77dzvamxbu7z61hnPtZMhVAwfxt6a9655CUie-4M64X81xQiQkncgPKHoCbKvnPv9wWEI_WNamOcAKNUa3B1ulaG0AefUMQrVcEmhPt3pbavn3F6S_2AxIs-Yv7jl85OigFMU69Mi8VE7WIb9Tbastp7GMws.DR_NR2Ar5Od663rj6tJQrGvKD7ZZKNfYYmcgpIQC8xxKfYt_U_DY2yP5Qjo4mTT5QX1BsT8rZoG4XL6mEukmryZZjzkuXNPIIhExz4rMThEgz3x5Gse5gj_L3x5x9L4n5VLJpMpRt85R_nYQAeWuk3J0.U1Yk0ZDqs2v4_sK9uZ745TaV8Un0mywkIjYz0ZKGm1Ys0Zfqs2v4_sKGUHYznWR0u1dBugK1nfKdpHdBmy-bIfKspyfqnHb0mv-b5HRd0AdY5HDsnHIxnH0krNtknjc1g1DsPjuxn1msnfKopHYs0ZFY5HfdPfK-pyfqnHfvndtznH04P7tznjm4PdtzrjmsPdtzrjR3P7tzPWndn7tzrjmsndtzrjmzPNtzrjmsPfKBpHYYnjFxnW0Y0AdW5H6knHfLPjcvP-tknj0kg17xnH0zg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYzn1R1n1m3njR0UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzd-mvC0IZN15H64rHbdPHmLrjbvnjnsPHn3njR0ThNkIjYkPHRznWDzPjDvPWDd0ZPGujdhnyP9rjcLnj0snj7-mHRY0AP1UHYLwj0dnWb4wj7anDDkPjNj0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tsg1nkrjm4rNts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqnHm0uhPdIjYs0AulpjYs0Au9IjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00mLFW5HmkPjb1%26word%3D%25E6%258B%2589%25E9%2592%25A9%26ck%3D5070.1.200.311.148.300.143.676%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D1.0.1.0.1.313.0%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_nj_e110f9_265e1f_%25E6%258B%2589%25E9%2592%25A9; gate_login_token=608b49af81703c60ed7e5d4385d363eb7c7978e95e69536ab58e065e28aa67ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552184198,1552188249,1552212421,1552212432; X_MIDDLE_TOKEN=1aa03a0015af433963fe7254160b5490; _gat=1; LGRID=20190310181818-d2fd762a-431d-11e9-90b4-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1552213099',
        'Host': 'm.lagou.com',
        'Referer': 'https://m.lagou.com/search.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    datas = {
        'positionName': "java大数据",  # 职位名称
        'city':'全国',
        'pageNo':'1',
        'pageSize':'15'

    }
    #打开要写入的文件
    writefile = open("mobleLagouInfo.txt","a+")

    for i in range(193,200):
        time.sleep(2)
        print(i)
        url = "https://m.lagou.com/search.json?city={city}&positionName={positionName}&pageNo={pageNo}&pageSize={pageSize}".format(
            city=datas["city"],positionName=datas["positionName"],pageNo=i,pageSize=datas["pageSize"] )
        response = requests.post(url,data=json.dumps(datas), headers=header)
        print(response.content)
        if response.content:  # 如果response内有返回值
            temp_dic = response.json()
            allCompany = temp_dic['content']['data']['page']['result']
            #每一条company的信息：
            # {'city': '北京', 'createTime': '2019-03-08', 'companyFullName': '高德软件有限公司', 'companyName': '阿里巴巴-高德',
            #  'logger': {'name': 'com.lagou.entity.mobile.MobilePosition', 'traceCapable': True},
            #  'companyLogo': 'i/image2/M01/DA/2B/CgoB5lxlALuAVqFqAAAMZt7n5C8976.jpg', 'positionId': 5560047,
            #  'salary': '30k-60k', 'companyId': 91, 'positionName': 'Java大数据研发工程师/专家'}

            for company in allCompany:
                print(company)
                #根据positionId来确定信息转到主页
                writefile.write(str(company['positionId']) + '\t')
                writefile.write(str(company['companyId']) + '\t')
                writefile.write(company['positionName'] + '\t')
                writefile.write(company['city']+'\t')
                writefile.write(company['salary']+'\t')
                writefile.write(company['companyName']+'\t')
                writefile.write(company['companyFullName']+'\t')
                writefile.write(company['createTime']+'\t'+'\n')


    writefile.close()

if __name__ == "__main__":
    get_PositionInfo()
