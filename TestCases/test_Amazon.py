import pytest
from PageObjects.HomePage import Home_Page
from PageObjects.DealsPage import Deals_Page
from PageObjects.ProductPage import Product_Page
from PageObjects.ProductSelection import ProductSelection_Page
from PageObjects.AddToCartPage import AddToCart_Page


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
