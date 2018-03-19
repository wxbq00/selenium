import requests
r=requests.get('http://www.baidu.com')
# par={'keyword':'lucas'}
# r=requests.get('http://zzk.cnblogs.com/s/blogpost?Keywords=yoyoketang',params=par)
# print(r.content,r.text)
# import json
# payload={'yoyo':'helloworld'
#          ,
#          'python':'214234234'
#          }
# data=json.dumps(payload)
# r=requests.post('http://httpbin.org/post',json=data)
# print(r.text)
###############################
# import urllib.request
#
# headers = {'Use-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
# url = "http://blog.ithomer.net"
# req = urllib.request.Request(url, headers=headers)
# content = urllib.request.urlopen(req).read()
# print(content)
##########################


# import requests
# url=' https://ing.cnblogs.com/ajax/ing/Publish '
# headers={
# "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
# "Accept": "application/json, text/javascript, */*; q=0.01",
# "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
# "Accept-Encoding": "gzip, deflate, br",
# "Content-Type": "application/x-www-form-urlencoded",
# # "VerificationToken": "xxx...",  # 已省略
# "X-Requested-With": "XMLHttpRequest",
# "Content-Length": "25",
# "Cookie": "xxx.....", # 已省略
# "Connection": "keep-alive"
#
#
# }
# payload={
# 'isSuccess':'True',
# 'responseText':'wqeq'
# }
# s=requests.session()
# r=s.post(url,json=payload,headers=headers,verify=False)
# print(r.json())
#####################################################
import json
json.dumps(['foo',{'bar':'1.0,2'}])
print(json.dumps('\'foo\bar'))



