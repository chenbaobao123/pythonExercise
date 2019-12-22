
import requests
from http import cookiejar #cookiejar可以自动保存cookie
from urllib import parse 
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
# session类可以自动保存cookies == cookiejar
session = requests.session()

#1.代码登陆
login_url = 'https://www.yaozh.com/login'
login_form_data = {
    'username': 'chenbaobao',
    'pwd': 'python123456',
    'formhash': 'C40FC1FD0E',
    'backurl': 'https%3A%2F%2Fwww.yaozh.com%2F'
}
login_response = session.post(login_url,headers=header,data=login_form_data)

#2.登录成功后 带着有效的cookie访问请求目标数据
member_url = 'https://www.yaozh.com/member/'
data = session.get(member_url,headers=header).content.decode('utf-8')
with open('geren.html','w',encoding='utf-8') as f:
    f.write(data)





