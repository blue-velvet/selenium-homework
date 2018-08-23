from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Application:
    def __init__(self, driver):
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\KC\\PycharmProjects\\drivers\\chromedriver.exe')

    def quit(self):
        self.driver.quit()

    def open_cart(driver):
        driver.find_element_by_css_selector("a.link[href$='/checkout']").click()

    def open_home_page(driver):
        driver.get("http://localhost/litecart/")