from selenium.webdriver.common.by import By
import time

class CartPage:

    LOGO_XPATH = '//*[@id="finalizar"]/section[1]/div[1]/a'
    LOGO_CART_XPATH = "/html/body/div[2]/header/div/div/div[4]/div/nav/ul/li[12]/div/a/i"
    SUBTOTAL_XPATH = '//div[@id="carrito-home"]//div[@class="col-xs-4 subtotal"]'

    def __init__(self, driver, test_context_obj):
        self.driver = driver
        self.test_context_obj = test_context_obj

    def return_home_page(self):
        self.driver.find_element(By.XPATH, self.LOGO_XPATH).click()

    def subtotal_text(self):
        self.driver.find_element(By.XPATH, self.LOGO_CART_XPATH).click()
        time.sleep(1)
        return self.driver.find_element(By.XPATH, self.SUBTOTAL_XPATH).text




