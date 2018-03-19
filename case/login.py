import time
from selenium import webdriver
from case.config.config import Config
import csv,xlrd

key='2018-2-02'


class Login():

    def user_login(self,driver):
        url = Config().get('URL')
        driver.get(url)
        driver.implicitly_wait(30)
        driver.maximize_window()
        username = driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/ui-view/div/form/fieldset/div[1]/input')
        username.clear()
        username.send_keys('mn-admin@mobilenowgroup.com')
        userpasswd = driver.find_element_by_xpath("//input[@name='password']")
        userpasswd.clear()
        userpasswd.send_keys('MobileNow2017!')
        loginbt = driver.find_element_by_xpath( '/html/body/div/div/div/div/div/div[2]/ui-view/div/form/fieldset/button')
        loginbt.click()



login=Login()

