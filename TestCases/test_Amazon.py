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
    def test_Scenario_01(self):
        obj_LoginPage = Login_Page(self.driver)
        obj_LoginPage.click_on_signin_button_on_homepage()
        obj_LoginPage.enter_email_address_text()
        obj_LoginPage.click_on_continue_button()
        obj_LoginPage.enter_password_text()
        obj_LoginPage.click_on_signin_button()

        obj_HomePage = Home_Page(self.driver)
        obj_HomePage.Header_Footer()
        obj_HomePage.card_details()





