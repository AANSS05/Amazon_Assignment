import time
from selenium.webdriver.common.by import By

class Home_Page:
    def __init__(self,driver):
        self.driver = driver
        self.todays_deal_button_xpath = "//*[contains(text(),'Today's Deals')]"
        self.todays_deal_button_xpath = """//a[contains(text(),"Today's Deals")]"""
        self.header_xpath = "//div[@id='nav-main']"
        self.footer_xpath = "//div[@id='navFooter']"
        self.card_list_header_xpath = "//div[@class = 'a-cardui-header']"
        self.card_list_footer_xpath = "//div[@class='a-cardui-footer']/a"

    def click_on_todays_deal(self):
        self.driver.find_element(By.XPATH,self.todays_deal_button_xpath).click()

    def Header_Footer(self):
        print(self.driver.find_element(By.XPATH, self.header_xpath).text)
        time.sleep(2)
        self.driver.save_screenshot("scenario1_Header.png")
        self.driver.execute_script("window.scrollBy(0,7000)", "")
        print(self.driver.find_element(By.XPATH, self.footer_xpath).text)
        time.sleep(2)
        self.driver.save_screenshot("scenario1_Footer.png")

    def card_details(self):
        card_header_keys = self.driver.find_elements(By.XPATH, self.card_list_header_xpath)
        card_footer_values = self.driver.find_elements(By.XPATH, self.card_list_footer_xpath)
        card_header_footer = {k.text: v.get_attribute('href') for k, v in zip(card_header_keys, card_footer_values)}
        print(card_header_footer)
        self.driver.save_screenshot("scenario1_Card_header_Footer.png")
