from PageObjects.LoginPage import Login_Page
from PageObjects.HomePage import Home_Page
import pytest


@pytest.mark.usefixtures("setUp")
class TestAllScenarios:
    def test_Scenario1(self):
        obj_LoginPage = Login_Page(self.driver)
        obj_LoginPage.click_on_signin_button_on_homepage()
        obj_LoginPage.enter_email_address_text()
        obj_LoginPage.click_on_continue_button()
        obj_LoginPage.enter_password_text()
        obj_LoginPage.click_on_signin_button()
        obj_HomePage = Home_Page(self.driver)
        obj_HomePage.Header_Footer()
        obj_HomePage.card_details()

    def test_card_links(self):
        obj_HomePage = Home_Page(self.driver)
        obj_HomePage.card_details()
