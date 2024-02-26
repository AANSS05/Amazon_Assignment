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

    def test_scenario_02(self):
        obj_HomePage = Home_Page(self.driver)
        obj_HomePage.click_on_todays_deal()

        obj_DealPage = Deals_Page(self.driver)
        obj_DealPage.sort_discount_filter_by_high_to_low()
        obj_DealPage.click_on_average_rating_4_and_up()
        obj_DealPage.click_on_prime_deals_checkbox_and_verify_is_it_selected()
        obj_DealPage.click_on_deal_of_the_day_deal_type()
        obj_DealPage.capturing_the_cards_only_for_deal_of_the_day()

    def test_scenario_03(self):
            obj_ProductPage = Product_Page(self.driver)
            obj_HomePage = Home_Page(self.driver)
            obj_DealPage = Deals_Page(self.driver)
            obj_ProductSelection = ProductSelection_Page(self.driver)

            obj_HomePage.click_on_todays_deal()

            obj_DealPage.click_on_mobile_and_accessories()
            obj_DealPage.sort_discount_filter_by_high_to_low()
            obj_DealPage.click_on_average_rating_4_and_up()
            obj_DealPage.click_on_prime_deals_checkbox_and_verify_is_it_selected()
            obj_DealPage.click_on_deal_of_the_day_deal_type()
            obj_DealPage.click_on_card_with_highest_discount_percentage()
            obj_ProductSelection.sorting_products_based_on_avg_customer_review()
            obj_ProductSelection.clicking_on_product_with_highest_review_count()

            obj_ProductPage.print_product_details()
            obj_ProductPage.add_product_to_cart()

    def test_scenario_04(self):
            obj_ProductSelection = ProductSelection_Page(self.driver)
            obj_ProductPage = Product_Page(self.driver)
            obj_AddToCartPage = AddToCart_Page(self.driver)
            obj_AddToCartPage.back_to_product_page()
            obj_ProductPage.back_to_productSelection_page()
            obj_ProductSelection.sort_items_lowest_price()
            obj_ProductPage.print_product_details()
            obj_ProductPage.check_eligibleFor_free_delivery_option()
            obj_ProductPage.add_to_cart()

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
