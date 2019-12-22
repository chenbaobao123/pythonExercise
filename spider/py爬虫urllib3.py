import urllib.request
def handler_openner():
    #系统的urlopen并没有添加代理的功能，所以需要我们自定义这个功能
    #安全 套接层 ssl第三方的CA数字证书
    #http 80端口 和 https 443端口
    #urlopen为什么可以请求数据 handler处理器 自己的opener请求数据
    url = 'http://www.baidu.com'
    #创建自己的处理器
    handler = urllib.request.HTTPHandler()
    #创建自己的opener
    opener = urllib.request.build_opener(handler)
    #用自己创建的opener调用openner方法请求数据
    response = opener.open(url)
    data = response.read().decode('utf-8')
    # print(response)
    print(data)
handler_openner()
