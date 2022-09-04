import os

from page_objets.cart_page import *
from page_objets.home_page import *
from page_objets.product_page import *
from utils.test_context import TestContext
from behave import *
from selenium import webdriver

@given('I go to homepage')
def homepage(context):
    context.driver = webdriver.Chrome(executable_path=os.getcwd() + '\\drivers\\chromedriver.exe')
    context.driver.get('https://www.florclick.com/')
    context.driver.maximize_window()
    context.test_context_obj = TestContext()

    context.home_page = HomePage(driver=context.driver, test_context_obj=context.test_context_obj)
    context.product_page = ProductPage(driver=context.driver, test_context_obj=context.test_context_obj)
    context.cart_page = CartPage(driver=context.driver, test_context_obj=context.test_context_obj)

    context.driver.find_element(By.XPATH, '//*[@id="cookies"]/div/form/p/button[1]').click()

@when('I add an article "{order}" to the cart')
def add_one_article(context, order):
    context.home_page.click_to_first_product()
    context.product_page.get_price(order)
    context.product_page.add_to_cart()
    context.product_page.select_complement()
    context.product_page.add_dedicatory()
    context.cart_page.return_home_page()

@then('I can see the total price of the cart')
def total_cart(context):
    assert (context.test_context_obj.get_suma() == context.cart_page.subtotal_text())


