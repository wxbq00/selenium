# from selenium import webdriver
# import sys
# from time import sleep
# from threading import Thread
# def test_baidu_search(browser,url):
#     driver=None
#     if browser=='firefox':
#         driver=webdriver.Firefox()
#     if browser=='chrome':
#         driver=webdriver.Chrome()
#     if driver==None:
#         exit()
#     driver.get(url)
#     driver.find_element_by_id('kw').send_keys('123')
#     driver.find_element_by_id('su').click()
#     driver.quit()
# if __name__ == '__main__':
#     data={'firefox':'http://www.baidu.com','chrome':'http://www.baidu.com'}
#     threads=[]
#     for b,url in data.items():
#         t=Thread(target=test_baidu_search,args=(b,url))
#         threads.append(t)
#     for th in threads:
#         th.start()

#####################################################
'''
             ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛

'''
# import requests
# url = "https://passport.cnblogs.com/user/signin"
# headers={
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
# }
# s=requests.session()
# r=s.get(url,headers=headers,verify=False)
# print(s.cookies)
# #添加需要登录的2个cookie
# c = requests.cookies.RequestsCookieJar()
# c.set('.CNBlogsCookie','B6A90E181901313D86B97AA3838F22706ADEC4D6A1456771C0E63994FDB9810EE3A2008C5F5B89610E26C2870D0BEEB80CDFDE78F88C69857B540E9ED7550DC6396E44E6A800B8401B912E9434F699E3B275ED11')
# c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8PhlBN8IFxtHhqIV3s0LCDkbEn3CfWgZM6I8YtisgwtSMrJ7jAw-j7K6mnuZq2jvuCdlgEBSX0rRIYXK-WlHfUPRZhL3zwbhU8HGOo1Wr_REsldV70EsBl1hskKlIcTu-acWR1b6xOOee-eIZYWLnCVuhG41Jti5YBc8i6jVXCv5cRvf5yQcXspk-Fzy0H93irNVi4yYCvrlmXLH939b-pg_UskXMUvIfrlsqVGtDNKmBBp4SxS_1YEwhW5l9EwrbcfVJoE9d5KJOAUYXk4QmSg37zWS3HFi1zEDjmt7wzND')
# s.cookies.update(c)
# print(s.cookies)
# url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
# body = {"__VIEWSTATE": "",
#  "__VIEWSTATEGENERATOR":"FE27D343",
#  "Editor$Edit$txbTitle":"这是绕过登录的标题：上海-悠悠",
# "Editor$Edit$EditorBody":"<p>这里是中文内容：http://www.cnblogs.com/yoyoketang/</p>",
#  "Editor$Edit$Advanced$ckbPublished":"on",
# "Editor$Edit$Advanced$chkDisplayHomePage":"on",
#  "Editor$Edit$Advanced$chkComments":"on",
# "Editor$Edit$Advanced$chkMainSyndication":"on",
# "Editor$Edit$lkbDraft":"存为草稿",
#  }
# r2 = s.post(url2, data=body, verify=False)
# print(r.content)

#####################################################
import requests
url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-1202247993797-yunda.html"
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
}# get方法其它加个User-Agent就可以了
s=requests.session()
r=s.get(url,headers=headers,verify=False)
result=r.json()
data=result['data']
print(data)
print(data[0])
get_result=data[0]['context']
print(get_result)
if u"已签收" in get_result:
   print ("快递单已签收成功")
else:
   print ("未签收")







