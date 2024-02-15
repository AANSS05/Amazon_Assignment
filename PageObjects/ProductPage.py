from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import Select


class Product_Page:

    def __init__(self,driver):
        self.driver = driver

        self.product_title_xpath = "//span[contains(@id,'productTitle')]"
        self.star_rating_of_the_product_xpath = "//div[contains(@id,'averageCustomerReviews_feature_div')]//div//span//span[contains(@id,'acrPopover')]"
        self.number_of_reviews_of_the_product_xpath = "//div[contains(@id,'averageCustomerReviews_feature_div')]//div//span/following-sibling::span[contains(@class,'a-declarative')]//a//span"
        self.price_of_the_product_xpath = "//span[contains(@class,'priceToPay')]//span//span/following-sibling::span"
        self.replacement_policy_xpath = "//li[@class='a-carousel-card tw-scroll-carousel-element']/div[@id='RETURNS_POLICY']//div/following-sibling::div//span"
        self.add_product_to_cart_xpath = "//span[contains(@id,'submit.add-to-cart')][contains(@class,'a-spacing-small')]"
        self.selecting_quantity_one_xpath = "//select[@name='quantity']//option[@value='1']"
        self.selecting_quantity_two_xpath = "//select[@name='quantity']//option[@value='2']"
        self.dropdown_button_for_quantity = "//select[contains(@id,'quantity')]"
        self.free_delivery_xpath = "//div[@id='mir-layout-DELIVERY_BLOCK']//a[contains(text(),'FREE delivery')]"
        self.click_dropdown_xpath = "//select[@name='quantity']"
        self.select_quantity_xpath = "//select[@name='quantity']/option[@value='2']"
        self.actual_text = "FREE delivery"

    def print_product_details(self):
        product_title = self.driver.find_element(By.XPATH, self.product_title_xpath).text
        star_rating_of_the_product = self.driver.find_element(By.XPATH, self.star_rating_of_the_product_xpath).text
        number_of_reviews_of_the_product = self.driver.find_element(By.XPATH, self.number_of_reviews_of_the_product_xpath).text
        price_of_the_product = self.driver.find_element(By.XPATH, self.price_of_the_product_xpath).text
        print("Title of the product is: " + product_title)
        print("Star rating of the product is: " + star_rating_of_the_product)
        print("Total number of reviews of the product is: " + number_of_reviews_of_the_product)
        print("Price of the product is: " + price_of_the_product)

    def add_product_to_cart(self):

        return_replacement_info = (self.driver.find_element(By.XPATH, self.replacement_policy_xpath)).text
        dropdown_button = self.driver.find_element(By.XPATH,self.dropdown_button_for_quantity)
        quantity = Select(dropdown_button)
        if "Return" or "Replacement" in return_replacement_info:
            quantity.select_by_value("2")
        else:
            quantity.select_by_value("1")


        add_to_card_button = self.driver.find_element(By.XPATH, self.add_product_to_cart_xpath)
        add_to_card_button.click()
        time.sleep(5)

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


