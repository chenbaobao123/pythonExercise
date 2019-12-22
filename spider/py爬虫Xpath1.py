import requests
import re
#安装支持 解析html和XML的解析库 lxml 
from lxml import etree
url = 'https://news.baidu.com/'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
response = requests.get(url,headers=header)
data = response.content.decode('utf-8')
with open('baidunew.html','w',encoding='utf-8') as f:
    f.write(data)
#利用Xpath解析数据
#抓取‘标题’ ‘url’

#1.转解析类型
xpath_data = etree.HTML(data)
#2.调用 xpath的方法 (1.)节点 /  (2.)跨节点 // (3.)精确的标签 //a[@属性='属性值'] (4.)标签包裹的内容 text() (5.)属性：@href 
#xpath返回的数据类型：list; xpath小标是从1开始的，只能取平级关系的标签，跨节点不能
result = xpath_data.xpath('//a/text()')
# result = xpath_data.xpath('//a[@mon="ct=1&a=1&c=top&pn=0"]/text()')
# result = xpath_data.xpath('//a[@mon="ct=1&a=1&c=top&pn=0"]/@href')

print(result)