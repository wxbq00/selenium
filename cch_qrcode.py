from selenium import webdriver
import time
import unittest
from random import randint
from selenium.webdriver.support.select import Select
import HTMLTestRunner
listaa=r'/Users/Tiernan/Desktop/wcn_selenium'
class cch(object):

    def setup(self):
        self.driver = webdriver.Chrome('/Users/Tiernan/Desktop/chromedriver.exe')
        self.driver.get('http://stagingcachecache.cache-cache.cn/admin/#/login')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        username = self.driver.find_element_by_xpath(
            "//input[@name='email']")

        username.clear()
        username.send_keys('admin@example.com')
        userpasswd = self.driver.find_element_by_xpath("//input[@name='password']")
        userpasswd.clear()
        userpasswd.send_keys('password')
        loginbt = self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/ui-view/div/form/fieldset/button')
        loginbt.click()
    def test_create_qrcode(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/sidebar/div[1]/ul/li[7]/a').click()
        self.driver.find_element_by_xpath('//*[@id="campaignsList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr[5]/td[2]/a').click()#edit
        self.driver.find_element_by_xpath('//*[@id="campaignEdit"]/div/div[2]/div/div/div[1]/div/button/span').click()#new
        time.sleep(2)#需要的
        self.driver.find_element_by_id('name').send_keys(randint(1,1000))
        js = "var q=document.body.scrollTop=100000"
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath('//*[@id="qrCodeEdit"]/div[2]/div/div/div[2]/form/div[4]/div[1]/div/label/input').click()#article
        s=self.driver.find_element_by_xpath('//*[@id="qrCodeEdit"]/div[2]/div/div/div[2]/form/div[4]/div[1]/article-select/select')
        Select(s).select_by_visible_text('亲爱的，报名成功啦～')
        self.driver.find_element_by_xpath('//*[@id="qrCodeEdit"]/div[1]/ul/li[1]/button').click()
        name=self.driver.find_elements_by_xpath('//*[@id="campaignEdit"]/div/div[2]/div/div/div[2]/div/table/tbody/tr/td[2]/a')
        name[-1].click()
        self.driver.find_element_by_xpath('//*[@id="qrCodeEdit"]/div[1]/ul/li[2]/button/span[2]').click()#generate
        self.driver.back()

test=cch()
for i in range(1,10):
    test.test_create_qrcode()





