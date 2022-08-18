import os
from pages.base import WebPage
from pages.elements import WebElement


class ProductPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/books/829644/'

        super().__init__(web_driver, url)

    # кнопка "Добавить в корзину"
    btn_in_cart = WebElement(css_selector='.btn.btn-small.btn-primary.btn-buy')
    # кнопка "Оформить"
    btn_to_cart = WebElement(css_selector='.btn.btn-small.btn-more.tobasket')
    # кнопка "Добавить в отложенное"
    btn_fave = WebElement(css_selector='.fave')

    # Счетчик товаров в корзине
    counter_cart = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a')
    # Счетчик товаров в "отложено"
    counter_postponed = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-putorder.basket-in-dreambox-a')
