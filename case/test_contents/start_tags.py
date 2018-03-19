from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from case.login import Login,key
from case.config.screen import Screen
from case.log.log import Log
from case.config.config import DRIVER_PATH
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
        cls.driver.find_element_by_xpath('/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[4]/a/span').click()#tags
    @Screen(driver)
    def test_createTag(self):
        self.driver.find_element_by_xpath('//*[@id="articleList"]/div[1]/div/ul/li/button').click()#create

        self.driver.find_element_by_xpath('//div[@class="form-group"]/input').clear()
        self.driver.find_element_by_xpath('//div[@class="form-group"]/input').send_keys(key)
        # js='document.body.getElementsByTagName("button")[0].click()'
        # self.driver.execute_script(js)
         # self.driver.current_window_handle()
        self.driver.find_element_by_xpath('//button[@title="Create"]').click()#不能创建相同名字的tag
            # js='document.getElementsByTagName("button")[0].click();'
            # self.driver.execute_script(js)
        # self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/ul/li[7]/a').click()
        try:
            WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/ul/li[7]/a')).click()  # LAST分页
        except Exception as e:
            print(e)
        name = self.driver.find_elements_by_xpath(
            '//*[@id="articleList"]/div[3]/div/div/div[2]/div/table/tbody/tr/td[1]/div')
        text = [c.text for c in name]
        self.assertEqual(key, text[-1])

    @Screen(driver)
    def test_action(self):

        self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/div/table/tbody/tr[2]/td[7]/div/a[1]').click()
        name=self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/div/table/tbody/tr[2]/td[1]/div/input')
        oldName=name.get_attribute('value')

        name.send_keys('123')
        self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/div/table/tbody/tr[2]/td[7]/div/a[1]').click()
        newName=self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/div/table/tbody/tr[2]/td[1]/div').text
        self.assertNotEqual(oldName,newName)
    # def test_deleteTag(self):
    #     tr=self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/div/table/tbody/tr/td[7]/div/a[2]')
    #     name=tr[-2].text
    #     print(name)
    #     tr[-2].click()
    #     self.driver.switch_to_alert().accept()
    #     list=self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/div/table/tbody/tr/td[1]/div')
    #     text=[c.text for c in list]
    #     print(text)
    #     self.assertNotIn(name,text)
    @Screen(driver)
    def test_searchByName(self):
        self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/ul/li[1]/a').click()#first page
        self.driver.find_element_by_xpath('//*[@id="articleList"]/div[2]/div/div/input').send_keys(key)
        value=self.driver.find_element_by_xpath('//*[@id="articleList"]/div[2]/div/div/input').get_attribute('value')
        name=self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/div/table/tbody/tr/td[1]/div')
        text=[c.text for c in name]
        print(text)
        for i in text:
            self.assertIn(value.lower(),i.lower())
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()

