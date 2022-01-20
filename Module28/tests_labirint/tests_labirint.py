import pytest
import sys

from selenium.webdriver import ActionChains

from Module28.pages_labirint.Pages_start_footer import StartLabFooter
from Module28.pages_labirint.config import base_url
from Module28.pages_labirint.pages_start_lab import StartLab

sys.path.append("/Selenium_cookie/pages_labirint")


@pytest.mark.headers_bar
def test_main_page(driver):
    start = StartLab(driver)
    start.visit()
    start.title().click()
    assert driver.current_url == base_url


@pytest.mark.headers_bar
def test_successful_bar_books(driver):
    start = StartLab(driver)
    start.visit()
    start.get_bar_books().click()
    assert driver.current_url == base_url + 'books/'


@pytest.mark.headers_bar
def test_successful_bar_main_2021(driver):
    start = StartLab(driver)
    start.visit()
    start.get_main_2021().click()
    assert driver.current_url == base_url + 'best/'


@pytest.mark.headers_bar
def test_successful_bar_school(driver):
    start = StartLab(driver)
    start.visit()
    start.get_school().click()
    assert driver.current_url == base_url + 'school/'


@pytest.mark.headers_bar
def test_successful_bar_games(driver):
    start = StartLab(driver)
    start.visit()
    start.get_games().click()
    assert driver.current_url == base_url + 'games/'


@pytest.mark.headers_bar
def test_successful_bar_office(driver):
    start = StartLab(driver)
    start.visit()
    start.get_office().click()
    assert driver.current_url == base_url + 'office/'


@pytest.mark.headers_bar
def test_successful_bar_house_hold(driver):
    start = StartLab(driver)
    start.visit()
    action = ActionChains(driver)
    action.move_to_element(start.get_modal_window()).move_to_element(start.get_house_hold()).click(
        start.get_house_hold()).perform()

    assert driver.current_url == base_url + 'household/'


@pytest.mark.headers_ehe
@pytest.mark.headers_bar
def test_successful_bar_multimedia(driver):
    start = StartLab(driver)
    start.visit()
    action = ActionChains(driver)
    action.move_to_element(start.get_modal_window()).move_to_element(start.get_multimedia()).click(
        start.get_multimedia()).perform()

    assert driver.current_url == base_url + 'multimedia/'


@pytest.mark.headers_ehe
@pytest.mark.headers_bar
def test_successful_bar_souvenir(driver):
    start = StartLab(driver)
    start.visit()
    action = ActionChains(driver)
    action.move_to_element(start.get_modal_window()).move_to_element(start.get_souvenir()).click(
        start.get_souvenir()).perform()
    assert driver.current_url == base_url + 'souvenir/'


@pytest.mark.headers_ehe
@pytest.mark.headers_bar
def test_successful_bar_journals(driver):
    start = StartLab(driver)
    start.visit()
    action = ActionChains(driver)
    action.move_to_element(start.get_modal_window()).move_to_element(start.get_journals()).click(
        start.get_journals()).perform()
    assert driver.current_url == base_url + 'journals/'


@pytest.mark.body
def test_successful_top_read(driver):
    start = StartLab(driver)
    start.visit()
    start.get_top_read().click()
    assert driver.current_url == base_url + 'top/toread/'
    assert start.get_top_read_book().is_displayed()


@pytest.mark.body
def test_successful_best_buy(driver):
    start = StartLab(driver)
    start.visit()
    start.get_top_best_buy().click()
    assert driver.current_url == base_url + 'best/sale/'


@pytest.mark.body
def test_successful_insta_photo(driver):
    start = StartLab(driver)
    start.visit()
    assert driver.current_url == base_url
    assert start.get_insta_photo().is_displayed()


@pytest.mark.body
def test_successful_insta_photo_child(driver):
    start = StartLab(driver)
    start.visit()
    start.get_inst_child_bootom().click()
    assert start.get_inst_child().is_displayed()


@pytest.mark.footer
def test_successful_footer_in_pocket(driver):
    start = StartLab(driver)
    start.visit()
    for i in range(len(start.get_footer_in_the_pocket())):
        assert start.get_footer_in_the_pocket()[i].is_displayed()


@pytest.mark.footer
def test_successful_footer_social_networks(driver):
    start = StartLab(driver)
    start.visit()

    for i in range(len(start.get_social_networks())):
        assert start.get_social_networks()[i].is_displayed()


@pytest.mark.footer
def test_successful_footer_katalog(driver):
    start = StartLab(driver)
    start.visit()
    for i in range(len(start.get_catalog())):
        assert start.get_catalog()[i].is_displayed()


@pytest.mark.footer
def test_successful_footer_important(driver):
    start = StartLab(driver)
    start.visit()
    for i in range(len(start.get_footer_important())):
        assert start.get_footer_important()[i].is_displayed()


