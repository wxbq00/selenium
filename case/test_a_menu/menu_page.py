from selenium.webdriver.common.by import By
from case.two_time_package import Yoyo
from case.login import Login,key
class Menu(Yoyo):
    new_menu_loc=('xpath','//*[@id="menu"]/div/div/div/div[1]/ol/li[1]/div/a[2]')
    article_checkbox_loc=('xpath','//input[@value="article"]')
    menu_name_loc=('id','name')
    new_article_loc=('xpath','//*[@id="menu"]/div/div/div/div[2]/form/div[2]/div[1]/div[2]/article-select-component/span/a')
    article_choose_loc=('xpath','//*[@id="menu"]/div/div/div/div[2]/form/div[2]/div[1]/div[2]/article-select-component/span/ul/li[1]/a')
    slug_loc=('id','slug')
    title_loc=('id','title')
    tag_loc=('xpath','//input[@type="search"]')
    save_loc=('xpath','//*[@id="articleEdit"]/div/div/div[1]/div/div[2]/form/button')
    article_loc=('xpath','//*[@id="menu"]/div/div/div/div[2]/form/div[2]/div[1]/div[2]/article-select-component/select/option')#下拉列表中的文章数
    save_draft_loc=('xpath','//*[@id="menu"]/action-button-list/ul/li[1]/button/span[2]')
    publish_loc = ('xpath', '//*[@id="menu"]/action-button-list/ul/li[2]/button/span[2]')
    contents_loc=('xpath','/html/body/div/div/div/sidebar/div[1]/ul/li[3]/a/span[1]')
    articles_bar_loc=('xpath','/html/body/div/div/div/sidebar/div[1]/ul/li[3]/ul/li[1]/a/span')
    last_button_loc=('xpath','//*[@id="articleList"]/div[3]/div[2]/div/div[2]/ul/li[6]/a')



    def click_new_menu(self):
        self.click(self.new_menu_loc)
    def click_article_checkbox(self):
        self.click(self.article_checkbox_loc)
    def input_menu_name(self):
        self.send_keys(self.menu_name_loc,key)
    def click_new_article(self):
        self.click(self.new_article_loc)
    def move_click_article(self):
        self.move_to_element(self.article_choose_loc)
        self.click(self.article_choose_loc)
    def input_slug(self):
        self.send_keys(self.slug_loc,'www.baidu.com')
    def input_title(self):
        self.send_keys(self.title_loc,key)
    def click_input_tag(self):
        self.click(self.tag_loc)
        self.send_keys(self.tag_loc,key)
    def click_save(self):
        self.click(self.save_loc)
    def click_save_draft(self):
        self.click(self.save_draft_loc)
    def click_publish(self):
        self.click(self.publish_loc)
    def click_contents(self):
        self.click(self.contents_loc)
    def click_article_bar(self):
        self.click(self.articles_bar_loc)
    def click_last(self):
        self.click(self.last_button_loc)
    def clear_menu_name(self):
        self.clear(self.menu_name_loc)