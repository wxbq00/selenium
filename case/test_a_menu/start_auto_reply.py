from selenium import webdriver
import time
import unittest
from case.login import Login,key
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from case.log.log import Log
from case.config.config import Config,DATA_PATH
from case.config.file_reader import ExcelReader
from selenium.webdriver.support.select import Select
from case.two_time_package import Yoyo

from case.config.config import DRIVER_PATH
from case.config.screen import Screen

logger=Log()
class auto_reply(unittest.TestCase):

    excel=DATA_PATH+'/data.xlsx'
    driver = webdriver.Chrome(DRIVER_PATH)
    @classmethod
    def setUpClass(cls):


        yoyo=Yoyo(cls.driver)
        Login().user_login(cls.driver)
        cls.driver.find_element_by_xpath(
            '/html/body/div/div/div/sidebar/div[1]/ul/li[3]/a/span[1]').click()  # contents

        time.sleep(1)
        cls.driver.find_element_by_xpath(
            '/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[1]/a/span').click()  # articles

        cls.driver.find_element_by_xpath('/html/body/div/div/div/sidebar/div[1]/ul/li[2]/a/span[1]').click()
        time.sleep(1)
        cls.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/sidebar/div[1]/ul/li[2]/ul/li[2]/a/span').click()  # auto-reply

    @Screen(driver)
    def test_create_autoReply(self):
        self.driver.find_element_by_xpath('//*[@id="triggerList"]/div[1]/div/action-button-list/ul/li[1]/button/span[2]').click()#create
        self.driver.find_element_by_id('keyword').send_keys(key)
        checkbox=self.driver.find_element_by_xpath('//input[@type="checkbox"]')
        checkbox.click()
        s=self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[2]/div/form/div[3]/article-select-component/select')
        Select(s).select_by_visible_text('selenium')
        # s.click()
        # js = 'document.getElementsByClassName("ui-select-choices-row-inner")[1].click();'
        # self.driver.execute_script(js)
        self.driver.find_element_by_xpath('//*[@id="triggerEdit"]/ul/li[1]/button/span[2]').click()#save

        # WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_xpath('//*[@id="triggerEdit"]/ul/li[2]/button/span[2]')).click()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/sidebar/div[1]/ul/li[2]/ul/li[2]/a/span').click()
        # js = "window.scrollTo(0,document.body.scrollHeight)"
        # self.driver.execute_script(js)

        self.driver.find_element_by_xpath('//*[@id="triggerList"]/div[4]/div/div[2]/div/ul/li[8]/a').click()#last


        time.sleep(2)
        keyword=self.driver.find_elements_by_xpath('//*[@id="triggerList"]/div[4]/div/div[2]/div/table/tbody/tr/td[2]/a')

        text=[c.text for c in keyword]
        logger.info(text)
        for i in text:
            print(i)
        self.assertEqual(key,text[-1])

    @Screen(driver)
    def test_filter_by_article(self):
        ca = self.driver.find_element_by_xpath('//*[@id="triggerList"]/div[3]/div/div[2]/div[3]/label/input')  # article checkbox
        ca.click()
        columns = self.driver.find_elements_by_xpath('//*[@id="triggerList"]/div[4]/div/div[2]/div/table/tbody/tr/td[3]')
        contents = [c.text for c in columns]

        logger.info(contents)
        for i in contents:
            self.assertEqual('articleList',i)
    @Screen(driver)
    def test_sortByKeyword(self):
        # ca = self.driver.find_element_by_xpath(
        #     '//*[@id="triggerList"]/div[3]/div/div[2]/div[3]/label/input')  # article checkbox
        # ca.click()
        keyword=self.driver.find_element_by_xpath('//*[@id="triggerList"]/div[4]/div/div[2]/div/table/thead/tr/th[2]')
        keyword.click()
        page=self.driver.find_elements_by_xpath('//*[@id="triggerList"]/div[4]/div/div[2]/div/ul/li/a')#页数
        #print(type(page))#list

        list=[]
        for i in page[3:-1]:
            time.sleep(2)
            col = self.driver.find_elements_by_xpath(
            '//*[@id="triggerList"]/div[4]/div/div[2]/div/table/tbody/tr/td[2]/a')
            keyword_text = [c.text for c in col]

            list.extend(keyword_text)
            i.click()


            #print(i.text)
        new = [x for x in list if x != '']#要对List进行迭代删除操作的，防止删除操作后在下一个迭代循环中索引值的错乱，要复制一个列表用来迭代。
        print(new)
        print(sorted(new))
        self.assertTrue(new == sorted(new))






    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()