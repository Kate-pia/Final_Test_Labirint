import os
from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.labirint.ru/'

        super().__init__(web_driver, url)

    # Переключатель "Моя корзина:"
    # Страница товара
    btn_product = WebElement(xpath='//a[@id="buy797977"]')
    # кнопка "В КОРЗИНУ"
    btn_in_cart = WebElement(css_selector='.btn.buy-link.btn-primary')
    cart_btn = WebElement(
        css_selector='.b-header-b-personal-e-link.top-link-main.analytics-click-js.cart-icon-js[href="/cart/"]')
    # Кнопка "Оформить корзину"
    btn_cart = WebElement(xpath='//a[href="/cart/"]')
    # Переключатель "Отложенные:"
    postponed = WebElement(xpath='//a[contains(text(), "Отложенные: ")]')
    # Кнопка "Очистить корзину"
    delete_cart = WebElement(xpath='//a[contains(text(), "Очистить корзину")]')
    # Кнопка "Переслать корзину"
    send_cart = WebElement(xpath='//span[contains(text(), "Переслать корзину")]')
    # Кнопка увеличить количество товара "+"
    btn_increase = WebElement(class_name="btn.btn-increase.btn-increase-cart")
    # Кнопка уменишить количество товара "-"
    btn_lessen = WebElement(class_name="btn.btn-lessen.btn-lessen-cart")
    # Кнопка "Сертификаты и купоны"

    # Поле ввода кода скидки для авторизации
    input_code_email = WebElement(css_selector='.full-input__input.formvalidate-error[type="text"]')

    # Кнопка "Забыл ввести код скидки"

    # Кнопка "Перейти к оформлению"

    # Кнопка "Восстановить удаленное"
    restore_cart = WebElement(xpath='//a[contains(text(), "Восстановить удаленное")]')
