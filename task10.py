import pytest
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(executable_path="C:\\Users\\KC\\PycharmProjects\\drivers\\geckodriver.exe")
    request.addfinalizer(wd.quit)
    return wd

def get_size(size):
    return float(size[:-2])

def get_color(color):
    return color[4:-1].split(", ")

def test_task10(driver):
    driver.get("http://localhost/litecart/")
    campaign_item = driver.find_element_by_css_selector("#box-campaigns")

    #получение параметров на главной странице
    main_text = campaign_item.find_element_by_css_selector(".name").text
    main_regular_price = campaign_item.find_element_by_css_selector(".regular-price").text
    main_regular_price_color = campaign_item.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    main_regular_price_size = campaign_item.find_element_by_css_selector(".regular-price").value_of_css_property(
        "font-size")
    main_regular_price_tag = campaign_item.find_element_by_css_selector(".regular-price").tag_name
    main_campaign_price = campaign_item.find_element_by_css_selector(".campaign-price").text
    main_campaign_price_color = campaign_item.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    main_campaign_price_size = campaign_item.find_element_by_css_selector(".campaign-price").value_of_css_property(
        "font-size")
    main_campaign_price_tag = campaign_item.find_element_by_css_selector(".campaign-price").tag_name

    #навигируемся на страницу товара
    driver.find_element_by_css_selector("#box-campaigns a").click()

    #получение параметров на странице товара
    page_text = driver.find_element_by_css_selector("h1.title").text
    page_regular_price = driver.find_element_by_css_selector(".regular-price").text
    page_regular_price_color = driver.find_element_by_css_selector(".regular-price").value_of_css_property("color")
    page_regular_price_size = driver.find_element_by_css_selector(".regular-price").value_of_css_property(
        "font-size")
    page_regular_price_tag = driver.find_element_by_css_selector(".regular-price").tag_name
    page_campaign_price = driver.find_element_by_css_selector(".campaign-price").text
    page_campaign_price_color = driver.find_element_by_css_selector(".campaign-price").value_of_css_property("color")
    page_campaign_price_size = driver.find_element_by_css_selector(".campaign-price").value_of_css_property(
        "font-size")
    page_campaign_price_tag = driver.find_element_by_css_selector(".campaign-price").tag_name

    #анализ данных
    print("*PRICE SYNCHRONIZATION*")
    if main_text == page_text:
        print("Text is the same")
    if main_regular_price == page_regular_price:
        print("Regular price is the same")
    if main_campaign_price == page_campaign_price:
        print("Campaign price is the same")

    print("*PRICE SIZE*")
    if get_size(main_campaign_price_size) > get_size(main_regular_price_size):
        print("Campaign price is less than regular on main page")
    if get_size(page_campaign_price_size) > get_size(page_regular_price_size):
        print("Campaign price is less than regular on second page")

    print("*PRICE COLOR*")
    if get_color(main_campaign_price_color)[1] == get_color(main_campaign_price_color)[2] == '0':
        print("Main campaign price is red")
    if get_color(page_campaign_price_color)[1] == get_color(page_campaign_price_color)[2] == '0':
        print("Page campaign price is red")
    if get_color(main_regular_price_color)[0] == get_color(main_regular_price_color)[1] == get_color(main_regular_price_color)[2]:
        print("Main regular price is grey")
    if get_color(page_regular_price_color)[0] == get_color(page_regular_price_color)[1] == get_color(page_regular_price_color)[2]:
        print("Page regular price is grey")

    print("*PRICE TAG*")
    if main_campaign_price_tag == 'strong':
        print("Main campaign price is strong")
    if page_campaign_price_tag == 'strong':
        print("Page campaign price is strong")
    if main_regular_price_tag == 's':
        print("Main regular price is crossed out")
    if page_regular_price_tag == 's':
        print("Page regular price is crossed out")

