import requests
header = { # 登录抓包获取的头部
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
 "Accept": "*/*",
 "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate",
 "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"X-Requested-With": "XMLHttpRequest",
"Content-Length": "423",
    "Connection": "keep-alive"
}
body = {"key1": "value1",
 "key2": "value2"}# 这里账号密码就是抓包的数据
s = requests.session()
login_url = "http://xxx.login" #　自己找带token网址
login_ret = s.post(login_url, headers=header, data=body)
# 这里token在返回的json里，可以直接提取
token = login_ret.json()["token"]
# 这是登录后发的一个post请求
post_url = "http://xxx"
# 添加token到请求头
header["token"] = token
# 如果这个post请求的头部其它参数变了，也可以直接更新
header["Content-Length"]="9"
body1 = {
 "key": "value"
}
post_ret = s.post(post_url, headers=header, data=body1)
print( post_ret.content)



