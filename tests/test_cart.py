from pages.cart import CartPage
from pages.product import ProductPage


def test_clear_cart(web_browser):
    """ Проверка кнопки "Очистить корзину" """

    page = ProductPage(web_browser)

    page.btn_in_cart.click()
    page.btn_to_cart.click()
    page_cart = CartPage(web_browser)

    assert page_cart.product.is_visible()

    page_cart.clear_cart.click()
    assert page_cart.counter_cart.get_text() == '0'


def test_restore_cart(web_browser):
    """ Проверка кнопки "Восстановить удаленное" из корзины """

    page = ProductPage(web_browser)

    page.btn_in_cart.click()
    page.btn_to_cart.click()

    page_cart = CartPage(web_browser)
    assert page_cart.product.is_visible()
    assert page_cart.counter_cart.get_text() == '1'

    page_cart.clear_cart.click()
    assert page_cart.counter_cart.get_text() == '0'
    page_cart.restore_cart.click()
    assert page_cart.counter_cart.get_text() == '1'


def test_increase_product_in_cart(web_browser):
    """Проверка поля увеличения количества товара """

    page = ProductPage(web_browser)

    page.btn_in_cart.click()
    page.btn_to_cart.click()

    page_cart = CartPage(web_browser)

    page_cart.quantity.scroll_to_element()
    page_cart.quantity.send_keys("2")
    page_cart.wait_page_loaded()
    page_cart.btn_lessen.click()
    page_cart.wait_page_loaded()
    assert page_cart.counter_cart.get_text() == '1'


def test_btn_increase_product_in_cart(web_browser):
    """Проверка кнопки "+" увеличения количества товара """

    page = ProductPage(web_browser)

    page.btn_in_cart.click()
    page.btn_to_cart.click()

    page_cart = CartPage(web_browser)

    assert page_cart.counter_cart.get_text() == '1'
    page_cart.quantity.scroll_to_element()
    page_cart.btn_increase.click()
    page_cart.wait_page_loaded()
    assert page_cart.counter_cart.get_text() == '2'


def test_lessen_product_in_cart(web_browser):
    """Проверка кнопки "-" уменьшения количества товара """

    page = ProductPage(web_browser)

    page.btn_in_cart.click()
    page.btn_to_cart.click()

    page_cart = CartPage(web_browser)

    page_cart.quantity.scroll_to_element()
    page_cart.btn_increase.click()
    page_cart.wait_page_loaded()
    page_cart.btn_lessen.click()
    page_cart.wait_page_loaded()
    assert page_cart.counter_cart.get_text() == '1'


def test_checkout_order(web_browser):
    """Проверка кнопки "Перейти к оформлению" """

    page = ProductPage(web_browser)

    page.btn_in_cart.click()
    page.btn_to_cart.click()

    page_cart = CartPage(web_browser)

    assert page_cart.counter_cart.get_text() == '1'

    page_cart.btn_checkout.click()

    assert page_cart.get_current_url() == "https://www.labirint.ru/basket/checkout/"






