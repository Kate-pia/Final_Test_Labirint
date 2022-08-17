from pages.cart import CartPage


def test_add_product_in_cart(web_browser):
    """Проверка добавления товара в корзину """

    page = CartPage(web_browser)

    page.search.send_keys('тестирование')
    page.btn_search.click()

    page.product.click()
    page.btn_in_cart.click()
    page.btn_to_cart.click()
    assert page.product.is_visible()
    assert page.counter_cart.get_text() == '1'


def test_clear_cart(web_browser):
    """ Проверка кнопки "Очистить корзину" """

    page = CartPage(web_browser)

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

    page = CartPage(web_browser)

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

    page = CartPage(web_browser)

    page.search.send_keys('тестирование')
    page.btn_search.click()

    page.product.click()
    page.btn_fave.click()
    page.wait_page_loaded()

    assert page.counter_postponed.get_text() == '1'


def test_increase_product_in_cart(web_browser):
    """Проверка кнопки "+" увеличения колчества товара """

    page = CartPage(web_browser)

    page.search.send_keys('тестирование')
    page.btn_search.click()

    page.product.click()
    page.btn_in_cart.click()
    page.btn_to_cart.click()
    assert page.product.is_visible()

    page.btn_increase.click()
    page.wait_page_loaded()
    assert page.counter_cart.get_text() == '2'


def test_lessen_product_in_cart(web_browser):
    """Проверка кнопки "-" уменьшения количества товара """

    page = CartPage(web_browser)

    page.search.send_keys('тестирование')
    page.btn_search.click()

    page.product.click()
    page.btn_in_cart.click()
    page.btn_to_cart.click()
    assert page.btn_increase.is_clickable()
    page.btn_increase.click()
    # page.btn_increase.click()
    # page.btn_lessen.click()
    # page.refresh()
    assert page.btn_quantity.get_text() == '2'


def test_checkout_order(web_browser):
    """Проверка кнопки "Перейти к оформлению" """

    page = CartPage(web_browser)

    page.search.send_keys('тестирование')
    page.btn_search.click()

    page.product.click()
    page.btn_in_cart.click()
    page.btn_to_cart.click()
    assert page.btn_checkout.is_clickable()
    page.btn_checkout.click()
    page.wait_page_loaded()
    #
    # assert page.get_current_url() == "https://www.labirint.ru/basket/checkout/"






