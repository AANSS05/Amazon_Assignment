import pytest
from PageObjects.HomePage import Home_Page
from PageObjects.DealsPage import Deals_Page
from PageObjects.LoginPage import Login_Page
from PageObjects.ProductPage import Product_Page
from PageObjects.ProductSelection import ProductSelection_Page
from PageObjects.AddToCartPage import AddToCart_Page
from PageObjects.CheckoutPage import Checkout_page
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("setUp")
class TestAllScenarios:
    
    def test_scenario_05(self):
        obj_HomePage = Home_Page(self.driver)
        obj_AddToCartPage = AddToCart_Page(self.driver)
        obj_CheckoutPage = Checkout_page(self.driver)
        obj_HomePage.click_on_your_account_and_add_HM_address()
        obj_HomePage.click_on_cart()
        obj_AddToCartPage.verify_quantity()
        obj_AddToCartPage.Verify_Items_added()
        obj_AddToCartPage.click_on_proceed_to_buy_button()
        obj_CheckoutPage.click_on_use_this_address()
        obj_CheckoutPage.click_on_COD()
        obj_CheckoutPage.click_on_use_this_payment_method_button()
        obj_CheckoutPage.click_on_free_delivery_option()
        obj_CheckoutPage.get_order_summary_and_order_total()
