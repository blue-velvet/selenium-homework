import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(executable_path="C:\\Users\\KC\\PycharmProjects\\drivers\\geckodriver.exe")
    request.addfinalizer(wd.quit)
    return wd

def check_sorting():
    login(driver)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    list_of_countries = driver.get_elements_by_css_selector(".row")
    for country in list_of_countries:
        print(country.find_element_by_css_selector("td:nth child(5) > a").text)


def login(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()