@pytest.mark.footer
def test_succesful_footer_intresting(driver):
    start = StartLab(driver)
    start.visit()
    for i in range(len(start.get_footer_interesting())):
        assert start.get_footer_interesting()[i].is_displayed()


@pytest.mark.footer
def test_succesful_footer_labirint_to_all(driver):
    start = StartLab(driver)
    start.visit()
    for i in range(len(start.get_footer_labirint_to_all())):
        assert start.get_footer_labirint_to_all()[i].is_displayed()


@pytest.mark.footer
def test_succesful_footer_my_labirint(driver):
    start = StartLab(driver)
    start.visit()
    for i in range(len(start.get_footer_my_labirint())):
        assert start.get_footer_my_labirint()[i].is_displayed()


@pytest.mark.footer
def test_succesful_footer_help(driver):
    start = StartLab(driver)
    start.visit()
    for i in range(len(start.get_footer_help())):
        assert start.get_footer_help()[i].is_displayed()


@pytest.mark.body
def test_succesful_find_books_topread(driver):
    start = StartLab(driver)
    start.visit()
    for i in range(6):
        assert start.get_what_read_red()[i].is_displayed()


@pytest.mark.body
def test_succesful_find_books_best(driver):
    start = StartLab(driver)
    start.visit()
    for i in range(3):
        assert start.get_books_best()[i].is_displayed()


@pytest.mark.body
def test_succesful_find_books_labirint_now(driver):
    start = StartLab(driver)
    start.visit()
    for i in range(4):
        assert start.get_books_current()[i].is_displayed()


@pytest.mark.body
def test_succesful_find_books_labirint_kids_navigator(driver):
    start = StartLab(driver)
    start.visit()
    for i in range(4):
        assert start.get_books_for_kids()[i].is_displayed()


@pytest.mark.body
def test_succesful_find_books_labirint_now_carusel(driver):
    start = StartLab(driver)
    start.visit()
    start.get_books_best_carousel().click()
    for i in range(2, 5):
        assert start.get_books_best()[i].is_displayed()


@pytest.mark.body
def test_succesful_find_books_labirint_novelty(driver):
    start = StartLab(driver)
    start.visit()
    for i in range(6):
        assert start.get_books_novelty()[i].is_displayed()


@pytest.mark.body
def test_succesful_find_books_wath_now(driver):
    start = StartLab(driver)
    start.visit()
    assert start.get_books_news().is_displayed()


@pytest.mark.body
def test_succesful_find_labirint_books_revie(driver):
    start = StartLab(driver)
    start.visit()
    for i in range(5):
        assert start.get_books_reviews()[i].is_displayed()


@pytest.mark.body
def test_succesful_find_labirint_text_footer(driver):
    start = StartLab(driver)
    start.visit()
    assert start.get_labirint_text_footer() == 'Лабиринт – книжный интернет-магазин с доставкой по всей России. У нас вы подберете себе чтение по душе. Главные новинки, нестареющая классика, книги для учебы, работы и творчества, детская литература – все это можно купить у нас. Получить свои книги легко и быстро можно в ближайших пунктах выдачи или с курьерской доставкой. Мы любим дарить подарки, радовать большими скидками, интересными конкурсами и флешмобами. Ведь Лабиринт – это не просто интернет-магазин книг, а настоящий клуб любителей чтения. Станьте его частью!'


