from selenium.webdriver.common.by import By
from case.two_time_package import Yoyo
from case.login import Login,key

login_url='http://test-wnc1.wcnmobilenowgroup.com/admin/#/login'
class Location(Yoyo):
    locationTitle_loc=('xpath','/html/body/div[1]/div/div/sidebar/div[1]/ul/li[4]/a/span[1]')
    manage_location_loc=('xpath','/html/body/div/div/div/sidebar/div[1]/ul/li[4]/ul/li[6]/a/span')

    manage_new_loc=('xpath','//*[@id="articleList"]/div[1]/div/action-button-list/ul/li/button/span[2]')
    manage_name_loc=('xpath','//input[@type="text"]')
    radius_loc=('xpath','//input[@type="number"]')
    manage_save_loc=('xpath','//*[@id="locationTypeEdit"]/ul/li/button/span[2]')
    userName_loc=('xpath','/html/body/div/div/div/div/div/div[2]/ui-view/div/form/fieldset/div[1]/input')
    psw_loc=('xpath',"//input[@name='password']")
    loginBtn_loc=('xpath', '/html/body/div/div/div/div/div/div[2]/ui-view/div/form/fieldset/button')
    location_loc=('xpath','/html/body/div[1]/div/div/sidebar/div[1]/ul/li[4]/ul/li[1]/a/span')

    new_loc=('xpath','//*[@id="articleList"]/div[1]/div/action-button-list/ul/li[1]/button/span[2]')
    title_loc=('id','title')
    tag_loc=('xpath','//input[@type="search"]')
    imageBtn_loc=('xpath','//*[@id="articleEdit"]/div/div/div[1]/div/div[2]/form/location-edit-store-component/div/div[1]/div[2]/div[2]/div[7]/button[2]')

    img_loc=('xpath','/html/body/div[1]/div/div/div/div[2]/image-select/div/div[2]/div[2]/div[2]/div/div[2]/div/table/tbody/tr/td[1]/img')
    address_loc=('id','address')
    getBtn_loc=('xpath','//*[@id="articleEdit"]/div/div/div[1]/div/div[2]/form/location-edit-store-component/div/div[3]/button/span[2]')
    save_loc=('xpath','//*[@id="articleEdit"]/div/ul/li[1]/button/span[2]')
    publish_loc=('xpath','//*[@id="articleEdit"]/div/ul/li[2]/button/span[2]')
    name_loc=('xpath','//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/a')
    search_loc=('xpath','//*[@id="articleList"]/div[2]/div/div/input')
    location_title_loc=('xpath','//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/tbody/tr/td[3]/a')
    title_header_loc=('xpath','//*[@id="articleList"]/div[3]/div[2]/div/div[2]/div/table/thead/tr/th[3]')
    def input_username(self,username):
        self.send_keys(self.userName_loc,username)

    def input_password(self, password):
        self.send_keys(self.psw_loc, password)

    def click_login(self):
        self.click(self.loginBtn_loc)

    def login(self,username,password):
        self.open(login_url)
        self.input_username(username)
        self.input_password(password)
        self.click_login()
        self.click(self.locationTitle_loc)

    def click_location(self):
        self.click(self.location_loc)
    def click_new(self):
        self.click(self.new_loc)
    def input_title(self):
        self.send_keys(self.title_loc,key)
    def click_tag(self):
        self.click(self.tag_loc)
    def click_imgbtn(self):
        self.click(self.imageBtn_loc)
    def click_img(self):
        img = self.find_elements(self.img_loc)
        img[0].click()
    def input_address(self):
        self.send_keys(self.address_loc,'上海市襄阳南路218号')
    def click_getAddress(self):
        self.click(self.getBtn_loc)
    def click_save(self):
        self.click(self.save_loc)
    def click_publish(self):
        self.click(self.publish_loc)
    def click_manage(self):
        self.click(self.manage_location_loc)
    def click_manage_new(self):
        self.click(self.manage_new_loc)
    def input_name(self):
        self.send_keys(self.manage_name_loc,'lucas')
    def input_radius(self):
        self.send_keys(self.radius_loc,'1000')
    def click_manage_save(self):
        self.click(self.manage_save_loc)
    def input_keyword(self):
        self.send_keys(self.search_loc,key)






