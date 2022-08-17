import os
from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    # кнопка "Лабиринт"
    btn_labirint = WebElement(css_selector='.b-header-b-logo-e-logo')

    # локаторы строки поиска
    search_form = WebElement(id="searchform")
    search = WebElement(id="search-field")

    # кнопка "Поиск"
    btn_search = WebElement(class_name='b-header-b-search-e-btn')

    # Названия товаров в результате поиска
    products_titles = ManyWebElements(css_selector='.product-title-link')

    # Окно авторизации
    auth_window = WebElement(xpath='//div[contains(text(), "Полный доступ к Лабиринту")]')

    # меню иконок
    header_icon = WebElement(xpath='//div[@class="b-header-b-personal-wrapper"]')
    # кнопка "Сообщения"
    btn_message = WebElement(xpath='//span[contains(text(), "Сообщения")]')
    # кнопка "Мой Лаб"
    btn_my_lab = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.top-link-main_cabinet.'
                                         'js-b-autofade-wrap')
    # кнопка "Отложено"
    btn_postponed = WebElement(xpath='//span[contains(text(), "Отложено")]')
    # кнопка "Корзина"
    btn_cart = WebElement(xpath='//span[contains(text(), "Корзина")]')

    # локаторы кнопок в меню страницы
    # кнопка "Книги"
    btn_books = WebElement(css_selector='.b-header-b-menu-e-text[href="/books/"]')
    # кнопка "Все книги" из выпадающего списка "Книги"
    btn_all_books = WebElement(css_selector='.b-menu-list-title.b-menu-list-title-first[href="/books/"]')
    # кнопка "Главное 2022"
    btn_best = WebElement(css_selector='.b-header-b-menu-e-text[href="/best/"]')
    # кнопка "Школа"
    btn_school = WebElement(css_selector='.b-header-b-menu-e-text[href="/school/"]')
    # кнопка "Игрушки"
    btn_games = WebElement(css_selector='.b-header-b-menu-e-text[href="/games/"]')
    # кнопка "Канцтовары"
    btn_office = WebElement(css_selector='.b-header-b-menu-e-text[href="/office/"]')
    # кнопка "еще"
    btn_still = WebElement(xpath='//span[contains(text(), "Еще")]')
    # кнопка "CD/DVD"
    btn_cd_dvd = WebElement(xpath='//a[@title="Аудиокниги, музыка, видеофильмы, компьютерные программы, игры и др."]')
    # кнопка "Сувениры"
    btn_souvenir = WebElement(xpath='//a[@title="Сувениры, альбомы для фотографий, фоторамки, календари."]')
    # кнопка "Журналы"
    btn_journals = WebElement(xpath='//a[@title="Литературные журналы: художественные и публицистические, '
                                    'поэтические."]')
    # кнопка "Товары для дома"
    btn_household = WebElement(xpath='//a[@title="Товары для дома"]')
    # кнопка "Клуб"
    btn_club = WebElement(css_selector='.b-header-b-menu-e-text[href="/club/"]')

    # Строка меню
    header_menu = WebElement(xpath='//div[@class="b-header-b-menu-wrapper"]')
    sec_menu = WebElement(xpath='//div[@class="b-header-b-sec-menu-wrapper relative"]')

    # кнопка "Доставка и оплата"
    btn_delivery = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/help/"]')
    # кнопка "Сертификаты"
    btn_certificates = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/top/certificates/"]')
    # кнопка "Рейтинги"
    btn_rating = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/rating/?id_genre=-1&nrd=1"]')
    # кнопка "Новинки"
    btn_novelty = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/novelty/"]')
    # кнопка "Скидки"
    btn_sale = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/sale/"]')
    # кнопка "Контакты"
    btn_contact = WebElement(xpath='//a[contains(text(), "Контакты")]')
    # кнопка "Поддержка"
    btn_support = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/support/"]')
    # кнопка "Самовывоз"
    btn_maps = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/maps/"]')

    # Фильтр
    filter_list = WebElement(class_name='sorting-items')
    # фильтр "релевантные"
    filter_relevance = WebElement(xpath='//a[contains(text(), "релевантные")]')
    # фильтр "новинки"
    filter_new = WebElement(xpath='//a[contains(text(), "новинки")]')
    # фильтр "Лидеры продаж"
    filter_leaders = WebElement(xpath='//a[contains(text(), "лидеры продаж")]')
    # фильтр "рецензируемые"
    filter_review = WebElement(xpath='//a[contains(text(), "рецензируемые")]')
    # фильтр "дешевые"
    filter_cheap = WebElement(xpath='//a[contains(text(), "дешевые")]')
    # фильтр "дорогие"
    filter_expensive = WebElement(xpath='//a[contains(text(), "дорогие")]')
    expensive = WebElement(xpath='//span[contains(text(), Сначала дорогие)]')
    # фильтр "с макс. скидкой"
    filter_max_sale = WebElement(xpath='//a[contains(text(), "с макс. скидкой")]')
    # фильтр "по названию А-Я"
    filter_name_forward = WebElement(xpath='//a[@href="?stype=0&order=name&way=forward"]')
    # фильтр "по названию Я-А"
    filter_name_back = WebElement(xpath='//a[@href="?stype=0&order=name&way=back"]')
    # фильтр "по автору А-Я"
    filter_author_forward = WebElement(xpath='//a[@href="?stype=0&order=author&way=forward"]')
    # фильтр "по автору Я-А"
    filter_author_back = WebElement(xpath='//a[@href="?stype=0&order=author&way=back"]')

    # "подвал" страницы
    footer = WebElement(xpath='//div[@class="b-rfooter-wrapper"]')


    # btn_help_order = WebElement(xpath='//*[@id="body-top"]/div[5]/div[2]/div/div[4]/div[2]/div[2]/ul/li[2]/a')
    btn_pay = WebElement(css_selector='.b-rfooter-e-item[href="/help/?clause=132"]')
    # btn_help_order = WebElement(css_selector='b-rfooter-e-item-link analytics-click-js[href="/help/order/"]')
    btn_help_order = WebElement(xpath='//a[contains(text(), "Как сделать заказ")]')











