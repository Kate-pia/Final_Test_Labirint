from pages.product import ProductPage
import pytest


@pytest.mark.product
class TestProdFromProductPage:
    def test_add_product_in_cart(self, web_browser):
        """Проверка добавления товара в корзину """

        page = ProductPage(web_browser)

        page.btn_in_cart.click()

        assert page.counter_cart.get_text() == '1'

    def test_to_cart(self, web_browser):
        """Проверка добавления товара в корзину """

        page = ProductPage(web_browser)

        page.btn_in_cart.click()
        page.btn_to_cart.click()

        assert page.counter_cart.get_text() == '1'


def test_add_in_postponed(web_browser):
    """Проверка добавления товара в Отложенное """

    page = ProductPage(web_browser)

    page.btn_fave.click()
    page.wait_page_loaded()

    assert page.counter_postponed.get_text() == '1'

