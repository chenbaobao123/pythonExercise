import urllib.request
def proxy_user():
    proxy_list = [
        {'http':'171.35.167.197:9999'},
        {'http':'117.69.201.58:9999'},
        {'http':'117.69.201.195:9999'},
        {'http':'183.164.238.171:9999'},
        {'http':'120.83.105.126:9999'}
    ]
    url = 'https://www.wddsss.com/main/home'
    for proxy in proxy_list:
        print(proxy)
        #利用遍历出来的ip创建处理器
        proxy_handler = urllib.request.ProxyHandler(proxy)
        #用处理器创建opener
        opener = urllib.request.build_opener(proxy_handler)
        try:
            # opener.open('https://www.baidu.com',timeout=1)
            # print(proxy_list.index(proxy))
            data = opener.open(url).read().decode('utf-8')
            with open('zhouwei%s.html' %(proxy_list.index(proxy)),'w',encoding='utf-8') as f:
                f.write(data)
        except Exception as e:
            print(e)

        # #用opener去请求数据

proxy_user()