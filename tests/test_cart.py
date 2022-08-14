from pages.cart import MainPage
from pages.labirint_main import MainPage


def test_add_product_in_cart(web_browser):
    """Проверка добавления товара в корзину """

    page = MainPage(web_browser)

    page.search.send_keys('сказка')
    page.btn_search.click()
    page.scroll_down()
    page.btn_product.click()
    page.btn_cart.click()


