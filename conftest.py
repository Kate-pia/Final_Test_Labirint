import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def web_browser():
    web_driver = webdriver.Chrome('/chromedriver/chromedriver.exe')
    web_driver.maximize_window()
    yield web_driver

    web_driver.quit()

# def add_item_to_cart(xpath_item, driver_init):
#     # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
#     item_name = wait_of_element_located(
#         xpath=xpath_item,
#         driver_init=driver_init)
#     item_name.click()
#
#     # Поиск и ожидание кнопки добавления товара и клик по этой кнопке
#     item_add_button = wait_of_element_located(
#         xpath='//*[@id=\"add-to-cart-sauce-labs-fleece-jacket\"]',
#         driver_init=driver_init)
#     item_add_button.click()
#
#     # Ждем пока товар добавится в корзину, появится span(кол-во позиций в корзине)
#     # Возвращаем True или False в зависимости добавлися товар или нет
#     shop_cart_with_item = wait_of_element_located(
#         xpath='//*[@id=\"shopping_cart_container\"]/a/span',
#         driver_init=driver_init)
#     return shop_cart_with_item