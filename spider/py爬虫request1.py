#POST请求
import requests
#内网 需要 认证
url = 'https://www.12306.cn'
headr = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
# proxy = {'http':'171.35.167.197:9999'}
#https 是第三方 CA 证书认证的
#12306虽然是https 但它不是CA证书，是有自己颁布的证书，所以访问此网站是告诉Web忽略证书访问

#请求对象
response = requests.get(url=url,headers=headr,verify=False)
data = response.content.decode('utf-8')
with open('12306.html','w',encoding='utf-8') as f:
    f.write(data)