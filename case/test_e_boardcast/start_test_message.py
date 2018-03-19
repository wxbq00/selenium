from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
#from case.config.browser_engine import browser_engine
from case.config.screen import Screen
from case.log.log import Log

from case.login import Login,key,login
from case.config.config import DRIVER_PATH
class location(unittest.TestCase):
    driver = webdriver.Chrome(DRIVER_PATH)
    logger = Log()
    @classmethod
    def setUpClass(cls):

        Login().user_login(cls.driver)
        cls.driver.find_element_by_xpath('/html/body/div/div/div/sidebar/div[1]/ul/li[5]/a/span[1]').click()#boardcast
    @Screen(driver)
    def test_create_message(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/sidebar/div[1]/ul/li[5]/ul/li[2]/a/span').click()#message
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="articleList"]/div/div/ul/li/button/span[2]').click()#new

        self.driver.find_element_by_id('broadcastName').send_keys(key)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[2]/div/form/div[4]/div/label/input').click()# article list
        s=self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[2]/div/form/div[4]/article-list-select-component/select')
        Select(s).select_by_visible_text('testlucas')
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[5]/div[2]/div/table/tbody/tr[4]/td[1]/input').click()
        # js='var q=document.body.scrollTop=10000'
        # self.driver.execute_script(js)
        # self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[6]/label/input').click()#schedule
        # js='document.getElementById("pickr").removeAttribute("readonly");'
        # self.driver.execute_script(js)
        # self.driver.find_element_by_id('pickr').clear()
        # self.driver.find_element_by_id('pickr').send_keys('2017-08-03 18:20')#schedule有问题
        js = 'var q=document.body.scrollTop=0'
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath('//*[@id="triggerEdit"]/ul/li/button/span[2]')#send
        self.driver.switch_to_alert().accept()

    @Screen(driver)
    def test_a_delete(self):
        first=self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/div/table/tbody/tr[2]/td[1]/a')
        contents=first.text
        all=self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/div/table/tbody/tr/td[1]/a')
        all_text=[c.text for c in all]
        delete_btn=self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/div/table/tbody/tr[2]/td[7]/button')
        delete_btn.click()
        self.driver.switch_to_alert().accept()
        time.sleep(2)
        self.assertIn(contents,all_text)



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()



