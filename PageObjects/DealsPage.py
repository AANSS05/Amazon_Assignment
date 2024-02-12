import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Deals_Page:

    def __init__(self,driver):
        self.driver = driver
        self.average_rating_above_4_css = "span[aria-label$='4 and up']"
        self.prime_deals_checkbox_xpath = "//li[contains(@class,'CheckboxFilter-module')]//i[contains(@aria-label,'Prime')]"
        self.sort_by_dropdown_name = "sort"
        self.discount_option = 'Sort by: Discount - High to Low'
        self.deal_of_the_day_link_xpath = '//*[@aria-label="Deal type filter"]//*[contains(text(),"Deal of the day")]'
        self.all_deal_of_the_day_cards_xpath = '//*[contains(@class,"DealCard-module__contentWithPadding")]//a//div'
        self.all_cards_value_xpath = "//*[contains(@class,'DealCard-module__contentWithPadding')]//a//div"
        self.accessories_text = 'Accessories'
        self.amazon_text = 'Amazon'
        self.clothing_text = 'Clothing'


    def sort_discount_filter_by_high_to_low(self):
        discount_filter_dropdown = self.driver.find_element(By.NAME,self.sort_by_dropdown_name)
        self.driver.execute_script("arguments[0].scrollIntoView();",discount_filter_dropdown )
        discount_options = Select(discount_filter_dropdown)
        discount_options.select_by_visible_text(self.discount_option)
        time.sleep(5)
        self.driver.save_screenshot("Discount_Filter.png")

    def click_on_average_rating_4_and_up(self):
        average_rating_4_and_up_link = self.driver.find_element(By.CSS_SELECTOR,self.average_rating_above_4_css)
        self.driver.execute_script("arguments[0].scrollIntoView();",average_rating_4_and_up_link)
        average_rating_4_and_up_link.click()
        time.sleep(5)
        self.driver.save_screenshot("Rating.png")


    def click_on_prime_deals_checkbox_and_verify_is_it_selected(self):
        self.driver.find_element(By.XPATH,self.prime_deals_checkbox_xpath).click()
        time.sleep(5)
        self.driver.save_screenshot("Checkbox.png")
        # print('checkbox :',self.driver.find_element(By.XPATH,self.prime_deals_checkbox_xpath).is_selected())

    def click_on_deal_of_the_day_deal_type(self):
        self.driver.find_element(By.XPATH,self.deal_of_the_day_link_xpath).click()
        time.sleep(5)
        self.driver.save_screenshot("Deal_of_the_day.png")

    def capturing_the_cards_only_for_deal_of_the_day(self):
        # either Accessories or AMAZON  not both CLOTHING should not be present in the name as well
        all_cards = self.driver.find_elements(By.XPATH,self.all_cards_value_xpath)
        all_cards_value_list = [value.text for value in all_cards]
        all_cards_filtered_values = []
        for value in all_cards_value_list:
            if self.clothing_text not in value:
                if self.accessories_text in value and self.amazon_text not in value:
                    all_cards_filtered_values.append(value)
                elif self.amazon_text in value and self.accessories_text not in value:
                    all_cards_filtered_values.append(value)

        for value in all_cards_filtered_values:
            print(value)
