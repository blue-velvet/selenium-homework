import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import string, random, time



@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(executable_path='C:\\Users\\KC\\PycharmProjects\\drivers\\chromedriver.exe')
    request.addfinalizer(wd.quit)
    return wd


def test_user_login(driver):

    open_home_page(driver)

    #генерим тестовые данные
    firstname = gen_string(7)
    lastname = gen_string(7)
    address1 = gen_string(7)
    city = gen_string(7)
    password = gen_string(7)
    postcode = gen_postcode(5)
    phone = gen_postcode(7)
    email = gen_email(5)

    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/en/create_account']").click()
    fill_form(driver, firstname, lastname, address1, postcode, city, email, phone, password)
    logout(driver)
    open_home_page(driver)
    login(driver, email, password)
    logout(driver)
    #распечатка использованных данных
    print(firstname, lastname, address1, postcode, city, email, phone, password)


def gen_string(n):
    a = string.ascii_letters
    return ''.join([random.choice(a) for i in range(n)])


def gen_postcode(n):
    a = string.digits
    return ''.join([random.choice(a) for i in range(n)])


def gen_email(n):
    a = string.ascii_letters
    return ''.join([random.choice(a) for i in range(n)]) + '@email.com'


def logout(driver):
    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/en/logout']").click()


def fill_form(driver, firstname, lastname, address1, postcode, city, email, phone, password):
    type(driver, 'firstname', firstname)
    type(driver, 'lastname', lastname)
    type(driver, 'address1', address1)
    type(driver, 'postcode', postcode)
    type(driver, 'city', city)
    type(driver, 'email', email)
    type(driver, 'phone', phone)
    type(driver, 'password', password)
    type(driver, 'confirmed_password', password)

    Select(driver.find_element_by_css_selector("select[name='country_code']")).select_by_value("US")
    time.sleep(2) #поменять на нормальное ожидание
    Select(driver.find_element_by_css_selector("select[name='zone_code']")).select_by_value("CA")

    driver.find_element_by_name('create_account').click()


def type(driver, field_name, value):
    driver.find_element_by_name(field_name).clear()
    driver.find_element_by_name(field_name).click()
    driver.find_element_by_name(field_name).send_keys(value)


def login(driver, email, password):
    type(driver, 'email', email)
    type(driver, 'password', password)
    time.sleep(4) #проблема с антивирусом
    driver.find_element_by_css_selector("button[name='login']").click()


def open_home_page(driver):
    driver.get("http://localhost/litecart/")
