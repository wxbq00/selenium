from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://bj.ganji.com/")
h=driver.current_window_handle#当前窗口
print(h)
driver.find_element_by_link_text("招聘求职").click()
all_h=driver.window_handles#所有的窗口
print(all_h)
for i in all_h:
    if i !=h:#首页
        driver.switch_to.window(i)
        print(driver.title)
#driver.switch_to.window(all_h[1])#方法二
driver.close()
driver.switch_to_window(h)

driver.implicitly_wait()