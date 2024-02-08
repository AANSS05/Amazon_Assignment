class Home_Page:
    todays_deal_button_xpath = "//*[contains(text(),'Today's Deals')]"
    average_rating_above_4_css = "span[aria-label$='4 and up']"
    prime_deals_checkbox_xpath = "//span[contains(text(),'Prime eligible')]"
    sort_by_dropdown_name = "sort"
    deal_of_the_day_link_xpath ='//*[@aria-label="Deal type filter"]//*[contains(text(),"Deal of the day")]'
    all_deal_of_the_day_cards_xpath = '//*[contains(@class,"DealCard-module__contentWithPadding")]//a//div'

    def click_on_todays_deal(self):
        pass

    def sort_discount_filter_by_high_to_low(self):
        pass

    def click_on_average_rating_4_and_up(self):
        pass

    def click_on_prime_deals_checkbox(self):
        pass