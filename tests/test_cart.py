from pages.cart import MainPage
from pages.labirint_main import MainPage


def test_add_product_in_cart(web_browser):
    """Проверка добавления товара в корзину """

    page = MainPage(web_browser)

    page.search.send_keys('тестирование')
    page.btn_search.click()

    page.product.click()
    page.btn_in_cart.click()
    page.btn_to_cart.click()
    assert page.product.is_visible()
    assert page.counter_cart.get_text() == '1'


def test_clear_cart(web_browser):
    """ Проверка кнопки "Очистить корзину" """

    page = MainPage(web_browser)

    page.search.send_keys('тестирование')
    page.btn_search.click()

    page.product.click()
    page.btn_in_cart.click()
    page.btn_to_cart.click()
    assert page.product.is_visible()
    page.clear_cart.click()
    assert page.counter_cart.get_text() == '0'


def test_restore_cart(web_browser):
    """ Проверка кнопки "Восстановить удаленное" из корзины """

    page = MainPage(web_browser)

    page.search.send_keys('тестирование')
    page.btn_search.click()

    page.product.click()
    page.btn_in_cart.click()
    page.btn_to_cart.click()
    assert page.product.is_visible()
    assert page.counter_cart.get_text() == '1'
    page.clear_cart.click()
    assert page.counter_cart.get_text() == '0'
    page.restore_cart.click()
    assert page.counter_cart.get_text() == '1'


def test_add_in_postponed(web_browser):
    """Проверка добавления товара в Отложенное """

    page = MainPage(web_browser)

    page.search.send_keys('тестирование')
    page.btn_search.click()

    page.product.click()
    page.btn_fave.click()
    page.wait_page_loaded()

    assert page.counter_postponed.get_text() == '1'


def test_increase_product_in_cart(web_browser):
    """Проверка кнопки "Переслать корзину" """

    page = MainPage(web_browser)

    page.search.send_keys('тестирование')
    page.btn_search.click()

    page.product.click()
    page.btn_in_cart.click()
    page.btn_to_cart.click()
    assert page.product.is_visible()
    page.btn_increase.scroll_to_element()
    page.btn_increase.click()
    page.refresh()
    assert page.counter_cart.get_text() == '2'


def test_lessen_product_in_cart(web_browser):
    """Проверка кнопки "Переслать корзину" """

    page = MainPage(web_browser)

    page.search.send_keys('тестирование')
    page.btn_search.click()

    page.product.click()
    page.btn_in_cart.click()
    page.btn_to_cart.click()
    assert page.product.is_visible()
    page.btn_lessen.scroll_to_element()
    page.btn_lessen.click()
    page.refresh()
    assert page.counter_cart.get_text() == '0'





