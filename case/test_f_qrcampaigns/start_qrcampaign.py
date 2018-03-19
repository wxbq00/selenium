from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from case.login import Login,key
#from case.config.browser_engine import browser_engine
from case.config.config import DRIVER_PATH
from case.config.screen import Screen
from case.log.log import Log
class location(unittest.TestCase):
    driver = webdriver.Chrome(DRIVER_PATH)
    logger = Log()
    @classmethod
    def setUpClass(cls):

        Login().user_login(cls.driver)
        cls.driver.find_element_by_xpath('/html/body/div[1]/div/div/sidebar/div[1]/ul/li[7]/a/span').click()
    @Screen(driver)
    def test_create_qrcampagin(self):
        self.driver.find_element_by_xpath('//*[@id="campaignsList"]/div[1]/div/ul/li/button/span[2]').click()#new
        self.driver.find_element_by_id('name').send_keys(key)
        self.driver.find_element_by_xpath('//*[@id="campaignEdit"]/div/ul/li/button/span[2]').click()
        self.driver.find_element_by_xpath('//*[@id="campaignEdit"]/div/div[2]/div/div/div[1]/div/button/span').click()#new
        time.sleep(1)
        self.driver.find_element_by_id('name').send_keys(key)
        self.driver.find_element_by_xpath('//input[@value="articleList"]').click()
        s=self.driver.find_element_by_xpath('//*[@id="qrCodeEdit"]/div[2]/div/div/div[2]/form/div[4]/div[2]/article-list-select-component/select')
        Select(s).select_by_visible_text('lucas')
        self.driver.find_element_by_xpath('//*[@id="qrCodeEdit"]/div[1]/ul/li[1]/button/span[2]').click()#save
        self.driver.find_element_by_xpath('//*[@id="campaignEdit"]/div/div[2]/div/div/div[2]/div/table/tbody/tr[2]/td[4]/a').click()#edit
        self.driver.find_element_by_xpath('//*[@id="qrCodeEdit"]/div[1]/ul/li[2]/button/span[2]').click()

        self.driver.find_element_by_xpath('//*[@id="qrCodeEdit"]/div[1]/ul/li[1]/button/span[2]').click()#save



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()



