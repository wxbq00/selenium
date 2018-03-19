from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from case.config.config import Config

from case.config.file_reader import ExcelReader
from case.config.config import DRIVER_PATH
from case.config.screen import Screen
from case.log.log import Log



from selenium.webdriver.common.action_chains import ActionChains

from case.login import Login,key
from case.config.config import DRIVER_PATH
class article_unittest(unittest.TestCase):

    logger = Log()
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(DRIVER_PATH)
        Login().user_login(cls.driver)
        cls.driver.find_element_by_xpath('/html/body/div/div/div/sidebar/div[1]/ul/li[3]/a/span[1]').click()  # contents
        time.sleep(1)
        cls.driver.find_element_by_xpath(
            '/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[1]/a/span').click()  # articles


    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()

    def test_a_create_article(self):
        self.driver.find_element_by_xpath('//*[@id="articleList"]/div[1]/div/ul/li[1]/button/span[2]').click()  # new
        article = self.driver.find_element_by_xpath('//*[@id="articleList"]/div[1]/div/ul/li[1]/ul/li[1]/a')  # article
        ActionChains(self.driver).move_to_element(article).perform()
        article.click()
        time.sleep(3)
        # self.driver.find_element_by_css_selector('.fileInput').click()
        # self.driver.find_element_by_xpath("//input[@type='file']").send_keys(r'C:\pic\a.jpg')
        #
        # self.driver.find_element_by_xpath(
        #     '/html/body/div[1]/div/div/add-file-component/div/div[2]/image-select-component/div/div[1]/button').click()#add image
        # WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_xpath(
        #     '/html/body/div[1]/div/div/add-file-component/div/div[2]/image-select-component/div/div[1]/button')).click()

        self.driver.find_element_by_id('slug').send_keys('www.baidu.com')
        self.driver.find_element_by_id('title').send_keys(key)
        self.driver.find_element_by_xpath("//input[@type='search']").click()
        self.driver.find_element_by_xpath("//input[@type='search']").send_keys(key)
        js = 'document.getElementsByClassName("ui-select-choices-row-inner")[0].click();'
        self.driver.execute_script(js)
        js = "var q=document.body.scrollTop=100000"
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath(
            '//*[@id="articleEdit"]/div/div/div[1]/div/div[2]/form/article-edit-page-component/div/div[2]/div[3]/div[2]').send_keys(
            'test')
        time.sleep(2)
        js = "var q=document.body.scrollTop=0"
        self.driver.execute_script(js)
        self.driver.find_element_by_xpath('//*[@id="articleEdit"]/div/ul/li[1]/button/span[2]').click()  # save

        self.driver.find_element_by_xpath('//*[@id="articleEdit"]/div/ul/li[2]/button/span[2]').click()  # publish


    def test_f_filter_by_article(self):
        message = self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div[1]/div/div[2]/div[4]/label/input')  # messages checkbox
        message.click()
        external_link=self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div[1]/div/div[2]/div[6]/label/input')
        external_link.click()
        text=self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[5]')
        content = [c.text for c in text]
        self.assertIn('Page',content)
        self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div[2]/div/div[2]/ul/li[4]/a').click()#分页
        text2 = self.driver.find_elements_by_xpath(
            '//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[5]')
        content2 = [c.text for c in text2]
        self.assertIn('Page', content2)
        self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div[2]/div/div[2]/ul/li[5]/a').click()
        text3 = self.driver.find_elements_by_xpath(
            '//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[5]')
        content3 = [c.text for c in text3]
        self.assertIn('Page', content3)


    def test_g_filterByPublished(self):
        unpublished = self.driver.find_element_by_xpath(
            '//*[@id="articleList"]/div[3]/div[1]/div/div[2]/div[2]/label/input')
        draft = self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div[1]/div/div[2]/div[3]/label/input')
        unpublished.click()
        # draft.click()
        published = self.driver.find_elements_by_xpath(
            '//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[4]/article-status-label/span')
        text = [c.text for c in published]
        self.assertNotIn('Unpublished', text)


    def test_h_search_by_keyword(self):
        self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div[2]/div/div[2]/ul/li[3]/a').click()#第一页
        self.driver.find_element_by_xpath('//*[@placeholder="Search"]').send_keys(key)
        value = self.driver.find_element_by_xpath('//*[@placeholder="Search"]').get_attribute('value')
        time.sleep(1)
        tr = self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/a')

        keyword = [c.text for c in tr]
        print(keyword)
        # assert value in keyword
        for i in keyword:
            self.assertIn(value.lower(), i.lower())

    @Screen(driver)
    def test_e_delete(self):
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[1]/a/span').click()  # articles
        self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[7]/button').click()

        self.driver.switch_to_alert().accept()
        self.assertTrue(self.driver.find_element_by_xpath('//*[@id="toast-container"]/div/div[1]').is_displayed())


    def test_b_create_message(self):
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[1]/a/span').click()  # articles
        self.driver.find_element_by_xpath('//*[@id="articleList"]/div[1]/div/ul/li[1]/button/span[2]').click()  # new
        message = self.driver.find_element_by_xpath('//*[@id="articleList"]/div[1]/div/ul/li[1]/ul/li[2]/a')  # message
        ActionChains(self.driver).move_to_element(message).perform()
        message.click()
        self.driver.find_element_by_id('title').send_keys(key)
        self.driver.find_element_by_id('description').send_keys(key)
        self.driver.find_element_by_xpath('//*[@id="articleEdit"]/div/ul/li[1]/button/span[2]').click()#save
        self.driver.find_element_by_xpath('//*[@id="articleEdit"]/div/ul/li[2]/button').click()#publish
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[1]/a/span').click()  # articles
        text=self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/a')
        word=[c.text for c in text]
        self.assertIn(key,word)
    # def test_c_edit_message(self):
    #     self.driver.find_element_by_xpath('//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[7]/a').click()
    #     self.driver.find_element_by_id('title').clear()
    #     self.driver.find_element_by_id('title').send_keys(key)
    #     self.driver.find_element_by_xpath('//*[@id="articleEdit"]/div/ul/li[1]/button/span[2]').click()  # save
    #
    #     self.driver.find_element_by_xpath(
    #         '/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[1]/a/span').click()  # articles
    #     text = self.driver.find_element_by_xpath(
    #         '//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr[2]/td[3]/a')
    #     word = [c.text for c in text]
    #     self.assertIn(key, word)

    def test_d_create_externalLink(self):
        self.driver.find_element_by_xpath('//*[@id="articleList"]/div[1]/div/ul/li[1]/button/span[2]').click()  # new
        external = self.driver.find_element_by_xpath('//*[@id="articleList"]/div[1]/div/ul/li[1]/ul/li[3]/a')  #external
        ActionChains(self.driver).move_to_element(external).perform()
        external.click()
        self.driver.find_element_by_id('title').send_keys(key)
        self.driver.find_element_by_id('description').send_keys('new link')
        self.driver.find_element_by_xpath('//*[@id="articleEdit"]/div/ul/li[1]/button/span[2]').click()  # save
        self.driver.find_element_by_xpath('//*[@id="articleEdit"]/div/ul/li[2]/button').click()  # publish
        self.driver.find_element_by_xpath(
            '/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[1]/a/span').click()  # articles
        text=self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/a')

        type=self.driver.find_elements_by_xpath('//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[5]')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()



