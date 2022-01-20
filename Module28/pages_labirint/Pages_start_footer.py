from selenium.webdriver.common.keys import Keys


class StartLabFooter:
    def __init__(self, driver):
        self.driver = driver
        self.list_social_networks = []
        self.list = []

    def apply_cookie(self):
        return self.driver.find_element_by_css_selector('.cookie-policy__button.js-cookie-policy-agree')

    def get_scroll_footer(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.END)

    def get_swith_to_windows(self):
        self.driver.switch_to_window(self.driver.window_handles[1])

    def get_footer_app_store(self):
        return self.driver.find_element_by_css_selector(
            ".b-rfooter-e-logo.b-rfooter-e-logo-appstore.analytics-click-js")

    def get_footer_google_play(self):
        return self.driver.find_element_by_css_selector(
            ".b-rfooter-e-logo.b-rfooter-e-logo-googleplay.analytics-click-js")

    def get_footer_app_galery(self):
        return self.driver.find_element_by_css_selector(
            ".b-rfooter-e-logo.b-rfooter-e-logo-appgallery.analytics-click-js")

    def get_social_networks_list(self):
        for i in range(len(self.driver.find_elements_by_xpath(
                '//div[contains(text(), "Мы в соцсетях")]//following-sibling::div/ul/li'))):
            self.list_social_networks.append(self.driver.find_elements_by_xpath(
                '//div[contains(text(), "Мы в соцсетях")]//following-sibling::div/ul/li/a')[i])
        return self.list_social_networks

    def get_footer_catalog_books(self):
        for i in range(len(self.driver.find_elements_by_xpath(
                '//div[contains(text(), "Каталог")]//following-sibling::div/ul/li'))):
            self.list.append(self.driver.find_elements_by_xpath(
                '//div[contains(text(), "Каталог")]//following-sibling::div/ul/li/a')[i])
        return self.list

    def get_footer_important(self):
        for i in range(len(self.driver.find_elements_by_xpath(
                '//div[contains(text(), "Важно")]//following-sibling::div/ul/li'))):
            self.list.append(
                self.driver.find_elements_by_xpath('//div[contains(text(), "Важно")]//following-sibling::div/ul/li/a')[
                    i])
        return self.list

    def get_footer_fav(self):
        for i in range(len(self.driver.find_elements_by_xpath(
                '//div[contains(text(), "Интересно")]//following-sibling::div/ul/li'))):
            self.list.append(self.driver.find_elements_by_xpath(
                '//div[contains(text(), "Интересно")]//following-sibling::div/ul/li/a')[i])
        return self.list
