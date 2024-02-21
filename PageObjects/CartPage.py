from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException

class Cart_Page:
    
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.proceed_to_buy_button_name = 'proceedToRetailCheckout'
        self.cart_items_link_xpath = "//a[@class='a-link-normal sc-product-link']/child::img"
        self.replacement_widget_xpath = "(//span[contains(text(),'Replacement')])[1]"
        self.selcted_qty_item_1_select_tag_xpath = "(//span[@tabindex='-1' and @data-a-class='quantity'])[1]"
        self.selcted_qty_item_2_select_tag_xpath = "(//span[@tabindex='-1' and @data-a-class='quantity'])[2]"

    def verify_quantity(self):
        # 1. Verify if the item u selected is applicable for Return/Replacement
        # If applicable Select the quantity to 2, it not select the quantity to 1
        cart_items = self.driver.find_elements(By.XPATH,self.cart_items_link_xpath)
        for item in cart_items:
            item.click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        if self.driver.find_element(By.XPATH,self.replacement_widget_xpath).is_displayed():
            self.wait.until(ec.presence_of_element_located((By.XPATH,self.selcted_qty_item_1_select_tag_xpath)))
            qty = self.driver.find_element(By.XPATH,self.selcted_qty_item_1_select_tag_xpath)
            if qty == '2':
                assert True
        else:
            print('Quantity mismatch')
    
        self.driver.switch_to.window(self.driver.window_handles[2])
        if self.driver.find_element(By.XPATH,self.replacement_widget_xpath).is_displayed():
            self.wait.until(ec.presence_of_element_located((By.XPATH,self.selcted_qty_item_2_select_tag_xpath)))
            qty = self.driver.find_element(By.XPATH,self.selcted_qty_item_2_select_tag_xpath)
            if qty == '2':
                assert True
        else:
            print('Quantity mismatch')

        self.driver.switch_to.window(self.driver.window_handles[0])

        
    def Verify_Items_added(self):
        try:
            if self.driver.find_element(By.ID,'deselect-all').is_displayed():
                assert True
        except NoSuchElementException:
            'no item found in cart'

    def click_on_proceed_to_buy_button(self):
        self.driver.find_element(By.NAME, self.proceed_to_buy_button_name).click()
