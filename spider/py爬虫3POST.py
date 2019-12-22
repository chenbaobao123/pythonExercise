import requests
#1.确定请求链接
url = 'https://fanyi.baidu.com/sug'
#2.发送请求
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
value = input('请输入你要查的词')
data = {'kw':value}
response = requests.post(url=url,headers=headers,data=data)
#3.解析数据
data = response.json()
print(data)
q = data['data'][0]['k']
h = data['data'][0]['v'].split(';')[-2]
print(q,'==',h)
