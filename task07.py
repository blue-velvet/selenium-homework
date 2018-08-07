import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(executable_path="C:\\Users\\KC\\PycharmProjects\\drivers\\geckodriver.exe")
    request.addfinalizer(wd.quit)
    return wd


def check_element(driver, locator):
    try:
        driver.find_element_by_css_selector(locator)
        return True
    except EC.NoSuchElementException:
        return False


def test_example(driver):

    login(driver)
    clicks(driver)


def clicks(driver):
    for i in range(1, 18):
        driver.find_element_by_css_selector("ul#box-apps-menu li:nth-child(%s)" % i).click()
        check_element(driver, "[h1]")
        childs = driver.find_elements_by_css_selector("ul.docs li")
        if childs:
            for j in range(2, len(childs) + 1):
                driver.find_element_by_css_selector("ul.docs li:nth-child(%s)" % j).click()
                check_element(driver, "[h1]")


def login(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
