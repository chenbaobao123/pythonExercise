import urllib.request
def load_baidu():
    url = 'http://www.baidu.com/'
    #添加请求头的信息
    header = {
        #浏览器版本
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    # response = urllib.request.urlopen(url)
    #创建请求对象
    request = urllib.request.Request(url=url,headers=header)
    #请求网络数据(不能在此处添加请求头信息)
    response = urllib.request.urlopen(request)
    data = response.read().decode('utf-8')
    with open('header.html','w',encoding='utf-8') as f:
        f.write(data)
    #打印响应头
    # print(response.headers)
    '''
    Accept-Ranges: bytes
Cache-Control: no-cache
Content-Length: 227
Content-Type: text/html
Date: Mon, 09 Dec 2019 07:37:29 GMT
P3p: CP=" OTI DSP COR IVA OUR IND COM "
P3p: CP=" OTI DSP COR IVA OUR IND COM "
Pragma: no-cache
Server: BWS/1.1
Set-Cookie: BD_NOT_HTTPS=1; path=/; Max-Age=300
Set-Cookie: BIDUPSID=E0E67E5FB003BB97C81EB929AA9B4A1A; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: PSTM=1575877049; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
Set-Cookie: BAIDUID=E0E67E5FB003BB978700690B378E3CF1:FG=1; max-age=31536000; expires=Tue, 08-Dec-20 07:37:29 GMT; domain=.baidu.com; path=/; version=1; comment=bd
Strict-Transport-Security: max-age=0
Traceid: 1575877049028884634617312224107374964441
X-Ua-Compatible: IE=Edge,chrome=1
Connection: close
    '''
    # #打印请求头(两个方法)
    print(request.headers)
    # print(request.get_header('User-agent'))

load_baidu()