import json
import csv
#需求 json中的数据 转换为 csv文件
#1. 读，创建文件
json_fp = open('json2.json','r')
csv_fp = open('csv1.csv','w',encoding='utf-8')
#2.提出表头 表内容
data_list = json.load(json_fp)
# sheet_title = data_list[0].keys()
sheet_title = {'姓名','年龄'}
# print(sheet_data)
# print(type(sheet_data))
sheet_data = []
for data in data_list:
    sheet_data.append(data.values())
#3.csv 写入器
writer = csv.writer(csv_fp)
#4.写入表头
writer.writerow(sheet_title)
#5.写入内容
writer.writerows(sheet_data)
#6.关闭俩个文件
json_fp.close()
csv_fp.close()