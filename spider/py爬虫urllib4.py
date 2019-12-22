'''
handler:
1.系统的urllib不支持代理的添加，需自己创建对应的处理器handler
2.1代理处理器：ProxyHandler
2.2拿着ProxyHandler创建opener : build_opener()
2.3用opener.open(url)就可以请求数据了
auth认证handler
Cookieshandler
URLError
'''

import urllib.request
def create_proxy_handler():
    url = 'https://www.wddsss.com/main/home'
    #添加代理
    proxy = {
        #免费的代理写法
        # 'http':'http://	171.35.167.197:9999'
        'http':'171.35.167.197:9999'
        #付费的代理写法
        # 'http':'username:pwd@127.168.12.11:8080'
    }
    #创建代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)
    #创建自己的opener
    opener = urllib.request.build_opener(proxy_handler)
    #拿着代理ip去发送请求
    data = opener.open(url).read().decode('utf-8')
    # print(data)
    #保存数据
    with open('zhouwei.html','w',encoding='utf-8') as f:
        f.write(data)
create_proxy_handler()