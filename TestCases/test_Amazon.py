import pytest
from PageObjects.HomePage import Home_Page
from PageObjects.DealsPage import Deals_Page
from PageObjects.ProductPage import Product_Page
from PageObjects.ProductSelection import ProductSelection_Page


@pytest.mark.usefixtures("setUp")
class TestAllScenarios:

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