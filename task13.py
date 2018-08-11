import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(executable_path='C:\\Users\\KC\\PycharmProjects\\drivers\\chromedriver.exe')
    request.addfinalizer(wd.quit)
    return wd


def test_waitings(driver):

    wait = WebDriverWait(driver, 10)
    # adding 3 items
    for i in range(3):
        open_home_page(driver)
        add_item(driver, i, wait)

    open_cart(driver)

    table = driver.find_element_by_css_selector("table.dataTable")
    items = table.find_elements_by_css_selector("td.item")

    # deleting 3 items
    for i in range(len(items)):
        delete_item(driver, items, wait, i)


def add_item(driver, i, wait):
    items = driver.find_elements_by_xpath("//li[contains(@class,'product')]")
    items[0].click()
    try:
        Select(driver.find_element_by_css_selector("select[name='options[Size]']")).select_by_value("Medium")
    except:
        pass
    driver.find_element_by_css_selector("button[value='Add To Cart']").click()
    # wait
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(i + 1)))


def delete_item(driver, items, wait, i):
    driver.find_element_by_css_selector("button[value='Remove']").click()
    wait.until(EC.staleness_of(items[len(items) - i - 1]))


def open_cart(driver):
    driver.find_element_by_css_selector("a.link[href$='/checkout']").click()


def open_home_page(driver):
    driver.get("http://localhost/litecart/")
