
#coding=utf-8
import time
from selenium import webdriver
from case.log.log import Log
from case.config.config import DRIVER_PATH
from case.config.screen import Screen
log=Log()

class TestMyLog(object):
    driver = webdriver.Chrome(DRIVER_PATH)
    @Screen(driver)
    def print_log(self):

        log.info("打开浏览器")
        self.driver.maximize_window()
        log.info("最大化浏览器窗口。")
        self.driver.implicitly_wait(8)

        self.driver.get("https://www.basaaidu.com")
        log.info("打开百度首页。")
        time.sleep(1)
        log.info("暂停一秒。")
        self.driver.quit()
        log.info("关闭并退出浏览器。")
loger=TestMyLog()
loger.print_log()