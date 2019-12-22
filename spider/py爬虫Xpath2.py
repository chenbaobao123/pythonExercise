import requests
from lxml import etree
import json
class BtcSpider(object):
    def __init__(self):
        self.base_url = 'https://www.chainnode.com/forum/61-'
        self.headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }
    #1.发请求
    def get_response(self,url):
        response = requests.get(url,headers=self.headers)
        data = response.content.decode('utf-8')
        return data
    #2.解析数据
    def parse_data(self,data):
        #1.转类型
        x_data = etree.HTML(data)
        #2，根据Xpath路径开始解析
        title_list = x_data.xpath('//a[@class="link-dark-major font-bold bbt-block"]/text()')
        url_list = x_data.xpath('//a[@class="link-dark-major font-bold bbt-block"]/@href')
        data_list = []
        for index,title in enumerate(title_list):
            news = {}
            news[title] = 'https://www.chainnode.com'+url_list[index]
            data_list.append(news)
        # print(data_list)
        return data_list
    #3.保存数据
    def save_data(self,data):
        #利用json模块将list转换为str
        data_str = json.dumps(data)
        with open('8btc.json','w',encoding='utf-8') as f:
            f.write(data_str)
    #4.启动
    def run(self):
        pass
        #1.拼接 完成url
        url = self.base_url+'1.html'
        #2.发请求
        data = self.get_response(url)
        #3.做解析
        result = self.parse_data(data)
        #4.保存
        self.save_data(result)
btc = BtcSpider().run()