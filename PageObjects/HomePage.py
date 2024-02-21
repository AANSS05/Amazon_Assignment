from selenium.webdriver.common.by import By
import time

class Home_Page:
    def __init__(self,driver):
        self.driver = driver
        self.todays_deal_button_xpath = """//a[contains(text(),"Today's Deals")]"""
        self.header_xpath = "//div[@id='nav-main']"
        self.footer_xpath = "//div[@id='navFooter']"
        self.card_list_header_xpath = "//div[@class = 'a-cardui-header']"
        self.card_list_footer_xpath = "//div[@class='a-cardui-footer']/a"
        self.cart_link_id = 'nav-cart'
        self.account_link_id = 'nav-link-accountList'
        self.edit_address_widget_xpath = "//span[text()='Edit addresses for orders and gifts']"
        self.add_address_widget_xpath = "//h2[text()='Add address']"
        self.full_name_textfield_id = 'address-ui-widgets-enterAddressFullName'
        self.mobile_number_textfield_id = 'address-ui-widgets-enterAddressPhoneNumber'
        self.pincode_textfield_id = 'address-ui-widgets-enterAddressPostalCode'
        self.address_line1_textfield_id = 'address-ui-widgets-enterAddressLine1'
        self.address_line2_textfield_id = 'address-ui-widgets-enterAddressLine2'
        self.landmark_textfield_id = 'address-ui-widgets-landmark'
        self.default_address_checkbox_id = 'address-ui-widgets-use-as-my-default'
        self.add_address_button_xpath = "//input[@aria-labelledby='address-ui-widgets-form-submit-button-announce']"
        self.full_name = 'HM_Tester'
        self.mobile_number = '8147237538'
        self.pincode = '560068'
        self.address_line1 = '#53/1,2 3,4, Hosur Rd'
        self.address_line2 = 'Madivala'
        self.landmark = 'Next to madivala police station'

    def Header_Footer(self):
        print(self.driver.find_element(By.XPATH, self.header_xpath).text)
        time.sleep(2)
        self.driver.save_screenshot("scenario1_Header.png")
        self.driver.execute_script("window.scrollBy(0,6000)", "")
        print(self.driver.find_element(By.XPATH, self.footer_xpath).text)
        time.sleep(2)
        self.driver.save_screenshot("scenario1_Footer.png")


    def card_details(self):
        card_header_keys = self.driver.find_elements(By.XPATH, self.card_list_header_xpath)
        card_footer_values = self.driver.find_elements(By.XPATH, self.card_list_footer_xpath)
        card_header_footer = {k.text: v.get_attribute('href') for k, v in zip(card_header_keys, card_footer_values)}
        print(card_header_footer)
        self.driver.save_screenshot("scenario1_Card_header_Footer.png")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,-6000)", "")



    def click_on_todays_deal(self):
        self.driver.find_element(By.XPATH,self.todays_deal_button_xpath).click()

    def click_on_cart(self):
        self.driver.find_element(By.ID,self.cart_link_id).click()
    
    def click_on_your_account_and_add_HM_address(self):
        self.driver.find_element(By.ID,self.account_link_id ).click()
        self.driver.find_element(By.XPATH,self.edit_address_widget_xpath).click()
        self.driver.find_element(By.XPATH,self.add_address_widget_xpath).click()
        self.driver.find_element(By.ID,self.full_name_textfield_id).send_keys(self.full_name)
        self.driver.find_element(By.ID,self.mobile_number_textfield_id).send_keys(self.mobile_number)
        self.driver.find_element(By.ID,self.pincode_textfield_id).send_keys(self.pincode)
        self.driver.find_element(By.ID,self.address_line1_textfield_id).send_keys(self.address_line1)
        self.driver.find_element(By.ID,self.address_line2_textfield_id).send_keys(self.address_line2)
        self.driver.find_element(By.ID,self.landmark_textfield_id).send_keys(self.landmark)
        self.driver.find_element(By.ID,self.default_address_checkbox_id).click()
        self.driver.find_element(By.XPATH,self.add_address_button_xpath).click()
    
