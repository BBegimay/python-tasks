from Module28.pages_labirint.config import base_url


class StartLab:
    def __init__(self, driver):
        self.driver = driver

    def visit(self):
        self.driver.get(base_url)
        self.driver.maximize_window()

    def title(self):
        return self.driver.find_element_by_css_selector('.b-header-b-logo-e-logo')

    def get_labirint_find_books(self):
        return self.driver.find_element_by_xpath('//*[ @ id = "search-field"]')

    def get_bar_books(self):
        return self.driver.find_element_by_css_selector(".b-header-b-menu-e-link a[href='/books/']")

    def get_main_2021(self):
        return self.driver.find_element_by_css_selector(".b-header-b-menu-e-link a[href='/best/']")

    def get_school(self):
        return self.driver.find_element_by_css_selector(".b-header-b-menu-e-link a[href='/school/']")

    def get_games(self):
        return self.driver.find_element_by_css_selector(".b-header-b-menu-e-link a[href='/games/']")

    def get_office(self):
        return self.driver.find_element_by_css_selector(".b-header-b-menu-e-link a[href='/office/']")

    def get_house_hold(self):
        return self.driver.find_element_by_xpath('//*[@id="header-more"]/div/ul/li[8]/a')

    def get_multimedia(self):
        return self.driver.find_element_by_xpath('//a[@title="Аудиокниги, музыка, видеофильмы, компьютерные программы, игры и др."]')

    def get_souvenir(self):
        return self.driver.find_element_by_xpath('//a[@title="Сувениры, альбомы для фотографий, фоторамки, календари."]')

    def get_journals(self):
        return self.driver.find_element_by_xpath('//a[@title="Литературные журналы: художественные и публицистические, поэтические."]')

    def get_club(self):
        return self.driver.find_element_by_css_selector(
            ".b-header-b-menu-e-list-item .b-header-b-menu-e-text a[href='/club/']")

    def get_top_read(self):
        return self.driver.find_element_by_css_selector(".h2.mt20.relative.main-block-carousel-title-outer a[href='/top/toread/']")

    def get_top_read_book(self):
        return self.driver.find_element_by_xpath('//*[@id="newslist"]/div/div[2]/div[3]/div/div[1]')

    def get_top_best_buy(self):
        return self.driver.find_element_by_css_selector(".autodiscounts.autodiscounts_main a[href='/best/sale/']")

    def get_insta_photo(self):
        return self.driver.find_element_by_css_selector('div.b-insta-row.b-insta-row-m-middle .b-insta-col')

    def get_inst_child_bootom(self):
        return self.driver.find_element_by_css_selector('span.js-insta-switch.tacenter.b-switcher.b-switcher-m-right.b-switcher-m-blue')

    def get_inst_child(self):
        return self.driver.find_element_by_css_selector('.b-insta-row.b-insta-row-m-middle .b-insta-col.b-insta-col-m-middle')

    def get_footer_in_the_pocket(self):
        return self.driver.find_elements_by_css_selector('.b-rfooter-e-logo-wrapper .b-rfooter-e-logo.b-rfooter-e-logo-appstore.analytics-click-js')

    def get_social_networks(self):
        return self.driver.find_elements_by_xpath(
            '//div[contains(text(), "Мы в соцсетях")]//following-sibling::div/ul/li')

    def get_catalog(self):
        return self.driver.find_elements_by_xpath('//div[contains(text(), "Каталог")]//following-sibling::div/ul/li')

    def get_footer_important(self):
        return self.driver.find_elements_by_xpath('//div[contains(text(), "Важно")]//following-sibling::div/ul/li')

    def get_footer_interesting(self):
        return self.driver.find_elements_by_xpath('//div[contains(text(), "Интересно")]//following-sibling::div/ul/li')

    def get_footer_labirint_to_all(self):
        return self.driver.find_elements_by_xpath('//div[contains(text(), "Лабиринт - всем")]//following-sibling::div/ul/li')

    def get_footer_my_labirint(self):
        return self.driver.find_elements_by_xpath(
            '//div[contains(text(), "Мой Лабиринт")]//following-sibling::div/ul/li')

    def get_footer_help(self):
        return self.driver.find_elements_by_xpath('//div[contains(text(), "Помощь")]//following-sibling::div/ul/li')

    def get_what_read_red(self):
        return self.driver.find_elements_by_xpath('//div[@ data-title = "Что почитать: выбор редакции"]/div')

    def get_books_best(self):
        return self.driver.find_elements_by_xpath('//div[@ data-title = "Читатели выбирают сегодня"]/div[2]/div')

    def get_books_current(self):
        return self.driver.find_elements_by_xpath(
            '//div[@ data-title = "Лабиринт. Сейчас — книжные события октября"]/div[1]/div')

    def get_books_for_kids(self):
        return self.driver.find_elements_by_xpath(
            '//div[@ data-title = "Детский навигатор — что читать детям и с детьми"]/div[1]/div')

    def get_books_best_carousel(self):
        return self.driver.find_element_by_css_selector(
            '.carousel-navigation.carousel-navigation-today .best-carousel-arrow-right.carousel-arrow')

    def get_books_novelty(self):
        return self.driver.find_elements_by_xpath('//div[@ data-title = "Книги: новинки 2021"]/div')

    def get_books_news(self):
        return self.driver.find_element_by_xpath('//h3[contains(text(), "Что нового")]//following-sibling::div')

    def get_books_reviews(self):
        return self.driver.find_elements_by_xpath('//div[@ data-title = "Книжные обзоры и рецензии"]/div')

    def get_labirint_text_footer(self):
        return self.driver.find_element_by_xpath('//h2[contains(text(), "Интернет-магазин книг в деталях")]//following-sibling::p').text

    def get_labirint_find_reserch_books_positive(self):
        return self.driver.find_element_by_xpath('//*[@id="searchform"]/div[1]/button')

    def get_modal_window(self):
        return self.driver.find_element_by_xpath('//span[contains(text(), "Еще")]')
