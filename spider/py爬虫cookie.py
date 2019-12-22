'''---cookie,是什么,有什么作用？---'''
#http请求是无状态的请求协议，不会记住用户的状态和信息，也不清楚你在这之前访问过什么？
#因为网站需要记录用户是否登录时，就需要在用户登录后创建一些信息，并且要把这些信息记录在当前用户的浏览器中，记录的内容就是cookie
#用户使用当前的浏览器继续访问同一个服务器时，会主动携带这个网站设置的cookie信息
#cookie会在浏览器中记录信息，并且在访问时携带这个信息：
    #1.浏览器更换或删除cookie后，信息丢失
    #2.cookie在浏览器中记录的信息是不安全的，因为不能记录敏感信息

'''---session,是什么,有什么作用？---'''
#session是在服务器端进行数据的记录，并且在给每个用户会生成一个sessionID，并且把这个sessionID设置在用户的浏览器中，也就是设置cookie

'''---使用requests中的session方法----'''
#最终请求的目标地址
#https://study.163.com/member/login.htm?returnUrl=aHR0cHM6Ly9zdHVkeS4xNjMuY29tL3VzZXIvc2V0dGluZy5odG0.
#登陆的信息