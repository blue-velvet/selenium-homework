import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(executable_path='C:\\Users\\KC\\PycharmProjects\\drivers\\chromedriver.exe')
    request.addfinalizer(wd.quit)
    return wd


def test_add_item(driver):
    login(driver)

    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/admin/?app=catalog&doc=catalog']").click()
    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/admin/?category_id=0&app=catalog&doc=edit_product']").click()

    driver.find_element_by_name("status").click()
    type(driver, "name[en]", "Pink Duck")
    #driver.find_element_by_css_selector("[value=1]")
    driver.find_element_by_xpath("//a[@href='#tab-prices']").click()
    driver.find_element_by_css_selector("input[name='prices[USD]']").send_keys('25')
    driver.find_element_by_css_selector("button[name=save]").click()


def login(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()


def type(driver, field_name, value):
    driver.find_element_by_name(field_name).clear()
    driver.find_element_by_name(field_name).click()
    driver.find_element_by_name(field_name).send_keys(value)
