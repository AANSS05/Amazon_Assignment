from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions 
from selenium.common.exceptions import NoSuchElementException

class Checkout_page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,15)
        self.use_this_address_button_xpath = "//input[@data-testid='Address_selectShipToThisAddress']"
        self.full_name_text_box_id = 'address-ui-widgets-enterAddressFullName'
        self.mobile_number_text_box_id = 'address-ui-widgets-enterAddressPhoneNumber'
        self.pincode_text_box_id = 'address-ui-widgets-enterAddressPostalCode'
        self.address_line1_text_box_id = 'address-ui-widgets-enterAddressLine1'
        self.address_line2_text_box_id = 'address-ui-widgets-enterAddressLine2'
        self.landmark_text_box_id = 'address-ui-widgets-landmark'
        self.use_this_address_newaddress_button_xpath = "//input[@aria-labelledby='address-ui-widgets-form-submit-button-announce']"
        self.cod_radio_button_xpath = "//input[contains(@value,'Cash&isExpired=false&paymentMethod=COD&tfxEligible=false')]"
        self.use_this_payment_method_button_xpath = "//span[text()='Use this payment method']/ancestor::span/child::input[@class='a-button-input a-button-text']"
        self.free_delivery_radio_button_xpath = "//span[text()='FREE ']"
        self.change_address_link_id = 'addressChangeLinkId'
        self.add_a_new_address_link_id = 'add-new-address-popover-link'
        self.order_summary_widget_id = 'spc-order-summary'

    def click_on_use_this_address(self):
        self.driver.find_element(By.XPATH,self.use_this_address_button_xpath).is_displayed()
        self.driver.find_element(By.XPATH,self.use_this_address_button_xpath).click()
        
    def click_on_COD(self):
        self.driver.find_element(By.XPATH,self.cod_radio_button_xpath).click()

    def click_on_use_this_payment_method_button(self):
        self.driver.find_element(By.XPATH,self.use_this_payment_method_button_xpath).click()

    def click_on_free_delivery_option(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.free_delivery_radio_button_xpath))
        try:
            if self.driver.find_element(By.XPATH,self.free_delivery_radio_button_xpath).is_displayed():
                self.driver.find_element(By.XPATH,self.free_delivery_radio_button_xpath).click()
            else:
                print('No free delivery option is displayed')
        except NoSuchElementException:
            print('Element not found on the page.')

    def click_on_change_on_delivery_address(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.change_address_link_id))
        self.driver.find_element(By.ID,self.change_address_link_id).click()

    def get_order_summary_and_order_total(self):
        order_summary_element = self.driver.find_element(By.ID,self.order_summary_widget_id)
        print(order_summary_element.text)