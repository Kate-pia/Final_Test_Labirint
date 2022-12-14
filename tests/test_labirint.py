# для запуска тестов перейдите в папку tests введя команду cd tests,
# после чего введите в терминале команду pytest -v test_labirint.py
from pages.labirint_main import MainPage
import pytest


def test_search_form_is_visible(web_browser):
    """Строка "Поиск по Лабиринту" видна на странице"""

    page = MainPage(web_browser)

    assert page.search_form.is_visible()


def test_sec_menu_is_visible(web_browser):
    """ Меню с контактной информацией видно на странице"""

    page = MainPage(web_browser)

    assert page.sec_menu.is_visible()


def test_header_menu_is_visible(web_browser):
    """ Главное меню товаров видно на странице """

    page = MainPage(web_browser)

    assert page.header_menu.is_visible()


def test_header_icon_is_visible(web_browser):
    """ Меню с иконками видно на странице"""

    page = MainPage(web_browser)

    assert page.header_icon.is_visible()


def test_footer_is_visible(web_browser):
    """ Меню подвала видно на странице"""

    page = MainPage(web_browser)
    page.scroll_down()

    assert page.footer.is_visible()


@pytest.mark.parametrize("param", ['тестирование', 'python'])
def test_check_main_search(web_browser, param):
    """Проверка поля "Поиск по Лабиринту" """

    page = MainPage(web_browser)

    page.search.send_keys(param)
    page.btn_search.click()

    assert page.products_titles.count() >= 1

    # Проверяем, что пользователь нашел соответствующие товары
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert param in title.lower(), msg


def test_check_wrong_input_in_search(web_browser):
    """ Проверка, что ввод с неправильной раскладки клавиатуры работает корректно """

    page = MainPage(web_browser)

    # Проверка ввода запроса "тестирование" с английской раскладки:
    page.search.send_keys('ntcnbhjdfybt')
    page.btn_search.click()

    #  Проверяем, что пользователь может видеть список товаров
    assert page.products_titles.count() >= 1

    # Проверяем, что пользователь нашел соответствующие товары
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'тестирование' in title.lower(), msg


def test_check_input_numbers_in_search(web_browser):
    """ Проверка, что при вводе цифр поиск работает корректно """

    page = MainPage(web_browser)

    # Попробуем ввести несколько цифр:
    page.search.send_keys("125")
    page.btn_search.click()

    # Проверяем, что пользователь может видеть список :
    assert page.products_titles.count() >= 1

    # Проверяем, что пользователь нашел соответствующие товары:
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert '125' in title.lower(), msg


def test_selection_product(web_browser):
    """ Проверка выбора товара после поиска """

    page = MainPage(web_browser)

    page.search.send_keys('тестирование')
    page.btn_search.click()
    page.product.scroll_to_element()
    page.product.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/books/829644/'


def test_title_product(web_browser):
    """Проверка, что у всех товаров есть название"""

    page = MainPage(web_browser)

    page.search.send_keys('детектив')
    page.btn_search.click()

    assert page.products_titles.get_attribute('title') != ''


def test_photo_product(web_browser):
    """Проверка, что у всех товаров есть изображение"""

    page = MainPage(web_browser)

    page.search.send_keys('детектив')
    page.btn_search.click()

    assert page.products_titles.get_attribute('src') != ''


def test_filter_relevance(web_browser):
    """Проверка фильтра "релевантные" """

    page = MainPage(web_browser)

    page.search.send_keys('python')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_relevance.click()
    page.wait_page_loaded()

    assert page.get_current_url() == "https://www.labirint.ru/search/python/?stype=0&order=relevance&way=back"


def test_filter_leaders(web_browser):
    """Проверка фильтра "Лидеры продаж" """

    page = MainPage(web_browser)

    page.search.send_keys('python')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_leaders.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/search/python/?stype=0&order=popularity&way=forward'


def test_filter_new(web_browser):
    """Проверка фильтра "новинки" """

    page = MainPage(web_browser)

    page.search.send_keys('python')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_new.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.labirint.ru/search/python/?stype=0&order=date&way=back'


def test_filter_review(web_browser):
    """Проверка фильтра "рецензируемые" """

    page = MainPage(web_browser)

    page.search.send_keys('python')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_review.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/search/python/?stype=0&order=review&way=back'


def test_filter_cheap(web_browser):
    """Проверка фильтра "дешевые" """

    page = MainPage(web_browser)

    page.search.send_keys('python')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_cheap.scroll_to_element()
    page.filter_cheap.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/search/python/?stype=0&order=price&way=forward'


def test_filter_expensive(web_browser):
    """Проверка фильтра "дорогие" """

    page = MainPage(web_browser)

    page.search.send_keys('python')
    page.btn_search.click()
    page.filter_list.click()
    page.wait_page_loaded()
    page.filter_cheap.scroll_to_element()
    page.filter_expensive.scroll_to_element()
    page.filter_expensive.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/search/python/?stype=0&order=price&way=back'


def test_filter_max_sale(web_browser):
    """Проверка фильтра "с макс. скидкой" """

    page = MainPage(web_browser)

    page.search.send_keys('python')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_max_sale.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/search/python/?stype=0&order=actd&way=back'


def test_filter_name_forward(web_browser):
    """Проверка фильтра "по названию А-Я" """

    page = MainPage(web_browser)

    page.search.send_keys('python')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_name_forward.scroll_to_element()
    page.filter_name_forward.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.labirint.ru/search/python/?stype=0&order=name&way=forward'


def test_filter_name_back(web_browser):
    """Проверка фильтра "по названию Я-А" """

    page = MainPage(web_browser)

    page.search.send_keys('python')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_name_back.scroll_to_element()
    page.filter_name_back.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.labirint.ru/search/python/?stype=0&order=name&way=back'


def test_filter_author_forward(web_browser):
    """Проверка фильтра "по автору А-Я" """

    page = MainPage(web_browser)

    page.search.send_keys('python')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_author_forward.scroll_to_element()
    page.filter_author_forward.click()
    page.wait_page_loaded()
    assert page.get_current_url() == 'https://www.labirint.ru/search/python/?stype=0&order=author&way=forward'


def test_filter_author_back(web_browser):
    """Проверка фильтра "по автору Я-А" """

    page = MainPage(web_browser)

    page.search.send_keys('python')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_author_back.scroll_to_element()
    page.filter_author_back.click()
    page.wait_page_loaded()

    assert page.get_current_url() == 'https://www.labirint.ru/search/python/?stype=0&order=author&way=back'
