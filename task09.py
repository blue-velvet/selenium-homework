import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(executable_path="C:\\Users\\KC\\PycharmProjects\\drivers\\geckodriver.exe")
    request.addfinalizer(wd.quit)
    return wd

def test_check_sorting(driver):

    def login(driver):
        driver.get("http://localhost/litecart/admin/")
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("login").click()

    login(driver)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    list1 = []

    #составляем список всех стран
    list_of_countries = driver.find_elements_by_css_selector("tr.row")
    #проходимся в цикле по каждой стране
    for country in list_of_countries:
        #добавляем страну в список
        list1.append(country.find_element_by_xpath("td[5]/a").text)

        #поиск по зонам
        if int(country.find_element_by_xpath("td[6]").text) > 0:
            country.find_element_by_xpath("td[5]/a").send_keys(Keys.CONTROL + Keys.RETURN)
            time.sleep(1)
            driver.switch_to_window(driver.window_handles[1])

            list_of_zones = driver.find_elements_by_css_selector("table#table-zones tr:not(.header)")

            list2 = []

            for zone in list_of_zones:
                if zone.find_element_by_xpath("td[3]").text is not '':
                    list2.append(zone.find_element_by_xpath("td[3]").text)

            if str(list2) == str(sorted(list2)):
                print("ZONES YES")
            driver.close()
            driver.switch_to_window(driver.window_handles[0])

    if str(list1) == str(sorted(list1)):
        print(list1)
        print("COUNTRIES YES")
