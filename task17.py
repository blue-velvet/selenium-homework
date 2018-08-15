import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(executable_path='C:\\Users\\KC\\PycharmProjects\\drivers\\chromedriver.exe')
    request.addfinalizer(wd.quit)
    return wd


def test_check_logs(driver):
    login(driver)
    driver.find_element_by_css_selector("a[href $= 'doc=catalog']").click()
    driver.find_element_by_link_text("Rubber Ducks").click()
    for id in range(1, 6):
        driver.find_element_by_css_selector("a[href $= 'category_id=1&product_id=%s']" % str(id)).click()
        for l in driver.get_log("browser"):
            if l is not None:
                print("!!!Log message is present!!!")
        driver.back()


def login(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
