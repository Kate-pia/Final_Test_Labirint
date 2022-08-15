from pages.labirint_main import MainPage


def test_search_form_is_visible(web_browser):
    """Строка "Поиск по Лабиринту" видна на странице"""

    page = MainPage(web_browser)

    assert page.search_form.is_visible()


def test_sec_menu_is_visible(web_browser):
    """Строка "Поиск по Лабиринту" видна на странице"""

    page = MainPage(web_browser)

    assert page.sec_menu.is_visible()


def test_header_menu_is_visible(web_browser):
    """ Строка "Поиск по Лабиринту" видна на странице """

    page = MainPage(web_browser)

    assert page.header_menu.is_visible()


def test_scroll_page(web_browser):
    """ Проверка скроллинга страницы"""

    page = MainPage(web_browser)
    page.scroll_down()

    assert page.header_menu.is_visible()


def test_header_icon_is_visible(web_browser):
    """Строка "Поиск по Лабиринту" видна на странице"""

    page = MainPage(web_browser)

    assert page.header_icon.is_visible()


def test_check_main_search(web_browser):
    """Проверка поля "Поиск по Лабиринту" """

    page = MainPage(web_browser)

    page.search = 'детектив'
    page.btn_search.click()

    assert page.products_titles.count() >= 1


def test_check_wrong_input_in_search(web_browser):
    """ Проверка, что ввод с неправильной раскладки клавиатуры работает правильно """

    page = MainPage(web_browser)

    # Попробуйте ввести запрос "Детектив" с английской раскладки:
    page.search = 'Ltntrnbd'
    page.btn_search.click()

    #  Проверяем, что пользователь может видеть список товаров
    assert page.products_titles.count() >= 1

    # Проверяем, что пользователь нашел соответствующие товары
    for title in page.products_titles.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'Детектив' in title.lower(), msg


def test_check_input_numbers_in_search(web_browser):
    """ Проверка, что при вводе цифр поиск работает нормально. """

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


def test_title_product(web_browser):
    """Проверка, что у всех товаров есть название"""

    page = MainPage(web_browser)

    page.search = 'детектив'
    page.btn_search.click()

    assert page.products_titles.get_attribute('title') != ''


def test_photo_product(web_browser):
    """Проверка, что у всех товаров есть изображение"""

    page = MainPage(web_browser)

    page.search = 'детектив'
    page.btn_search.click()

    assert page.products_titles.get_attribute('src') != ''


def test_check_sort_by_price(web_browser):
    """ Проверка сортировки продуктов """

    page = MainPage(web_browser)

    page.search = 'роман'
    page.btn_search.click()

    # Прокрутка до элемента, чтобы он стал виден пользователю
    page.sort_products_by_price.scroll_to_element()
    page.sort_products_by_price.click()
    page.wait_page_loaded()

    # Получение цен всех выведенных продуктов
    all_prices = page.products_prices.get_text()

    # Конвертирование всех цен из строк в числа
    all_prices = [float(p.replace(' ', '')) for p in all_prices]

    # Make sure products are sorted by price correctly:
    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"


# Проверка фильтров
def test_filter_relevance(web_browser):
    """Проверка фильтра "релевантные" """

    page = MainPage(web_browser)

    page.search.send_keys('комиксы')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_relevance.click()


def test_filter_leaders(web_browser):
    """Проверка фильтра "Лидеры продаж" """

    page = MainPage(web_browser)

    page.search.send_keys('комиксы')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_leaders.click()
    #assert 'Сначала лидеры продаж' in page.get_current_url()
    #assert page.get_current_url() == "https://www.labirint.ru/search/%D0%B4%D0%B5%D1%82%D0%B5%D0%BA%D1%82%D0%B8%D0%B2/?stype=0&order=popularity&way=forward"


def test_filter_new(web_browser):
    """Проверка фильтра "новинки" """

    page = MainPage(web_browser)

    page.search.send_keys('комиксы')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_new.click()


def test_filter_review(web_browser):
    """Проверка фильтра "рецензируемые" """

    page = MainPage(web_browser)

    page.search.send_keys('комиксы')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_review.click()


def test_filter_cheap(web_browser):
    """Проверка фильтра "дешевые" """

    page = MainPage(web_browser)

    page.search.send_keys('комиксы')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_cheap.click()


def test_filter_expensive(web_browser):
    """Проверка фильтра "дорогие" """

    page = MainPage(web_browser)

    page.search.send_keys('комиксы')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_expensive.click()


def test_filter_max_sale(web_browser):
    """Проверка фильтра "с макс. скидкой" """

    page = MainPage(web_browser)

    page.search.send_keys('комиксы')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_max_sale.click()


def test_filter_name_forward(web_browser):
    """Проверка фильтра "по названию А-Я" """

    page = MainPage(web_browser)

    page.search.send_keys('комиксы')
    page.btn_search.click()
    page.filter_list.click()
    page.scroll_down()
    page.filter_name_forward.click()


def test_filter_name_back(web_browser):
    """Проверка фильтра "по названию Я-А" """

    page = MainPage(web_browser)

    page.search.send_keys('комиксы')
    page.btn_search.click()
    page.filter_list.click()
    page.filter_name_back.find()
    page.filter_name_back.click()

