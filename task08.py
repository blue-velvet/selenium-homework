import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(executable_path="C:\\Users\\KC\\PycharmProjects\\drivers\\geckodriver.exe")
    print(wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def check_element(driver, locator):
    try:
        driver.find_element_by_css_selector(locator)
        return True
    except EC.NoSuchElementException:
        return False


def test_sticker_check(driver):

    def login(driver):
        driver.get("http://localhost/litecart/")

    login(driver)
    count = 0
    #поиск всех уток
    ducks = driver.find_elements_by_css_selector("a.link[title $= Duck]")
    #проверяем на наличие стикера "поуточно"
    for i in ducks:
        count += check_element(i, "div[class $= sale")
    #выводим количество найденных стикеров
    print("Number of stickers is " + str(count))
