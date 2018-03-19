from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

from case.login import Login,key

from case.config.config import DRIVER_PATH
from case.config.screen import Screen
from case.log.log import Log
class article_unittest(unittest.TestCase):
    driver = webdriver.Chrome(DRIVER_PATH)
    logger = Log()
    @classmethod
    def setUpClass(cls):

        cls.driver = webdriver.Chrome(DRIVER_PATH)

        cls.driver = webdriver.Chrome()

        Login().user_login(cls.driver)
        cls.driver.find_element_by_xpath('/html/body/div/div/div/sidebar/div[1]/ul/li[3]/a/span[1]').click()  # contents
        time.sleep(1)
        cls.driver.find_element_by_xpath(
            '/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[2]/a').click()  # article list
    @Screen(driver)
    def test_create_articlelist(self):
        self.driver.find_element_by_xpath(
            '//*[@id="articleList"]/div[1]/div/action-button-list/ul/li/button/span[2]').click()  # new
        time.sleep(2)
        self.driver.find_element_by_id('name').send_keys(key)
        s = self.driver.find_element_by_xpath(
            '//*[@id="articleListEdit"]/div[2]/form/div[2]/ol/li[2]/article-select-component/select')
        Select(s).select_by_visible_text('beijing')
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="articleListEdit"]/div[2]/form/div[2]/ol/li[2]/button/span').click()  # add to list
        self.driver.find_element_by_xpath(
            '//*[@id="articleListEdit"]/div[2]/action-button-list/ul/li/button/span[2]').click()  # save
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[2]/a').click()
        text=self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[2]/div/div/div[2]/div/table/tbody/tr/td[1]/a')
        contents=[c.text for c in text]
        self.assertIn(key,contents)

    @Screen(driver)
    def test_delete_articleList(self):
        time.sleep(2)
        self.driver.find_elements_by_xpath( '//*[@id="articleList"]/div[2]/div/div/div[2]/div/table/tbody/tr/td[1]/a')[-1].click()#最后一个

        self.driver.find_element_by_xpath('//*[@id="articleListEdit"]/div[2]/action-button-list/ul/li[2]/button').click()#delete
        time.sleep(2)
        text = self.driver.find_elements_by_xpath(
            '//*[@id="articleList"]/div[2]/div/div/div[2]/div/table/tbody/tr/td[1]/a')
        contents = [c.text for c in text]
        self.assertNotIn(key,contents)

    @Screen(driver)
    def test_sortByName(self):
        self.driver.find_element_by_xpath('//*[@id="articleList"]/div[2]/div/div/div[2]/div/table/thead/tr/th[1]').click()#name
        name = self.driver.find_elements_by_xpath(
            '//*[@id="articleList"]/div[2]/div/div/div[2]/div/table/tbody/tr/td[1]/a')
        text = [c.text for c in name]
        list = [c.lower() for c in text]
        print(list)
        self.assertTrue(list == sorted(list))


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()

