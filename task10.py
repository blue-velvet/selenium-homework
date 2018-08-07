import pytest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(executable_path="C:\\Users\\KC\\PycharmProjects\\drivers\\geckodriver.exe")
    request.addfinalizer(wd.quit)
    return wd

def test_task10(driver):
    driver.get("http://localhost/litecart/")
    campaign_item = driver.find_element_by_css_selector("#box-campaigns")
    main_text = campaign_item.find_element_by_css_selector(".name").text
    main_regular_price = campaign_item.find_element_by_css_selector(".regular-price").text
    main_regular_price_color = campaign_item.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    main_regular_price_size = campaign_item.find_element_by_css_selector(".regular-price").value_of_css_property(
        "font-size")
    main_campaign_price = campaign_item.find_element_by_css_selector(".campaign-price").text
    main_campaign_price_color = campaign_item.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    main_campaign_price_size = campaign_item.find_element_by_css_selector(".regular-price").value_of_css_property(
        "font-size")
    print(main_text, main_regular_price, main_campaign_price)
    driver.find_element_by_css_selector("#box-campaigns a").click()
    time.sleep(3)
    #page_text = driver.find_element_by_xpath("h1[@class = 'title']").text
    page_text = driver.find_element_by_css_selector("h1.title").text
    page_regular_price = driver.find_element_by_css_selector(".regular-price").text
    page_regular_price_color = driver.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    page_campaign_price = driver.find_element_by_css_selector(".campaign-price").text
    page_campaign_price_color = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    print(page_text, page_regular_price, page_campaign_price)


