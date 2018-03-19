
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from case.login import Login,key
from case.test_d_location.location_page import Location,login_url,key

from case.config.config import DRIVER_PATH
from case.config.screen import Screen
from case.log.log import Log
class location(unittest.TestCase):
    driver = webdriver.Chrome(DRIVER_PATH)
    logger = Log()
    @classmethod
    def setUpClass(cls):


        cls.login=Location(cls.driver)#实例化类
        cls.login.login('mn-admin@mobilenowgroup.com','MobileNow2017!')
        # Login().user_login(cls.driver)
        # location=cls.driver.find_element_by_xpath('/html/body/div[1]/div/div/sidebar/div[1]/ul/li[4]/a/span[1]')
        # location.click()
    # def test_create_location(self):
    #     li=self.driver.find_elements_by_xpath('/html/body/div[1]/div/div/sidebar/div[1]/ul/li[4]/ul/li')
    #     li[-1].click()
    #     self.driver.find_element_by_class_name('active').click()
    #     self.driver.find_element_by_xpath('//*[@id="articleList"]/div[1]/div/action-button-list/ul/li/button/span[2]').click()
    #     self.driver.find_element_by_xpath('//input[@type="text"]').send_keys('lucas')
    #     self.driver.find_element_by_xpath('//input[@type="number"]').send_keys('1000')
    #     self.driver.find_element_by_xpath('//*[@id="locationTypeEdit"]/ul/li/button/span[2]').click()
        # self.login.click_manage()
        # self.login.click_manage_new()
        # self.login.input_name()
        # self.login.input_radius()
        # self.login.click_manage_save()

    @Screen(driver)
    def test_createLocation(self):

        self.login.click_location()
        self.login.click_new()
        self.login.input_title()
        self.login.click_tag()
        self.login.js_execute('document.getElementsByClassName("ui-select-choices-row-inner")[0].click();')
        self.login.js_execute('document.body.scrollTop=150')
        self.login.click_imgbtn()
        self.login.click_img()
        self.login.js_scroll_end()
        self.login.input_address()
        self.login.click_getAddress()
        time.sleep(5)
        self.login.js_scroll_top()
        self.login.click_save()
        self.login.click_publish()
        self.login.click_location()
        time.sleep(2)#重要
        title = self.driver.find_elements_by_xpath(
            '//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/a')

        text=[c.text for c in title]
        self.assertIn(key,text)

    @Screen(driver)
    def test_search(self):
        self.login.input_keyword()
        tr = self.login.find_elements(self.login.location_title_loc)
        keyword = [c.text for c in tr]
        for i in keyword:
            self.assertIn(key.lower(), i.lower())

    @Screen(driver)
    def test_sortByTitle(self):
        self.login.click(self.login.title_header_loc)
        tr = self.login.find_elements(self.login.location_title_loc)
        text = [c.text for c in tr]
        list = [c.lower() for c in text]
        print(list)
        self.assertTrue(list == sorted(list))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()
