#导入网络请求模块
import requests
import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
'''---爬取百度网页内容---'''
#创建请求头
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
#发送网络请求
# response = requests.get(url='https://www.baidu.com',headers=headers)
#获取请求的内容(有下面2种方法可以获取)
# print(response.content.decode('utf-8'))
# print(response.text)
# #获取响应头
# print(response.headers)
# #状态码
# print(response.status_code)

'''---爬取网页上的gif动图---'''
# 创建请求头
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
#发送网络请求
# response = requests.get(url='http://5b0988e595225.cdn.sohucs.com/images/20190905/e268c8f85e2645e98f1f83d7e6ac0884.gif',headers=headers)
#将获取的二进制内容进行保存，方法1，不需要写关闭文件的操作，代码运行结束后会自动运行关闭文件的代码
#方法1
# with open('baidu.png','wb') as f:
#     f.write(response.content)
#方法2
# f = open('baidu.png','wb')
# f.write(response.content)
# f.close()

'''---爬取猫眼Top100榜---'''
'''
1.分析界面，确定数据来源，确定请求链接
https://maoyan.com/board/4?offset=0
https://maoyan.com/board/4?offset=10
2.判断这个链接返回的数据里有没有想要的数据
 #确定数据来源的链接 https://maoyan.com/board/4?offset=0
3.写代码请求
4.解析数据 ——拿到想要的数据
5.保存数据
'''
#定义一个爬虫类
class MYSpider(object):
    def __init__(self,base_url,headers):
        self.base_url = base_url
        self.headers = headers
    #获取第一页内容
    def get_onePage(self):
        #拼接URL
        url = self.base_url
        #发送请求
        response = requests.get(url=url,headers=headers)
        response.encoding = 'utf-8'
        # print(response.content.decode('utf-8'))
        #做判断是否请求成功
        if response.status_code == 200:
            content = response.content.decode('utf-8')
            # print(content)
            return content
        else:
            return None
            print(response.status_code)
    #解析数据
    def parse_onePage(self,html):
        '''使用正则表达式解析数据，需要导入re模块'''
        #获取排名
        # pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?</dd>',re.S)
        #获取排名和名字
        pattern = re.compile('<span.*?site-item.*?>\s+(.*?)\s*?</span>',re.S)
        # print(re.findall(pattern,html))
        return re.findall(pattern,html)
        
    #保存数据
    def save(self,data):
        #循环一次拿到一条数据
        for value in data:
            
            with open('movie_str.txt','a',encoding='utf-8') as f:
                f.write(movie_str)

if __name__ == '__main__':
    base_url = 'https://tophub.fun/main/home/hot'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    myspider = MYSpider(base_url,headers)
    #调用获取数据的方法
    html = myspider.get_onePage()
    # print(html)
    #解析数据
    movie_data = myspider.parse_onePage(html)
    print(movie_data)
    #保存数据
    # myspider.save(movie_data)