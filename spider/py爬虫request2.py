
import requests
from http import cookiejar #cookiejar可以自动保存cookie
from urllib import parse 
# 1.1登录的网址
login_url = 'https://www.yaozh.com/login'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
cookies = 'acw_tc=707c9f9815759480679131401e169c797992e318d1621576ba63d7811c1715; PHPSESSID=j1ivh2c4djljahstlusq1gcbs3; _ga=GA1.2.635722897.1575948068; _gid=GA1.2.434848064.1576052343; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1576052347; yaozh_logintime=1576052357; yaozh_user=854816%09chenbaobao; yaozh_userId=854816; yaozh_jobstatus=kptta67UcJieW6zKnFSe2JyXnoaZbJltlpqHnKZxanJT1qeSoMZYoNdzaJFyVMbNx8%2FGxdCZxqSHn9ibbHFXpJLUrZCnyqPKhnSqm2linYe295e0194944b02249bCa7BB5E848073cTlpuZmmucbpWah5ymcWlyU9WinpiDcdieamqbWmOYnJiRmZaUbJ1ml5iHnLA%3D8b2453fd762858898af5c8ac6e41f382; db_w_auth=735857%09chenbaobao; UtzD_f52b_saltkey=lQwxcvPw; UtzD_f52b_lastvisit=1576048758; UtzD_f52b_lastact=1576052358%09uc.php%09; UtzD_f52b_auth=fc0bXXzR1CvRz8J8wf371e2HzND4rqNKZzq%2BS%2F2InKQIRJ6qxNpk7cSKytrc5Fgx8VW0iZW38WlDHegMfiE5svmsOEk; yaozh_uidhas=1; yaozh_mylogin=1576052360; acw_tc=707c9f9815759480679131401e169c797992e318d1621576ba63d7811c1715; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1575945216%2C1575948068%2C1576052342'
cookie_dict = {}
cookie_list = cookies.split('; ')
for cookie in cookie_list:
    cookie_dict[cookie.split('=')[0]] = cookie.split('=')[1]
#以上for循环还可以使用字典推导式完成
#cook_dict = {cookie.split('=')[0]=cookie.split('=')[1] for cookie in cookie_list}
response = requests.get(url=login_url,headers=header,cookies=cookie_dict)
data = response.content.decode('utf-8')
with open('yaozhi.html','w',encoding='utf-8') as f:
    f.write(data)









