import json
import time 
import requests

# #1.字符串和 dic list 转换 方法：loads dumps
# #字符串(json)---dict list
# data = '[{"name":"张三","age":"16"},{"name":"李四","age":"18"}]'
# list_data = json.loads(data) #转换为list
# print(type(data))
# print(type(list_data))
# #dict list --- 字符串
# list2 = [{"name":"张三","age":"16"},{"name":"李四","age":"18"}]
# json_data = json.dumps(list2) #转换为str



# #2.文件对象和 dic list 转换 方法：load dump

# #dict list 写入文件
# list2 = [{"name":"张三","age":"16"},{"name":"李四","age":"18"}]
# #fp 是 file path
# fp = open('json2.json','w')
# json.dump(list2,fp) #直接转换为str写入文件
# fp.close()

# #读取文件json ---List dict
# fp = open('json2.json','r')
# result = json.load(fp)  #读取json文件

'''动态界面的爬取'''
# #时间戳 变为时间格式
# timestamp = 1576153596866
# timearray = time.localtime(float(timestamp/1000))
# tt = time.strftime('%Y--%m--%d %H:%M:%S',timearray)
# print(tt)

#将当前时间变为时间戳格式
timestamp = int(time.time()*1000)
base_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={}&keyword=python&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
url = base_url.format(timestamp)

header = {
'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
response = requests.get(url=url,headers=header)
str_data = response.content.decode('utf-8')

#将数据转化成python对象
dict_data = json.loads(str_data)
dict_data2 = dict_data['Data']
list_data = dict_data2['Posts']
for dict_value in list_data:
    career = dict_value['RecruitPostName']
    print(career)

# print(dict_data)