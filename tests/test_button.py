from pages.labirint_main import MainPage
from selenium.webdriver import ActionChains
import pytest


def test_check_btn_labirint(web_browser):
    """Проверка перехода на страницу "Лабиринт" при нажатии на логотип """

    page = MainPage(web_browser)

    page.btn_labirint.click()

    assert page.get_current_url() == "https://www.labirint.ru/"


@pytest.mark.header_menu
class TestHeaderMenuFromMainPage:
    def test_check_btn_message(self, web_browser):
        """Проверка перехода на страницу "Сообщения" """

        page = MainPage(self, web_browser)

        page.btn_message.click()
        text = page.auth_window.get_text()

        assert text == "Полный доступ к Лабиринту"

    def test_check_btn_my_lab(self, web_browser):
        """Проверка кнопки "Мой Лаб" """

        page = MainPage(self, web_browser)

        page.btn_my_lab.click()
        text = page.auth_window.get_text()

        assert text == "Полный доступ к Лабиринту"


def test_check_btn_postponed(web_browser):
    """Проверка перехода на страницу "Отложено" """

    page = MainPage(web_browser)

    page.btn_postponed.click()

    assert page.get_current_url() == "https://www.labirint.ru/cabinet/putorder/"


def test_check_btn_cart(web_browser):
    """Проверка перехода на страницу "Корзина" """

    page = MainPage(web_browser)

    page.btn_cart.click()

    assert page.get_current_url() == "https://www.labirint.ru/cart/"


def test_check_btn_books(web_browser):
    """Проверка перехода на страницу "Книги" """

    page = MainPage(web_browser)

    page.btn_books.click()

    assert page.get_current_url() == "https://www.labirint.ru/books/"


def test_check_submenu_books(web_browser):
    """Проверка открытия подменю "Книги" и перехода на страницу "Все книги" """

    page = MainPage(web_browser)

    submenu_books = page.btn_books.find()
    ActionChains(web_browser).move_to_element(submenu_books).perform()
    page.btn_all_books.click()
    assert page.get_current_url() == "https://www.labirint.ru/books/"


def test_check_btn_best(web_browser):
    """Проверка перехода на страницу "Главное 2022" """

    page = MainPage(web_browser)

    page.btn_best.click()

    assert page.get_current_url() == "https://www.labirint.ru/best/"


def test_check_btn_school(web_browser):
    """Проверка перехода на страницу "Школа" """

    page = MainPage(web_browser)

    page.btn_school.click()

    assert page.get_current_url() == "https://www.labirint.ru/school/"


def test_check_btn_games(web_browser):
    """Проверка перехода на страницу "Игрушки" """

    page = MainPage(web_browser)

    page.btn_games.click()

    assert page.get_current_url() == "https://www.labirint.ru/games/"


def test_check_btn_office(web_browser):
    """Проверка перехода на страницу "Канцтовары" """

    page = MainPage(web_browser)

    page.btn_office.click()

    assert page.get_current_url() == "https://www.labirint.ru/office/"


def test_check_btn_cd_dvd(web_browser):
    """Проверка перехода на страницу "CD/DVD" """

    page = MainPage(web_browser)

    submenu_still = page.btn_still.find()
    ActionChains(web_browser).move_to_element(submenu_still).perform()
    page.btn_cd_dvd.click()

    assert page.get_current_url() == "https://www.labirint.ru/multimedia/"


def test_check_btn_souvenir(web_browser):
    """Проверка перехода на страницу "Сувениры" """

    page = MainPage(web_browser)

    submenu_still = page.btn_still.find()
    ActionChains(web_browser).move_to_element(submenu_still).perform()
    page.btn_souvenir.click()

    assert page.get_current_url() == "https://www.labirint.ru/souvenir/"


def test_check_btn_journals(web_browser):
    """Проверка перехода на страницу "Журналы" """

    page = MainPage(web_browser)

    submenu_still = page.btn_still.find()
    ActionChains(web_browser).move_to_element(submenu_still).perform()
    page.btn_journals.click()

    assert page.get_current_url() == "https://www.labirint.ru/journals/"


def test_check_btn_household(web_browser):
    """Проверка перехода на страницу "Товары для дома" """

    page = MainPage(web_browser)

    submenu_still = page.btn_still.find()
    ActionChains(web_browser).move_to_element(submenu_still).perform()
    page.btn_household.click()

    assert page.get_current_url() == "https://www.labirint.ru/household/"


def test_check_btn_club(web_browser):
    """Проверка перехода на страницу "Клуб" """
    page = MainPage(web_browser)
    page.btn_club.click()

    assert page.get_current_url() == "https://www.labirint.ru/club/"


def test_check_btn_delivery(web_browser):
    """Проверка перехода на страницу "Доставка и оплата" """

    page = MainPage(web_browser)

    page.btn_delivery.click()

    assert page.get_current_url() == "https://www.labirint.ru/help/"


def test_check_btn_certificates(web_browser):
    """Проверка перехода на страницу "Сертификаты" """

    page = MainPage(web_browser)

    page.btn_certificates.click()

    assert page.get_current_url() == "https://www.labirint.ru/top/certificates/"


def test_check_btn_rating(web_browser):
    """Проверка перехода на страницу "Рейтинги" """

    page = MainPage(web_browser)

    page.btn_rating.click()

    assert page.get_current_url() == "https://www.labirint.ru/rating/?id_genre=-1&nrd=1"


def test_check_btn_novelty(web_browser):
    """Проверка перехода на страницу "Новинки" """

    page = MainPage(web_browser)

    page.btn_novelty.click()

    assert page.get_current_url() == "https://www.labirint.ru/novelty/"


def test_check_btn_sale(web_browser):
    """Проверка перехода на страницу "Скидки" """

    page = MainPage(web_browser)

    page.btn_sale.click()

    assert page.get_current_url() == "https://www.labirint.ru/sale/"


def test_check_btn_contact(web_browser):
    """Проверка перехода на страницу "Контакты" """

    page = MainPage(web_browser)

    page.btn_contact.click()

    assert page.get_current_url() == "https://www.labirint.ru/contact/"


def test_check_btn_support(web_browser):
    """Проверка перехода на страницу "Поддержка" """

    page = MainPage(web_browser)

    page.btn_support.click()

    assert page.get_current_url() == "https://www.labirint.ru/support/"


def test_check_btn_maps(web_browser):
    """Проверка перехода на страницу "Самовывоз" """

    page = MainPage(web_browser)

    page.btn_maps.click()

    assert page.get_current_url() == "https://www.labirint.ru/maps/"


# def test_btn_geolock(web_browser):
#     """Проверка смены "Местоположение" """
#
#     page = MainPage(web_browser)
#
#     page.btn_geolock.click()
#     page.input_city.click()
#     page.input_city.send_keys("Москва").submit()
#     title = page.city_title.get_attribute('title')
#     assert title == "Москва"
#
#
# def test_help_order_in_footer(web_browser):
#     """Проверка перехода на страницу "Как сделать заказ" """
#
#     page = MainPage(web_browser)
#     page.wait_page_loaded()
#     page.btn_help_order.scroll_to_element()
#
#     assert page.btn_help_order.is_clickable()
#     page.btn_help_order.click()
#     assert page.get_current_url() == "https://www.labirint.ru/help/order/"
#

# def test_help_pay(web_browser):
#     """Проверка перехода на страницу "Самовывоз" """
#
#     page = MainPage(web_browser)
#     page.wait_page_loaded()
#     page.btn_pay.scroll_to_element()
#     page.btn_pay.click()
#
#     assert page.get_current_url() == "https://www.labirint.ru/help/?clause=132"



