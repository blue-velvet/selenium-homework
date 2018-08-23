import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_waitings(app):

    wait = WebDriverWait(driver, 10)
    # adding 3 items
    for i in range(3):
        app.open_home_page(driver)
        app.add_item(driver, i, wait)

    app.open_cart(driver)

    table = driver.find_element_by_css_selector("table.dataTable")
    items = table.find_elements_by_css_selector("td.item")

    # deleting 3 items
    for i in range(len(items)):
        app.delete_item(driver, items, wait, i)