@pytest.mark.footer
def test_succesful_find_saite_app_store(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_app_store().click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://apps.apple.com/ru/app/%D0%BB%D0%B0%D0%B1%D0%B8%D1%80%D0%B8%D0%BD%D1%82-%D1%80%D1%83-%D0%BA%D0%BD%D0%B8%D0%B6%D0%BD%D1%8B%D0%B9-%D0%BC%D0%B0%D0%B3%D0%B0%D0%B7%D0%B8%D0%BD/id1008650482'


@pytest.mark.footer
def test_succesful_find_saite_google_play(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_google_play().click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://play.google.com/store/apps/details?id=ru.labirint.android'


@pytest.mark.footer
def test_succesful_find_saite_app_galery(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_app_galery().click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://appgallery.huawei.com/app/C101184737?appId=C101184737&source=appshare&subsource=C101184737'


@pytest.mark.footer
def test_succesful_find_my_social_networks_VK(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_social_networks_list()[0].click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://vk.com/labirint_ru'


@pytest.mark.footer
def test_succesful_find_my_social_networks_VK_kids(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_social_networks_list()[1].click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://vk.com/labirintdeti'


@pytest.mark.footer
def test_succesful_find_my_social_networks_you_tube(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_social_networks_list()[2].click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://www.youtube.com/user/labirintruTV'


@pytest.mark.footer
def test_succesful_find_my_social_networks_instagram(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_social_networks_list()[3].click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://www.instagram.com/labirintru/'


@pytest.mark.footer
def test_succesful_find_my_social_networks_instgram_kids(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_social_networks_list()[4].click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://www.instagram.com/labirintdeti/'


@pytest.mark.footer
def test_succesful_find_my_social_networks_facebook(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_social_networks_list()[5].click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://www.facebook.com/labirintru'


@pytest.mark.footer
def test_succesful_find_my_social_networks_ok(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_social_networks_list()[6].click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://ok.ru/labirintru'


@pytest.mark.footer
def test_succesful_find_my_social_networks_twitter(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_social_networks_list()[7].click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://twitter.com/labirint_ru'


@pytest.mark.footer
def test_succesful_find_my_social_networks_zen(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_social_networks_list()[8].click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://zen.yandex.ru/labirintru'


@pytest.mark.footer
def test_succesful_find_my_social_networks_telegram(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_social_networks_list()[9].click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://t.me/labirintru'


@pytest.mark.footer
def test_succesful_find_my_social_networks_tiktok(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_social_networks_list()[10].click()
    start.get_swith_to_windows()
    assert driver.current_url == 'https://www.tiktok.com/@labirintru'


@pytest.mark.footer
def test_succesful_find_footer_katalog_all_books(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_catalog_books()[0].click()
    assert driver.current_url == base_url + 'books/'


@pytest.mark.footer
def test_succesful_find_footer_katalog_school_books(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_catalog_books()[1].click()
    assert driver.current_url == base_url + 'school/'


@pytest.mark.footer
def test_succesful_find_footer_katalog_journals(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_catalog_books()[2].click()
    assert driver.current_url == base_url + 'journals/'


@pytest.mark.footer
def test_succesful_find_footer_katalog_games(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_catalog_books()[3].click()
    assert driver.current_url == base_url + 'games/'


@pytest.mark.footer
def test_succesful_find_footer_katalog_office(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_catalog_books()[4].click()
    assert driver.current_url == base_url + 'office/'


@pytest.mark.footer
def test_succesful_find_footer_katalog_multimedia(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_catalog_books()[5].click()
    assert driver.current_url == base_url + 'multimedia/'


@pytest.mark.footer
def test_succesful_find_footer_katalog_souvenir(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_catalog_books()[6].click()
    assert driver.current_url == base_url + 'souvenir/'


@pytest.mark.footer
def test_succesful_find_footer_katalog_household(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_catalog_books()[7].click()
    assert driver.current_url == base_url + 'household/'


@pytest.mark.footer
def test_succesful_find_footer_important_actions(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_important()[0].click()
    assert driver.current_url == base_url + 'actions/'


@pytest.mark.footer
def test_succesful_find_footer_important_best(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_important()[1].click()
    assert driver.current_url == base_url + 'best/'


@pytest.mark.footer
def test_succesful_find_footer_important_bonus_za_recenziyu(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_important()[2].click()
    assert driver.current_url == base_url + 'top/bonus-za-recenziyu/'


@pytest.mark.footer
def test_succesful_find_footer_important_certificates(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_important()[3].click()
    assert driver.current_url == base_url + 'top/certificates/'


@pytest.mark.footer
def test_succesful_find_footer_important_exclusive(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.apply_cookie().click()
    assert start.get_footer_important()[4].is_displayed


@pytest.mark.footer
def test_succesful_find_footer_important_pred_zakaz(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.apply_cookie().click()
    assert start.get_footer_important()[5].is_displayed


@pytest.mark.footer
def test_succesful_find_footer_intresting_labarint_now(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_fav()[0].click()
    assert driver.current_url == base_url + 'now/'


@pytest.mark.footer
def test_succesful_find_footer_intresting_kids_navigator(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_fav()[1].click()
    assert driver.current_url == base_url + 'child-now/'


@pytest.mark.footer
def test_succesful_find_footer_intresting_reviews(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_fav()[2].click()
    assert driver.current_url == base_url + 'reviews/'


@pytest.mark.footer
def test_succesful_find_footer_new_books(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_fav()[3].click()
    assert driver.current_url == base_url + 'news/books/'


@pytest.mark.footer
def test_succesful_find_footer_littest(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_fav()[5].click()
    assert driver.current_url == base_url + 'littest/'


@pytest.mark.footer
def test_succesful_find_footer_news(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_fav()[6].click()
    assert driver.current_url == base_url + 'news/'


@pytest.mark.footer
def test_succesful_find_footer_contests(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_fav()[7].click()
    assert driver.current_url == base_url + 'contests/'


@pytest.mark.footer
def test_succesful_find_footer_club(driver):
    start = StartLab(driver)
    start.visit()
    start = StartLabFooter(driver)
    start.get_scroll_footer()
    start.get_footer_fav()[8].click()
    assert driver.current_url == base_url + 'club/'


@pytest.mark.find_books
def test_succesful_find_books_positive(driver):
    start = StartLab(driver)
    start.visit()
    start.get_labirint_find_books().send_keys('python')
    start.get_labirint_find_reserch_books_positive().click()
    assert driver.find_element_by_css_selector(
        '.index-top-title').text == 'Все, что мы нашли в Лабиринте по запросу «python»'
