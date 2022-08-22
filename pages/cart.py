import os
from pages.base import WebPage
from pages.elements import WebElement


class CartPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/cart/'

        super().__init__(web_driver, url)

    # Пример товара добавленного в корзину
    product = WebElement(xpath='//a[@href="/books/829644/"]')

    # Счетчик товаров в корзине
    counter_cart = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a')
    # Счетчик товаров в "отложено"
    counter_postponed = WebElement(css_selector='.b-header-b-personal-e-icon-count-m-putorder.basket-in-dreambox-a')

    # Кнопка "Очистить корзину"
    clear_cart = WebElement(xpath='//a[contains(text(), "Очистить корзину")]')
    # Кнопка "Восстановить удаленное"
    restore_cart = WebElement(xpath='//a[contains(text(), "Восстановить удаленное")]')

    # Поле изменения количества товара
    quantity = WebElement(xpath='//input[@class="quantity"]')
    # Кнопка увеличить количество товара "+"
    btn_increase = WebElement(xpath='//span[@class="btn btn-increase btn-increase-cart"]')

    # Кнопка уменишить количество товара "-"
    btn_lessen = WebElement(xpath='//span[@class="btn btn-lessen btn-lessen-cart"]')

    # Кнопка "Перейти к оформлению"
    btn_checkout = WebElement(css_selector='.btn.btn-primary.btn-large.fright.start-checkout-js')
