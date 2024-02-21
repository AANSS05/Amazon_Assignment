from selenium.webdriver.common.by import By


class Home_Page:
    def __init__(self,driver):
        self.driver = driver
        self.todays_deal_button_xpath = """//a[contains(text(),"Today's Deals")]"""
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

    def click_on_todays_deal(self):
        self.driver.find_element(By.XPATH,self.todays_deal_button_xpath).click()

    def click_on_cart(self):
        self.driver.find_element(By.ID,self.cart_link_id).click()
    
    def click_on_your_account_and_add_HM_address(self):
        self.driver.find_element(By.ID,self.account_link_id ).click()
        self.driver.find_element(By.XPATH,self.edit_address_widget_xpath).click()
        self.driver.find_element(By.XPATH,self.add_address_widget_xpath).click()
        self.driver.find_element(By.ID,self.full_name_textfield_id).send_keys('HM_Tester')
        self.driver.find_element(By.ID,self.mobile_number_textfield_id).send_keys('8147237538')
        self.driver.find_element(By.ID,self.pincode_textfield_id).send_keys('560068')
        self.driver.find_element(By.ID,self.address_line1_textfield_id).send_keys(' #53/1,2 3,4, Hosur Rd')
        self.driver.find_element(By.ID,self.address_line2_textfield_id).send_keys('Madivala')
        self.driver.find_element(By.ID,self.landmark_textfield_id).send_keys('Next to madivala police station')
        self.driver.find_element(By.ID,self.default_address_checkbox_id).click()
        self.driver.find_element(By.XPATH,self.add_address_button_xpath).click()
    
