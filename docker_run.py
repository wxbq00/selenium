



from selenium import webdriver
chrome_capabilities ={
    "browserName": "chrome",
    "version": "",
    "platform": "ANY",
    "javascriptEnabled": True,
    # "marionette": True,
}
browser = webdriver.Remote("http://127.0.0.1:5555/wd/hub", desired_capabilities=chrome_capabilities)
browser.get("http://www.163.com")
print(browser.title)
browser.get_screenshot_as_file(r"D:/sample/chrome.png")
browser.quit()