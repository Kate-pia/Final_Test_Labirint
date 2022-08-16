import os
from pages.base import WebPage
from pages.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)


    # Переключатель "Моя корзина:"
    # кнопка "Поиск"
    search = WebElement(id="search-field")
    btn_search = WebElement(class_name='b-header-b-search-e-btn')
    # Страница товара
    prod = WebElement(xpath='//a[@href="/books/829644/"]')

    # кнопка "В КОРЗИНУ"
    btn_in_carts = WebElement(css_selector='.btn.btn-small.btn-primary.btn-buy')
    btn_pro = WebElement(id="buy829644")
    cart_btn = WebElement(
        css_selector='.b-header-b-personal-e-link.top-link-main.analytics-click-js.cart-icon-js[href="/cart/"]')
    # Кнопка "Оформить корзину"
    btn_cart = WebElement(xpath='//a[href="/cart/"]')

