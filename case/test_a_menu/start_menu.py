from selenium import webdriver
import time
import unittest
from case.login import Login,key
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from case.two_time_package import Yoyo
from case.config.config import DRIVER_PATH

from case.config.screen import Screen
from case.log.log import Log
logger=Log()
from case.test_a_menu.menu_page import Menu
class menu(unittest.TestCase):
    driver = webdriver.Chrome(DRIVER_PATH)
    yoyo=Yoyo(driver)
    @classmethod
    def setUpClass(cls):


        cls.menu=Menu(cls.driver)


        Login().user_login(cls.driver)
        cls.driver.find_element_by_xpath('/html/body/div/div/div/sidebar/div[1]/ul/li[2]/a/span[1]').click()  # basic
        time.sleep(1)
        # lo=Login()
        # lo.login('mn-admin@mobilenowgroup.com', 'MobileNow2017!')
        # time.sleep(3)
        # cls.driver.find_element_by_xpath('/html/body/div/div/div/sidebar/div[1]/ul/li[2]/a/span[1]').click()  # basic
        # time.sleep(1)
        cls.driver.find_element_by_xpath(
            '/html/body/div/div/div/sidebar/div[1]/ul/li[2]/ul/li[1]/a/span').click()  # menu
    @Screen(driver)
    def test_a_edit_menu(self):#新建文章，判断文章数量是否正确
        self.menu.click_new_menu()
        self.menu.click_article_checkbox()
        self.menu.clear_menu_name()
        self.menu.input_menu_name()
        self.menu.click_new_article()#new
        self.menu.move_click_article()
        time.sleep(1)
        self.menu.input_slug()
        self.menu.input_title()
        self.menu.click_input_tag()
        self.yoyo.js_execute('document.getElementsByClassName("ui-select-choices-row-inner")[0].click();')
        self.yoyo.js_scroll_end()
        self.menu.click_save()  # save
        time.sleep(1)
        contents=[c.text for c in self.menu.article_loc]
        self.assertIn(key,contents)
        self.menu.click_save_draft()
        self.menu.click_publish()
        self.driver.switch_to_alert().accept()
        self.menu.click_contents()  # contents
        time.sleep(1)
        self.menu.click_article_bar()
        self.menu.click_last()
        title=self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/a')
        text=[c.text for c in title]
        self.assertIn(key,text)


        tr=self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr')
        self.assertEqual(len(contents),len(tr)-1)#不相等
        self.driver.find_element_by_xpath('/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[4]/a/span').click()#tag


        tag_name=self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[3]/div/div/div[2]/div/table/tbody/tr/td[1]/div')
        tag=[c.text for c in tag_name]
        self.assertIn(key,tag)

    @Screen(driver)
    def test_barticle_list(self):#判断list的数量是否相同
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[2]/a/span').click()  # article list

        tr = self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[2]/div/div/div[2]/div/table/tbody/tr/td[1]/a')

        num=len(tr)

        self.driver.find_element_by_xpath('/html/body/div/div/div/sidebar/div[1]/ul/li[2]/a/span[1]').click()  # basic
        time.sleep(1)
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/sidebar/div[1]/ul/li[2]/ul/li[1]/a/span').click()  # menu
        self.driver.find_element_by_xpath('//*[@id="menu"]/div/div/div/div[1]/ol/li[1]/div/a[2]').click()#edit
        self.driver.find_element_by_xpath('//input[@value="articleList"]').click()
        # WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_id('pageType')).click()#有问题
        self.driver.find_element_by_xpath('//*[@id="menu"]/div/div/div/div[2]/form/div[2]/div[3]/div[2]/select').click()#article list
        option=self.driver.find_elements_by_xpath('//*[@id="menu"]/div/div/div/div[2]/form/div[2]/div[3]/div[2]/select/option')#article list
        print(len(option))
        self.assertEqual(len(option)-1,num)

    @Screen(driver)
    def test_createLink(self):
        self.driver.find_element_by_xpath('//input[@value="url"]').click()
        self.driver.find_element_by_id('url').send_keys('http://www.baidu.com')
        self.driver.find_element_by_xpath(
            '//*[@id="menu"]/action-button-list/ul/li[1]/button/span[2]').click()  # save draft
        self.driver.find_element_by_xpath(
            '//*[@id="menu"]/action-button-list/ul/li[2]/button/span[2]').click()  # publish
        time.sleep(2)
        self.driver.switch_to_alert().accept()




    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
if __name__ == '__main__':
    unittest.main()







