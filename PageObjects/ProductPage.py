from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select


class Product_Page:

    def __init__(self,driver):
        self.driver = driver

       
        self.dropdown_button_for_quantity = "//select[contains(@id,'quantity')]"
        self.free_delivery_xpath = "//div[@id='mir-layout-DELIVERY_BLOCK']//a[contains(text(),'FREE delivery')]"
        self.click_dropdown_xpath = "//select[@name='quantity']"
        self.select_quantity_xpath = "//select[@name='quantity']/option[@value='2']"
        self.actual_text = "FREE delivery"





    def back_to_productSelection_page(self):
        self.driver.back()

    def check_eligibleFor_free_delivery_option(self):
        text = (self.driver.find_element(By.XPATH, self.free_delivery_xpath)).text
        if text == self.actual_text:
            self.click_dropdown_and_select_quantity()

    def click_dropdown_and_select_quantity(self):
        dropdown = self.driver.find_element(By.XPATH, self.click_dropdown_xpath)
        time.sleep(2)
        discount_options = Select(dropdown)
        discount_options.select_by_value("2")
        time.sleep(2)

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, self.add_product_to_cart_xpath).click()
        time.sleep(4)

