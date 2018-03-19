
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from case.login import Login,key
from case.config.screen import Screen
from case.log.log import Log

from case.config.config import DRIVER_PATH
class location(unittest.TestCase):
    driver = webdriver.Chrome(DRIVER_PATH)
    logger = Log()
    @classmethod
    def setUpClass(cls):

        Login().user_login(cls.driver)
        cls.driver.find_element_by_xpath('/html/body/div/div/div/sidebar/div[1]/ul/li[5]/a/span[1]').click()
    @Screen(driver)
    def test_create_subscriber_qrcode(self):
        self.driver.find_element_by_xpath('/html/body/div/div/div/sidebar/div[1]/ul/li[5]/ul/li[1]/a/span').click()
        self.driver.find_element_by_xpath('//*[@id="teamList"]/div[1]/div/ul/li/button/span[2]').click()
        self.driver.find_element_by_id('name').send_keys(key)
        js = "var q=document.body.scrollTop=100000"
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath('//input[@placeholder="Add QR Code"]').click()
        js='document.getElementsByClassName("ui-select-choices-row-inner")[2].click();'
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath('//*[@id="groupEdit"]/div/ul/li/button/span[2]').click()#save
        type=self.driver.find_elements_by_xpath('//*[@id="teamList"]/div[3]/div/div/div[2]/div/table/tbody/tr/td[3]')
        text=[c.text for c in type]
        self.assertEqual('qrcodeIds',text[-1])

    @Screen(driver)
    def test_sortByCount(self):
        self.driver.find_element_by_xpath('//*[@id="teamList"]/div[3]/div/div/div[2]/div/table/thead/tr/th[2]').click()
        count=self.driver.find_elements_by_xpath('//*[@id="teamList"]/div[3]/div/div/div[2]/div/table/tbody/tr/td[2]')
        num=[c.text for c in count]
        print(num)
        t = []
        c=[]
        for i in num:
            t.append(int(i))
            c.append(int(i))
        t.sort(reverse=True)
        # t.reverse()
        self.assertEqual(c,t)#fail

    @Screen(driver)
    def test_d_search(self):

        self.driver.find_element_by_xpath('//*[@placeholder="Search"]').send_keys(key)
        value = self.driver.find_element_by_xpath('//*[@placeholder="Search"]').get_attribute('value')
        time.sleep(1)
        tr = self.driver.find_elements_by_xpath(
            '//*[@id="teamList"]/div[3]/div/div/div[2]/div/table/tbody/tr/td[1]/a')

        keyword = [c.text for c in tr]
        print(keyword)
        # assert value in keyword
        for i in keyword:
            self.assertIn(value.lower(), i.lower())

    @Screen(driver)
    def test_esortByName(self):
        self.driver.find_element_by_xpath('//*[@placeholder="Search"]').clear()
        self.driver.find_element_by_xpath(
            '//*[@id="teamList"]/div[3]/div/div/div[2]/div/table/thead/tr/th[1]').click()#name
        name = self.driver.find_elements_by_xpath(
            '//*[@id="teamList"]/div[3]/div/div/div[2]/div/table/tbody/tr/td[1]/a')
        text = [c.text for c in name]
        # self.driver.find_element_by_xpath('//*[@id="fileList"]/div[3]/div[2]/div/div[2]/div/ul/li[4]/a').click()  # 分页
        # text1 = [c.text for c in name]
        # text.extend(text1)
        list = [c.lower() for c in text]
        print(list)
        self.assertTrue(list == sorted(list))
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()



