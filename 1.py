import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Firefox(executable_path="C:\\Users\\KC\\PycharmProjects\\drivers\\geckodriver.exe")
    wd.implicitly_wait(2)
    request.addfinalizer(wd.quit)
    return wd

'''получение RGB элемента в виде списка'''
def pars_color(str):
    rgb = []
    start = str.find("(")
    end = str.find(")")
    clr = str[start+1:end]
    rgb = clr.split(", ")
    return rgb


def prices(driver,locator):
    list = []
    items = driver.find_elements_by_css_selector(locator)
    url = driver.current_url #url текущей страницы
    item = items[0]

    #Получаем обычную и акционную стоимость товара
    price_reg = item.find_element_by_css_selector("s.regular-price")
    price_sale = item.find_element_by_css_selector("strong.campaign-price")

    #Получаем текст
    text_pr = price_reg.text
    list.append(text_pr)
    text_ps = price_sale.text
    list.append(text_ps)

    #Получаем размер
    size_pr = price_reg.value_of_css_property("font-size")
    size_ps = price_sale.value_of_css_property("font-size")
    if size_pr < size_ps:
        print("Size of regular price less than campaign price on page: " + url)
    else:
        print("Size of regular price more than campaign price on page: " + url)

    #получаем цвет акционной цены и проверяем, является ли он красным
    color_sale = pars_color(price_sale.value_of_css_property("color"))
    if int(color_sale[1]) == 0 and int(color_sale[2]) == 0:
        print("The campaign price's color is red on page: " + url)
    else:
        print("The campaign price's color is not red on page: " + url)

    #получаем цвет регулярной цены и проверяем, является ли он серым
    color_reg = pars_color(price_reg.value_of_css_property("color"))
    if color_reg[0] == color_reg[1] and color_reg[0] == color_reg[2]:
        print("The regular price's color is gray on page: " + url)
    else:
        print("The regular price's color is not gray on page: " + url)

    #определяем, выделена ли акционная цена жирным
    style_sale = price_sale.tag_name
    if style_sale == "strong":
        print("Text of campaign price is bold on page: " + url)
    else:
        print("Text of campaign price is not bold on page: " + url)

    #определяем, зачеркнута ли обычная цена
    style_reg = price_reg.tag_name
    if style_reg == "s":
        print("Text of regular price is line-through on page: " + url)
    else:
        print("Text of regular price is not line-through on page: " + url)

    return list


def test_product(driver):
    #поиск элементов на главной странице
    main = []
    driver.get("http://localhost/litecart/")
    name_main = driver.find_element_by_css_selector("div#box-campaigns li.product div.name").text
    main.append(name_main)
    main.extend(prices(driver,"div#box-campaigns li.product"))

    #переход на страницу товара
    driver.find_element_by_css_selector("div#box-campaigns li.product").click()

    #поиск элементов на странице товара странице
    page = []
    name_page = driver.find_element_by_css_selector("h1.title").text
    page.append(name_page)
    page.extend(prices(driver, "div#box-product"))

    #сравнение товаров
    if main == page:
        print("Text and prices are equal on both pages")
    else:
        print("Text and prices are not equal")