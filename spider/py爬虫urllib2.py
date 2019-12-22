'''
User-Agent:
1.模拟真实的浏览器发送请求
2.request.add_header()动态添加head数据
IP代理：
免费的IP:时效性差，错误率高
付费的IP：时效性好，错误率低，花钱贵
IP分类：
透明：对方知道我们真实的IP
匿名：对方不知道我们真实的IP，但知道你使用了代理
高匿：对方不知道我们真实的IP，也不知道你使用了代理
'''
import urllib.request
import random
def load_baidu():
    url = 'http://www.baidu.com'
    user_agent_list=['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
                     'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
                     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
                     'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50']  
#每次请求的浏览器都不一样的
    random_user_agent = random.choice(user_agent_list)
    request = urllib.request.Request(url)
    #增加对应的请求头信息
    request.add_header('User-Agent',random_user_agent)
    #请求数据   
    response = urllib.request.urlopen(request)
    print(request.headers)

load_baidu()