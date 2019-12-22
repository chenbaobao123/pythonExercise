import requests
import re 
url = 'https://news.baidu.com/'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
response = requests.get(url,headers=header)
data = response.content.decode('utf-8')
with open('baidunew.html','w',encoding='utf-8') as f:
    f.write(data)
#利用正则解析数据
#抓取‘标题’ ‘url’
pattern = re.compile('<strong>.*?<a href="(.*?)".*?>(.*?)</a>.*?</strong>',re.S)
result = pattern.findall(data)
print(result)