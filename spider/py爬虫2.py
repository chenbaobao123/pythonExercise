#导入网络请求模块
import requests
import re

#定义一个爬虫类
class MaoyanSpider(object):
    def __init__(self):
        self.base_url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36','Cookie': '__mta=55336468.1575276247194.1575429940175.1575429949815.67; uuid_n_v=v1; uuid=E7B78CD014DF11EA89470DC982E4B91ECFCA10BF3408461BA112ABD91C5D9A67; _csrf=e687df883a654bb3067be748d197da5f9725b18ea44454f1d8cd6436370d1415; _lxsdk_cuid=16ec5c7f812c8-0497ce11b8200a-2393f61-1fa400-16ec5c7f813c8; _lxsdk=E7B78CD014DF11EA89470DC982E4B91ECFCA10BF3408461BA112ABD91C5D9A67; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1575276247,1575343232,1575344888,1575345850; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=55336468.1575276247194.1575377584185.1575429886423.65; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1575429950; _lxsdk_s=16eceeff2d2-ab-d81-971%7C%7C12'}

    #请求页面信息
    def get_pageInfo(self,url):
        response = requests.get(url=url,headers=self.headers)
        if response.status_code == 200:
            return response.content.decode('utf-8')
        else:
            return None
            print(response.status_code)
    #设置10个页面的url
    def get_url(self):
        urls = []
        for i in range(0,100,10):
            urls.append(self.base_url.format(i))
        return urls
    #解析界面
    def parse_pageInfo(self,html):
        # pattern = re.compile('<dd>.*?<a.*?title="(.*?)".*?</a>.*?<p.*?star.*?>/s*(.*?)/s*</p>.*?<p.*?releasetime.*?>(.*?)</p>.*?<i.*?integer.*?>(.*?)</i>.*?<i.*?fraction.*?>(.*?)</i>>*?</dd>',re.S)
        pattern = re.compile('<dd>.*?<p.*?<a.*?title="(.*?)".*?</p>.*?'
                            +'<p.*?star.*?>\s*(.*?)\s*</p>.*?releasetime.*?'
                            +'>(.*?)</p>.*?movie-item-number score-num.*?'
                            +'<i.*?integer.*?>(.*?)</i>.*?<i.*?fraction.*?>(.*?)</i>.*?</p>.*?</dd>',re.S)
        # print(re.findall(pattern,html))
        return re.findall(pattern,html)
    #保存数据
    def save(self,data):
        #循环一次拿到一条数据
        for values in data:
            for value in values:
                for val in value:
                    with open('movie_str2.txt','a',encoding='utf-8') as f:
                        f.write(val)
                        f.write(' ;')
                with open('movie_str2.txt','a',encoding='utf-8') as f:
                    f.write('\n')
    #保存爬虫内容
    #爬虫的所有逻辑结构都放在这里
    def run(self):
        urls = self.get_url()
        data = []
        for url in urls:
            html = self.get_pageInfo(url)
            result = self.parse_pageInfo(html)
            data.append(result)
        print(data)
        self.save(data)

    
if __name__ == '__main__':
    maoyanspider = MaoyanSpider()
    maoyanspider.run()