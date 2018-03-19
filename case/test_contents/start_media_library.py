
from selenium import webdriver
import time
import unittest
from case.login import Login,key
from selenium.webdriver.common.action_chains import ActionChains
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
        cls.driver.find_element_by_xpath('/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[3]/a/span').click()#media library
    @Screen(driver)
    def test_create_new(self):
        self.driver.find_element_by_xpath(
            '//*[@id="fileList"]/div[1]/div/action-button-list/ul/li[1]/button/span[2]').click()  # new
        time.sleep(2)
        self.driver.find_element_by_id('name').send_keys(key)
        self.driver.find_element_by_xpath('//input[@type="search"]').click()
        self.driver.find_element_by_xpath('//input[@type="search"]').send_keys(key)#tag
        js = 'document.getElementsByClassName("ui-select-choices-row-inner")[0].click();'
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[2]/div[2]/form/div[4]/label/input').click()
        self.driver.find_element_by_xpath("//input[@type='file']").send_keys(r'/Users/Tiernan/Desktop/lucas/a.jpg ')
        self.driver.find_element_by_xpath('//*[@id="fileEdit"]/ul/li[1]/button/span[2]').click()
        tags=self.driver.find_elements_by_xpath('//*[@id="fileList"]/div[3]/div[1]/div/div[2]/div/label/span')

        contents=[c.text for c in tags]
        self.assertTrue(contents[-1].find(key))
        tags[-1].click()
        name=self.driver.find_elements_by_xpath('//*[@id="fileList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/a')
        text=[c.text for c in name]
        self.assertIn(key, text)

    @Screen(driver)
    def test_d_search(self):
        tags = self.driver.find_element_by_xpath('//*[@id="fileList"]/div[3]/div[1]/div/div[2]/div[4]/label/span')
        tags.click()
        self.driver.find_element_by_xpath('//*[@placeholder="Search"]').send_keys(key)
        value = self.driver.find_element_by_xpath('//*[@placeholder="Search"]').get_attribute('value')
        time.sleep(1)
        # self.driver.find_element_by_xpath('//*[@id="fileList"]/div[3]/div[2]/div/div[2]/div/ul/li[6]/a').click()#last page
        tr = self.driver.find_elements_by_xpath(
            '//*[@id="fileList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/a')

        keyword = [c.text for c in tr]
        print(keyword)
        # assert value in keyword
        for i in keyword:
            self.assertIn(value.lower(), i.lower())

    @Screen(driver)
    def test_filterByImage(self):
        self.driver.find_element_by_xpath('//*[@id="fileList"]/div[2]/div/div/input').clear()

        self.driver.find_element_by_xpath('//*[@id="fileList"]/div[3]/div[1]/div/div[2]/div[1]/label/input').click()#image
        type=self.driver.find_elements_by_xpath('//*[@id="fileList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[4]')
        text=[c.text for c in type]
        self.assertNotIn('Image',text)

    @Screen(driver)
    def test_sortByName(self):
        self.driver.find_element_by_xpath(
            '//*[@id="fileList"]/div[3]/div[1]/div/div[2]/div[1]/label/input').click()  # image
        self.driver.find_element_by_xpath('//*[@id="fileList"]/div[3]/div[2]/div/div[2]/div/table/thead/tr/th[3]').click()
        name=self.driver.find_elements_by_xpath('//*[@id="fileList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/a')
        text=[c.text for  c in name]
        # self.driver.find_element_by_xpath('//*[@id="fileList"]/div[3]/div[2]/div/div[2]/div/ul/li[4]/a').click()  # 分页
        # text1 = [c.text for c in name]
        # text.extend(text1)
        list= [c.lower() for c in text]
        print(list)
        self.assertTrue(list==sorted(list))

    @Screen(driver)
    def test_t_delete(self):
        delete=self.driver.find_element_by_xpath('//*[@id="fileList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[6]/button')#delete
        name=self.driver.find_element_by_xpath('//*[@id="fileList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[3]/a')

        n=name.text
        delete.click()
        self.driver.switch_to_alert().accept()
        time.sleep(2)
        tr = self.driver.find_elements_by_xpath(
            '//*[@id="fileList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/a')
        text=[c.text for c in tr]

        self.assertNotIn(n,text)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()

