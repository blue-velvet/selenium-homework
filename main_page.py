from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class MainPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def add_item(self, i, wait):
        items = self.driver.find_elements_by_xpath("//li[contains(@class,'product')]")
        items[0].click()
        try:
            Select(self.driver.find_element_by_css_selector("select[name='options[Size]']")).select_by_value("Medium")
        except:
            pass
        self.driver.find_element_by_css_selector("button[value='Add To Cart']").click()
        # wait
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(i + 1)))

    def delete_item(self, items, wait, i):
        self.driver.find_element_by_css_selector("button[value='Remove']").click()
        wait.until(EC.staleness_of(items[len(items) - i - 1]))