'''
获取个人中心的页面
1.代码登录 登录成功 Cookie有效
    1.1登录的网址
    1.2登录的参数
    1.3发送登录请求
2.自动带着Cookie 去请求个人中心
'''
import urllib.request
from http import cookiejar #cookiejar可以自动保存cookie
from urllib import parse 
# 1.1登录的网址
login_url = 'https://www.yaozh.com/login'
#登录之前登录页的网址 https://www.yaozh.com/login/，需要在这里找登录参数
#注意：后台根据发送的请求方式来判断的，GET请求方式返回登录页面，POST请求方式返回登录结果页面
# 1.2登录的参数
login_form_data = {
    'username':'13151073762',
    'pwd':'python123456',
    'formhash':'041448A7E5',
    'backurl':'https%3A%2F%2Fwww.yaozh.com%2F'
}
#1.3发送登录请求POST
cookie_jar = cookiejar.CookieJar()
#定义有添加cookie功能的处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)
#根据处理器生成opener
opener = urllib.request.build_opener(cookie_handler)

#添加请求头；带着参数发送POST请求
header = {
    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
#POST参数需要转译；POST请求data要求为bytes类型
login_str = urllib.parse.urlencode(login_form_data).encode('utf-8')
login_request = urllib.request.Request(url=login_url,headers=header,data=login_str)
opener.open(login_request) #如果登录成功，cookiejar自动保存cookie

#2.自动带着Cookie 去请求个人中心
center_url = 'https://www.yaozh.com/member/'
center_request = urllib.request.Request(url=center_url,headers=header)
response = opener.open(center_url)
data = response.read().decode('utf-8')
with open('yaozhi.html','w',encoding='utf-8') as f:
    f.write(data)
