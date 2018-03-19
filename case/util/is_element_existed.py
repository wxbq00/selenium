# coding:utf-8
from selenium import webdriver
from case.config.config import DRIVER_PATH
driver = webdriver.Chrome(DRIVER_PATH)
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
def is_element_exist(css):
    s=driver.find_elements_by_css_selector(css_selector=css)
    if len(s)==0:
        print('元素不存在：%s'%css)
        return False
    elif len(s)==1:
        return True
    else:
        print('找到%s个元素:%s'%(len(s),css))
        return False
if is_element_exist("#kw"):
    driver.find_element_by_id("kw").send_keys("yoyoketang")
# 判断页面有无标签为input元素
if is_element_exist("input"):
    driver.find_element_by_tag_name("input").send_keys("yoyoketang")
# 判断页面有无id为xxx的元素
if is_element_exist("xxx"):
    driver.find_element_by_id("xxx").send_keys("yoyoketang")

